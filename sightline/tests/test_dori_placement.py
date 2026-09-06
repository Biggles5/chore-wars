"""Pin dori_placement.py to the audited optics numbers from the build spec.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "hardware"))

import dori_placement as dp  # noqa: E402

EAVE_20FT = 6.1
EAVE_10FT = 3.05


def test_identify_reach_105deg_8mp():
    # Audited: 105 degree 8MP holds identify density only inside 5.9 m.
    assert dp.reach_m(3840, 105, 250) == pytest.approx(5.9, abs=0.05)


def test_identify_reach_60deg_8mp():
    # Audited: 60 degree 8MP reaches identify density at 13.3 m.
    assert dp.reach_m(3840, 60, 250) == pytest.approx(13.3, abs=0.05)


def test_identify_reach_60deg_12mp():
    # Audited: 12MP (4608 px horizontal, DECISIONS.md D-004) reaches about 16 m.
    assert dp.reach_m(dp.SENSORS_H_PX["12mp"], 60, 250) == pytest.approx(16.0, abs=0.1)


def test_pitch_30deg_boundary_at_20ft_eave():
    # Audited: at a 6.1 m eave, pitch <= 30 degrees only beyond about 7.6 m.
    assert dp.min_ground_for_pitch(EAVE_20FT, 30) == pytest.approx(7.62, abs=0.05)


def test_105deg_8mp_fails_identity_at_20ft_eave():
    # The whole identify ring sits at 37 to 42+ degrees of pitch: no hold window.
    p = dp.placement(EAVE_20FT, "8mp", 105)
    assert not p.identify_window_hold.exists
    ring = next(r for r in p.rings if r["level"] == "identify")
    assert 36.0 <= ring["pitch_at_edge_deg"] <= 43.0


def test_60deg_8mp_works_at_20ft_eave():
    # Identify ring edge at 13.3 m ground, about 19 degrees of pitch (audited "~19").
    p = dp.placement(EAVE_20FT, "8mp", 60)
    assert p.identify_window_hold.exists
    ring = next(r for r in p.rings if r["level"] == "identify")
    assert ring["ground_reach_m"] == pytest.approx(13.3, abs=0.05)
    assert 18.0 <= ring["pitch_at_edge_deg"] <= 20.0


def test_10ft_eave_benign_beyond_2p4m():
    assert dp.min_ground_for_pitch(EAVE_10FT, 30) == pytest.approx(2.34, abs=0.1)


def test_dori_thresholds_2025_rev():
    assert dp.DORI_PX_PER_M == {
        "validate": 500.0, "identify": 250.0, "recognize": 125.0,
        "observe": 62.5, "detect": 25.0,
    }


def test_dori_level_at_monotonic():
    assert dp.dori_level_at(3840, 60, 5.0) in ("validate", "identify")
    assert dp.dori_level_at(3840, 60, 13.0) == "identify"
    assert dp.dori_level_at(3840, 60, 20.0) == "recognize"
    assert dp.dori_level_at(3840, 60, 200.0) == "none"


def test_density_matches_reach_inverse():
    d = dp.reach_m(3840, 105, 250)
    assert dp.px_per_m(3840, 105, d) == pytest.approx(250.0, rel=1e-9)
