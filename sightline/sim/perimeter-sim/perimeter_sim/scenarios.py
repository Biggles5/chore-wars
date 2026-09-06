"""Scripted scenarios for the perimeter simulator.

Each scenario is a scripted cast of actors over a simulated clock. The
timescale compresses hours of night into seconds of wall time; event
timestamps always use the simulated clock so downstream consumers see
2:14 AM, not the developer's laptop time.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from .model import Actor


@dataclass
class Scenario:
    name: str
    description: str
    start_clock: str          # "HH:MM" simulated local time
    duration_s: float         # simulated seconds
    timescale: float          # sim seconds per wall second
    armed: bool               # deter armed (night/away modes)
    actors: list = field(default_factory=list)


def _wp(*points):
    out = []
    for p in points:
        if len(p) == 3:
            out.append({"pos": [p[0], p[1]], "pause_s": p[2]})
        else:
            out.append({"pos": [p[0], p[1]]})
    return out


def build_scenarios() -> dict:
    s = {}

    s["quiet-night"] = Scenario(
        name="quiet-night",
        description="Eight hours of nothing much: a passing car, a cat, a deer at 3 AM. No deter events. This is the baseline that proves the system stays quiet.",
        start_clock="22:00", duration_s=8 * 3600, timescale=600, armed=True,
        actors=[
            Actor(id="car-pass", cls="vehicle", label="passing car",
                  waypoints=_wp((-6, -16), (22, -16)), speed_mps=8.0, start_s=1800),
            Actor(id="cat", cls="animal", label="neighborhood cat",
                  waypoints=_wp((-6, -2), (3, -2, 20), (3, -6), (-6, -6)),
                  speed_mps=1.0, start_s=3 * 3600),
            Actor(id="deer", cls="animal", label="deer",
                  waypoints=_wp((0, 18), (8, 16, 60), (16, 18)),
                  speed_mps=0.7, start_s=5 * 3600),
        ],
    )

    s["car-prowler-0214"] = Scenario(
        name="car-prowler-0214",
        description="2:14 AM. A car stops on the street, a prowler works the driveway toward the porch, deter fires, prowler flees, car leaves. The flagship demo.",
        start_clock="02:10", duration_s=360, timescale=12, armed=True,
        actors=[
            Actor(id="prowl-car", cls="vehicle", label="prowler's car",
                  waypoints=_wp((22, -16), (14, -15.5, 260), (-6, -16)),
                  speed_mps=6.0, start_s=0),
            Actor(id="prowler", cls="person", label="prowler",
                  waypoints=_wp((14, -14), (15, -8, 20), (14, -4, 15),
                                (9, -2.5, 10), (6.5, -1.5, 30), (14, -14)),
                  speed_mps=1.3, start_s=236, on_deter_goto=[20, -16]),
        ],
    )

    s["porch-pirate"] = Scenario(
        name="porch-pirate",
        description="2:05 PM. A package sits on the porch. Someone walks straight up, grabs it, and leaves. Deter fires in package-protect mode.",
        start_clock="14:05", duration_s=300, timescale=10, armed=True,
        actors=[
            Actor(id="package", cls="package", label="delivered package",
                  waypoints=_wp((6.8, -1.2, 600),), speed_mps=0.0, start_s=0),
            Actor(id="pirate", cls="person", label="porch pirate",
                  waypoints=_wp((2, -15), (5, -4), (6.5, -1.5, 12), (0, -15)),
                  speed_mps=1.6, start_s=20, on_deter_goto=[-4, -17]),
        ],
    )

    s["party-arrivals"] = Scenario(
        name="party-arrivals",
        description="7:30 PM, disarmed. Guests arrive: a car parks in the driveway, three people walk to the door. The system watches, greets, and never deters.",
        start_clock="19:30", duration_s=600, timescale=10, armed=False,
        actors=[
            Actor(id="guest-car", cls="vehicle", label="guest car",
                  waypoints=_wp((22, -16), (14, -8, 500)), speed_mps=4.0, start_s=10),
            Actor(id="guest-1", cls="person", label="guest",
                  waypoints=_wp((14, -8), (9, -3), (6.5, -1.2, 400)),
                  speed_mps=1.2, start_s=60),
            Actor(id="guest-2", cls="person", label="guest",
                  waypoints=_wp((14, -8), (9, -3.5), (7.0, -1.6, 380)),
                  speed_mps=1.1, start_s=75),
            Actor(id="guest-3", cls="person", label="guest walking up",
                  waypoints=_wp((-6, -15), (4, -12), (6.5, -1.8, 300)),
                  speed_mps=1.4, start_s=180),
        ],
    )

    s["deer-3am"] = Scenario(
        name="deer-3am",
        description="3 AM deer in the back yard. Detected, classified, logged, ignored. No deter for animals, ever.",
        start_clock="03:00", duration_s=300, timescale=6, armed=True,
        actors=[
            Actor(id="deer", cls="animal", label="deer",
                  waypoints=_wp((0, 18), (6, 15, 90), (12, 16, 60), (16, 19)),
                  speed_mps=0.6, start_s=10),
        ],
    )

    s["mail-daily"] = Scenario(
        name="mail-daily",
        description="11:40 AM mail carrier. Familiar path, home mode, no deter. The daily pattern the narrator learns to summarize in one line.",
        start_clock="11:40", duration_s=240, timescale=8, armed=False,
        actors=[
            Actor(id="mail", cls="person", label="mail carrier",
                  waypoints=_wp((-6, -15), (4, -13), (6.5, -1.5, 8), (4, -13), (-6, -15)),
                  speed_mps=1.5, start_s=10),
        ],
    )

    return s


SCENARIOS = build_scenarios()
