"""Mock central-station receiver (COPS / Rapid Response / Becklar class).

Accepts the AVS-01 scored, video-verified dispatch payload so the demo
shows the full chain: node -> correlator -> Guardian -> central station.

Run: python3 -m uvicorn receiver:app --port 8097 (from this directory)

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

from datetime import datetime

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Mock central station", version="0.1.0")
_queue = []


@app.post("/dispatch")
def dispatch(payload: dict):
    if payload.get("schema") != "sightline.dispatch.v1":
        raise HTTPException(422, "sightline.dispatch.v1 required")
    avs = payload.get("avs01") or {}
    if avs.get("score", 0) < 2:
        # a real station would refuse unverified noise; so does the mock
        raise HTTPException(422, "receiver accepts AVS-01 score >= 2 only")
    record = {
        "received_at": datetime.now().astimezone().isoformat(),
        "avs_score": avs.get("score"),
        "site_id": payload.get("site_id"),
        "story_id": payload.get("story_id"),
        "operator_action": ("priority dispatch review" if avs.get("score", 0) >= 3
                            else "operator review"),
    }
    _queue.append(record)
    return {"ok": True, "queued_as": record["operator_action"],
            "position": len(_queue)}


@app.get("/queue")
def queue():
    return {"pending": _queue[-50:], "count": len(_queue)}


@app.get("/health")
def health():
    return {"ok": True, "station": "mock (COPS SecureNet class, $5.99/account/mo est.)"}
