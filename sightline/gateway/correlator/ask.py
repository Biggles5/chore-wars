"""Ask: chat over event memory.

Deterministic mock mode answers from the story store with cited story ids
and timestamps; optional Claude mode uses the same retrieval and hands the
retrieved stories (never raw frames) to the model. Same guardrail as the
narrator: nothing visual that is not in the data.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import os
from datetime import datetime


def _clock(ts):
    return ts[11:16] if ts else "?"


def _ampm(ts):
    if not ts or len(ts) < 16:
        return "?"
    h = int(ts[11:13])
    return f"{h % 12 or 12}:{ts[14:16]} {'AM' if h < 12 else 'PM'}"


def _is_night(ts):
    if not ts or len(ts) < 13:
        return False
    h = int(ts[11:13])
    return h >= 21 or h < 7


def _summline(s):
    bits = [f"{_ampm(s['started_ts'])}: {s.get('title', 'activity')}"]
    if s.get("deter", {}).get("fired"):
        out = s["deter"].get("outcome")
        bits.append("deter fired" + (", they fled" if out == "fled" else ""))
    if s.get("verified"):
        bits.append("verified")
    return " (".join([bits[0], ", ".join(bits[1:])]) + (")" if len(bits) > 1 else "")


def answer_mock(question: str, stories: list) -> dict:
    ql = question.lower()
    sources = []

    def cite(sel):
        for s in sel:
            sources.append({"story_id": s["story_id"], "ts": s["started_ts"],
                            "title": s.get("title", "")})

    if not stories:
        return {"answer": "No events in memory yet. Run a scenario or give it a night.",
                "sources": [], "mode": "mock"}

    if any(k in ql for k in ("last night", "tonight", "overnight", "while i slept")):
        night = [s for s in stories if _is_night(s["started_ts"])]
        if not night:
            return {"answer": "Nothing overnight. The perimeter stayed quiet.",
                    "sources": [], "mode": "mock"}
        cite(night[:5])
        lines = [_summline(s) for s in night[:5]]
        return {"answer": "Overnight: " + "; ".join(lines) + ".",
                "sources": sources, "mode": "mock"}

    if any(k in ql for k in ("car", "vehicle", "truck")):
        sel = [s for s in stories
               if any(e["class"] == "vehicle" for e in s.get("entities", []))]
        if not sel:
            return {"answer": "No vehicles on record.", "sources": [], "mode": "mock"}
        cite(sel[:5])
        return {"answer": "Vehicles: " + "; ".join(_summline(s) for s in sel[:5]) + ".",
                "sources": sources, "mode": "mock"}

    if any(k in ql for k in ("who", "person", "people", "anyone")):
        sel = [s for s in stories
               if any(e["class"] == "person" for e in s.get("entities", []))]
        if not sel:
            return {"answer": "No people on record.", "sources": [], "mode": "mock"}
        cite(sel[:5])
        n_ver = sum(1 for s in sel if s.get("verified"))
        return {"answer": f"{len(sel)} event(s) involving people, {n_ver} verified: "
                          + "; ".join(_summline(s) for s in sel[:5]) + ".",
                "sources": sources, "mode": "mock"}

    if any(k in ql for k in ("deter", "lights", "strobe", "scared")):
        sel = [s for s in stories if s.get("deter", {}).get("fired")]
        if not sel:
            return {"answer": "Deterrence has not fired.", "sources": [], "mode": "mock"}
        cite(sel[:5])
        return {"answer": "Deter events: " + "; ".join(
            f"{_ampm(s['deter']['ts'])} on {', '.join(s['deter'].get('segments', []))}"
            f" ({s['deter'].get('outcome', 'unknown')})" for s in sel[:5]) + ".",
                "sources": sources, "mode": "mock"}

    alerts = [s for s in stories if s.get("severity") == "alert"]
    cite(stories[:3])
    return {"answer": f"{len(stories)} stor{'ies' if len(stories) != 1 else 'y'} in memory, "
                      f"{len(alerts)} alert(s). Latest: {_summline(stories[0])}.",
            "sources": sources, "mode": "mock"}


def answer(question: str, stories: list, mode: str = None) -> dict:
    mode = mode or os.environ.get("SIGHTLINE_ASK_MODE", "mock")
    if mode == "claude" and os.environ.get("ANTHROPIC_API_KEY"):
        try:
            import json as _json
            import anthropic
            client = anthropic.Anthropic()
            msg = client.messages.create(
                model="claude-sonnet-5", max_tokens=500,
                system=("You answer questions about home perimeter events using ONLY "
                        "the story JSON provided. Never invent visual details. Cite "
                        "timestamps. Tight, plain answers. No em dashes."),
                messages=[{"role": "user", "content":
                           f"Stories: {_json.dumps(stories[:10])}\n\nQuestion: {question}"}])
            return {"answer": msg.content[0].text, "sources":
                    [{"story_id": s["story_id"], "ts": s["started_ts"],
                      "title": s.get("title", "")} for s in stories[:5]],
                    "mode": "claude"}
        except Exception:
            pass
    return answer_mock(question, stories)
