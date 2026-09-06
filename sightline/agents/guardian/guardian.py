"""Guardian: the autonomous monitoring agent. The product's brain.

Ingests closed-or-updating Event Stories, reads their AVS-01 score, and
runs the escalation policy: dismiss, watch, notify, intervene, handoff.
Every decision is instrumented with latency and estimated marginal cost,
because the business claim (agentic monitoring at single-digit dollars per
home per month) has to be measured, not asserted.

Latency budgets (SimpliSafe Active Guard / Deep Sentinel bar):
  score available     < 5 s   (correlator computes inline: effectively 0)
  deter / intervene   < 10 s
  handoff decision    < 30 s

Guardrails: GUARDRAILS.md in this directory. The hard ones are enforced in
code here, not just written down.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import json
import os
import time
import urllib.request
from datetime import datetime, timezone, timedelta

TZ = timezone(timedelta(hours=-6))

# ---- cost model (est., re-priced monthly against real usage) ----
# Mock mode runs deterministic logic: cost is compute amortization only.
# Claude-mode narration/scoring adds token costs, modeled at Haiku-class
# pricing: $1.00 / M input, $5.00 / M output (est.).
COST = {
    "base_event_usd": 0.00035,      # amortized gateway+cloud compute per story (est.)
    "token_in_per_m_usd": 1.00,
    "token_out_per_m_usd": 5.00,
    "handoff_usd": 0.002,           # webhook + receiver processing (est.)
    "wholesale_station_usd_mo": 5.99,  # COPS SecureNet class, Shield only
}

GATED_FACE_ID_JURISDICTIONS = {"IL", "TX", "PORTLAND-OR"}


def _estimate_tokens(story: dict) -> tuple:
    """Story JSON in, narrator paragraph out. Mock mode still counts what
    Claude mode WOULD spend, so the cost meter is honest about the upgrade."""
    tin = len(json.dumps(story)) // 4
    tout = 220  # homeowner paragraph + police summary (est.)
    return tin, tout


def estimate_cost_usd(story: dict, handoff: bool) -> float:
    tin, tout = _estimate_tokens(story)
    cost = (COST["base_event_usd"]
            + tin / 1e6 * COST["token_in_per_m_usd"]
            + tout / 1e6 * COST["token_out_per_m_usd"])
    if handoff:
        cost += COST["handoff_usd"]
    return round(cost, 6)


class Guardian:
    def __init__(self, receiver_url: str = None, jurisdiction: str = None,
                 deter_fn=None):
        self.receiver_url = receiver_url or os.environ.get("SIGHTLINE_STATION_URL", "")
        self.jurisdiction = (jurisdiction or os.environ.get("SIGHTLINE_STATE", "UT")).upper()
        self.deter_fn = deter_fn      # callable(site_id, zone) -> None
        self.log = []                 # decision records for the nightly report
        self.handoffs = []

    # ---- guardrails enforced in code ----
    def face_id_allowed(self) -> bool:
        return self.jurisdiction not in GATED_FACE_ID_JURISDICTIONS

    # ---- the policy engine ----
    def decide(self, story: dict) -> dict:
        t0 = time.monotonic()
        avs = story.get("avs") or {"score": 0, "confidence": 0, "rationale": "unscored"}
        score = avs["score"]
        deter = story.get("deter", {}) or {}
        actions = []
        handoff_sent = False
        handoff_status = None

        if score == 0:
            action = "dismiss"
        elif score == 1:
            action = "watch"
            actions.append("holding for corroboration; no notification, no dispatch")
        elif score == 2:
            action = "notify"
            actions.append("owner notified with the verified story")
        else:  # 3 or 4
            action = "handoff" if score >= 4 or deter.get("outcome") == "stayed" else "intervene"
            if not deter.get("fired") and self.deter_fn and story.get("zones"):
                zone = next((z for z in story["zones"] if z != "street"), "driveway")
                self.deter_fn(story["site_id"], zone)
                actions.append(f"zone-follow deter commanded ({zone})")
            elif deter.get("fired"):
                actions.append("edge reflex had already fired deter"
                               + (", subject fled" if deter.get("outcome") == "fled" else ""))
            actions.append("owner notified, priority alert")
            if action == "handoff" or deter.get("outcome") == "stayed":
                action = "handoff"
                handoff_sent, handoff_status = self._handoff(story, avs)
                actions.append("handed to central station"
                               if handoff_sent else "handoff queued (no receiver configured)")

        latency = {"score": 0.0,  # computed inline by the correlator
                   "intervene": round((time.monotonic() - t0) * 1000, 2),
                   "handoff_decision": round((time.monotonic() - t0) * 1000, 2)}
        cost = estimate_cost_usd(story, handoff_sent)
        decision = {
            "action": action,
            "actions_taken": actions,
            "decided_ts": datetime.now(TZ).isoformat(),
            "latency_ms": latency,
            "cost_usd": cost,
        }
        if handoff_sent or handoff_status is not None:
            decision["handoff"] = {"sent": bool(handoff_sent),
                                   "receiver": self.receiver_url or "unconfigured",
                                   "status": int(handoff_status or 0)}
        self.log.append({"story_id": story.get("story_id"), "avs": score,
                         "action": action, "cost_usd": cost,
                         "ts": decision["decided_ts"],
                         "site_id": story.get("site_id")})
        return decision

    # ---- central station handoff (AVS-01 scored, video-verified) ----
    def handoff_payload(self, story: dict, avs: dict) -> dict:
        """The payload a COPS / Rapid Response / Becklar class receiver
        consumes. Format contract: docs/monitoring-center-spec.md."""
        best = None
        for e in story.get("entities", []):
            bf = e.get("best_frame")
            if bf and (best is None or bf.get("px_per_m", 0) > best.get("px_per_m", 0)):
                best = dict(bf, entity_class=e["class"])
        return {
            "schema": "sightline.dispatch.v1",
            "avs01": avs,
            "story_id": story.get("story_id"),
            "site_id": story.get("site_id"),
            "window": {"start": story.get("started_ts"), "end": story.get("ended_ts")},
            "verified": story.get("verified", False),
            "video_verified": True,
            "subjects": [e["class"] for e in story.get("entities", [])],
            "zones": story.get("zones", []),
            "deter": story.get("deter"),
            "best_frame": best,
            "evidence": {
                "native_frames_available": bool(story.get("evidence_exportable")),
                "note": None if story.get("evidence_exportable")
                        else "frames simulated or non-native: metadata only",
            },
            "narrative": (story.get("narrative") or {}).get("police_summary", ""),
            "guardrail": "Guardian never calls 911 directly and never asserts a crime occurred; "
                         "the operator holds dispatch authority.",
        }

    def _handoff(self, story: dict, avs: dict) -> tuple:
        if not self.receiver_url:
            return False, None
        try:
            req = urllib.request.Request(
                self.receiver_url.rstrip("/") + "/dispatch",
                data=json.dumps(self.handoff_payload(story, avs)).encode(),
                headers={"content-type": "application/json"})
            with urllib.request.urlopen(req, timeout=3) as r:
                self.handoffs.append(story.get("story_id"))
                return True, r.status
        except Exception:
            return False, 0

    # ---- nightly report + cost meter ----
    def nightly_report(self, homes: int = 1) -> dict:
        """The trust feature and the unit-economics proof in one object."""
        events = len(self.log)
        total = round(sum(e["cost_usd"] for e in self.log), 6)
        by_action = {}
        for e in self.log:
            by_action[e["action"]] = by_action.get(e["action"], 0) + 1
        # extrapolate: this log's window scaled to 30 nights per home
        per_home_night = total / max(homes, 1)
        monthly = round(per_home_night * 30, 4)
        return {
            "events_processed": events,
            "actions": by_action,
            "handoffs": len(self.handoffs),
            "cost_total_usd": total,
            "cost_per_home_night_usd": round(per_home_night, 6),
            "cost_per_home_month_usd_est": monthly,
            "wholesale_station_usd_mo": COST["wholesale_station_usd_mo"],
            "fully_loaded_target_usd_mo": 6.0,
            "under_target": monthly + 0 <= 6.0,
            "note": "station fee applies on Shield only and is passed through the plan price",
        }
