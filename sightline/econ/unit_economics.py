"""SightLine unit economics engine. Spreadsheet as code.

Every constant is named, sourced, or marked (est.). The kill thresholds are
encoded as tests (tests/test_econ_thresholds.py): blended CAC under $1,000,
monitoring marginal cost under $6/home/month, blended plan gross margin
over 60%, and attrition never modeled better than 8% without a cited
justification.

Incumbent benchmarks (Section 0 ground truth):
- ADT Q2 2026: ~$1,800/sub net SAC ($345M net SAC / 190K gross adds),
  13.1% gross attrition, 2.3-year payback, ~$7.4B net debt.
- Vivint 2019 Form 425: ~$2,150 gross creation cost.
- Wholesale monitoring: COPS SecureNet class $5.99/account/month.
- RMR portfolios trade ~26x to 50x monthly RMR (Barnes).
- Price umbrella: SimpliSafe Active Guard $49.99 to $79.99/mo,
  Deep Sentinel $60 to $100/mo/camera.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict

# ---- plans ----
PLANS = {
    "core": {"price_mo": 0.0},
    "plus": {"price_mo": 9.99},
    "shield": {"price_mo": 19.99},
}

# ---- monthly cost to serve, per paying home (est., re-priced monthly) ----
COST_TO_SERVE = {
    "guardian_compute_mo": 0.42,     # cost meter extrapolation, margin for growth (est.)
    "cloud_storage_plus_mo": 0.60,   # 60-day event/story/clip retention (est.)
    "support_amortized_mo": 0.75,    # support agent + human escalations (est.)
    "wholesale_station_mo": 5.99,    # COPS SecureNet class, Shield only
    "payment_fees_pct": 0.031,
}

# ---- CAC by channel (est. where noted) ----
CAC_CHANNELS = {
    "dealer_attach": {"cac": 250.0, "note": "dealer commission + demo amortization (est.)"},
    "inbound": {"cac": 450.0, "note": "content + paid + close labor (est.)"},
    "insurer_subsidized": {"cac": 150.0, "note": "State Farm template: partner funds acquisition (est.)"},
    "door_knock_benchmark": {"cac": 1975.0, "note": "midpoint of ADT $1,800 net and Vivint $2,150 gross; benchmark only, not our channel"},
}
CHANNEL_MIX = {"dealer_attach": 0.60, "inbound": 0.25, "insurer_subsidized": 0.15}

# ---- attrition ----
ATTRITION_SCENARIOS = {"good": 0.05, "base": 0.09, "adt_actual": 0.131}
ATTRITION_FLOOR = 0.08
ATTRITION_FLOOR_NOTE = ("Modeling attrition under 8% requires a cited justification; "
                        "nobody in this industry earns 5% without contracts, and we "
                        "refuse contracts on principle.")

PAYING_MIX = {"plus": 0.60, "shield": 0.40}  # of paying subscribers (est.)


def monitoring_marginal_cost_mo(plan: str) -> float:
    c = COST_TO_SERVE["guardian_compute_mo"] + COST_TO_SERVE["support_amortized_mo"]
    if plan in ("plus", "shield"):
        c += COST_TO_SERVE["cloud_storage_plus_mo"]
    if plan == "shield":
        c += COST_TO_SERVE["wholesale_station_mo"]
    return round(c, 2)


def gross_margin_mo(plan: str) -> dict:
    price = PLANS[plan]["price_mo"]
    cost = monitoring_marginal_cost_mo(plan) + price * COST_TO_SERVE["payment_fees_pct"]
    margin = price - cost
    return {"plan": plan, "price_mo": price, "cost_mo": round(cost, 2),
            "margin_mo": round(margin, 2),
            "margin_pct": round(100 * margin / price, 1) if price else 0.0}


def blended(paying_mix: dict = None) -> dict:
    mix = paying_mix or PAYING_MIX
    price = sum(PLANS[p]["price_mo"] * w for p, w in mix.items())
    margin = sum(gross_margin_mo(p)["margin_mo"] * w for p, w in mix.items())
    cost = sum(monitoring_marginal_cost_mo(p) * w for p, w in mix.items())
    return {"arpu_mo": round(price, 2), "margin_mo": round(margin, 2),
            "margin_pct": round(100 * margin / price, 1),
            "marginal_cost_mo": round(cost, 2)}


def blended_cac(mix: dict = None) -> float:
    mix = mix or CHANNEL_MIX
    return round(sum(CAC_CHANNELS[ch]["cac"] * w for ch, w in mix.items()), 2)


# The structural difference vs incumbents: they subsidize hardware and
# recoup through contract RMR; we sell the kit at positive margin, so the
# subscription never has to dig out of a hardware hole.
HARDWARE_MARGIN_PER_INSTALL = 400.0  # SKU 1 at $1,701 installed vs COGS+install (est.)


def ltv(attrition_annual: float, justification: str = None,
        paying_mix: dict = None) -> dict:
    if attrition_annual < ATTRITION_FLOOR and not justification:
        raise ValueError(ATTRITION_FLOOR_NOTE)
    b = blended(paying_mix)
    churn_mo = attrition_annual / 12.0
    lifetime_mo = 1.0 / churn_mo
    net_cac = blended_cac() - HARDWARE_MARGIN_PER_INSTALL
    return {
        "attrition_annual": attrition_annual,
        "lifetime_months": round(lifetime_mo, 1),
        "ltv_margin_usd": round(b["margin_mo"] * lifetime_mo, 0),
        "payback_months": round(blended_cac() / b["margin_mo"], 1),
        "net_cac_after_hardware_margin": round(net_cac, 0),
        "payback_months_net": 0.0 if net_cac <= 0 else round(net_cac / b["margin_mo"], 1),
        "justification": justification,
    }


def rmr_portfolio_value(subscribers: int, multiple: float = 35.0,
                        paying_share: float = 0.55) -> dict:
    """Barnes-range multiples: 26x conservative, 35x mid, 50x strong book."""
    rmr = subscribers * paying_share * blended()["arpu_mo"]
    return {"subscribers": subscribers, "paying_share": paying_share,
            "rmr_usd_mo": round(rmr, 0), "multiple": multiple,
            "portfolio_value_usd": round(rmr * multiple, 0)}


def incumbent_comparison() -> dict:
    ours = blended()
    return {
        "cac": {"sightline_blended": blended_cac(),
                "adt_net": 1800.0, "vivint_gross": 2150.0},
        "monitoring_cost_mo": {"sightline_marginal": ours["marginal_cost_mo"],
                               "incumbent_price_umbrella": [30.0, 80.0],
                               "simplisafe_active_guard": [49.99, 79.99],
                               "wholesale_station_actual": 5.99},
        "payback_months": {"sightline": ltv(ATTRITION_SCENARIOS["base"])["payback_months"],
                           "adt": 27.6},
        "attrition": {"sightline_base_assumption": ATTRITION_SCENARIOS["base"],
                      "adt_actual": ATTRITION_SCENARIOS["adt_actual"]},
        "note": "no contracts anywhere in ours; incumbents cannot drop contracts without breaking their debt covenants ($7.4B net at ADT)",
    }


# ---- scenarios ----
@dataclass
class Scenario:
    name: str
    description: str
    channel_mix: dict
    paying_mix: dict
    attrition: float
    subs_36mo: int
    extra: dict = field(default_factory=dict)


SCENARIOS = {
    "dealer-led": Scenario(
        name="dealer-led",
        description="Ride the installed lighting base: dealers attach SightLine to existing and new tracks. The base plan.",
        channel_mix={"dealer_attach": 0.75, "inbound": 0.20, "insurer_subsidized": 0.05},
        paying_mix={"plus": 0.60, "shield": 0.40},
        attrition=0.09, subs_36mo=18000,
        extra={"why": "170K+ incumbent lighting homes; dealer channel already trusted at the eave"},
    ),
    "insurer-led": Scenario(
        name="insurer-led",
        description="A State Farm-template partner subsidizes acquisition for loss-reduction data. Lower CAC, faster ramp, co-brand obligations.",
        channel_mix={"dealer_attach": 0.35, "inbound": 0.15, "insurer_subsidized": 0.50},
        paying_mix={"plus": 0.45, "shield": 0.55},
        attrition=0.08, subs_36mo=30000,
        extra={"why": "insurer distribution + premium-discount pull; Shield mix rises with monitoring bundled",
               "attrition_justification": "insurer-bundled accounts churn with the policy, not the gadget; still floored at 8%"},
    ),
    "licensing-pivot": Scenario(
        name="licensing-pivot",
        description="The kill-trigger plan: Ring/SimpliSafe bundle agentic monitoring under $20 before we reach 50K subs. Guardian licenses B2B2C to dealers and regional alarm companies, white-label.",
        channel_mix={"dealer_attach": 1.0},
        paying_mix={"plus": 0.0, "shield": 1.0},
        attrition=0.09, subs_36mo=60000,
        extra={"why": "SIGHTLINE_WHITE_LABEL=1: the stack runs branded for the licensee; we take a per-account platform fee",
               "platform_fee_mo": 4.0,
               "note": "revenue quality drops, capital intensity drops harder; the pivot is a config change, not a rewrite"},
    ),
}


def run_scenario(name: str) -> dict:
    sc = SCENARIOS[name]
    b = blended(sc.paying_mix)
    cac = round(sum(CAC_CHANNELS[ch]["cac"] * w for ch, w in sc.channel_mix.items()), 2)
    lt = ltv(sc.attrition, justification=sc.extra.get("attrition_justification"),
             paying_mix=sc.paying_mix)
    if name == "licensing-pivot":
        fee = sc.extra["platform_fee_mo"]
        margin_mo = fee - COST_TO_SERVE["guardian_compute_mo"]
        b = {"arpu_mo": fee, "margin_mo": round(margin_mo, 2),
             "margin_pct": round(100 * margin_mo / fee, 1),
             "marginal_cost_mo": COST_TO_SERVE["guardian_compute_mo"]}
        cac = 60.0  # partner acquires; ours is integration cost per account (est.)
    port = rmr_portfolio_value(sc.subs_36mo,
                               paying_share=1.0 if name == "licensing-pivot" else 0.55)
    return {"scenario": asdict(sc), "blended": b, "cac": cac, "ltv": lt,
            "portfolio_36mo": port,
            "ltv_to_cac": round(lt["ltv_margin_usd"] / cac, 1)}


if __name__ == "__main__":
    import json
    for n in SCENARIOS:
        print(n, json.dumps(run_scenario(n), indent=2)[:400], "...\n")
