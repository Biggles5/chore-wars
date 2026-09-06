"""Guardian agent tests: AVS-01 scoring, escalation policy, latency budgets,
cost meter under the $6/home/month target, central-station handoff, and the
jurisdiction guardrails.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
import json
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim" / "perimeter-sim"))
sys.path.insert(0, str(ROOT / "gateway" / "correlator"))
sys.path.insert(0, str(ROOT / "agents" / "guardian"))
sys.path.insert(0, str(ROOT / "agents" / "narrator"))

from perimeter_sim.bus import Bus  # noqa: E402
from perimeter_sim.engine import Engine  # noqa: E402
from perimeter_sim.model import load_house  # noqa: E402
from perimeter_sim.scenarios import SCENARIOS  # noqa: E402
from core import Correlator, HistReID  # noqa: E402
from narrator import narrate  # noqa: E402
from guardian import Guardian  # noqa: E402
import flags as flags_mod  # noqa: E402
import receiver as receiver_mod  # noqa: E402

SCAN = ROOT / "sim" / "perimeter-sim" / "scans" / "demo-house.json"


def _run(scenario, tmp_path, guardian=None, armed=True):
    house = load_house(SCAN)
    bus = Bus(tmp_path / scenario, mqtt_host="127.0.0.1", mqtt_port=1)
    eng = Engine(SCENARIOS[scenario], house, bus, tmp_path / scenario)
    corr = Correlator(reid=HistReID(), narrator=narrate,
                      armed_provider=lambda: armed,
                      guardian=guardian.decide if guardian else None)
    bus.add_listener(lambda t, p:
                     corr.ingest(p) if p.get("schema") == "sightline.event.v1" else None)
    eng.run_headless()
    bus.close()
    corr.flush()
    return corr.story_list()


def test_prowler_scores_avs3_and_guardian_intervenes(tmp_path):
    g = Guardian(jurisdiction="UT")
    s = _run("car-prowler-0214", tmp_path, guardian=g)[0]
    assert s["avs"]["score"] == 3
    assert s["avs"]["confidence"] >= 0.8
    assert "deter" in s["avs"]["rationale"].lower() or "fled" in s["avs"]["rationale"].lower()
    gd = s["guardian"]
    assert gd["action"] == "intervene"
    assert any("reflex" in a for a in gd["actions_taken"])
    assert gd["latency_ms"]["intervene"] < 10_000
    assert gd["latency_ms"]["handoff_decision"] < 30_000
    assert 0 < gd["cost_usd"] < 0.05


def test_deer_scores_zero_and_dismissed(tmp_path):
    g = Guardian(jurisdiction="UT")
    stories = _run("deer-3am", tmp_path, guardian=g)
    for s in stories:
        assert s["avs"]["score"] == 0
        assert s["guardian"]["action"] == "dismiss"


def test_disarmed_guests_score_zero(tmp_path):
    g = Guardian(jurisdiction="UT")
    stories = _run("party-arrivals", tmp_path, guardian=g, armed=False)
    for s in stories:
        assert s["avs"]["score"] == 0, s["avs"]
        assert s["guardian"]["action"] == "dismiss"


def test_cost_meter_under_six_dollars(tmp_path):
    """A full quiet night plus the flagship incident, extrapolated to a
    month, must land under the $6/home/month fully loaded target."""
    g = Guardian(jurisdiction="UT")
    _run("quiet-night", tmp_path, guardian=g)
    _run("car-prowler-0214", tmp_path / "b", guardian=g)
    report = g.nightly_report(homes=1)
    assert report["events_processed"] >= 2
    assert report["cost_per_home_month_usd_est"] < 6.0, report
    assert report["under_target"] is True


class _Recv(BaseHTTPRequestHandler):
    got = []

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        _Recv.got.append(body)
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"ok": true}')

    def log_message(self, *a):
        pass


def test_handoff_reaches_station(tmp_path):
    srv = ThreadingHTTPServer(("127.0.0.1", 0), _Recv)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    port = srv.server_address[1]
    g = Guardian(receiver_url=f"http://127.0.0.1:{port}", jurisdiction="UT")
    story = {
        "story_id": "s-handoff1", "site_id": "site-demo",
        "started_ts": "2026-09-06T02:13:00-06:00", "zones": ["driveway"],
        "verified": True, "entities": [{"entity_id": "e", "class": "person"}],
        "avs": {"score": 3, "confidence": 0.9, "rationale": "verified person, deter, stayed"},
        "deter": {"fired": True, "ts": "2026-09-06T02:14:01-06:00",
                  "segments": ["seg-front"], "outcome": "stayed"},
        "evidence_exportable": False,
    }
    d = g.decide(story)
    srv.shutdown()
    assert d["action"] == "handoff"
    assert d["handoff"]["sent"] is True and d["handoff"]["status"] == 200
    payload = _Recv.got[-1]
    assert payload["schema"] == "sightline.dispatch.v1"
    assert payload["avs01"]["score"] == 3
    assert payload["evidence"]["native_frames_available"] is False
    assert "911" in payload["guardrail"]


def test_mock_receiver_rejects_unverified_noise():
    c = TestClient(receiver_mod.app)
    low = {"schema": "sightline.dispatch.v1", "avs01": {"score": 1}}
    assert c.post("/dispatch", json=low).status_code == 422
    ok = {"schema": "sightline.dispatch.v1", "avs01": {"score": 3},
          "site_id": "s", "story_id": "x"}
    r = c.post("/dispatch", json=ok)
    assert r.status_code == 200 and "priority" in r.json()["queued_as"]


def test_face_id_gated_jurisdictions(monkeypatch):
    assert Guardian(jurisdiction="IL").face_id_allowed() is False
    assert Guardian(jurisdiction="TX").face_id_allowed() is False
    assert Guardian(jurisdiction="PORTLAND-OR").face_id_allowed() is False
    assert Guardian(jurisdiction="UT").face_id_allowed() is True
    monkeypatch.setenv("SIGHTLINE_STATE", "OR")
    monkeypatch.setenv("SIGHTLINE_CITY", "Portland")
    f = flags_mod.feature_flags()
    assert f["face_recognition"]["enabled"] is False
    assert "Portland" in f["face_recognition"]["gated_reason"]
    monkeypatch.setenv("SIGHTLINE_STATE", "UT")
    monkeypatch.setenv("SIGHTLINE_CITY", "")
    assert flags_mod.feature_flags()["face_recognition"]["enabled"] is True


def test_white_label_pivot_is_config(monkeypatch):
    monkeypatch.setenv("SIGHTLINE_WHITE_LABEL", "1")
    monkeypatch.setenv("SIGHTLINE_BRAND", "AcmeSecure")
    b = flags_mod.branding()
    assert b["white_label"] is True and b["name"] == "AcmeSecure"
