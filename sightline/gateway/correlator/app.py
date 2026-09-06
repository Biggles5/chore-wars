"""SightLine correlator: the gateway brain.

Sprint 1 scope (DECISIONS.md D-009): boots, subscribes to the site's MQTT
event tree, validates payloads, keeps a recent-event buffer, and exposes
health + ingest + query REST. The track/story/re-ID interfaces are declared
here and filled in Sprint 2 without moving files.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import json
import os
import threading
from collections import deque
from pathlib import Path

import jsonschema
from fastapi import FastAPI, HTTPException

SCHEMA_DIR = Path(__file__).resolve().parents[1] / "schemas"
EVENT_VALIDATOR = jsonschema.Draft202012Validator(
    json.loads((SCHEMA_DIR / "event.v1.schema.json").read_text()))
TELEM_VALIDATOR = jsonschema.Draft202012Validator(
    json.loads((SCHEMA_DIR / "telemetry.v1.schema.json").read_text()))

MQTT_HOST = os.environ.get("SIGHTLINE_MQTT_HOST", "localhost")
MQTT_PORT = int(os.environ.get("SIGHTLINE_MQTT_PORT", "1883"))


class ReIDStub:
    """Cross-camera identity stitching interface.

    Sprint 2 implements color-histogram matching here; a real embedding
    model later replaces the internals behind the same two methods.
    """

    def embed(self, event: dict) -> list:
        return (event.get("object", {}).get("attributes", {}) or {}).get("hist", [])

    def same_identity(self, emb_a: list, emb_b: list) -> bool:
        raise NotImplementedError("Sprint 2")


class StoryAssembler:
    """Turns correlated tracks into Event Stories (Sprint 2).

    Story schema: timeline of events, best frames per DORI level, dwell,
    zones touched, deter outcome. Served over REST and websocket to the app.
    """

    def assemble(self, events: list) -> dict:
        raise NotImplementedError("Sprint 2")


class State:
    def __init__(self):
        self.events = deque(maxlen=2000)
        self.telemetry = {}
        self.rejected = 0
        self.mqtt_status = "disconnected"
        self.lock = threading.Lock()

    def ingest_event(self, payload: dict):
        EVENT_VALIDATOR.validate(payload)
        with self.lock:
            self.events.append(payload)

    def ingest_telemetry(self, payload: dict):
        TELEM_VALIDATOR.validate(payload)
        with self.lock:
            self.telemetry[payload["node_id"]] = payload


state = State()
app = FastAPI(title="SightLine correlator", version="0.1.0")


def _mqtt_loop():
    try:
        import paho.mqtt.client as mqtt
    except ImportError:
        state.mqtt_status = "paho-mqtt not installed"
        return

    def on_connect(client, userdata, flags, reason_code, properties=None):
        state.mqtt_status = f"connected {MQTT_HOST}:{MQTT_PORT}"
        client.subscribe("sightline/+/+/event", qos=1)
        client.subscribe("sightline/+/+/telemetry", qos=0)

    def on_message(client, userdata, msg):
        try:
            payload = json.loads(msg.payload)
            if msg.topic.endswith("/event"):
                state.ingest_event(payload)
            else:
                state.ingest_telemetry(payload)
        except Exception:
            state.rejected += 1

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,
                         client_id="sightline-correlator")
    client.on_connect = on_connect
    client.on_message = on_message
    while True:
        try:
            client.connect(MQTT_HOST, MQTT_PORT, keepalive=30)
            client.loop_forever(retry_first_connection=False)
        except Exception:
            state.mqtt_status = f"retrying {MQTT_HOST}:{MQTT_PORT}"
            import time
            time.sleep(3)


threading.Thread(target=_mqtt_loop, daemon=True).start()


@app.get("/health")
def health():
    return {"ok": True, "mqtt": state.mqtt_status,
            "events": len(state.events), "rejected": state.rejected,
            "nodes_reporting": sorted(state.telemetry)}


@app.post("/ingest")
def ingest(payload: dict):
    """Direct REST ingest, same validation as the bus path."""
    try:
        if payload.get("schema") == "sightline.event.v1":
            state.ingest_event(payload)
        elif payload.get("schema") == "sightline.telemetry.v1":
            state.ingest_telemetry(payload)
        else:
            raise HTTPException(422, "unknown schema")
    except jsonschema.ValidationError as e:
        raise HTTPException(422, e.message)
    return {"ok": True}


@app.get("/events")
def events(limit: int = 100, site_id: str = None, node_id: str = None):
    with state.lock:
        out = list(state.events)
    if site_id:
        out = [e for e in out if e["site_id"] == site_id]
    if node_id:
        out = [e for e in out if e["node_id"] == node_id]
    return out[-limit:]


@app.get("/telemetry")
def telemetry():
    with state.lock:
        return dict(state.telemetry)


@app.get("/stories")
def stories():
    """Event Stories land here in Sprint 2."""
    return {"stories": [], "note": "assembled stories ship in Sprint 2"}
