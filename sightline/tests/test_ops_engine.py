"""Ops Engine tests: scan-to-kit, runbook with QC gates, QC agent evals,
capacity engine, watchtower proactive tickets, and the gateway surface.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
import json
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "ops"))
sys.path.insert(0, str(ROOT / "agents" / "qc"))
sys.path.insert(0, str(ROOT / "gateway" / "correlator"))

import capacity  # noqa: E402
import qc  # noqa: E402
import scan_to_kit as sk  # noqa: E402
import watchtower as wt  # noqa: E402
from runbook import runbook_from_kit, COMMISSIONING_30  # noqa: E402


# ---- scan-to-kit ----

def test_all_samples_produce_kits():
    for n in (1, 2, 3):
        kit = sk.kit_from_scan(sk.load_sample(n))
        assert kit["schema"] == "sightline.kit.v1"
        assert kit["cameras"] and kit["cut_list"] and kit["connector_map"]
        assert kit["price"]["total_installed"] > 0
        assert kit["ar_overlay"]["schema"] == "sightline.ar.v1"
        assert kit["all_estimates"] is True


def test_cut_list_labels_and_margin():
    kit = sk.kit_from_scan(sk.load_sample(3))  # 48V, 6 segments
    labels = [c["label"] for c in kit["cut_list"]]
    assert labels[0] == "A1" and len(labels) == len(set(labels))
    seg_front = next(s for s in kit["model"]["segments"] if s["id"] == "front")
    front_cut = sum(c["length_ft"] for c in kit["cut_list"] if c["segment"] == "front")
    assert front_cut >= seg_front["length_ft"] * 1.019  # +2% scan margin


def test_identity_aim_hits_the_window_on_hard_house():
    """Sample 2: 20 ft eaves, the audited hard case. The planner must land
    chokepoints inside the identify window with usable pitch."""
    kit = sk.kit_from_scan(sk.load_sample(2))
    track = [c for c in kit["cameras"] if c["kind"] == "track"]
    assert track
    for cam in track:
        assert cam["aim"]["pitch_ok"], cam
        assert cam["aim"]["dori_at_chokepoint"] in ("identify", "validate"), cam
    porch_cam = next(c for c in track if c["chokepoint"] == "porch-line")
    assert porch_cam["aim"]["in_identify_window"]


def test_price_matches_camera_plan():
    kit = sk.kit_from_scan(sk.load_sample(1))
    n_track = sum(1 for c in kit["cameras"] if c["kind"] == "track")
    kit_line = next(k for k in kit["price"]["kit"] if "track node" in k["item"])
    assert kit_line["qty"] == n_track, "one source of truth: price follows the plan"


def test_bad_scan_rejected():
    with pytest.raises(Exception):
        sk.kit_from_scan({"schema": "sightline.scan.v1", "site_id": "x"})


# ---- runbook ----

def test_runbook_renders_with_gates():
    rb = runbook_from_kit(sk.kit_from_scan(sk.load_sample(1)))
    assert rb["schema"] == "sightline.runbook.v1"
    gates = [s for s in rb["steps"] if "qc_gate" in s]
    assert len(gates) >= 5
    assert set(rb["gates_required_for_warranty"]) >= {
        "gasket_seated", "connector_clicked", "node_aim", "controller_wiring"}
    assert len(COMMISSIONING_30) == 30
    assert rb["total_target_hr"] < 3.5  # the on-site threshold holds in the runbook too


# ---- QC agent evals: every fixture judged as its manifest expects ----

MANIFEST = json.loads((ROOT / "agents" / "qc" / "fixtures" / "manifest.json").read_text())


@pytest.mark.parametrize("entry", MANIFEST, ids=[e["file"] for e in MANIFEST])
def test_qc_fixture(entry):
    r = qc.review(str(ROOT / "agents" / "qc" / "fixtures" / entry["file"]),
                  entry["check"])
    assert r["passed"] is entry["expected_pass"], r
    if not r["passed"]:
        assert r["redo"], "a fail without redo instructions is useless on a ladder"
        assert all(len(x) > 30 for x in r["redo"])


def test_qc_wrong_subject():
    r = qc.review(str(ROOT / "agents" / "qc" / "fixtures" / "gasket_seated-1-pass.svg"),
                  "node_aim")
    assert not r["passed"] and "wrong subject" in r["verdict"]


def test_qc_warranty_requires_all_gates():
    fx = ROOT / "agents" / "qc" / "fixtures"
    photos = {c: str(fx / f"{c}-1-pass.svg") for c in qc.SPEC}
    assert qc.review_job(photos)["warranty_eligible"] is True
    photos["gasket_seated"] = str(fx / "gasket_seated-5-fail.svg")
    assert qc.review_job(photos)["warranty_eligible"] is False


# ---- capacity ----

def test_scheduler_places_jobs_route_aware():
    import random
    rng = random.Random(3)
    crews = [capacity.Crew(id=f"c{i}", home_base=(rng.uniform(0, 15), rng.uniform(0, 15)),
                           jobs_done=10) for i in range(3)]
    jobs = [capacity.Job(id=f"j{i}", site=(rng.uniform(0, 15), rng.uniform(0, 15)),
                         earliest_day=0) for i in range(20)]
    out = capacity.schedule_jobs(crews, jobs, horizon_days=5)
    assert out["scheduled"] >= 18
    assert out["avg_est_hours"] < 3.5


def test_forecaster_answers_the_metro_question():
    f = capacity.crews_needed(100)
    assert f["crews_needed"] <= 4
    assert f["months_to_capacity"] <= 2


# ---- watchtower ----

def _telem(node, rail=12.0, rssi=-55, loop=72.0, ts="2026-09-07T02:00:00-06:00"):
    return {"schema": "sightline.telemetry.v1", "site_id": "site-demo",
            "node_id": node, "ts": ts, "uptime_s": 100, "fw_version": "x",
            "power": {"rail_v": rail, "draw_w": 5}, "wifi_rssi_dbm": rssi,
            "storage": {"loop_hours": loop, "used_pct": 90}}


def test_watchtower_opens_proactive_tickets():
    w = wt.Watchtower(install_dates={"site-demo": "2026-09-01T00:00:00"})
    w.observe(_telem("node-fr", rail=8.9))
    w.observe(_telem("node-fl", rssi=-82))
    w.observe(_telem("node-rear"))
    tickets = w.open_tickets()
    kinds = {t["kind"] for t in tickets}
    assert kinds == {"voltage_sag", "wifi_weak"}
    sag = next(t for t in tickets if t["kind"] == "voltage_sag")
    assert any("injection" in s for s in sag["remedy"])
    # dedupe: same node, same problem, one ticket
    w.observe(_telem("node-fr", rail=8.8))
    assert len(w.open_tickets()) == 2


def test_watchtower_offline_sweep():
    w = wt.Watchtower()
    w.observe(_telem("node-fr", ts="2026-09-07T02:00:00-06:00"))
    w.sweep_offline("2026-09-07T02:10:00-06:00")
    assert any(t["kind"] == "node_offline" for t in w.open_tickets())


# ---- gateway surface ----

def test_gateway_ops_endpoints():
    import app as gw
    c = TestClient(gw.app)
    kit = c.post("/kit", json=sk.load_sample(1))
    assert kit.status_code == 200 and kit.json()["schema"] == "sightline.kit.v1"
    rb = c.get("/runbook/sample/1")
    assert rb.status_code == 200 and rb.json()["schema"] == "sightline.runbook.v1"
    fixtures = c.get("/qc/fixtures").json()
    assert len(fixtures) == 25
    r = c.post("/qc/review", json={"check": "gasket_seated",
                                   "photo": "gasket_seated-4-fail.svg"})
    assert r.status_code == 200 and r.json()["passed"] is False
    assert c.get("/qc/fixtures/gasket_seated-1-pass.svg").status_code == 200
