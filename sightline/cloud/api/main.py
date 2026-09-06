"""SightLine cloud API skeleton (optional layer; Core never touches it).

Accounts, plans, event sync (Plus/Shield), monitoring webhook dispatch
(Shield). In-memory stores stand in for the real database; every route and
payload shape is the contract the real service implements.

Run: python3 -m uvicorn main:app --port 8095 (from this directory)

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import time
import uuid

from fastapi import FastAPI, Header, HTTPException

app = FastAPI(title="SightLine cloud", version="0.1.0")

PLANS = {
    "core": {"price": 0.0, "cloud_sync": False, "monitoring": False,
             "note": "local only, forever; this API holds no event data for core"},
    "plus": {"price": 9.99, "cloud_sync": True, "retention_days": 60,
             "monitoring": False},
    "shield": {"price": 19.99, "cloud_sync": True, "retention_days": 60,
               "monitoring": True},
}

_accounts = {}   # account_id -> {email, plan, sites: [site_id]}
_sync = {}       # site_id -> {"stories": [...], "events_count": int}
_webhooks = []   # dispatched monitoring payloads (stub outbox)


def _auth(token: str | None) -> str:
    """Bearer token -> account id. Stub: token IS the account id."""
    if not token or not token.startswith("Bearer "):
        raise HTTPException(401, "bearer token required")
    account_id = token.removeprefix("Bearer ").strip()
    if account_id not in _accounts:
        raise HTTPException(401, "unknown account")
    return account_id


@app.get("/plans")
def plans():
    return {"plans": PLANS, "contracts": "none, ever"}


@app.post("/accounts")
def create_account(body: dict):
    email = (body or {}).get("email", "")
    if "@" not in email:
        raise HTTPException(422, "email required")
    account_id = f"acct-{uuid.uuid4().hex[:10]}"
    _accounts[account_id] = {"email": email, "plan": "core", "sites": []}
    return {"account_id": account_id, "plan": "core",
            "token": account_id, "note": "stub token = account id"}


@app.post("/accounts/plan")
def set_plan(body: dict, authorization: str = Header(default=None)):
    account_id = _auth(authorization)
    plan = (body or {}).get("plan")
    if plan not in PLANS:
        raise HTTPException(422, "unknown plan")
    _accounts[account_id]["plan"] = plan
    return {"account_id": account_id, "plan": plan}


@app.post("/sync/{site_id}/stories")
def sync_story(site_id: str, story: dict, authorization: str = Header(default=None)):
    """Gateway pushes closed stories on Plus/Shield. Core builds contain no
    client for this route: the check below is defense in depth, not the wall."""
    account_id = _auth(authorization)
    acct = _accounts[account_id]
    if not PLANS[acct["plan"]]["cloud_sync"]:
        raise HTTPException(403, "plan has no cloud sync (core is local only)")
    if story.get("schema") != "sightline.story.v1":
        raise HTTPException(422, "sightline.story.v1 required")
    box = _sync.setdefault(site_id, {"stories": [], "events_count": 0})
    box["stories"] = [s for s in box["stories"]
                      if s["story_id"] != story["story_id"]] + [story]
    box["stories"] = box["stories"][-500:]
    if (PLANS[acct["plan"]]["monitoring"] and story.get("verified")
            and story.get("severity") == "alert" and story.get("status") == "closed"):
        _webhooks.append({
            "dispatched_at": time.time(), "site_id": site_id,
            "payload": "see docs/monitoring-center-spec.md",
            "story_id": story["story_id"],
        })
    return {"ok": True, "retained_days": PLANS[acct["plan"]]["retention_days"]}


@app.get("/sync/{site_id}/stories")
def get_synced(site_id: str, authorization: str = Header(default=None)):
    _auth(authorization)
    return _sync.get(site_id, {"stories": [], "events_count": 0})


@app.get("/monitoring/outbox")
def monitoring_outbox(authorization: str = Header(default=None)):
    """Stub visibility into dispatched monitoring events (Shield).
    Real spec: docs/monitoring-center-spec.md (mTLS + HMAC webhook)."""
    _auth(authorization)
    return {"dispatched": _webhooks[-50:]}


@app.get("/health")
def health():
    return {"ok": True, "accounts": len(_accounts), "sites_synced": len(_sync)}
