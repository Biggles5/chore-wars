# Monitoring Center Payload Spec

Verified-event hand-off from SightLine to professional central stations. Shield plan feature. This document defines what a central station receives, how, and what it never receives.

## The rule that defines the product

Unverified events are NEVER forwarded. Not throttled, not summarized, never sent.

Industry alarm traffic is 94 to 98% false, and police response reflects it: unverified calls get deprioritized or ignored outright (Seattle ignored 96% of roughly 13,000 false alarm calls in 2023). A central station that receives only verified SightLine stories can dispatch with confidence, and responders learn that a SightLine call means something is actually there. That asymmetry is the entire value of this integration.

An event qualifies for hand-off only when the gateway correlator has assembled a sightline.story.v1 with verified=true, meaning an identify-grade capture or multi-node confirmation.

## Payload contents

A sightline.story.v1 subset, plus dispatch context:

- Story core: story_id, schema, site_id, verified (always true in this feed), start/update timestamps, entity classes observed, per-node event references.
- Site address: street address and geo, as registered at provisioning.
- Best-frame references: URLs to the strongest identify frames. Native pixels only. A frame may be attached or referenced only when the story's evidence_exportable flag is true (every frame native, no synthetic or simulated frames). When evidence_exportable is false the payload carries metadata only, no imagery.
- Deter status and outcome: whether zone-follow strobe fired, on which segments, and whether the entity left the property afterward.
- Live view grant: a time-boxed token (15 min est.) letting the operator open live streams for the involved nodes. Scoped to the story's nodes only, revoked on story close or homeowner cancel.
- Homeowner ack state: unacked, acked_dismissed (homeowner says false/known), acked_confirmed (homeowner requests dispatch), unreachable. Central station procedure branches on this field.

## Example payload

```json
{
  "schema": "sightline.story.v1/monitoring",
  "story_id": "st_9f2a7c",
  "site_id": "site_04481",
  "verified": true,
  "started_at": "2026-09-06T03:12:41Z",
  "updated_at": "2026-09-06T03:14:02Z",
  "site": {
    "address": "1847 NE Maple Ct, Vancouver, WA 98684",
    "geo": { "lat": 45.6318, "lon": -122.5121 }
  },
  "entities": [
    {
      "entity_id": "en_02",
      "class": "person",
      "first_seen_node": "SL-2611-A3F0-00412",
      "confirmed_by_nodes": ["SL-2611-A3F0-00413", "SL-2611-A3F0-00415"]
    }
  ],
  "evidence_exportable": true,
  "best_frames": [
    {
      "node": "SL-2611-A3F0-00413",
      "ts": "2026-09-06T03:13:05Z",
      "native_pixels": true,
      "url": "https://evidence.sightline.example/st_9f2a7c/f_0031.jpg"
    }
  ],
  "deter": {
    "fired": true,
    "mode": "zone_follow_strobe",
    "segments": [14, 22],
    "outcome": "entity_departed"
  },
  "live_view": {
    "token": "lv_...",
    "expires_at": "2026-09-06T03:29:02Z",
    "nodes": ["SL-2611-A3F0-00413", "SL-2611-A3F0-00415"]
  },
  "homeowner_ack": "unreachable"
}
```

## Delivery

- Transport: HTTPS webhook to the central station's receiver, mTLS (both sides pinned), plus HMAC signature over the body with a per-station shared secret. Either check failing rejects the delivery.
- SLA: first delivery attempt within 5 s of story verification (est.).
- Retry: exponential backoff (1 s, 2 s, 4 s... capped at 60 s) for up to 15 min, then the story is flagged undelivered and the homeowner is alerted through the app as fallback.
- Story updates (new frames, deter outcome, ack changes) are delivered as follow-up payloads with the same story_id; receivers must treat story_id as the dedup key.
- Idempotency: every delivery carries a delivery_id; duplicate delivery_ids must be ignored by the receiver.

## Non-negotiables

- verified=true only. No raw event feed, no motion pings, no "possible activity."
- Frame attachment strictly gated on evidence_exportable=true. Synthetic or upscaled frames never leave the system in this feed.
- Live view is time-boxed and story-scoped. No standing camera access for central stations.
- All deliveries and live-view accesses are logged to the story's chain of custody record.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
