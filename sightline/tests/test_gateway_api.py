"""Gateway API tests: ask, quote, scenes, deter, ingest over the wire.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
import json
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "gateway" / "correlator"))

import app as gateway_app  # noqa: E402

client = TestClient(gateway_app.app)
FIXTURE = json.loads(
    (ROOT / "gateway" / "schemas" / "fixtures" / "event_person_detect.json").read_text())


def test_health():
    r = client.get("/health")
    assert r.status_code == 200 and r.json()["ok"] is True


def test_ingest_and_story_assembly():
    r = client.post("/ingest", json=FIXTURE)
    assert r.status_code == 200
    stories = client.get("/stories").json()
    assert stories, "one event opens a story"
    s = stories[0]
    assert s["schema"] == "sightline.story.v1"
    assert any(e["class"] == "person" for e in s["entities"])


def test_ingest_rejects_invalid():
    r = client.post("/ingest", json={"schema": "sightline.event.v1", "junk": 1})
    assert r.status_code == 422


def test_ask_mock():
    client.post("/ingest", json=FIXTURE)
    r = client.post("/ask", json={"question": "what happened last night?"})
    assert r.status_code == 200
    d = r.json()
    assert d["mode"] == "mock"
    assert d["answer"]
    r2 = client.post("/ask", json={"question": ""})
    assert r2.status_code == 422


def test_quote_endpoint():
    r = client.post("/quote", json={
        "roofline_ft": 160, "corners": 4, "eave_heights_ft": [20, 10],
        "brand": "gemstone"})
    assert r.status_code == 200
    d = r.json()
    assert d["in_sku1_band"] is True
    assert d["all_estimates"] is True
    r2 = client.post("/quote", json={"corners": 4})
    assert r2.status_code == 422


def test_scenes_flow():
    d = client.get("/scenes").json()
    assert d["active"] == "Night"
    assert any(m["enforced"] for m in d["masks"])
    r = client.post("/scenes", json={"active": "Party"})
    assert r.json()["active"] == "Party"
    r = client.post("/scenes", json={"active": "Nope"})
    assert r.status_code == 422
    client.post("/scenes", json={"active": "Night"})


def test_scene_designer_mock():
    r = client.post("/scenes/design", json={
        "text": "watch the driveway and back yard, quiet hours lights", "name": "Test"})
    d = r.json()["scene"]
    assert d["armed"] is True
    assert "driveway" in d["deter_zones"] and "back-yard" in d["deter_zones"]
    assert d["quiet_lights"] is True
    r2 = client.post("/scenes/design", json={
        "text": "welcome guests, lights off deterrence off"})
    assert r2.json()["scene"]["armed"] is False


def test_deter_endpoint():
    r = client.post("/deter/site-demo")
    assert r.status_code == 200
    assert r.json()["ok"] is True
