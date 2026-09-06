"""Cloud API skeleton tests: plans, sync gating, monitoring dispatch.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
import json
import sys
from pathlib import Path

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "cloud" / "api"))

import main as cloud  # noqa: E402

client = TestClient(cloud.app)

STORY = {
    "schema": "sightline.story.v1", "story_id": "s-cloudtest01",
    "site_id": "site-demo", "started_ts": "2026-09-06T02:13:40-06:00",
    "status": "closed", "severity": "alert", "verified": True,
    "entities": [], "timeline": [],
}


def _account(plan="core"):
    r = client.post("/accounts", json={"email": "r@mabry.ai"})
    tok = r.json()["token"]
    if plan != "core":
        client.post("/accounts/plan", json={"plan": plan},
                    headers={"Authorization": f"Bearer {tok}"})
    return tok


def test_plans_have_no_contracts():
    d = client.get("/plans").json()
    assert d["contracts"] == "none, ever"
    assert d["plans"]["core"]["price"] == 0.0
    assert d["plans"]["core"]["cloud_sync"] is False


def test_core_cannot_sync():
    tok = _account("core")
    r = client.post("/sync/site-x/stories", json=STORY,
                    headers={"Authorization": f"Bearer {tok}"})
    assert r.status_code == 403


def test_plus_syncs_no_monitoring():
    tok = _account("plus")
    r = client.post("/sync/site-p/stories", json=STORY,
                    headers={"Authorization": f"Bearer {tok}"})
    assert r.status_code == 200 and r.json()["retained_days"] == 60
    out = client.get("/monitoring/outbox",
                     headers={"Authorization": f"Bearer {tok}"}).json()
    assert all(w["site_id"] != "site-p" for w in out["dispatched"])


def test_shield_dispatches_verified_alerts_only():
    tok = _account("shield")
    hdr = {"Authorization": f"Bearer {tok}"}
    client.post("/sync/site-s/stories", json=STORY, headers=hdr)
    unverified = dict(STORY, story_id="s-cloudtest02", verified=False)
    client.post("/sync/site-s/stories", json=unverified, headers=hdr)
    out = client.get("/monitoring/outbox", headers=hdr).json()["dispatched"]
    ids = [w["story_id"] for w in out if w["site_id"] == "site-s"]
    assert "s-cloudtest01" in ids
    assert "s-cloudtest02" not in ids, "unverified events are NEVER forwarded"


def test_auth_required():
    assert client.get("/monitoring/outbox").status_code == 401
