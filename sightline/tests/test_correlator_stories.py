"""Correlator story assembly tests: sim events in, Event Stories out.

Feeds real simulator runs through the correlator core and asserts the
Sprint 2 gate: the 2:14 AM scenario yields one alert story with an
identity-grade best frame, a deter beat, a fled outcome, and a narrative
that cites the timestamps.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
import json
import sys
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim" / "perimeter-sim"))
sys.path.insert(0, str(ROOT / "gateway" / "correlator"))
sys.path.insert(0, str(ROOT / "agents" / "narrator"))

from perimeter_sim.bus import Bus  # noqa: E402
from perimeter_sim.engine import Engine  # noqa: E402
from perimeter_sim.model import load_house  # noqa: E402
from perimeter_sim.scenarios import SCENARIOS  # noqa: E402
from core import Correlator, HistReID  # noqa: E402
from narrator import narrate  # noqa: E402

SCAN = ROOT / "sim" / "perimeter-sim" / "scans" / "demo-house.json"
STORY_VALIDATOR = jsonschema.Draft202012Validator(
    json.loads((ROOT / "gateway" / "schemas" / "story.v1.schema.json").read_text()))


def _stories_for(scenario, tmp_path):
    house = load_house(SCAN)
    bus = Bus(tmp_path / scenario, mqtt_host="127.0.0.1", mqtt_port=1)
    eng = Engine(SCENARIOS[scenario], house, bus, tmp_path / scenario)
    corr = Correlator(reid=HistReID(), narrator=narrate)
    bus.add_listener(lambda topic, p:
                     corr.ingest(p) if p.get("schema") == "sightline.event.v1" else None)
    eng.run_headless()
    bus.close()
    corr.flush()
    stories = corr.story_list()
    for s in stories:
        STORY_VALIDATOR.validate(s)
    return stories


def test_car_prowler_story(tmp_path):
    stories = _stories_for("car-prowler-0214", tmp_path)
    assert len(stories) == 1, "one incident, one story"
    s = stories[0]
    assert s["status"] == "closed"
    assert s["severity"] == "alert"
    assert s["verified"] is True
    classes = {e["class"] for e in s["entities"]}
    assert classes == {"person", "vehicle"}
    person = next(e for e in s["entities"] if e["class"] == "person")
    assert person["best_frame"]["dori_level"] == "identify"
    assert person["best_frame"]["channel"] == "identity"
    assert len(person["node_tracks"]) >= 2, "person stitched across nodes"
    assert s["deter"]["fired"] is True
    assert s["deter"]["ts"][11:16] == "02:14"
    assert s["deter"]["outcome"] == "fled"
    beats = " | ".join(b["beat"] for b in s["timeline"])
    assert "identity-grade capture" in beats
    assert "deter fired" in beats
    assert s["evidence_exportable"] is False, "simulated frames are never evidence"


def test_car_prowler_narrative(tmp_path):
    s = _stories_for("car-prowler-0214", tmp_path)[0]
    n = s["narrative"]
    assert n["mode"] == "mock"
    assert "02:14" in n["homeowner"] or "2:14" in n["homeowner"]
    assert "left immediately" in n["homeowner"]
    ps = n["police_summary"]
    assert "identify grade" in ps
    assert "NOT available" in ps and "simulated" in ps
    assert "—" not in n["homeowner"] + ps, "no em dashes, ever"


def test_quiet_night_stories_stay_info(tmp_path):
    stories = _stories_for("quiet-night", tmp_path)
    assert stories, "even a quiet night logs its stories"
    for s in stories:
        assert s["severity"] in ("info", "watch")
        assert "deter" not in s or not s["deter"].get("fired")


def test_party_arrivals_single_story_no_alert(tmp_path):
    stories = _stories_for("party-arrivals", tmp_path)
    assert len(stories) == 1
    s = stories[0]
    persons = [e for e in s["entities"] if e["class"] == "person"]
    assert len(persons) == 3, "three distinct guests, not one smeared identity"
    assert not s.get("deter", {}).get("fired")


def test_reid_keeps_distinct_actors_apart(tmp_path):
    stories = _stories_for("car-prowler-0214", tmp_path)
    s = stories[0]
    assert len(s["entities"]) == 2, "car and person stay separate entities"
