"""SightLine narrator agent.

Turns a sightline.story.v1 JSON into the homeowner paragraph and the police
export summary. Two modes:

- mock: deterministic templates over story fields only. Runs offline, always.
- claude: Anthropic API with prompts/system.v1.txt. Used when
  SIGHTLINE_NARRATOR_MODE=claude and ANTHROPIC_API_KEY is set; falls back
  to mock on any failure so the demo never blocks.

Both modes obey the same guardrails: nothing visual that is not in the
JSON, timestamps cited, simulated frames never called evidence.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path

PROMPT_FILE = Path(__file__).parent / "prompts" / "system.v1.txt"
CLAUDE_MODEL = "claude-sonnet-5"


def _clock(ts: str) -> str:
    return ts[11:19] if ts else ""


def _ampm(ts: str) -> str:
    try:
        return datetime.fromisoformat(ts).strftime("%-I:%M %p")
    except Exception:
        return _clock(ts)


def _classes(story: dict) -> dict:
    counts = {}
    for e in story.get("entities", []):
        counts[e["class"]] = counts.get(e["class"], 0) + 1
    return counts


def narrate_mock(story: dict) -> dict:
    counts = _classes(story)
    zones = [z for z in story.get("zones", []) if z != "street"] or story.get("zones", [])
    start = _ampm(story.get("started_ts", ""))
    beats = story.get("timeline", [])

    parts = []
    subject = " and ".join(
        (f"a {c}" if n == 1 else f"{n} {c}s") for c, n in counts.items()) or "activity"
    where = zones[0] if zones else "the perimeter"
    parts.append(f"{start}: {subject} in the {where}.")

    # cite the person's best identify-grade frame when there is one, else
    # the first identity-grade beat in the timeline
    ident = None
    person = next((e for e in story.get("entities", []) if e["class"] == "person"), None)
    if person and (person.get("best_frame", {}) or {}).get("dori_level") in ("identify", "validate"):
        ident = person["best_frame"]
    else:
        ident = next((b for b in beats if "identity-grade capture" in b["beat"]), None)
    if ident:
        node = ident.get("node_id")
        parts.append("An identify-grade frame was captured at "
                     + _clock(ident["ts"]) + (f" ({node})." if node else "."))

    deter = story.get("deter", {})
    if deter.get("fired"):
        outcome = deter.get("outcome", "unknown")
        line = f"Deterrence lights fired at {_clock(deter.get('ts', ''))}"
        if outcome == "fled":
            line += " and they left immediately."
        elif outcome == "stayed":
            line += "; they did not leave."
        else:
            line += "."
        parts.append(line)

    if story.get("status") == "closed" and story.get("dwell_s"):
        parts.append(f"Total time on the property: {story['dwell_s']:.0f} seconds. "
                     f"Clips and frames are on your gateway.")
    else:
        parts.append("Clips and frames are on your gateway.")
    homeowner = " ".join(parts)

    lines = [
        f"SIGHTLINE EVENT SUMMARY (site {story.get('site_id', '')}, story {story.get('story_id', '')})",
        f"Window: {_clock(story.get('started_ts', ''))} to {_clock(story.get('ended_ts', '')) or 'open'}",
        f"Severity: {story.get('severity', '')}. Verified: {'yes' if story.get('verified') else 'no'}.",
        f"Subjects: " + (", ".join(f"{n}x {c}" for c, n in counts.items()) or "none classified"),
        f"Zones: " + (", ".join(story.get("zones", [])) or "n/a")
        + ". Nodes: " + (", ".join(story.get("nodes", [])) or "n/a"),
    ]
    for e in story.get("entities", []):
        bf = e.get("best_frame")
        if bf:
            lines.append(
                f"Best frame ({e['class']}): {_clock(bf['ts'])} {bf['node_id']} "
                f"{bf['channel']} channel, {bf['dori_level']} grade, {bf['px_per_m']} px/m, "
                f"event {bf['event_id']}")
    if deter.get("fired"):
        lines.append(f"Deterrence: zone-follow strobe at {_clock(deter.get('ts', ''))} "
                     f"on {', '.join(deter.get('segments', []))}. Outcome: {deter.get('outcome', 'unknown')}.")
    lines.append(
        "Evidence: native-pixel frames "
        + ("AVAILABLE for export with chain of custody."
           if story.get("evidence_exportable")
           else "NOT available (frames are simulated or non-native). Narrative only, not evidence."))
    return {"homeowner": homeowner, "police_summary": "\n".join(lines),
            "mode": "mock", "generated_ts": datetime.now().astimezone().isoformat()}


def narrate_claude(story: dict) -> dict:
    import anthropic  # optional dependency, only in claude mode
    client = anthropic.Anthropic()
    msg = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=800,
        system=PROMPT_FILE.read_text(),
        messages=[{"role": "user", "content":
                   "Event Story JSON:\n" + json.dumps(story, indent=2)}],
    )
    out = json.loads(msg.content[0].text)
    return {"homeowner": out["homeowner"], "police_summary": out["police_summary"],
            "mode": "claude", "generated_ts": datetime.now().astimezone().isoformat()}


def narrate(story: dict, mode: str = None) -> dict:
    mode = mode or os.environ.get("SIGHTLINE_NARRATOR_MODE", "mock")
    if mode == "claude" and os.environ.get("ANTHROPIC_API_KEY"):
        try:
            return narrate_claude(story)
        except Exception:
            pass
    return narrate_mock(story)
