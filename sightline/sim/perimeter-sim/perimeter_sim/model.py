"""House, node, and actor models for the perimeter simulator.

Loads a "scan" JSON (the same shape the real scan-to-quote flow produces),
builds virtual nodes whose DORI rings come from hardware/dori_placement.py
(the same math real placement uses), and provides the geometry used by the
event engine.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import json
import math
import sys
from dataclasses import dataclass, field
from pathlib import Path

_HARDWARE = Path(__file__).resolve().parents[3] / "hardware"
sys.path.insert(0, str(_HARDWARE))
import dori_placement as dp  # noqa: E402


def norm_deg(a: float) -> float:
    """Normalize to (-180, 180]."""
    while a <= -180:
        a += 360
    while a > 180:
        a -= 360
    return a


def bearing_deg(from_xy, to_xy) -> float:
    """Compass-style bearing: 0 = +y (north), 90 = +x (east), clockwise."""
    dx = to_xy[0] - from_xy[0]
    dy = to_xy[1] - from_xy[1]
    return norm_deg(math.degrees(math.atan2(dx, dy)))


def point_in_poly(pt, poly) -> bool:
    x, y = pt
    inside = False
    n = len(poly)
    j = n - 1
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
            inside = not inside
        j = i
    return inside


@dataclass
class Channel:
    name: str            # wide | identity | door
    sensor: str          # 8mp | 12mp
    hfov_deg: float
    boresight_deg: float  # absolute compass bearing of the channel center
    rings_ground_m: dict = field(default_factory=dict)  # dori level -> ground reach

    def covers(self, rel_bearing_to_boresight: float) -> bool:
        return abs(norm_deg(rel_bearing_to_boresight)) <= self.hfov_deg / 2.0


@dataclass
class Node:
    id: str
    kind: str            # track | door
    pos: tuple
    height_m: float
    facing_deg: float
    channels: list
    deter_segments: list

    def best_view(self, actor_pos, face_m: float = dp.FACE_HEIGHT_M):
        """Best channel view of a target: returns dict or None if out of FOV."""
        ground = math.dist(self.pos, actor_pos)
        brg = bearing_deg(self.pos, actor_pos)
        pitch = dp.pitch_deg(self.height_m, ground, face_m)
        best = None
        for ch in self.channels:
            if not ch.covers(brg - ch.boresight_deg):
                continue
            h_px = dp.SENSORS_H_PX[ch.sensor]
            dens = dp.px_per_m(h_px, ch.hfov_deg, ground)
            level = "none"
            for lv in dp.DORI_ORDER:
                if dens >= dp.DORI_PX_PER_M[lv]:
                    level = lv
                    break
            # Identity-grade capture needs acceptable pitch. Door nodes are at
            # eye level so pitch is near zero and never gates.
            if level in ("validate", "identify") and pitch > dp.PITCH_USABLE_DEG:
                level = "recognize"
            if best is None or dens > best["px_per_m"]:
                best = {
                    "channel": ch.name,
                    "px_per_m": round(dens, 1),
                    "dori_level": level,
                    "ground_m": round(ground, 2),
                    "distance_m": round(dp.los_from_ground(self.height_m, ground, face_m), 2),
                    "bearing_deg": round(norm_deg(brg - self.facing_deg), 1),
                    "pitch_deg": round(pitch, 1),
                }
        # Anything beyond the detect ring of every channel is not a detection.
        if best is not None and best["dori_level"] == "none":
            return None
        return best


@dataclass
class House:
    site_id: str
    name: str
    footprint: list
    eave_m: float
    segments: list       # roofline segments (id, from, to, leds)
    zones: list          # named polys
    nodes: list

    def zone_at(self, pt) -> str:
        for z in self.zones:
            if point_in_poly(pt, z["poly"]):
                return z["id"]
        return "yard"

    def node_map(self) -> dict:
        return {n.id: n for n in self.nodes}


def load_house(scan_path: str | Path) -> House:
    raw = json.loads(Path(scan_path).read_text())
    nodes = []
    for nd in raw["nodes"]:
        channels = []
        wide = nd.get("wide")
        if wide:
            channels.append(Channel(
                name="door" if nd["kind"] == "door" else "wide",
                sensor=wide["sensor"], hfov_deg=wide["hfov_deg"],
                boresight_deg=nd["facing_deg"],
            ))
        ident = nd.get("identity")
        if ident:
            channels.append(Channel(
                name="identity", sensor=ident["sensor"], hfov_deg=ident["hfov_deg"],
                boresight_deg=bearing_deg(nd["pos"], ident["aim"]),
            ))
        for ch in channels:
            h_px = dp.SENSORS_H_PX[ch.sensor]
            ch.rings_ground_m = {
                lv: round(dp.reach_m(h_px, ch.hfov_deg, dp.DORI_PX_PER_M[lv]), 2)
                for lv in dp.DORI_ORDER
            }
        nodes.append(Node(
            id=nd["id"], kind=nd["kind"], pos=tuple(nd["pos"]),
            height_m=nd["height_m"], facing_deg=nd["facing_deg"],
            channels=channels, deter_segments=nd.get("deter_segments", []),
        ))
    return House(
        site_id=raw["site_id"], name=raw["name"], footprint=raw["footprint"],
        eave_m=raw["eave_height_m"], segments=raw["roofline_segments"],
        zones=raw["zones"], nodes=nodes,
    )


@dataclass
class Actor:
    id: str
    cls: str                     # person | vehicle | animal | package | unknown
    waypoints: list              # [{"pos": [x, y], "pause_s": 0}]
    speed_mps: float
    start_s: float = 0.0
    on_deter_goto: list = None   # flee target; None means ignores deter
    label: str = ""
    # runtime state
    pos: tuple = None
    wp_i: int = 0
    pause_left: float = 0.0
    active: bool = False
    done: bool = False
    fleeing: bool = False

    def spawn(self):
        self.pos = tuple(self.waypoints[0]["pos"])
        self.wp_i = 1
        self.pause_left = self.waypoints[0].get("pause_s", 0.0)
        self.active = True

    def flee(self):
        if self.on_deter_goto and not self.fleeing:
            self.fleeing = True
            self.waypoints = [{"pos": list(self.pos)}, {"pos": self.on_deter_goto}]
            self.wp_i = 1
            self.pause_left = 0.0
            self.speed_mps *= 2.5

    def step(self, dt: float):
        if not self.active or self.done:
            return
        if self.pause_left > 0:
            self.pause_left = max(0.0, self.pause_left - dt)
            return
        if self.wp_i >= len(self.waypoints):
            self.active = False
            self.done = True
            return
        target = self.waypoints[self.wp_i]["pos"]
        dist = math.dist(self.pos, target)
        step = self.speed_mps * dt
        if step >= dist:
            self.pos = tuple(target)
            self.pause_left = self.waypoints[self.wp_i].get("pause_s", 0.0)
            self.wp_i += 1
            if self.wp_i >= len(self.waypoints) and self.pause_left <= 0:
                self.active = False
                self.done = True
        else:
            f = step / dist
            self.pos = (self.pos[0] + (target[0] - self.pos[0]) * f,
                        self.pos[1] + (target[1] - self.pos[1]) * f)
