"""SightLine DORI placement math.

Given eave height, lens FOV, and sensor resolution, returns the DORI rings
(validate/identify/recognize/observe/detect), the pitch-limited capture
window, and a placement verdict. This is the single source of optics truth:
the simulator, the quote agent, and the install guides all import it.

Model (see DECISIONS.md D-004, D-005):
- Pixel density at a target: h_px / (2 * d * tan(hfov/2)), d = ground
  (horizontal) distance to the target. Thin-lens, distortion-free
  approximation. The audited anchors treat ring distances as ground
  distances (pitch 37 deg at the 5.9 m ring edge of a 6.1 m eave), so the
  model does too.
- Pitch: atan((eave_m - face_m) / ground_m), face height 1.7 m (est.).
- Face recognition holds to 30 degrees downward pitch, usable to 40.
- DORI thresholds (px/m): Validate 500 (2025 rev), Identify 250,
  Recognize 125, Observe 62.5, Detect 25.

Audited anchors this module must reproduce (pinned by tests/test_dori_placement.py):
- 105 deg 8MP: identify reach 5.9 m. At a 6.1 m eave that whole ring sits at
  37 to 42+ degrees of pitch, so the lens fails for identity.
- 60 deg 8MP: identify reach 13.3 m, pitch about 19 degrees at the ring edge.
- 60 deg 12MP (4608 px): identify reach 16 m.
- 6.1 m eave: pitch <= 30 degrees beyond 7.6 m ground distance.
- 3.05 m eave (10 ft): benign beyond about 2.4 m.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass, field, asdict

DORI_PX_PER_M = {
    "validate": 500.0,
    "identify": 250.0,
    "recognize": 125.0,
    "observe": 62.5,
    "detect": 25.0,
}
DORI_ORDER = ["validate", "identify", "recognize", "observe", "detect"]

FACE_HEIGHT_M = 1.7  # target face height above grade (est.)
PITCH_HOLD_DEG = 30.0    # face recognition holds to this downward pitch
PITCH_USABLE_DEG = 40.0  # usable to this, degraded

# Common sensor horizontal pixel counts. "12mp" is the 16:9 security SKU,
# 4608 x 2592 (see DECISIONS.md D-004).
SENSORS_H_PX = {
    "8mp": 3840,
    "12mp": 4608,
}


def px_per_m(h_px: int, hfov_deg: float, ground_m: float) -> float:
    """Horizontal pixel density (px/m) on a target at ground distance."""
    if ground_m <= 0:
        return float("inf")
    return h_px / (2.0 * ground_m * math.tan(math.radians(hfov_deg) / 2.0))


def reach_m(h_px: int, hfov_deg: float, density_px_per_m: float) -> float:
    """Ground distance at which density falls to the given threshold."""
    return h_px / (2.0 * density_px_per_m * math.tan(math.radians(hfov_deg) / 2.0))


def pitch_deg(eave_m: float, ground_m: float, face_m: float = FACE_HEIGHT_M) -> float:
    """Downward pitch from the node to a face at ground distance ground_m."""
    dz = max(eave_m - face_m, 0.0)
    if ground_m <= 0:
        return 90.0
    return math.degrees(math.atan2(dz, ground_m))


def min_ground_for_pitch(eave_m: float, pitch_limit_deg: float = PITCH_HOLD_DEG,
                         face_m: float = FACE_HEIGHT_M) -> float:
    """Closest ground distance where pitch stays within the limit."""
    dz = max(eave_m - face_m, 0.0)
    if dz == 0:
        return 0.0
    return dz / math.tan(math.radians(pitch_limit_deg))


def los_from_ground(eave_m: float, ground_m: float, face_m: float = FACE_HEIGHT_M) -> float:
    """Line-of-sight distance from the node to a face at ground distance ground_m."""
    dz = max(eave_m - face_m, 0.0)
    return math.hypot(ground_m, dz)


@dataclass
class Ring:
    level: str
    threshold_px_per_m: float
    los_reach_m: float
    ground_reach_m: float
    pitch_at_edge_deg: float


@dataclass
class CaptureWindow:
    """Ground interval where identify density AND acceptable pitch coexist."""
    near_m: float
    far_m: float
    exists: bool
    pitch_limit_deg: float


@dataclass
class Placement:
    eave_m: float
    sensor_h_px: int
    hfov_deg: float
    face_m: float
    rings: list = field(default_factory=list)
    identify_window_hold: CaptureWindow = None
    identify_window_usable: CaptureWindow = None
    verdict: str = ""

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2)


def dori_level_at(h_px: int, hfov_deg: float, distance_m: float) -> str:
    d = px_per_m(h_px, hfov_deg, distance_m)
    for level in DORI_ORDER:
        if d >= DORI_PX_PER_M[level]:
            return level
    return "none"


def identify_window(eave_m: float, h_px: int, hfov_deg: float,
                    pitch_limit_deg: float = PITCH_HOLD_DEG,
                    face_m: float = FACE_HEIGHT_M) -> CaptureWindow:
    """Ground interval where px/m >= 250 and pitch <= limit. Empty if none."""
    near = min_ground_for_pitch(eave_m, pitch_limit_deg, face_m)
    far = reach_m(h_px, hfov_deg, DORI_PX_PER_M["identify"])
    exists = far > near
    return CaptureWindow(near_m=round(near, 2), far_m=round(far, 2),
                         exists=exists, pitch_limit_deg=pitch_limit_deg)


def placement(eave_m: float, sensor: str | int, hfov_deg: float,
              face_m: float = FACE_HEIGHT_M) -> Placement:
    """Full placement report for one channel at one eave height."""
    h_px = SENSORS_H_PX[sensor] if isinstance(sensor, str) else int(sensor)
    rings = []
    for level in DORI_ORDER:
        ground = reach_m(h_px, hfov_deg, DORI_PX_PER_M[level])
        rings.append(Ring(
            level=level,
            threshold_px_per_m=DORI_PX_PER_M[level],
            los_reach_m=round(los_from_ground(eave_m, ground, face_m), 2),
            ground_reach_m=round(ground, 2),
            pitch_at_edge_deg=round(pitch_deg(eave_m, ground, face_m), 1) if ground > 0 else 90.0,
        ))
    hold = identify_window(eave_m, h_px, hfov_deg, PITCH_HOLD_DEG, face_m)
    usable = identify_window(eave_m, h_px, hfov_deg, PITCH_USABLE_DEG, face_m)
    if hold.exists:
        verdict = ("identity capable: aim the chokepoint between "
                   f"{hold.near_m} and {hold.far_m} m ground distance")
    elif usable.exists:
        verdict = ("marginal: identify density only at degraded pitch (30 to 40 deg), "
                   f"usable window {usable.near_m} to {usable.far_m} m")
    else:
        verdict = "fails for identity at this eave: identify ring is entirely inside the pitch limit"
    p = Placement(eave_m=eave_m, sensor_h_px=h_px, hfov_deg=hfov_deg, face_m=face_m,
                  rings=[asdict(r) for r in rings],
                  identify_window_hold=hold, identify_window_usable=usable,
                  verdict=verdict)
    return p


def main() -> None:
    ap = argparse.ArgumentParser(description="SightLine DORI placement calculator")
    ap.add_argument("--eave-ft", type=float, help="eave height in feet")
    ap.add_argument("--eave-m", type=float, help="eave height in meters")
    ap.add_argument("--sensor", default="8mp", help="8mp, 12mp, or horizontal pixel count")
    ap.add_argument("--hfov", type=float, default=110.0, help="horizontal FOV in degrees")
    args = ap.parse_args()
    if args.eave_m is None and args.eave_ft is None:
        ap.error("provide --eave-m or --eave-ft")
    eave = args.eave_m if args.eave_m is not None else args.eave_ft * 0.3048
    sensor = args.sensor if args.sensor in SENSORS_H_PX else int(args.sensor)
    print(placement(eave, sensor, args.hfov).to_json())


if __name__ == "__main__":
    main()
