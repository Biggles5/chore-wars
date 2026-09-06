# SPRINT-REPORT: Sprint 1

Date: 2026-09-06. Gate: `make demo` runs quiet-night end to end. **Gate met.**

## What works

- `make demo` boots the simulator on quiet-night and serves the live top-down view at http://localhost:8090: house, FOV wedges, identity-channel identify rings, actors moving, deter segments flashing, event feed with thumbnails, sim clock, armed state, bus status.
- `make sim SCENARIO=car-prowler-0214`: car stops at 2:10, prowler works the driveway, the identity channel captures him at identify grade (467 px/m, 27 deg pitch) through the factory-aimed chokepoint, deter fires at 02:14:01 on seg-front and seg-east, prowler flees, car leaves.
- `make sim-headless SCENARIO=<name>`: full night simulates in under half a second, writes schema-validated JSONL. Six scenarios.
- Every published message validates against the v1 schemas at publish time. Quiet-night publishes about 3,900 messages (46 events plus telemetry), zero deter. Animals never deter. Disarmed modes never deter.
- DORI math is one module shared by placement tooling and the sim, pinned by tests to the audited anchors: 105 deg 8MP identify 5.9 m (fails at a 20 ft eave, pitch 37+), 60 deg 8MP 13.3 m at 19 deg pitch, 12MP 16 m, 30 deg pitch boundary 7.6 m, 10 ft eave benign beyond 2.4 m.
- Correlator boots standalone or in Docker, subscribes to the site topic tree, validates, buffers, serves `/health`, `/events`, `/telemetry`, REST `/ingest` (rejects bad payloads with the exact schema error).
- `make test`: 18 tests, all green, about 1.5 s.

## What's mocked

- Detection is geometric (FOV plus density threshold), no ML. Confidence and color histograms are deterministic synthetics; histograms are stable per actor across nodes so the Sprint 2 re-ID stub has something honest to key on.
- Deter decision runs inside the sim for now (DECISIONS.md D-013). Topics and payloads are final; Sprint 2 moves the decision to the correlator.
- Thumbnails are procedural SVG stamped SIMULATED, `media.synthetic: true` enforced by tests. Nothing synthetic can enter an evidence path.
- Frigate and Home Assistant are configured but idle against the sim (no RTSP source). Compose file validates; the full stack was not booted in this build environment (no Docker daemon available here), only the correlator was run and exercised directly.
- Correlator re-ID and story assembly are declared interfaces that raise NotImplementedError until Sprint 2.

## Exact commands

```bash
cd sightline
make setup
make demo                                  # quiet-night live view :8090
make sim SCENARIO=car-prowler-0214         # the 2:14 AM flagship
make sim-headless SCENARIO=porch-pirate    # writes runs/<id>/events.jsonl
make test                                  # 18 tests
make gateway                               # docker: broker + correlator + frigate + HA
```

## Top 3 risks going into Sprint 2

1. **Story assembly quality is the product.** The correlator has to stitch node-local tracks into one narrative (car and person are separate actors seen by 3+ nodes). The color-histogram stub will be brittle across day/night; the interface must make swapping in a real embedding model trivial, and the eval fixtures need adversarial cases (two people, similar clothing).
2. **Deter latency budget (<1 s local) is unproven.** Moving the deter decision from sim-internal to sim -> broker -> correlator -> HA -> WLED adds four hops. Sprint 2 must measure the loop on the real bus and keep a node-local fallback rule in the firmware design if the gateway path cannot hold the budget.
3. **App-to-correlator contract drift.** The app builds against the correlator websocket in Sprint 2 while the story schema is still settling. Mitigation: define `story.v1.schema.json` first, fixtures before UI, same discipline as event v1.
