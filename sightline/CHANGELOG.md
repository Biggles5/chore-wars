# CHANGELOG

## 0.1.0 (2026-09-06) Sprint 1

- Repo scaffold: README, DECISIONS, ROADMAP, Makefile, requirements.
- Wire schemas v1: `sightline.event.v1`, `sightline.telemetry.v1`, MQTT topic tree, retention policy, evidence rule, fixtures.
- `hardware/dori_placement.py`: DORI rings (2025 rev thresholds incl. Validate 500), pitch-limited identify windows, placement verdicts, CLI. 10 tests pinned to the audited optics anchors.
- Perimeter simulator: house from scan JSON, virtual nodes sharing the placement math, actor paths, node-local tracks, schema-validated events and telemetry, procedural SVG thumbnails stamped SIMULATED, MQTT publishing with in-process fallback and JSONL log.
- Scenarios: quiet-night, car-prowler-0214 (deter fires 02:14:01), porch-pirate, party-arrivals, deer-3am, mail-daily.
- Live top-down web view (canvas, SSE, light theme) with deter flash on roofline segments and an event feed with thumbnails.
- Gateway: docker-compose (mosquitto, correlator, Frigate, Home Assistant), correlator skeleton with validated ingest and query, re-ID and story interfaces declared.
- Test suite: 18 passing (10 optics, 8 end-to-end sim).
