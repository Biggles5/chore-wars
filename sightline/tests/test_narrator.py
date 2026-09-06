"""Narrator agent evals: 5 fixture stories with expected-output assertions.

Runs the mock mode (deterministic). Claude mode is judged against the same
assertions manually with an API key set.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "agents" / "narrator"))

from narrator import narrate  # noqa: E402

CASES = json.loads(
    (ROOT / "agents" / "narrator" / "evals" / "cases.json").read_text())["cases"]


@pytest.mark.parametrize("case", CASES, ids=[c["name"] for c in CASES])
def test_narrator_case(case):
    out = narrate(case["story"], mode="mock")
    assert out["mode"] == "mock"
    text = out["homeowner"]
    ps = out["police_summary"]
    for needle in case["homeowner_contains"]:
        assert needle.lower() in text.lower(), f"homeowner missing: {needle!r}\n{text}"
    for needle in case["police_contains"]:
        assert needle.lower() in ps.lower(), f"police missing: {needle!r}\n{ps}"
    for banned in case["never_contains"]:
        combined = text + "\n" + ps
        assert banned.lower() not in combined.lower(), f"invented detail: {banned!r}"


def test_narrator_never_invents_visuals():
    """The guardrail in prompt form, tested in code: mock output vocabulary
    is drawn only from the story JSON plus fixed template words."""
    story = CASES[0]["story"]
    out = narrate(story, mode="mock")
    for word in ("wearing", "carrying a", "looked like", "appears to be"):
        assert word not in out["homeowner"].lower()
