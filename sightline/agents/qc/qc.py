"""QC agent: photo review against install spec, gate by gate.

Mock mode (required, default): fixture "photos" are SVG renders carrying a
machine-readable measurement block (what a vision model would extract from
the real photo). The judgment layer is identical either way: measurements
against spec thresholds, pass or fail with plain-language redo
instructions. Claude vision mode drops in behind `extract()` later; the
spec table and verdict logic never change.

Warranty activation requires every gate passed (ops/runbook.py).

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

SPEC = {
    "rail_level_spacing": {
        "thresholds": {"tilt_deg": 1.5, "spacing_var_pct": 8.0},
        "redo": {
            "tilt_deg": "Rail is off level by {v} degrees (limit {t}). Loosen the segment clips, re-set against the chalk line or the AR level guide, re-clip, reshoot.",
            "spacing_var_pct": "Module spacing varies {v}% (limit {t}%). Re-seat the snap-ins against the label marks; uneven spacing reads as sloppy from the street and it is the first thing an HOA sees.",
        },
    },
    "gasket_seated": {
        "thresholds": {"gap_mm": 0.5},
        "redo": {
            "gap_mm": "Visible gasket gap of {v} mm (limit {t} mm). Open the housing, check the gasket is not pinched or rolled, re-seat, torque the gland, reshoot the joint close-up. Water ingress here is the number one callback in the old install model; this gate exists to kill it.",
        },
    },
    "connector_clicked": {
        "thresholds": {"latch_engaged": True, "conductor_exposed_mm": 1.0},
        "redo": {
            "latch_engaged": "The connector latch is not fully engaged. Push until it clicks, tug-test it, reshoot with the latch window visible.",
            "conductor_exposed_mm": "{v} mm of exposed conductor at the connector (limit {t} mm). Re-strip to length or re-seat the wire so no copper shows, then reshoot.",
        },
    },
    "node_aim": {
        "thresholds": {"azimuth_err_deg": 5.0, "cant_err_deg": 2.0},
        "redo": {
            "azimuth_err_deg": "Azimuth is {v} degrees off the planned chokepoint (limit {t}). Open the app aim view, align the reticle to the chokepoint ring, re-lock.",
            "cant_err_deg": "Cant is {v} degrees off plan (limit {t}). The identify window is math, not vibes: re-set the cant screw to the planned angle and reshoot the aim screen.",
        },
    },
    "controller_wiring": {
        "thresholds": {"meter_v": 0.5, "strain_relief": True},
        "redo": {
            "meter_v": "Meter shows {v}V at the terminal (must read under {t}V before work). Kill the correct supply and reshoot with the meter leads on the terminal in frame.",
            "strain_relief": "No strain relief visible on the tap. Add the clamp, dress the pair, reshoot the terminal area.",
        },
    },
}


def extract(photo: str) -> dict:
    """Measurement extraction. Mock mode parses the SVG's qc-metadata block
    (the structured output a vision model would produce from the pixels)."""
    text = photo
    p = Path(photo)
    try:
        if p.exists():
            text = p.read_text()
    except OSError:
        pass  # long string, not a path
    m = re.search(r'<metadata id="qc">(.*?)</metadata>', text, re.S)
    if not m:
        raise ValueError("no measurement block: photo unreadable or wrong subject")
    return json.loads(m.group(1))


def review(photo: str, check: str) -> dict:
    """One gate review: pass, or fail with redo instructions."""
    if check not in SPEC:
        raise ValueError(f"unknown check {check}")
    data = extract(photo)
    if data.get("check") != check:
        return {"check": check, "passed": False, "measurements": data,
                "verdict": "wrong subject: this photo is for a different gate",
                "redo": [f"Shoot the {check.replace('_', ' ')} reference view "
                         f"shown in the step card and resubmit."]}
    spec = SPEC[check]
    failures = []
    for key, limit in spec["thresholds"].items():
        v = data.get(key)
        if isinstance(limit, bool):
            if bool(v) is not limit:
                failures.append((key, v, limit))
        else:
            if v is None or float(v) > limit:
                failures.append((key, v, limit))
    passed = not failures
    redo = [spec["redo"][k].format(v=v, t=t) for k, v, t in failures]
    return {
        "check": check,
        "passed": passed,
        "measurements": {k: data.get(k) for k in spec["thresholds"]},
        "verdict": "pass" if passed else "fail: " + "; ".join(k for k, _, _ in failures),
        "redo": redo,
        "mode": "mock",
    }


def review_job(photos: dict) -> dict:
    """All gates for a job: {check: photo}. Warranty eligibility comes back."""
    results = {c: review(p, c) for c, p in photos.items()}
    missing = [c for c in SPEC if c not in results]
    all_passed = not missing and all(r["passed"] for r in results.values())
    return {"gates": results, "missing": missing,
            "warranty_eligible": all_passed}
