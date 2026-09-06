"""The simulation engine.

Ticks the world, runs per-node detection using the same DORI math as real
placement, maintains node-local tracks, publishes schema-valid events and
telemetry on the bus, and runs the Sprint 1 deter placeholder (moves to the
correlator in Sprint 2, see DECISIONS.md D-013).

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import copy
import hashlib
import uuid
from datetime import datetime, timedelta, timezone

from . import thumbs
from .model import House
from .scenarios import Scenario

TZ = timezone(timedelta(hours=-6))
BASE_DATE = "2026-09-06"
UPDATE_EVERY_S = 4.0
TELEMETRY_EVERY_S = 30.0
DETER_DWELL_S = 6.0
DETER_HOLD_S = 20.0
DETER_COOLDOWN_S = 60.0
FW_VERSION = "0.1.0-sim"

_CONF_BASE = {"person": 0.78, "vehicle": 0.80, "animal": 0.70,
              "package": 0.85, "unknown": 0.50}


def _hist(actor_id: str) -> list:
    """Deterministic 8-bin color histogram per actor, sharpened so distinct
    actors sit well apart in cosine space (worst cross-similarity ~0.86 vs
    1.0 for the same actor). Same actor gives the same histogram at every
    node, which is what the re-ID stub keys on."""
    h = hashlib.sha256(actor_id.encode()).digest()
    bins = [(1 + h[i]) ** 2 for i in range(8)]
    total = float(sum(bins))
    return [round(b / total, 4) for b in bins]


class _Track:
    def __init__(self, track_id: str):
        self.track_id = track_id
        self.first_s = None
        self.last_update_s = None
        self.last_level = None
        self.last_event_id = None
        self.hot_s = 0.0          # continuous seconds at identify grade (deter input)
        self.last_deter_s = -1e9


class Engine:
    def __init__(self, scenario: Scenario, house: House, bus, run_dir):
        self.scn = copy.deepcopy(scenario)
        self.house = house
        self.bus = bus
        self.run_dir = run_dir
        self.t = 0.0              # simulated seconds since scenario start
        self.done = False
        self.tracks = {}          # (node_id, actor_id) -> _Track
        self.track_counter = {}   # node_id -> int
        self.deter_until = {}     # segment_id -> sim time it stays lit until
        self.counts = {}          # event type -> count
        self.recent = []          # last 100 events for the view/API
        self._next_telemetry = 0.0
        hh, mm = self.scn.start_clock.split(":")
        self.base_dt = datetime.fromisoformat(f"{BASE_DATE}T{hh}:{mm}:00").replace(tzinfo=TZ)

    # ---- time ----
    def now_iso(self) -> str:
        return (self.base_dt + timedelta(seconds=self.t)).isoformat()

    def clock(self) -> str:
        return (self.base_dt + timedelta(seconds=self.t)).strftime("%H:%M:%S")

    # ---- publishing ----
    def _emit(self, node_id: str, etype: str, actor=None, view=None, extra=None) -> dict:
        ev = {
            "schema": "sightline.event.v1",
            "event_id": str(uuid.uuid4()),
            "site_id": self.house.site_id,
            "node_id": node_id,
            "ts": self.now_iso(),
            "type": etype,
        }
        if actor is not None and view is not None:
            tr = self.tracks[(node_id, actor.id)]
            conf = min(0.97, _CONF_BASE[actor.cls] + min(0.18, view["px_per_m"] / 2500.0))
            ev["object"] = {
                "class": actor.cls, "confidence": round(conf, 2),
                "track_id": tr.track_id,
                "attributes": {"hist": _hist(actor.id), "label": actor.label},
            }
            ev["geometry"] = {
                "distance_m": view["distance_m"], "ground_m": view["ground_m"],
                "bearing_deg": view["bearing_deg"], "pitch_deg": view["pitch_deg"],
                "px_per_m": view["px_per_m"], "dori_level": view["dori_level"],
                "channel": view["channel"],
                "zone": self.house.zone_at(actor.pos),
                "pos": {"x": round(actor.pos[0], 2), "y": round(actor.pos[1], 2)},
            }
            ev["media"] = {"native_pixels": False, "synthetic": True,
                           "clip_ref": f"loop://{node_id}/{ev['ts']}/12s"}
        if extra:
            ev.update(extra)
        if etype in ("detection.start", "detection.end", "deter.fired") and "media" in ev:
            ev["media"]["thumb_ref"] = thumbs.write_thumb(self.run_dir, ev)
        self.bus.publish(f"sightline/{self.house.site_id}/{node_id}/event", ev)
        self.counts[etype] = self.counts.get(etype, 0) + 1
        self.recent.append(ev)
        del self.recent[:-100]
        return ev

    def _telemetry(self):
        for node in self.house.nodes:
            payload = {
                "schema": "sightline.telemetry.v1",
                "site_id": self.house.site_id, "node_id": node.id,
                "ts": self.now_iso(), "uptime_s": round(86400 + self.t, 1),
                "fw_version": FW_VERSION, "temp_c": 28.5, "heater_on": False,
                "wifi_rssi_dbm": -55,
                "power": {"rail_v": 12.1, "draw_w": 4.8},
                "storage": {"loop_hours": 72.0, "used_pct": 93.0},
            }
            self.bus.publish(
                f"sightline/{self.house.site_id}/{node.id}/telemetry", payload)

    # ---- deter (Sprint 1 placeholder, D-013) ----
    def _maybe_deter(self, node, actor, view, tr: _Track, dt: float):
        zone = self.house.zone_at(actor.pos)
        eligible = (self.scn.armed and actor.cls in ("person", "vehicle")
                    and zone != "street"
                    and view["dori_level"] in ("identify", "validate"))
        if eligible:
            tr.hot_s += dt
        else:
            tr.hot_s = 0.0
        if (tr.hot_s >= DETER_DWELL_S
                and self.t - tr.last_deter_s >= DETER_COOLDOWN_S):
            tr.last_deter_s = self.t
            tr.hot_s = 0.0
            for seg in node.deter_segments:
                self.deter_until[seg] = self.t + DETER_HOLD_S
            self._emit(node.id, "deter.fired", actor=actor, view=view, extra={
                "deter": {"pattern": "zone-follow-strobe",
                          "segments": list(node.deter_segments),
                          "trigger_event_id": tr.last_event_id or ""},
            })
            actor.flee()

    # ---- main loop ----
    def tick(self, dt: float):
        if self.done:
            return
        self.t += dt
        if self.t >= self._next_telemetry:
            self._telemetry()
            self._next_telemetry += TELEMETRY_EVERY_S

        for actor in self.scn.actors:
            if not actor.active and not actor.done and self.t >= actor.start_s:
                actor.spawn()
            actor.step(dt)

        for node in self.house.nodes:
            for actor in self.scn.actors:
                key = (node.id, actor.id)
                view = node.best_view(actor.pos) if actor.active else None
                tr = self.tracks.get(key)
                if view is not None and tr is None:
                    n = self.track_counter.get(node.id, 0) + 1
                    self.track_counter[node.id] = n
                    tr = _Track(f"{node.id}:t{n:03d}")
                    tr.first_s = self.t
                    tr.last_update_s = self.t
                    tr.last_level = view["dori_level"]
                    self.tracks[key] = tr
                    tr.last_event_id = self._emit(
                        node.id, "detection.start", actor=actor, view=view)["event_id"]
                elif view is not None and tr is not None:
                    if (view["dori_level"] != tr.last_level
                            or self.t - tr.last_update_s >= UPDATE_EVERY_S):
                        tr.last_update_s = self.t
                        tr.last_level = view["dori_level"]
                        tr.last_event_id = self._emit(
                            node.id, "detection.update", actor=actor, view=view)["event_id"]
                elif view is None and tr is not None:
                    dwell = round(self.t - tr.first_s, 1)
                    last_view = {"distance_m": 0, "ground_m": 0, "bearing_deg": 0,
                                 "pitch_deg": 0, "px_per_m": 0, "dori_level": "none",
                                 "channel": "wide"}
                    ev = {
                        "schema": "sightline.event.v1",
                        "event_id": str(uuid.uuid4()),
                        "site_id": self.house.site_id, "node_id": node.id,
                        "ts": self.now_iso(), "type": "detection.end",
                        "object": {"class": actor.cls, "confidence": _CONF_BASE[actor.cls],
                                   "track_id": tr.track_id,
                                   "attributes": {"hist": _hist(actor.id), "label": actor.label}},
                        "dwell_s": dwell,
                        "media": {"native_pixels": False, "synthetic": True},
                    }
                    ev["media"]["thumb_ref"] = thumbs.write_thumb(self.run_dir, ev)
                    self.bus.publish(
                        f"sightline/{self.house.site_id}/{node.id}/event", ev)
                    self.counts["detection.end"] = self.counts.get("detection.end", 0) + 1
                    self.recent.append(ev)
                    del self.recent[:-100]
                    del self.tracks[key]
                    continue
                if view is not None and tr is not None and node.kind == "track":
                    self._maybe_deter(node, actor, view, tr, dt)

        if self.t >= self.scn.duration_s:
            self.done = True

    def run_headless(self, tick_s: float = 0.5):
        while not self.done:
            self.tick(tick_s)

    # ---- view state ----
    def snapshot(self) -> dict:
        return {
            "kind": "state",
            "scenario": self.scn.name,
            "clock": self.clock(),
            "t": round(self.t, 1),
            "duration_s": self.scn.duration_s,
            "armed": self.scn.armed,
            "done": self.done,
            "mqtt": self.bus.mqtt_status,
            "correlator": getattr(self.bus, "http_status", "off"),
            "published": self.bus.published,
            "counts": self.counts,
            "actors": [
                {"id": a.id, "class": a.cls, "label": a.label,
                 "pos": [round(a.pos[0], 2), round(a.pos[1], 2)],
                 "fleeing": a.fleeing}
                for a in self.scn.actors if a.active
            ],
            "deter": [seg for seg, until in self.deter_until.items() if until > self.t],
        }
