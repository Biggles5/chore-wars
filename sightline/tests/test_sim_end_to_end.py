"""End-to-end simulator tests: the Sprint 1 gate in executable form.

quiet-night runs end to end, every published message validates against the
wire schemas, and the flagship 2:14 AM scenario produces a deter event at
the right time and place.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
import json
import sys
import time
from pathlib import Path

import jsonschema
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim" / "perimeter-sim"))

from perimeter_sim.bus import Bus  # noqa: E402
from perimeter_sim.engine import Engine  # noqa: E402
from perimeter_sim.model import load_house  # noqa: E402
from perimeter_sim.scenarios import SCENARIOS  # noqa: E402

SCAN = ROOT / "sim" / "perimeter-sim" / "scans" / "demo-house.json"
SCHEMAS = ROOT / "gateway" / "schemas"


def _run(name, tmp_path):
    house = load_house(SCAN)
    bus = Bus(tmp_path / name, mqtt_host="127.0.0.1", mqtt_port=1)  # no broker: in-process only
    eng = Engine(SCENARIOS[name], house, bus, tmp_path / name)
    t0 = time.monotonic()
    eng.run_headless()
    wall = time.monotonic() - t0
    bus.close()
    lines = [json.loads(l) for l in
             (tmp_path / name / "events.jsonl").read_text().splitlines()]
    return eng, lines, wall


def _validate_all(lines):
    validators = {
        "sightline.event.v1": jsonschema.Draft202012Validator(
            json.loads((SCHEMAS / "event.v1.schema.json").read_text())),
        "sightline.telemetry.v1": jsonschema.Draft202012Validator(
            json.loads((SCHEMAS / "telemetry.v1.schema.json").read_text())),
    }
    for line in lines:
        p = line["payload"]
        validators[p["schema"]].validate(p)


def test_quiet_night_end_to_end(tmp_path):
    eng, lines, wall = _run("quiet-night", tmp_path)
    assert eng.done
    assert wall < 60, "gate: full night must simulate in under a minute headless"
    _validate_all(lines)
    events = [l["payload"] for l in lines if l["payload"]["schema"] == "sightline.event.v1"]
    assert eng.counts.get("deter.fired", 0) == 0, "quiet night must stay quiet"
    classes = {e["object"]["class"] for e in events if "object" in e}
    assert "animal" in classes and "vehicle" in classes
    assert eng.counts["detection.start"] == eng.counts["detection.end"]
    telem = [l["payload"] for l in lines if l["payload"]["schema"] == "sightline.telemetry.v1"]
    assert len(telem) > 100  # heartbeats all night from 4 nodes


def test_car_prowler_0214_fires_deter(tmp_path):
    eng, lines, _ = _run("car-prowler-0214", tmp_path)
    _validate_all(lines)
    deters = [l["payload"] for l in lines if l["payload"].get("type") == "deter.fired"]
    assert len(deters) == 1
    d = deters[0]
    assert d["object"]["class"] == "person"
    assert d["ts"][11:16] == "02:14", f"deter must land at 2:14 AM, got {d['ts']}"
    assert d["geometry"]["dori_level"] == "identify"
    assert d["geometry"]["channel"] == "identity"
    assert d["geometry"]["zone"] in ("driveway", "front-walk", "porch")
    assert set(d["deter"]["segments"]) == {"seg-front", "seg-east"}
    # identity capture happened before deter, at identify grade, on the chokepoint channel
    idents = [l["payload"] for l in lines
              if l["payload"].get("geometry", {}).get("dori_level") == "identify"
              and l["payload"].get("object", {}).get("class") == "person"]
    assert idents and idents[0]["ts"] <= d["ts"]


def test_prowler_flees_after_deter(tmp_path):
    eng, lines, _ = _run("car-prowler-0214", tmp_path)
    prowler = [a for a in eng.scn.actors if a.id == "prowler"][0]
    assert prowler.fleeing and prowler.done


def test_animals_never_deter(tmp_path):
    eng, _, _ = _run("deer-3am", tmp_path)
    assert eng.counts.get("deter.fired", 0) == 0


def test_disarmed_never_deters(tmp_path):
    eng, _, _ = _run("party-arrivals", tmp_path)
    assert eng.counts.get("deter.fired", 0) == 0
    assert eng.counts.get("detection.start", 0) >= 4  # guests were all seen


def test_synthetic_flag_always_set(tmp_path):
    _, lines, _ = _run("porch-pirate", tmp_path)
    for l in lines:
        p = l["payload"]
        if p["schema"] == "sightline.event.v1" and "media" in p:
            assert p["media"]["synthetic"] is True
            assert p["media"]["native_pixels"] is False


def test_thumbnails_written(tmp_path):
    _, lines, _ = _run("mail-daily", tmp_path)
    refs = [l["payload"]["media"]["thumb_ref"] for l in lines
            if l["payload"].get("media", {}).get("thumb_ref")]
    assert refs
    for r in refs:
        f = tmp_path / "mail-daily" / r
        assert f.exists()
        assert "SIMULATED" in f.read_text()


def test_topics_match_tree(tmp_path):
    _, lines, _ = _run("deer-3am", tmp_path)
    for l in lines:
        parts = l["topic"].split("/")
        assert parts[0] == "sightline" and parts[1] == "site-demo"
        assert parts[3] in ("event", "telemetry")
