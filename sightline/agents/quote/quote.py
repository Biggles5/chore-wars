"""SightLine scan-to-kit quote agent.

Deterministic pricing engine: roofline geometry in, kit + price + install
time + DORI plan + per-terminal power check out. The agent wrapper is thin
by design; every number comes from shared modules (dori_placement,
power_budget) or the price book below, never from a model.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

_HW = Path(__file__).resolve().parents[2] / "hardware"
sys.path.insert(0, str(_HW))
sys.path.insert(0, str(_HW / "electronics"))
import dori_placement as dp  # noqa: E402
import power_budget as pb  # noqa: E402

# Price book, all install-target retail (est.)
PRICE = {
    "track_node": 279.0,
    "door_node": 179.0,
    "injection_kit": 89.0,
    "gateway": 199.0,
    "retrofit_base_install": 249.0,     # first node incl. tap + provision
    "retrofit_addl_install": 79.0,      # each additional node
    "rail48_per_ft": 14.0,              # SKU 2 factory-cut rail with bus (est.)
    "rail48_base_install": 449.0,
}
SKU1_TARGET = (1299.0, 1799.0)

# Coverage heuristics: one track node covers about 55 linear ft of roofline
# with its 110 degree wide channel at typical setbacks (est.); every quote
# gets a door node; corners beyond 4 add a node each (wrap coverage).
FT_PER_TRACK_NODE = 55.0

INSTALL_MIN = {
    "retrofit_first": 75, "retrofit_addl": 30, "injection": 20,
    "gateway": 20, "aim_per_node": 10,
    "rail48_base": 60, "rail48_per_100ft": 35, "rail48_per_node": 10,
}


def node_count(roofline_ft: float, corners: int) -> int:
    base = max(2, math.ceil(roofline_ft / FT_PER_TRACK_NODE))
    extra = max(0, corners - 4) // 2
    return base + extra


def dori_plan(eave_heights_ft: list) -> list:
    """Per-eave placement verdicts using the shared optics module."""
    plan = []
    for ft in eave_heights_ft:
        eave_m = ft * 0.3048
        p = dp.placement(eave_m, "12mp", 60)
        wide = dp.placement(eave_m, "8mp", 110)
        ident = next(r for r in p.rings if r["level"] == "identify")
        plan.append({
            "eave_ft": ft,
            "identity_channel": {
                "sensor": "12mp", "hfov_deg": 60,
                "identify_ring_ft": round(ident["ground_reach_m"] / 0.3048, 1),
                "aim_window_ft": [round(p.identify_window_hold.near_m / 0.3048, 1),
                                  round(p.identify_window_hold.far_m / 0.3048, 1)]
                if p.identify_window_hold.exists else None,
                "verdict": p.verdict,
            },
            "wide_channel_detect_ft": round(
                next(r for r in wide.rings if r["level"] == "detect")["ground_reach_m"] / 0.3048, 0),
        })
    return plan


def quote(roofline_ft: float, corners: int, eave_heights_ft: list,
          brand: str = "gemstone", led_load_w_per_terminal: float = 40.0,
          node_run_ft: float = 50.0) -> dict:
    """The quote. brand 'sightline48' prices SKU 2; everything else is the
    SKU 1 retrofit against that brand's rail rules."""
    n_track = node_count(roofline_ft, corners)
    n_door = 1
    is_48 = brand == "sightline48"
    b = pb.BRANDS[brand]

    terminals = []
    injections = 0
    if not is_48:
        n_terminals = b["terminals"]
        for i in range(n_track):
            term = (i % n_terminals) + 1
            same_terminal_nodes = i // n_terminals
            if same_terminal_nodes > 0:
                # one camera node per terminal: everything past that injects
                injections += 1
                terminals.append({"terminal": term, "node": f"track-{i+1}",
                                  "needs_injection": True,
                                  "notes": ["second node on this terminal: rule is one per terminal, feed from injection kit"]})
                continue
            chk = pb.check_terminal(brand, term, led_load_w_per_terminal,
                                    node_kind="track", node_run_ft=node_run_ft)
            if chk.needs_injection:
                injections += 1
            terminals.append({"terminal": term, "node": f"track-{i+1}",
                              "needs_injection": chk.needs_injection,
                              "v_at_node": chk.v_at_node,
                              "headroom_w": chk.headroom_w,
                              "notes": chk.notes})
        power = {"rail_v": b["rail_v"], "terminals": terminals,
                 "injection_kits": injections}
    else:
        power = {"rail_v": 48,
                 "budget": pb.rail48_budget(n_track, n_door,
                                            pb.led_load_estimate_w(roofline_ft, 48, duty=0.85))}

    kit = [
        {"item": "SightLine track node (dual sensor)", "qty": n_track,
         "unit": PRICE["track_node"]},
        {"item": "SightLine door node", "qty": n_door, "unit": PRICE["door_node"]},
        {"item": "Gateway (correlator + storage)", "qty": 1, "unit": PRICE["gateway"]},
    ]
    if not is_48 and injections:
        kit.append({"item": "Power injection kit", "qty": injections,
                    "unit": PRICE["injection_kit"]})
    if is_48:
        kit.append({"item": "48V factory-cut rail with blind-mate bus",
                    "qty": round(roofline_ft), "unit": PRICE["rail48_per_ft"]})

    hardware_total = sum(k["qty"] * k["unit"] for k in kit)
    if is_48:
        install = PRICE["rail48_base_install"]
        minutes = (INSTALL_MIN["rail48_base"]
                   + INSTALL_MIN["rail48_per_100ft"] * roofline_ft / 100.0
                   + INSTALL_MIN["rail48_per_node"] * (n_track + n_door)
                   + INSTALL_MIN["gateway"])
    else:
        install = (PRICE["retrofit_base_install"]
                   + PRICE["retrofit_addl_install"] * (n_track + n_door - 1))
        minutes = (INSTALL_MIN["retrofit_first"]
                   + INSTALL_MIN["retrofit_addl"] * (n_track + n_door - 1)
                   + INSTALL_MIN["injection"] * injections
                   + INSTALL_MIN["aim_per_node"] * n_track
                   + INSTALL_MIN["gateway"])

    total = round(hardware_total + install, 2)
    out = {
        "brand": brand,
        "inputs": {"roofline_ft": roofline_ft, "corners": corners,
                   "eave_heights_ft": eave_heights_ft,
                   "node_run_ft": node_run_ft,
                   "led_load_w_per_terminal": led_load_w_per_terminal},
        "kit": kit,
        "nodes": {"track": n_track, "door": n_door},
        "hardware_total": round(hardware_total, 2),
        "install": install,
        "total_installed": total,
        "install_time_hr": round(minutes / 60.0, 1),
        "under_3hr_target": (minutes / 60.0) < 3.0 if is_48 else None,
        "in_sku1_band": (SKU1_TARGET[0] <= total <= SKU1_TARGET[1]) if not is_48 else None,
        "power": power,
        "dori_plan": dori_plan(eave_heights_ft),
        "all_estimates": True,
    }
    return out
