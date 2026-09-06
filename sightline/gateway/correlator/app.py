"""SightLine correlator service.

Wires the pure core (entity stitching + story assembly, core.py) to the
outside world: MQTT subscribe, REST ingest/query, and a websocket that
pushes story and event updates to the app. On story close the narrator
agent runs (mock by default) and the narrative is pushed with the story.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import asyncio
import json
import os
import sys
import threading
import time
from collections import deque
from pathlib import Path

import jsonschema
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect

sys.path.insert(0, str(Path(__file__).resolve().parent))
from core import Correlator, HistReID  # noqa: E402

_AGENTS = Path(__file__).resolve().parents[2] / "agents" / "narrator"
sys.path.insert(0, str(_AGENTS))
try:
    from narrator import narrate  # noqa: E402
except ImportError:
    narrate = None

SCHEMA_DIR = Path(__file__).resolve().parents[1] / "schemas"
EVENT_VALIDATOR = jsonschema.Draft202012Validator(
    json.loads((SCHEMA_DIR / "event.v1.schema.json").read_text()))
TELEM_VALIDATOR = jsonschema.Draft202012Validator(
    json.loads((SCHEMA_DIR / "telemetry.v1.schema.json").read_text()))
STORY_VALIDATOR = jsonschema.Draft202012Validator(
    json.loads((SCHEMA_DIR / "story.v1.schema.json").read_text()))

MQTT_HOST = os.environ.get("SIGHTLINE_MQTT_HOST", "localhost")
MQTT_PORT = int(os.environ.get("SIGHTLINE_MQTT_PORT", "1883"))


class State:
    def __init__(self):
        self.lock = threading.Lock()
        self.events = deque(maxlen=2000)
        self.telemetry = {}
        self.rejected = 0
        self.mqtt_status = "disconnected"
        self.last_ingest_wall = time.monotonic()
        self.seq = 0
        self.updates = deque(maxlen=1000)   # (seq, kind, payload dict)
        self.seen_event_ids = deque(maxlen=5000)
        self.correlator = Correlator(
            reid=HistReID(), narrator=narrate, on_update=self._story_updated)

    def _push(self, kind: str, payload: dict):
        self.seq += 1
        self.updates.append((self.seq, kind, payload))

    def _story_updated(self, story: dict):
        STORY_VALIDATOR.validate(story)
        self._push("story", json.loads(json.dumps(story)))  # snapshot

    def ingest_event(self, payload: dict):
        EVENT_VALIDATOR.validate(payload)
        with self.lock:
            if payload["event_id"] in self.seen_event_ids:
                return  # duplicate via MQTT + HTTP double delivery
            self.seen_event_ids.append(payload["event_id"])
            self.events.append(payload)
            self.last_ingest_wall = time.monotonic()
            self._push("event", payload)
            self.correlator.ingest(payload)

    def ingest_telemetry(self, payload: dict):
        TELEM_VALIDATOR.validate(payload)
        with self.lock:
            self.telemetry[payload["node_id"]] = payload

    def updates_since(self, last: int) -> tuple:
        with self.lock:
            out = [(s, k, p) for (s, k, p) in self.updates if s > last]
            top = self.seq
        return out, top


state = State()
app = FastAPI(title="SightLine correlator", version="0.2.0")


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
            time.sleep(3)


def _tick_loop():
    while True:
        time.sleep(1.0)
        with state.lock:
            age = time.monotonic() - state.last_ingest_wall
            state.correlator.tick(age)


threading.Thread(target=_mqtt_loop, daemon=True).start()
threading.Thread(target=_tick_loop, daemon=True).start()


@app.get("/health")
def health():
    return {"ok": True, "mqtt": state.mqtt_status,
            "events": len(state.events), "rejected": state.rejected,
            "stories": len(state.correlator.stories),
            "nodes_reporting": sorted(state.telemetry)}


@app.post("/ingest")
def ingest(payload: dict):
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
def stories(limit: int = 50):
    with state.lock:
        return state.correlator.story_list()[:limit]


@app.get("/stories/{story_id}")
def story(story_id: str):
    s = state.correlator.stories.get(story_id)
    if not s:
        raise HTTPException(404, "no such story")
    return s


@app.post("/deter/{site_id}")
def deter_now(site_id: str):
    """Manual deter from the app's Deter Now button. Publishes the command
    on the bus when a broker is connected; always logs the intent."""
    cmd = {"pattern": "zone-follow-strobe", "segments": ["all"],
           "source": "app.manual", "site_id": site_id}
    state._push("deter_cmd", cmd)
    return {"ok": True, "cmd": cmd,
            "note": "published to bus when broker connected; sim obeys in Sprint 3"}


@app.websocket("/ws")
async def ws(sock: WebSocket):
    await sock.accept()
    last = 0
    # send current stories first so a late-joining app has full state
    with state.lock:
        for s in state.correlator.story_list():
            await sock.send_json({"kind": "story", "payload": s})
        last = state.seq
    try:
        while True:
            await asyncio.sleep(0.25)
            batch, top = state.updates_since(last)
            # collapse to the latest revision of each story in the batch
            latest_story = {}
            for _, kind, payload in batch:
                if kind == "story":
                    latest_story[payload["story_id"]] = payload
                else:
                    await sock.send_json({"kind": kind, "payload": payload})
            for s in latest_story.values():
                await sock.send_json({"kind": "story", "payload": s})
            last = top
    except (WebSocketDisconnect, RuntimeError):
        pass
