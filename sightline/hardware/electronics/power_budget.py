"""SightLine power budget math. One module, used by the quote agent, the
install guides, and docs/architecture/power.md. Everything NEC Class 2.

Ground rules (section 0 of the build spec, not re-litigated):
- Cameras are continuous loads. They never borrow the lights' duty-cycle
  oversubscription.
- 12V retrofit: 1 camera node per 5A terminal at a 12W ceiling, runs
  <= 75 ft on 18 AWG, else local injection.
- Retrofit node: 9 to 56V wide-input buck, taps POWER ONLY, buffers the
  data line, never loads the WS2811-family daisy chain.
- 48V clean-sheet rail: blind-mate bus, 3+ nodes with ~45% headroom on a
  384W supply.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict

# Copper resistance, ohms per 1000 ft, one conductor, 20 C (est.)
AWG_OHMS_PER_1000FT = {18: 6.385, 16: 4.016, 14: 2.525, 12: 1.588}

NODE_DRAW_W = {
    "track": 7.5,     # dual-sensor node, continuous, IR on (est.)
    "track_peak": 12.0,  # heater duty + IR + capture burst ceiling
    "door": 4.0,      # door node continuous (est.)
}
NODE_CEILING_W = 12.0          # hard per-node budget on 12V retrofit
RETROFIT_MAX_RUN_FT = 75.0     # 18 AWG at 12V before injection
BUCK_INPUT_RANGE_V = (9.0, 56.0)
BUCK_EFFICIENCY = 0.90         # >90% target

# Brand rail profiles for retrofit (from the incumbent audit)
BRANDS = {
    "gemstone":  {"rail_v": 12, "terminal_a": 5.0, "terminal_w": 60.0,
                  "terminals": 4, "supply_w": 400.0},
    "trimlight": {"rail_v": 12, "terminal_a": 5.0, "terminal_w": 60.0,
                  "terminals": 4, "supply_w": 240.0},
    "jellyfish": {"rail_v": 48, "terminal_a": 8.0, "terminal_w": 384.0,
                  "terminals": 1, "supply_w": 384.0},
    "oelo":      {"rail_v": 36, "terminal_a": 5.0, "terminal_w": 180.0,
                  "terminals": 6, "supply_w": 360.0},
    "everlights": {"rail_v": 24, "terminal_a": 5.0, "terminal_w": 120.0,
                   "terminals": 2, "supply_w": 240.0},
    "govee":     {"rail_v": 24, "terminal_a": 5.0, "terminal_w": 120.0,
                  "terminals": 2, "supply_w": 240.0},
    "sightline48": {"rail_v": 48, "terminal_a": 8.0, "terminal_w": 384.0,
                    "terminals": 1, "supply_w": 384.0},
}


def voltage_drop_v(load_w: float, rail_v: float, run_ft: float, awg: int = 18) -> float:
    """Round-trip voltage drop for a load at the end of a run."""
    ohms = AWG_OHMS_PER_1000FT[awg] * (run_ft * 2.0) / 1000.0
    amps = load_w / rail_v
    return amps * ohms


def voltage_at_node(load_w: float, rail_v: float, run_ft: float, awg: int = 18) -> float:
    return rail_v - voltage_drop_v(load_w, rail_v, run_ft, awg)


def drop_table(rail_v: float, load_w: float, awgs=(18, 16), runs=(25, 50, 75, 100, 150)) -> list:
    """Voltage drop table rows for the docs. Percent drop of nominal rail."""
    rows = []
    for awg in awgs:
        for run in runs:
            vd = voltage_drop_v(load_w, rail_v, run, awg)
            rows.append({"awg": awg, "run_ft": run, "rail_v": rail_v,
                         "load_w": load_w, "drop_v": round(vd, 2),
                         "drop_pct": round(100 * vd / rail_v, 1),
                         "v_at_node": round(rail_v - vd, 2)})
    return rows


@dataclass
class TerminalCheck:
    terminal: int
    rail_v: float
    led_load_w: float
    node_kind: str = None
    node_draw_w: float = 0.0
    node_run_ft: float = 0.0
    ok: bool = True
    needs_injection: bool = False
    v_at_node: float = None
    headroom_w: float = 0.0
    notes: list = field(default_factory=list)


def check_terminal(brand: str, terminal: int, led_load_w: float,
                   node_kind: str = None, node_run_ft: float = 0.0) -> TerminalCheck:
    """Can this terminal carry its LEDs plus (optionally) one camera node?

    Rules enforced:
    - at most ONE camera node per terminal (12V ceiling rule)
    - node draw counted at its 12W ceiling (continuous-load conservatism)
    - run beyond 75 ft on 18 AWG at 12V flags injection
    - buck input window: node must see a rail inside 9 to 56V after drop
    """
    b = BRANDS[brand]
    t = TerminalCheck(terminal=terminal, rail_v=b["rail_v"], led_load_w=led_load_w)
    budget = b["terminal_w"]
    if led_load_w > budget:
        t.ok = False
        t.notes.append(f"LED load {led_load_w}W exceeds the {budget}W terminal budget on its own")
    if node_kind:
        t.node_kind = node_kind
        t.node_draw_w = NODE_CEILING_W  # budget at the ceiling, always
        t.node_run_ft = node_run_ft
        total = led_load_w + t.node_draw_w
        t.headroom_w = round(budget - total, 1)
        if total > budget:
            t.ok = False
            t.needs_injection = True
            t.notes.append(
                f"LEDs {led_load_w}W + node ceiling {NODE_CEILING_W}W = {total}W "
                f"exceeds the {budget}W terminal: feed the node from an injection kit")
        if b["rail_v"] <= 12 and node_run_ft > RETROFIT_MAX_RUN_FT:
            t.needs_injection = True
            t.notes.append(
                f"{node_run_ft:.0f} ft exceeds the {RETROFIT_MAX_RUN_FT:.0f} ft "
                f"18 AWG limit at 12V: inject power at the node")
        v = voltage_at_node(t.node_draw_w, b["rail_v"], node_run_ft)
        t.v_at_node = round(v, 2)
        lo, hi = BUCK_INPUT_RANGE_V
        if not (lo <= v <= hi):
            t.ok = False
            t.needs_injection = True
            t.notes.append(f"rail at node {v:.1f}V is outside the buck's {lo} to {hi}V window")
    else:
        t.headroom_w = round(budget - led_load_w, 1)
    return t


def rail48_budget(n_track: int, n_door: int, led_load_w: float,
                  supply_w: float = 384.0) -> dict:
    """SKU 2 clean-sheet rail: continuous camera loads plus LED load against
    the supply, requiring the ~45% headroom target at 3 nodes."""
    cams = n_track * NODE_DRAW_W["track"] + n_door * NODE_DRAW_W["door"]
    total = cams + led_load_w
    headroom_pct = round(100 * (supply_w - total) / supply_w, 1)
    return {
        "supply_w": supply_w,
        "camera_w": round(cams, 1),
        "led_w": led_load_w,
        "total_w": round(total, 1),
        "headroom_pct": headroom_pct,
        "ok": total <= supply_w and headroom_pct >= 0,
        "meets_45pct_target": headroom_pct >= 45.0,
    }


def led_load_estimate_w(linear_ft: float, rail_v: float,
                        bulb_w: float = 0.96, spacing_in: float = 9.0,
                        duty: float = 1.0) -> float:
    """Worst-case LED track load for a run (Gemstone-class 0.96W bulbs)."""
    n = linear_ft * 12.0 / spacing_in
    return round(n * bulb_w * duty, 1)


if __name__ == "__main__":
    import json
    print(json.dumps({
        "drop_12v_12w_18awg": drop_table(12, 12, awgs=(18,)),
        "gemstone_terminal_with_node": asdict(
            check_terminal("gemstone", 1, led_load_w=40, node_kind="track", node_run_ft=60)),
        "rail48_3nodes": rail48_budget(3, 1, led_load_w=150),
    }, indent=2))
