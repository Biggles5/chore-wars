"""Market throughput simulator: one metro, old model vs Ops Engine.

Deterministic weekly simulation (default: Utah County). Demand arrives by
season, installer pools grow their own way (W2 hiring vs the certification
funnel), job durations come from the learning curve, the scheduler is the
capacity engine's math, and callbacks eat next week's capacity at each
model's rate. The gap between the two capacity lines is the growth thesis.

  python3 opssim.py run new-metro-launch
  python3 opssim.py run q4-crunch
  python3 opssim.py run callback-storm
  python3 opssim.py run <scenario> --emit-web    also writes the chart data
                                                 for website/demo

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "econ"))
import throughput as tp  # noqa: E402

WEEKS = 26
DAYS_PER_WEEK = 5.5          # crews work Saturdays in season
AVG_TICKET = 1701.0          # sample house 1 installed price (est.)
WEATHER_LOSS = 0.07          # fraction of crew-days lost to weather (est.)

SCENARIOS = {
    "new-metro-launch": {
        "description": "Day zero in a new metro (Utah County). Old model starts with 2 W2 crews and hires 1 per quarter. Ops Engine starts with 0 crews and only the recruitment funnel.",
        "start_month": 3,
        "base_demand_wk": 22.0,
        "demand_ramp_wk": 0.35,   # marketing + dealer referrals compound
        "old_crews_start": 2.0, "old_hire_per_quarter": 1.0,
        "new_crews_start": 0.0,
        "callback_new": tp.CALLBACK_RATE_NEW, "callback_old": tp.CALLBACK_RATE_OLD,
    },
    "q4-crunch": {
        "description": "The Q4 lighting crunch: demand more than doubles into November. The old model's fixed crews drown in backlog; the funnel scales into it.",
        "start_month": 9,
        "base_demand_wk": 30.0,
        "demand_ramp_wk": 0.0,
        "old_crews_start": 4.0, "old_hire_per_quarter": 1.0,
        "new_crews_start": 4.0,
        "callback_new": tp.CALLBACK_RATE_NEW, "callback_old": tp.CALLBACK_RATE_OLD,
    },
    "callback-storm": {
        "description": "A bad connector batch: callback rates spike 3x for a month (weeks 6 to 10). QC gates catch it at 6%; the old model's field splices ride to 33% and capacity collapses.",
        "start_month": 4,
        "base_demand_wk": 28.0,
        "demand_ramp_wk": 0.1,
        "old_crews_start": 4.0, "old_hire_per_quarter": 1.0,
        "new_crews_start": 4.0,
        "callback_new": tp.CALLBACK_RATE_NEW, "callback_old": tp.CALLBACK_RATE_OLD,
        "storm_weeks": (6, 10), "storm_multiplier": 3.0,
    },
}


def _season_mult(start_month: int, week: int) -> float:
    m = (start_month - 1 + week // 4) % 12
    return tp.LIGHTING_DEMAND_SHAPE[m] * 0.55 + tp.SECURITY_DEMAND_SHAPE[m] * 0.45


def simulate(name: str) -> dict:
    sc = SCENARIOS[name]
    rows = []
    state = {
        "old": {"crews": sc["old_crews_start"], "backlog": 0.0, "done": 0.0,
                "revenue": 0.0, "cb_debt": 0.0},
        "new": {"crews": sc["new_crews_start"], "backlog": 0.0, "done": 0.0,
                "revenue": 0.0, "cb_debt": 0.0, "crew_jobs": 0.0},
    }
    funnel_per_wk = tp.crews_certified_per_month() / 4.33

    for wk in range(1, WEEKS + 1):
        demand = (sc["base_demand_wk"] + sc["demand_ramp_wk"] * wk) * _season_mult(sc["start_month"], wk)

        # crew growth
        if wk % 13 == 0:
            state["old"]["crews"] += sc["old_hire_per_quarter"]
        state["new"]["crews"] = (state["new"]["crews"] * (tp.FUNNEL["retained_90d"] ** (1 / 13))
                                 + funnel_per_wk)

        # callback rates (storm scenario perturbs both, QC gates dampen new)
        cb_old, cb_new = sc["callback_old"], sc["callback_new"]
        if "storm_weeks" in sc and sc["storm_weeks"][0] <= wk <= sc["storm_weeks"][1]:
            cb_old *= sc["storm_multiplier"]
            cb_new *= 1.5  # gates catch the batch before it scales

        week_row = {"week": wk, "demand": round(demand, 1)}
        for model in ("old", "new"):
            s = state[model]
            if model == "old":
                jobs_day = tp.JOBS_PER_DAY_OLD
                hours = tp.install_hours("old")
            else:
                avg_jobs_done = s["crew_jobs"] / max(s["crews"], 0.5)
                hours = tp.job_hours_at(int(avg_jobs_done) + 1)
                jobs_day = min(tp.JOBS_PER_DAY_NEW, 9.0 / (hours + 0.5))
            cap = s["crews"] * jobs_day * DAYS_PER_WEEK * (1 - WEATHER_LOSS) * tp.UTILIZATION
            cap = max(cap - s["cb_debt"], 0.0)          # callbacks eat capacity
            want = s["backlog"] + demand
            installs = min(want, cap)
            s["backlog"] = want - installs
            cb_rate = cb_old if model == "old" else cb_new
            s["cb_debt"] = installs * cb_rate * 0.6     # callback truck-rolls next week
            s["done"] += installs
            s["revenue"] += installs * AVG_TICKET
            if model == "new":
                s["crew_jobs"] += installs
            week_row[model] = {
                "crews": round(s["crews"], 1),
                "capacity": round(cap, 1),
                "installs": round(installs, 1),
                "backlog": round(s["backlog"], 1),
                "utilization": round(min(installs / cap, 1.0), 2) if cap else 0.0,
            }
        rows.append(week_row)

    def month_rate(model, at_week):
        return round(sum(r[model]["installs"] for r in rows[at_week - 4:at_week]) * (4.33 / 4), 0)

    summary = {
        "scenario": name,
        "description": sc["description"],
        "weeks": WEEKS,
        "week12_installs_per_month": {"old": month_rate("old", 12),
                                      "new": month_rate("new", 12)},
        "total_installs": {m: round(state[m]["done"], 0) for m in ("old", "new")},
        "ending_backlog": {m: round(state[m]["backlog"], 0) for m in ("old", "new")},
        "revenue_usd": {m: round(state[m]["revenue"], 0) for m in ("old", "new")},
        "all_estimates": True,
    }
    return {"summary": summary, "weeks": rows}


def emit_web(result: dict):
    out = ROOT / "website" / "demo" / "opssim-data.js"
    out.write_text("// generated by sim/ops-sim/opssim.py; do not edit\n"
                   "window.OPSSIM = " + json.dumps(result) + ";\n")
    print("wrote", out)


def main():
    ap = argparse.ArgumentParser(prog="opssim")
    sub = ap.add_subparsers(dest="cmd", required=True)
    run = sub.add_parser("run")
    run.add_argument("scenario", choices=sorted(SCENARIOS))
    run.add_argument("--emit-web", action="store_true")
    args = ap.parse_args()

    result = simulate(args.scenario)
    s = result["summary"]
    print(f"scenario   {s['scenario']}: {s['description']}")
    print(f"{'wk':>3} {'demand':>7} | {'old crews':>9} {'installs':>8} {'backlog':>8} | "
          f"{'new crews':>9} {'installs':>8} {'backlog':>8}")
    for r in result["weeks"]:
        if r["week"] % 2 == 0:
            print(f"{r['week']:>3} {r['demand']:>7} | {r['old']['crews']:>9} "
                  f"{r['old']['installs']:>8} {r['old']['backlog']:>8} | "
                  f"{r['new']['crews']:>9} {r['new']['installs']:>8} {r['new']['backlog']:>8}")
    print(f"\nweek-12 installs/month  old: {s['week12_installs_per_month']['old']:.0f}   "
          f"new: {s['week12_installs_per_month']['new']:.0f}")
    print(f"26-week installs        old: {s['total_installs']['old']:.0f}   "
          f"new: {s['total_installs']['new']:.0f}")
    print(f"ending backlog          old: {s['ending_backlog']['old']:.0f}   "
          f"new: {s['ending_backlog']['new']:.0f}")
    if args.emit_web:
        emit_web(result)


if __name__ == "__main__":
    main()
