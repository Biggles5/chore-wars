# SightLine Central Station Integration Spec v1

Audience: monitoring partner engineering and operations (COPS SecureNet, Rapid Response, Becklar/AvantGuard class receivers). Scope: receiving sightline.dispatch.v1 events and operating on them.

## 1. What you receive, and what you never receive
SightLine forwards only verified events: AVS-01 score >= 2 with video verification. Events scoring below 2 are never sent. Guardian (our monitoring agent) never calls 911 and never asserts a crime. Your operator holds dispatch authority, always. Expected effect on your board: near-zero false traffic from this account base (industry baseline: 94-98% of dispatches are false).

## 2. Dispatch payload: sightline.dispatch.v1
Fields: AVS-01 score + confidence + rationale, story window, subjects, zones, deter status and outcome, best-frame reference with DORI grade, native-frames-available flag, police-readable narrative, and the guardrail line. Simulated or enhanced frames NEVER attach to a dispatch; if only simulated frames exist, you get metadata only and the flag reads false.

### Example payload
```json
{
  "schema": "sightline.dispatch.v1",
  "event_id": "evt_8f3a2c91d4",
  "site_id": "site_a1b2c3",
  "account_number": "SL-104477",
  "created_at": "2026-09-06T02:14:09Z",
  "avs01": {
    "score": 3,
    "confidence": 0.95,
    "rationale": "Single adult subject crossed perimeter zone Z2 at 02:13:41, approached rear door, manipulated handle for 22s. No known-person match on this site. Deter sequence escalated through levels 1-2."
  },
  "story_window": {
    "start": "2026-09-06T02:13:38Z",
    "end": "2026-09-06T02:14:07Z"
  },
  "subjects": [
    {
      "subject_ref": "subj_local_01",
      "type": "person",
      "count": 1,
      "site_reid": "ephemeral, per-site only"
    }
  ],
  "zones": ["Z2_rear_yard", "Z3_rear_door"],
  "deter": {
    "status": "completed",
    "levels_used": [1, 2],
    "outcome": "fled",
    "fled_at": "2026-09-06T02:14:03Z"
  },
  "evidence": {
    "best_frame_ref": "frm_5541",
    "best_frame_dori_grade": "recognize",
    "native_frames_available": false,
    "note": "Metadata only. Native frames not yet uplinked at dispatch time; simulated frames never attach. Native frames follow within the story window sync, typically <60s."
  },
  "live_view": {
    "grant_token": "lv_tok_29ce...",
    "expires_in_s": 900
  },
  "narrative": "At 2:14 AM a single adult entered the rear yard, approached the rear door, and manipulated the handle for 22 seconds before fleeing when deterrence activated. Video-verified, AVS-01 level 3.",
  "guardrail": "Guardian never calls 911 and never asserts a crime. This event is machine-scored and video-verified. Dispatch authority rests with the receiving operator."
}
```

Live-view grant token: time-boxed to 15 minutes (est.), scoped to the story cameras only.

## 3. Transport
- HTTPS webhook to your receiver endpoint.
- mTLS both directions, plus HMAC-SHA256 signature over the body (key exchanged at onboarding, rotated quarterly).
- First-attempt delivery SLA: 5s from operator-forward decision (est.).
- Retry: exponential backoff 1s, 2s, 4s, 8s, then 30s intervals to 15 minutes; events are idempotent by event_id, dedupe on it.
- Acknowledge with HTTP 200 and body {"ack": "<event_id>"}. Non-200 or timeout triggers retry.

## 4. Operator flow
1. Score 3-4: priority queue, operator reviews best frame + narrative, opens live view if needed, dispatches per your AVS-01 procedures.
2. Score 2: standard queue, video-verified but lower certainty; operator judgment.
3. Score <2: never sent. If you receive one, it is a bug; reject and flag.
4. Deter outcome "fled" with no re-entry inside story window: operator may close per your policy; the event still files to the account record.

## 5. Receiver conformance checklist
1. Accepts sightline.dispatch.v1 over HTTPS with mTLS client cert validation.
2. Verifies HMAC on every delivery, rejects on mismatch.
3. Acks within 2s with event_id echo.
4. Dedupes by event_id across retries.
5. Maps avs01.score to your AVS-01 handling tiers (2 standard, 3-4 priority).
6. Renders narrative and best-frame reference to the operator screen.
7. Honors native_frames_available=false as metadata-only (no frame fetch attempted until flag flips).
8. Exercises live-view token within its 15 min (est.) window and handles expiry gracefully.
9. Returns disposition (dispatched, closed, referred) to our postback endpoint within 24h.
10. Never initiates contact with the homeowner except per agreed escalation list.

## 6. Pilot proposal
- 90 days, N <= 500 accounts.
- Startup pricing ask: wholesale per-account rate in the $5.99/account/mo class (COPS SecureNet benchmark), with a volume step-down at 2,500 and 10,000 accounts.
- Joint success metrics: false dispatch rate, operator handle time per event, disposition postback rate, mean ack latency.
- Exit: either party, 30 days notice, account transition plan included.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
