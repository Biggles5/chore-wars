# Data architecture

One topic tree, versioned schemas, retention that matches the plan you pay for, and a hard wall around Core.

## MQTT topic tree

```
sightline/<site_id>/<node_id>/event        node -> gateway    sightline.event.v1     QoS 1
sightline/<site_id>/<node_id>/telemetry    node -> gateway    sightline.telemetry.v1 QoS 0
sightline/<site_id>/deter/cmd              gateway -> nodes   deter command          QoS 1
sightline/<site_id>/gateway/story          correlator -> app  sightline.story.v1     QoS 1
sightline/<site_id>/<node_id>/ota          gateway -> node    OTA control            QoS 1
```

Nothing retained on the broker. Stories are served over REST and websocket by the correlator; the broker is transport, not storage.

## Schemas

`gateway/schemas/*.schema.json` is the single source of truth. Every payload carries a `schema` field. Both ends validate; invalid payloads are rejected and counted, never coerced. Versioning: additive optional fields are free; anything else ships a new versioned file next to the old one. Old versions are never edited.

## Retention

| Where | What | How long | Plans |
|---|---|---|---|
| Node microSD | full-rate loop, native frames | 72 h ring | all |
| Gateway | events, stories, flagged clips | user-set cap, default 90 days (est.) | all |
| Cloud | events, stories, flagged clips | 60 days | Plus, Shield only |

## What never leaves the house on Core

On Core the cloud sync path does not exist. Not disabled, not dark-launched: the gateway build for Core contains no sync client, no cloud credentials, no upload queue. The only outbound traffic is OTA pulls and (if the owner opts in) anonymous fleet-health pings with no event data. This is the product's spine, not a marketing bullet: 72% of buyers have privacy concerns and the answer has to be architectural.

## Event memory and re-ID

Cross-camera re-ID embeddings are per-site and ephemeral: they exist to stitch one story and age out with it. There is no cross-site identity database, no face database, no enrollment. "Familiar person" features, when they ship, store the owner's own labels locally.

## Data flow summary

node (detect, native frames, 72 h loop) -> gateway (stitch, story, narrate, retain) -> app (render, act) -> optional cloud (Plus/Shield sync, monitoring hand-off on Shield).
