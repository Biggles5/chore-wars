"""SightLine parametric CAD: CadQuery models for the four Phase 0 parts.

  python3 sightline_cad.py          builds all parts, exports STL + STEP
                                    into exports/

Parts:
  1. track_node_housing: dual-sensor module for the Gemstone 30mm-lens
     channel line. Every mating dimension is a named parameter because the
     channel specs are from published data (est.) and the first test print
     calibrates them.
  2. retrofit_clip: universal channel clip; parameter presets for
     Gemstone / Trimlight / JellyFish profiles.
  3. door_node_housing: slim jamb-mount housing for the eye-level node.
  4. bench_fixture: Phase 0 bench plate for the dev board, buck, and camera.

Print guidance: PETG or ASA, 0.2 mm layers, 4 walls for outdoor parts.
STEP files are the ODM handoff. Mechanical capture carries the load;
VHB tape is a seal only, never structure.

Decision record: CadQuery over OpenSCAD (DECISIONS.md D-010): native STEP
export and python parametrics that share the repo toolchain.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

from pathlib import Path

import cadquery as cq

EXPORT_DIR = Path(__file__).parent / "exports"

# ---------------------------------------------------------------- parameters
# Gemstone-class channel (published data, est.: calibrate on first print)
CHANNEL = {
    "gemstone": {"inner_w": 38.0, "lip": 3.5, "depth": 22.0},
    "trimlight": {"inner_w": 34.0, "lip": 3.0, "depth": 20.0},
    "jellyfish": {"inner_w": 36.0, "lip": 3.2, "depth": 21.0},
}

NODE = {
    "len": 52.0,          # <= 52 mm module constraint
    "w": 36.0,
    "h": 30.0,            # matches the 30 mm lens line visually
    "wall": 2.4,
    "wide_lens_d": 14.0,  # wide channel aperture
    "ident_lens_d": 16.0, # identity channel aperture
    "ident_cant_deg": 20.0,  # factory cant from the scan (parametric)
    "ir_d": 8.0,
    "gasket_w": 1.8,
    "gasket_d": 1.4,
    "gland_d": 12.5,      # M12 gland boss
}

DOOR = {"len": 110.0, "w": 16.0, "h": 24.0, "wall": 2.0, "lens_d": 12.0}

BENCH = {"l": 220.0, "w": 140.0, "t": 4.0, "hole_d": 3.4}


# ---------------------------------------------------------------- parts
def track_node_housing(channel: str = "gemstone") -> cq.Workplane:
    ch = CHANNEL[channel]
    L, W, H, wall = NODE["len"], NODE["w"], NODE["h"], NODE["wall"]

    body = cq.Workplane("XY").box(L, W, H)
    # hollow: open the back (installer side), keep the face
    body = body.faces("<Z").shell(-wall)

    # face apertures: wide channel centered left, identity right with cant
    face = body.faces(">Z").workplane()
    body = face.center(-L / 4, 0).hole(NODE["wide_lens_d"])
    # identity aperture: canted bore through the face
    cant = (
        cq.Workplane("XY")
        .center(L / 4, 0)
        .transformed(rotate=(0, NODE["ident_cant_deg"], 0),
                     offset=(0, 0, H / 2 - wall * 2))
        .circle(NODE["ident_lens_d"] / 2)
        .extrude(wall * 6)
    )
    body = body.cut(cant)
    # IR window
    body = body.faces(">Z").workplane().center(0, W / 2 - 8).hole(NODE["ir_d"])

    # gasket groove around the face perimeter
    groove = (
        cq.Workplane("XY")
        .rect(L - wall * 2 + NODE["gasket_w"], W - wall * 2 + NODE["gasket_w"])
        .rect(L - wall * 2 - NODE["gasket_w"], W - wall * 2 - NODE["gasket_w"])
        .extrude(NODE["gasket_d"])
        .translate((0, 0, H / 2 - NODE["gasket_d"]))
    )
    body = body.cut(groove)

    # channel wings: ride the track lips (mechanical capture)
    wing_w = (ch["inner_w"] - W) / 2 + ch["lip"]
    if wing_w > 1.0:
        for side in (-1, 1):
            wing = (
                cq.Workplane("XY")
                .box(L, wing_w, 3.0)
                .translate((0, side * (W / 2 + wing_w / 2 - 0.01),
                            -H / 2 + ch["depth"] - 1.5))
            )
            body = body.union(wing)

    # rear gland boss
    boss = (
        cq.Workplane("XY")
        .center(0, -W / 2 + 10)
        .circle(NODE["gland_d"] / 2 + wall)
        .extrude(6.0)
        .translate((0, 0, -H / 2 - 6.0 + 0.01))
    )
    body = body.union(boss)
    body = (
        body.faces("<Z").workplane(origin=(0, -W / 2 + 10))
        .hole(NODE["gland_d"])
    )
    return body


def retrofit_clip(channel: str = "gemstone") -> cq.Workplane:
    ch = CHANNEL[channel]
    w = ch["inner_w"] + 2 * ch["lip"] + 6.0
    clip = cq.Workplane("XY").box(30.0, w, 8.0)
    # channel opening
    clip = clip.cut(
        cq.Workplane("XY").box(30.0, ch["inner_w"], 6.0).translate((0, 0, 1.01)))
    # lip hooks
    for side in (-1, 1):
        hook = (
            cq.Workplane("XY")
            .box(30.0, ch["lip"], 2.0)
            .translate((0, side * (ch["inner_w"] / 2 - ch["lip"] / 2), 3.0))
        )
        clip = clip.union(hook)
    # node screw bosses
    clip = clip.faces("<Z").workplane().pushPoints([(-10, 0), (10, 0)]).hole(3.4)
    return clip


def door_node_housing() -> cq.Workplane:
    L, W, H, wall = DOOR["len"], DOOR["w"], DOOR["h"], DOOR["wall"]
    body = cq.Workplane("XY").box(L, W, H).faces("<Z").shell(-wall)
    body = body.faces(">Z").workplane().center(-L / 2 + 18, 0).hole(DOOR["lens_d"])
    body = body.faces(">Z").workplane().center(-L / 2 + 34, 0).hole(6.0)  # IR
    # jamb screw slots at both ends
    for x in (-L / 2 + 8, L / 2 - 8):
        body = body.faces(">Z").workplane().center(x, 0).slot2D(8.0, 3.6, 90).cutThruAll()
    return body


def bench_fixture() -> cq.Workplane:
    p = BENCH
    plate = cq.Workplane("XY").box(p["l"], p["w"], p["t"])
    holes = []
    # ESP32-S3 devkit (est. 63.5 x 25.4 hole pattern), buck, camera post, WAGO rail
    holes += [(-70 + dx, -40 + dy) for dx in (0, 63.5) for dy in (0, 25.4)]
    holes += [(40 + dx, -45 + dy) for dx in (0, 30) for dy in (0, 15)]   # buck
    holes += [(-70, 30), (-40, 30)]                                      # camera post
    holes += [(30, 35), (60, 35), (90, 35)]                              # WAGO strip
    plate = plate.faces(">Z").workplane().pushPoints(holes).hole(p["hole_d"])
    # corner feet
    plate = plate.faces(">Z").workplane().pushPoints(
        [(x, y) for x in (-p["l"] / 2 + 8, p["l"] / 2 - 8)
         for y in (-p["w"] / 2 + 8, p["w"] / 2 - 8)]).hole(4.5)
    return plate


PARTS = {
    "track_node_housing_gemstone": lambda: track_node_housing("gemstone"),
    "retrofit_clip_gemstone": lambda: retrofit_clip("gemstone"),
    "retrofit_clip_trimlight": lambda: retrofit_clip("trimlight"),
    "retrofit_clip_jellyfish": lambda: retrofit_clip("jellyfish"),
    "door_node_housing": door_node_housing,
    "bench_fixture": bench_fixture,
}


def build_all():
    EXPORT_DIR.mkdir(exist_ok=True)
    for name, fn in PARTS.items():
        part = fn()
        cq.exporters.export(part, str(EXPORT_DIR / f"{name}.stl"))
        cq.exporters.export(part, str(EXPORT_DIR / f"{name}.step"))
        print(f"exported {name} (.stl + .step)")


if __name__ == "__main__":
    build_all()
