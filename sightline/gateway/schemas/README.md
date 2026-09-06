# SightLine wire schemas

Versioned JSON Schemas for everything that crosses the bus. The simulator, firmware, correlator, and app all validate against these files. There is one source of truth and this is it.

## Versioning policy

- Schema id and filename carry the version: `event.v1.schema.json`, `$id: sightline.event.v1`.
- Every payload carries a `schema` field naming its version. Consumers reject unknown versions.
- Additive optional fields bump nothing. Anything that removes, renames, or changes meaning bumps the version and ships a new file next to the old one. Old versions are never edited.

## MQTT topic tree (v1)

```
sightline/<site_id>/<node_id>/event        node -> gateway    sightline.event.v1
sightline/<site_id>/<node_id>/telemetry    node -> gateway    sightline.telemetry.v1
sightline/<site_id>/deter/cmd              gateway -> nodes   deter command (Sprint 2 schema)
sightline/<site_id>/gateway/story          correlator -> app  Event Story (Sprint 2 schema)
sightline/<site_id>/<node_id>/ota          gateway -> node    OTA control (Sprint 3 schema)
```

QoS 1 for events and deter commands, QoS 0 for telemetry. Retained: none (stories are served over REST and websocket by the correlator, not retained on the broker).

## Retention (enforced, per plan)

- Node: 72 hour microSD loop, always, all plans.
- Core ($0): nothing leaves the house. Gateway keeps events and stories locally. No cloud sync path exists on Core, not a disabled one, an absent one.
- Plus/Shield: 60 day cloud retention of events, stories, and flagged clips.

## Evidence rule (schema-enforced)

`media.native_pixels` must be `true` for any frame entering the evidence path. The simulator always sets `media.synthetic: true` and the correlator refuses to export anything synthetic or non-native. AI narrates, never fabricates imagery (State v. Puloka, 2024).

Fixtures used by the test suite live in `fixtures/`.
