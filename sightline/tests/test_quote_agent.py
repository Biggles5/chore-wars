"""Quote agent evals plus power-budget invariants.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "agents" / "quote"))
sys.path.insert(0, str(ROOT / "hardware" / "electronics"))

import power_budget as pb  # noqa: E402
import quote as q  # noqa: E402

CASES = json.loads(
    (ROOT / "agents" / "quote" / "evals" / "cases.json").read_text())["cases"]


@pytest.mark.parametrize("case", CASES, ids=[c["name"] for c in CASES])
def test_quote_case(case):
    out = q.quote(**case["input"])
    exp = case["expect"]
    if "track_nodes" in exp:
        assert out["nodes"]["track"] == exp["track_nodes"]
    if "door_nodes" in exp:
        assert out["nodes"]["door"] == exp["door_nodes"]
    if "in_sku1_band" in exp:
        assert out["in_sku1_band"] is exp["in_sku1_band"], out["total_installed"]
    if "injection_kits" in exp:
        assert out["power"]["injection_kits"] == exp["injection_kits"]
    if "rail_v" in exp:
        assert out["power"]["rail_v"] == exp["rail_v"]
    if "under_3hr_target" in exp:
        assert out["under_3hr_target"] is exp["under_3hr_target"], out["install_time_hr"]
    if "headroom_meets_45pct" in exp:
        assert out["power"]["budget"]["meets_45pct_target"] is exp["headroom_meets_45pct"]
    if "note_contains" in exp:
        notes = " ".join(n for t in out["power"]["terminals"] for n in t["notes"])
        assert exp["note_contains"] in notes
    assert out["all_estimates"] is True


def test_one_node_per_terminal_rule():
    # 6 nodes on a 4-terminal Gemstone box: exactly 2 must inject
    out = q.quote(roofline_ft=320, corners=8, eave_heights_ft=[20], brand="gemstone")
    assert out["nodes"]["track"] > 4
    injected = [t for t in out["power"]["terminals"] if t["needs_injection"]]
    assert len(injected) == out["power"]["injection_kits"]
    assert out["nodes"]["track"] - 4 == len(
        [t for t in injected if "one per terminal" in " ".join(t["notes"])])


def test_voltage_drop_known_value():
    # 12W at 12V over 75 ft of 18 AWG: 1A x (150 ft x 6.385 ohm/kft) = 0.96V
    assert pb.voltage_drop_v(12, 12, 75, 18) == pytest.approx(0.958, abs=0.01)


def test_node_never_exceeds_ceiling():
    chk = pb.check_terminal("gemstone", 1, led_load_w=40,
                            node_kind="track", node_run_ft=50)
    assert chk.node_draw_w == pb.NODE_CEILING_W  # budgeted at the ceiling


def test_buck_window_guard():
    # absurd run: node voltage collapses below the 9V buck floor -> injection
    chk = pb.check_terminal("gemstone", 1, led_load_w=10,
                            node_kind="track", node_run_ft=300)
    assert chk.needs_injection


def test_rail48_headroom_target():
    b = pb.rail48_budget(3, 1, led_load_w=150)
    assert b["ok"] and b["meets_45pct_target"]


def test_dori_plan_matches_shared_module():
    out = q.quote(roofline_ft=120, corners=4, eave_heights_ft=[20], brand="gemstone")
    plan = out["dori_plan"][0]
    # 12MP 60 deg at a 20 ft eave: identify ring about 52 ft (16 m)
    assert plan["identity_channel"]["identify_ring_ft"] == pytest.approx(52.4, abs=0.5)
    assert plan["identity_channel"]["aim_window_ft"] is not None
