"""SightLine throughput model: install economics, learning curves,
capacity-constrained growth, seasonality smoothing.

The ops thesis in numbers: skill moves to the factory and the agents, so a
certified two-person contractor crew does 3 installs/day instead of 1, is
productive by job 3 instead of after a season, and a metro's capacity is a
recruitment funnel, not a hiring plan. Threshold tests
(tests/test_econ_thresholds.py) hold this file to the claims.

Verified time baseline (Section 0 addendum): measure truck-roll ~1 h,
on-site channel cutting ~1.5 h, mounting at height ~2.5 h, field wiring
and splicing ~2 h, programming ~1 h: about 8 job-hours, 1 job/day, and
labor ~30% of a $2,000 to $8,000 ticket.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import math

# ---- the time model: where the minutes go (hours, single story) ----
OLD_MODEL_HOURS = {
    "measure_truck_roll": 1.0,
    "onsite_channel_cutting": 1.5,
    "mounting_at_height": 2.5,
    "field_wiring_splicing": 2.0,
    "programming": 1.0,
}
NEW_MODEL_HOURS = {
    "measure_truck_roll": 0.0,     # phone photogrammetry (~2.6% vs tape); scan kills the roll
    "onsite_channel_cutting": 0.0,  # factory-cut labeled kit (A1..N)
    "mounting_at_height": 1.4,     # snap-in modules + pre-planned ladder sets (est.)
    "field_wiring_splicing": 0.4,  # tool-free gasketed connectors; the splice is gone (est.)
    "programming": 0.3,            # auto-provision + commissioning check (est.)
    "qc_photo_gates": 0.3,         # photo per gate, QC agent grades in seconds (est.)
}

CREW_SIZE = 2
JOBS_PER_DAY_OLD = 1
JOBS_PER_DAY_NEW = 3
LOADED_W2_RATE_HR = 55.0            # wage + burden + truck + idle (est.)
CONTRACTOR_PAYOUT_PER_JOB = 450.0   # certified crew payout, SKU 1 retrofit (est.)
CONTRACTOR_DIRECT_COST_PER_JOB = 170.0  # their labor+fuel+insurance slice (est.)
CALLBACK_COST = 380.0               # truck roll + parts + goodwill (est.)
CALLBACK_RATE_OLD = 0.11            # splice-driven water ingress era (est.)
CALLBACK_RATE_NEW = 0.04            # gasketed connectors + QC gates (modeled; must stay < 5%)


def install_hours(model: str = "new") -> float:
    table = NEW_MODEL_HOURS if model == "new" else OLD_MODEL_HOURS
    return round(sum(table.values()), 2)


def install_economics() -> dict:
    old_hours = install_hours("old")
    new_hours = install_hours("new")
    old_cost = old_hours * CREW_SIZE * LOADED_W2_RATE_HR
    old_cost_cb = old_cost + CALLBACK_RATE_OLD * CALLBACK_COST
    new_cost_cb = CONTRACTOR_PAYOUT_PER_JOB + CALLBACK_RATE_NEW * CALLBACK_COST
    installer_margin = CONTRACTOR_PAYOUT_PER_JOB - CONTRACTOR_DIRECT_COST_PER_JOB
    return {
        "old_model": {"job_hours": old_hours, "crew_hours": old_hours * CREW_SIZE,
                      "jobs_per_day": JOBS_PER_DAY_OLD,
                      "labor_cost_per_install": round(old_cost, 0),
                      "cost_with_callbacks": round(old_cost_cb, 0)},
        "new_model": {"job_hours": new_hours, "crew_hours": new_hours * CREW_SIZE,
                      "jobs_per_day": JOBS_PER_DAY_NEW,
                      "payout_per_install": CONTRACTOR_PAYOUT_PER_JOB,
                      "cost_with_callbacks": round(new_cost_cb, 0)},
        "installer_earnings": {
            "margin_per_job": round(installer_margin, 0),
            "margin_per_crew_day": round(installer_margin * JOBS_PER_DAY_NEW, 0),
            "revenue_per_crew_day": round(CONTRACTOR_PAYOUT_PER_JOB * JOBS_PER_DAY_NEW, 0),
            "pitch": "a two-person crew grosses $1,350/day and keeps ~$840 (est.); "
                     "Christmas-light money, twelve months a year",
        },
        "callback_sensitivity": {
            rate: round(CONTRACTOR_PAYOUT_PER_JOB + rate * CALLBACK_COST, 0)
            for rate in (0.02, 0.04, 0.05, 0.08, 0.11)
        },
    }


# ---- learning curve: certified crews get fast, fast ----
def job_hours_at(job_n: int) -> float:
    """Half-day certification + guided runbook: job 1 slow, asymptote by ~job 6."""
    asymptote = install_hours("new")      # 2.4
    return round(asymptote + 2.4 * math.exp(-0.55 * (job_n - 1)), 2)


def qc_first_pass_at(job_n: int) -> float:
    """QC-gate first-pass rate by job number (modeled; pilots replace this)."""
    return round(min(0.95, 0.68 + 0.062 * (job_n - 1)), 3)


# ---- capacity-constrained growth: the recruitment funnel IS the ramp ----
FUNNEL = {
    "outreach_per_month": 40,       # dealer-gtm agent working one metro (est.)
    "response_rate": 0.15,
    "cert_completion": 0.60,        # half-day course, bench practical
    "first_job_rate": 0.85,
    "retained_90d": 0.85,
}
WORKDAYS_PER_MONTH = 22
UTILIZATION = 0.65                  # weather, routing, no-shows (est.)


def crews_certified_per_month() -> float:
    f = FUNNEL
    return (f["outreach_per_month"] * f["response_rate"]
            * f["cert_completion"] * f["first_job_rate"])


def crew_capacity_per_month(jobs_per_day: float = JOBS_PER_DAY_NEW) -> float:
    return jobs_per_day * WORKDAYS_PER_MONTH * UTILIZATION


def metro_capacity(months: int, model: str = "new") -> list:
    """Certified-crew count and install capacity by month from launch."""
    out = []
    crews = 0.0
    add = crews_certified_per_month()
    for m in range(1, months + 1):
        crews = crews * FUNNEL["retained_90d"] ** (1 / 3) + add
        jobs = JOBS_PER_DAY_NEW if model == "new" else JOBS_PER_DAY_OLD
        out.append({"month": m, "crews": round(crews, 1),
                    "capacity_installs_mo": round(crews * crew_capacity_per_month(jobs), 0)})
    return out


# ---- seasonality: Q4 lighting crunch, security fills the year ----
LIGHTING_DEMAND_SHAPE = [0.5, 0.5, 0.6, 0.7, 0.8, 0.8, 0.9, 1.0, 1.3, 1.9, 2.4, 2.2]
SECURITY_DEMAND_SHAPE = [1.0, 1.0, 1.1, 1.1, 1.2, 1.2, 1.2, 1.1, 1.1, 1.0, 0.9, 0.9]


def seasonality(base_lighting_mo: float = 60, base_security_mo: float = 45) -> list:
    """Monthly demand: lighting installs peak Q4; the retrofit-security SKU
    keeps crews earning January through September."""
    rows = []
    for i in range(12):
        light = base_lighting_mo * LIGHTING_DEMAND_SHAPE[i]
        sec = base_security_mo * SECURITY_DEMAND_SHAPE[i]
        rows.append({"month": i + 1, "lighting": round(light, 0),
                     "security": round(sec, 0), "total": round(light + sec, 0)})
    peak = max(r["total"] for r in rows)
    trough = min(r["total"] for r in rows)
    for r in rows:
        r["peak_to_trough"] = round(peak / trough, 2)
    return rows


if __name__ == "__main__":
    import json
    print(json.dumps(install_economics(), indent=2))
    print("hours by job:", [job_hours_at(n) for n in range(1, 7)])
    print("qc by job:", [qc_first_pass_at(n) for n in range(1, 7)])
    print("metro month 3:", metro_capacity(3)[-1])
