"""Support and dealer-GTM agent evals (5 cases each).

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "agents" / "support"))
sys.path.insert(0, str(ROOT / "agents" / "dealer-gtm"))

from support import triage  # noqa: E402
import dealer_gtm  # noqa: E402

SUPPORT_CASES = [
    ("safety-escalates",
     {"text": "I smelled something burning near the controller",
      "telemetry": {"power": {"rail_v": 12, "draw_w": 5}}},
     lambda r: r["escalate"] and r["severity"] == "critical"
     and "power off" in r["steps"][0].lower()),
    ("low-rail-injection",
     {"text": "camera keeps rebooting at night",
      "telemetry": {"power": {"rail_v": 8.9, "draw_w": 6}, "wifi_rssi_dbm": -60}},
     lambda r: not r["escalate"] and any("injection" in s for s in r["steps"])
     and "docs/guides/retrofit-install-12v.md" in r["guides"]),
    ("weak-wifi",
     {"text": "live view is choppy",
      "telemetry": {"power": {"rail_v": 11.8, "draw_w": 6}, "wifi_rssi_dbm": -81}},
     lambda r: any("bus pair" in s for s in r["steps"])),
    ("aim-question",
     {"text": "faces are blurry in the driveway clips", "telemetry": None},
     lambda r: any("dori_placement" in s for s in r["steps"])
     and "docs/guides/house-pilot.md" in r["guides"]),
    ("no-telemetry",
     {"text": "node seems dead", "telemetry": {}},
     lambda r: any("terminal budget" in s for s in r["steps"])),
]


@pytest.mark.parametrize("name,inp,check", SUPPORT_CASES,
                         ids=[c[0] for c in SUPPORT_CASES])
def test_support_case(name, inp, check):
    r = triage(inp["text"], inp["telemetry"])
    assert check(r), r
    assert r["mode"] == "mock"


LEAD = {"first_name": "Dana", "company": "Brightline Exteriors",
        "brand_installed": "Trimlight", "city": "Boise", "homes_estimate": "600"}


def test_gtm_renders_three_touches():
    seq = dealer_gtm.render(LEAD)
    assert len(seq) == 3
    assert [t["day"] for t in seq] == [0, 3, 7]
    assert seq[0]["channel"] == "email" and seq[1]["channel"] == "linkedin"


def test_gtm_merges_fields():
    seq = dealer_gtm.render(LEAD)
    joined = " ".join(t["subject"] + t["body"] for t in seq)
    for needle in ("Dana", "Brightline Exteriors", "Trimlight", "Boise", "600"):
        assert needle in joined
    assert "{" not in joined, "unresolved merge field"


def test_gtm_voice_rules():
    seq = dealer_gtm.render(LEAD)
    joined = " ".join(t["subject"] + t["body"] for t in seq)
    assert "—" not in joined, "no em dashes"
    assert "!" not in joined, "no exclamation marks"
    assert "hope this finds you well" not in joined.lower()


def test_gtm_missing_enrichment_raises():
    with pytest.raises(ValueError):
        dealer_gtm.render({"first_name": "Sam"})


def test_gtm_icp_and_booking():
    assert len(dealer_gtm.ICP["segments"]) == 4
    flow = dealer_gtm.booking_flow()
    assert any("make demo" in s for s in flow["steps"])
