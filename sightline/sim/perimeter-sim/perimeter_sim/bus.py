"""Event bus for the simulator.

Publishes exactly what real firmware publishes: same topics, same payloads,
validated against gateway/schemas at publish time. Three sinks, all active:

1. MQTT broker if reachable (localhost:1883, override SIGHTLINE_MQTT_HOST/PORT).
2. JSONL log under runs/<run_id>/events.jsonl (always).
3. In-process listeners (the live web view subscribes here).

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import json
import os
import threading
from pathlib import Path

import jsonschema

_SCHEMA_DIR = Path(__file__).resolve().parents[3] / "gateway" / "schemas"

_VALIDATORS = {}
for _f, _sid in (("event.v1.schema.json", "sightline.event.v1"),
                 ("telemetry.v1.schema.json", "sightline.telemetry.v1")):
    _VALIDATORS[_sid] = jsonschema.Draft202012Validator(
        json.loads((_SCHEMA_DIR / _f).read_text()))


class Bus:
    def __init__(self, run_dir: Path, mqtt_host: str = None, mqtt_port: int = None):
        self.run_dir = Path(run_dir)
        self.run_dir.mkdir(parents=True, exist_ok=True)
        self._log = open(self.run_dir / "events.jsonl", "a")
        self._lock = threading.Lock()
        self._listeners = []
        self.published = 0
        self.mqtt = None
        self.mqtt_status = "off"
        host = mqtt_host or os.environ.get("SIGHTLINE_MQTT_HOST", "localhost")
        port = int(mqtt_port or os.environ.get("SIGHTLINE_MQTT_PORT", "1883"))
        self._try_mqtt(host, port)

    def _try_mqtt(self, host: str, port: int):
        try:
            import paho.mqtt.client as mqtt
            client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,
                                 client_id="sightline-sim")
            client.connect(host, port, keepalive=30)
            client.loop_start()
            self.mqtt = client
            self.mqtt_status = f"connected {host}:{port}"
        except Exception:
            self.mqtt = None
            self.mqtt_status = f"no broker at {host}:{port} (in-process bus only)"

    def add_listener(self, fn):
        """fn(topic, payload_dict), called on the publishing thread."""
        self._listeners.append(fn)

    def publish(self, topic: str, payload: dict):
        sid = payload.get("schema")
        if sid in _VALIDATORS:
            _VALIDATORS[sid].validate(payload)  # fail loudly in the sim
        line = json.dumps({"topic": topic, "payload": payload})
        with self._lock:
            self._log.write(line + "\n")
            self._log.flush()
            self.published += 1
        if self.mqtt:
            try:
                self.mqtt.publish(topic, json.dumps(payload), qos=1)
            except Exception:
                pass
        for fn in list(self._listeners):
            try:
                fn(topic, payload)
            except Exception:
                pass

    def close(self):
        with self._lock:
            self._log.close()
        if self.mqtt:
            try:
                self.mqtt.loop_stop()
                self.mqtt.disconnect()
            except Exception:
                pass
