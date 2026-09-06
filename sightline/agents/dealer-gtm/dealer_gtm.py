"""SightLine dealer GTM agent: ICP, enrichment, 3-touch outreach, booking.

Deterministic sequence renderer over versioned templates: a lead record in,
personalized touches out. Structured to plug into Mabry-style agent
pipelines: the enrichment schema is the pipeline contract, the renderer is
a pure function, and Claude mode (optional) only rewrites within the
template's fact set.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).parent

# ---- ICP ----
ICP = {
    "segments": [
        {"id": "trimlight-dealer", "why": "300+ dealers, 120k+ homes of retrofit TAM, PE pressure to grow attach revenue"},
        {"id": "gemstone-dealer", "why": "Class 2 12V fleet matches SKU 1 exactly; the dev house is a Gemstone system"},
        {"id": "jellyfish-dealer", "why": "48V fleet, premium buyers, highest ticket tolerance"},
        {"id": "christmas-light-installer", "why": "seasonal crews hunting year-round revenue; permanent track is their upsell already"},
    ],
    "firmographics": {"crew_size": "2 to 15", "installs_per_year": "40+",
                      "geo": "US suburbs, HOA-heavy metros first"},
    "disqualifiers": ["no install crew (pure e-commerce)", "new-construction-only electrical subs"],
}


def load_sequence(version: str = "v1") -> dict:
    return json.loads((HERE / "sequences" / f"outreach.{version}.json").read_text())


def render(lead: dict, version: str = "v1") -> list:
    """lead: enrichment record (see enrichment_schema.json). Returns the
    3-touch sequence with merge fields resolved. Raises on missing fields
    so the pipeline surfaces bad enrichment instead of sending blanks."""
    seq = load_sequence(version)
    required = ["first_name", "company", "brand_installed", "city"]
    missing = [k for k in required if not lead.get(k)]
    if missing:
        raise ValueError(f"enrichment incomplete: missing {missing}")
    ctx = dict(lead)
    ctx.setdefault("homes_estimate", "a few hundred")
    out = []
    for touch in seq["touches"]:
        out.append({
            "day": touch["day"],
            "channel": touch["channel"],
            "subject": touch.get("subject", "").format(**ctx),
            "body": touch["body"].format(**ctx),
        })
    return out


def booking_flow() -> dict:
    return {
        "steps": [
            "Reply intent detected (any positive) -> agent sends the booking link with two concrete slots pulled from the calendar",
            "Booked -> demo prep: agent runs `make demo`, loads the dealer's own city into the sim house name, sends a calendar note with the 3-command run steps",
            "Demo (20 min): 2:14 AM scenario live, quote agent on one of THEIR past installs, dealer margin math",
            "Close: pilot kit order form (bench BOM + 2 nodes), co-branded HOA packet offer",
        ],
        "no_show": "one reschedule touch at +2 days, then park the lead 90 days",
    }


if __name__ == "__main__":
    demo_lead = {"first_name": "Dana", "company": "Brightline Exteriors",
                 "brand_installed": "Trimlight", "city": "Boise",
                 "homes_estimate": "600"}
    for t in render(demo_lead):
        print(f"--- day {t['day']} [{t['channel']}] {t['subject']}")
        print(t["body"][:200], "...\n")
