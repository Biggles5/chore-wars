"""Correlator core: entity stitching and Event Story assembly.

Pure logic, no I/O, fully testable. app.py wires it to MQTT, REST, and the
websocket. Re-ID is a color-histogram stub behind an interface a real
embedding model drops into (DECISIONS.md D-009).

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import math
import uuid
from datetime import datetime

CLOSE_GAP_EVENT_S = 120.0   # story closes after this much event-time silence
FLEE_WINDOW_S = 60.0        # entity gone this soon after deter counts as fled
PROTECTED_EXEMPT_ZONES = {"street"}


def _parse_ts(ts: str) -> datetime:
    return datetime.fromisoformat(ts)


def _clock(ts: str) -> str:
    return ts[11:19]


class HistReID:
    """Cosine similarity over color histograms. Same interface as a real
    embedding model: embed(event) -> vector, same_identity(a, b) -> bool."""

    def __init__(self, threshold: float = 0.95):
        self.threshold = threshold

    def embed(self, event: dict) -> list:
        return (event.get("object", {}).get("attributes", {}) or {}).get("hist") or []

    def same_identity(self, a: list, b: list) -> bool:
        if not a or not b or len(a) != len(b):
            return False
        dot = sum(x * y for x, y in zip(a, b))
        na = math.sqrt(sum(x * x for x in a))
        nb = math.sqrt(sum(x * x for x in b))
        if na == 0 or nb == 0:
            return False
        return dot / (na * nb) >= self.threshold


class _Entity:
    def __init__(self, cls: str, emb: list):
        self.entity_id = f"e-{uuid.uuid4().hex[:8]}"
        self.cls = cls
        self.emb = emb
        self.node_tracks = []
        self.best_frame = None
        self.first_ts = None
        self.last_ts = None
        self.zones = []
        self.last_zone = None
        self.last_level = None
        self.ident_beaten = False

    def public(self) -> dict:
        out = {"entity_id": self.entity_id, "class": self.cls,
               "node_tracks": list(self.node_tracks)}
        if self.best_frame:
            out["best_frame"] = self.best_frame
        return out


class Correlator:
    """Feeds on sightline.event.v1, emits sightline.story.v1.

    on_update(story_dict) fires whenever a story changes (open or close);
    the server pushes these to websocket clients and, on close, runs the
    narrator and fires on_update once more with the narrative attached.
    """

    def __init__(self, reid=None, narrator=None, on_update=None):
        self.reid = reid or HistReID()
        self.narrator = narrator
        self.on_update = on_update
        self.entities = []
        self.stories = {}        # story_id -> story dict
        self._open = {}          # site_id -> story_id
        self._events = {}        # story_id -> [events]
        self._deter_ts = {}      # story_id -> deter ts

    # ---- entity stitching ----
    def _entity_for(self, event: dict) -> _Entity:
        obj = event["object"]
        emb = self.reid.embed(event)
        for e in self.entities:
            if e.cls == obj["class"] and self.reid.same_identity(e.emb, emb):
                return e
        e = _Entity(obj["class"], emb)
        self.entities.append(e)
        return e

    # ---- story lifecycle ----
    def _story_for(self, event: dict) -> dict:
        site = event["site_id"]
        sid = self._open.get(site)
        if sid:
            story = self.stories[sid]
            last = self._events[sid][-1]["ts"] if self._events[sid] else story["started_ts"]
            gap = (_parse_ts(event["ts"]) - _parse_ts(last)).total_seconds()
            if gap <= CLOSE_GAP_EVENT_S:
                return story
            self._close(sid)
        story = {
            "schema": "sightline.story.v1",
            "story_id": f"s-{uuid.uuid4().hex[:10]}",
            "site_id": site,
            "started_ts": event["ts"],
            "status": "open",
            "severity": "info",
            "verified": False,
            "title": "",
            "zones": [],
            "nodes": [],
            "dwell_s": 0.0,
            "entities": [],
            "timeline": [],
            "evidence_exportable": False,
        }
        self.stories[story["story_id"]] = story
        self._open[site] = story["story_id"]
        self._events[story["story_id"]] = []
        return story

    def _beat(self, story: dict, event: dict, text: str):
        geo = event.get("geometry", {}) or {}
        item = {"ts": event["ts"], "event_id": event["event_id"], "beat": text,
                "node_id": event["node_id"]}
        if geo.get("zone"):
            item["zone"] = geo["zone"]
        if geo.get("dori_level"):
            item["dori_level"] = geo["dori_level"]
        thumb = (event.get("media", {}) or {}).get("thumb_ref")
        if thumb:
            item["thumb_ref"] = thumb
        story["timeline"].append(item)

    def _severity(self, story: dict):
        if story.get("deter", {}).get("fired"):
            story["severity"] = "alert"
            return
        classes = {e["class"] for e in story["entities"]}
        armed_zones = [z for z in story["zones"] if z not in PROTECTED_EXEMPT_ZONES]
        if ("person" in classes or "vehicle" in classes) and armed_zones:
            story["severity"] = "alert" if story["verified"] and "person" in classes else "watch"
        else:
            story["severity"] = "info"

    def _title(self, story: dict):
        classes = [e["class"] for e in story["entities"]]
        primary = ("person" if "person" in classes else
                   classes[0] if classes else "activity")
        zone = next((z for z in story["zones"] if z not in PROTECTED_EXEMPT_ZONES),
                    story["zones"][0] if story["zones"] else "perimeter")
        t = _parse_ts(story["started_ts"])
        clock = t.strftime("%-I:%M %p") if hasattr(t, "strftime") else story["started_ts"]
        story["title"] = f"{primary.capitalize()}, {zone}, {clock}"

    def ingest(self, event: dict):
        if event.get("schema") != "sightline.event.v1":
            return
        etype = event["type"]
        if etype not in ("detection.start", "detection.update",
                         "detection.end", "deter.fired"):
            return
        story = self._story_for(event)
        sid = story["story_id"]
        self._events[sid].append(event)
        geo = event.get("geometry", {}) or {}
        obj = event.get("object")

        entity = None
        if obj:
            entity = self._entity_for(event)
            if entity.entity_id not in [e["entity_id"] for e in story["entities"]]:
                story["entities"].append(entity.public())
            tid = obj["track_id"]
            if tid not in entity.node_tracks:
                entity.node_tracks.append(tid)
            if entity.first_ts is None:
                entity.first_ts = event["ts"]
            entity.last_ts = event["ts"]

        if event["node_id"] not in story["nodes"]:
            story["nodes"].append(event["node_id"])
        zone = geo.get("zone")
        if zone and zone not in story["zones"]:
            story["zones"].append(zone)

        if etype == "detection.start" and entity:
            self._beat(story, event,
                       f"{obj['class']} entered {zone or 'view'} ({event['node_id']}, {geo.get('channel', 'wide')})")
            if zone:
                entity.last_zone = zone
            entity.last_level = geo.get("dori_level")
        elif etype == "detection.update" and entity:
            if zone and entity.last_zone and zone != entity.last_zone:
                self._beat(story, event, f"{obj['class']} moved to {zone}")
            entity.last_zone = zone or entity.last_zone
            entity.last_level = geo.get("dori_level")
        elif etype == "detection.end" and entity:
            dwell = event.get("dwell_s")
            self._beat(story, event,
                       f"{obj['class']} left view of {event['node_id']}"
                       + (f" after {dwell:.0f}s" if dwell is not None else ""))
        elif etype == "deter.fired":
            det = event.get("deter", {}) or {}
            story["deter"] = {"fired": True, "ts": event["ts"],
                              "segments": det.get("segments", []),
                              "outcome": "unknown"}
            self._deter_ts[sid] = event["ts"]
            self._beat(story, event,
                       "deter fired: " + det.get("pattern", "strobe")
                       + " on " + ", ".join(det.get("segments", [])))

        # one identity-grade beat per entity, whichever node lands it first
        if (entity and not entity.ident_beaten
                and geo.get("dori_level") in ("identify", "validate")):
            entity.ident_beaten = True
            self._beat(story, event,
                       f"identity-grade capture: {geo.get('px_per_m')} px/m on the "
                       f"{geo.get('channel')} channel ({event['node_id']})")

        # verified: identify-grade capture, or the same entity confirmed by 2+ nodes
        if entity:
            nodes_seen = {t.split(":")[0] for t in entity.node_tracks}
            if (geo.get("dori_level") in ("identify", "validate")
                    or len(nodes_seen) >= 2):
                story["verified"] = True
            if entity.best_frame is None or (geo.get("px_per_m", 0) or 0) > entity.best_frame["px_per_m"]:
                bf = {"event_id": event["event_id"], "ts": event["ts"],
                      "node_id": event["node_id"],
                      "channel": geo.get("channel", "wide"),
                      "dori_level": geo.get("dori_level", "none"),
                      "px_per_m": geo.get("px_per_m", 0) or 0}
                thumb = (event.get("media", {}) or {}).get("thumb_ref")
                if thumb:
                    bf["thumb_ref"] = thumb
                entity.best_frame = bf
                for pe in story["entities"]:
                    if pe["entity_id"] == entity.entity_id:
                        pe["best_frame"] = bf
                        pe["node_tracks"] = list(entity.node_tracks)

        self._severity(story)
        self._title(story)
        if self.on_update:
            self.on_update(story)

    def _close(self, sid: str):
        story = self.stories[sid]
        if story["status"] == "closed":
            return
        events = self._events[sid]
        story["status"] = "closed"
        if events:
            story["ended_ts"] = events[-1]["ts"]
            story["dwell_s"] = round(
                (_parse_ts(story["ended_ts"]) - _parse_ts(story["started_ts"])).total_seconds(), 1)
        if story.get("deter", {}).get("fired"):
            deter_t = _parse_ts(self._deter_ts[sid])
            person_last = [
                _parse_ts(e["ts"]) for e in events
                if e.get("object", {}).get("class") == "person"]
            if person_last:
                gone = (max(person_last) - deter_t).total_seconds()
                story["deter"]["outcome"] = "fled" if gone <= FLEE_WINDOW_S else "stayed"
        # evidence rule: exportable only if every frame is native and real
        media = [e.get("media") for e in events if e.get("media")]
        story["evidence_exportable"] = bool(media) and all(
            m.get("native_pixels") is True and m.get("synthetic") is not True
            for m in media)
        if self.narrator:
            try:
                story["narrative"] = self.narrator(story)
            except Exception:
                pass
        if self._open.get(story["site_id"]) == sid:
            del self._open[story["site_id"]]
        if self.on_update:
            self.on_update(story)

    def flush(self):
        """Close every open story (scenario ended or shutdown)."""
        for sid in list(self._open.values()):
            self._close(sid)

    def tick(self, last_ingest_wall_age_s: float):
        """Call periodically with seconds since the last ingest; closes open
        stories when the feed has gone quiet in wall time."""
        if last_ingest_wall_age_s >= 5.0:
            self.flush()

    def story_list(self) -> list:
        return sorted(self.stories.values(), key=lambda s: s["started_ts"], reverse=True)
