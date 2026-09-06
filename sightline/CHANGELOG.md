# CHANGELOG

## 0.2.0 (2026-09-06) Sprint 2

- `story.v1` schema: entities, timeline beats, best frames, deter outcome, verified flag, evidence rule.
- Correlator: histogram re-ID (swap-in interface for real embeddings), story assembly, severity, fled/stayed outcomes, narrator on close, websocket push, dedupe across MQTT + HTTP delivery.
- Sim bus: HTTP ingest bridge to the correlator so the full pipeline runs with no Docker.
- Narrator agent: mock + Claude modes, versioned guardrailed prompt, 5 eval fixtures.
- App prototype (React + Vite, 390px, light theme): Home and Verified Event live against the sim; house map SVG, narrator card, live tiles, re-ID chips, timeline with thumbnails, police export preview, Deter now wired to the gateway.
- Browser-verified gate: car-prowler-0214 renders the full story in the app, deter fires in the sim view, narrative cites frame timestamps.
- 29 tests green.

## 0.1.0 (2026-09-06) Sprint 1

- Repo scaffold: README, DECISIONS, ROADMAP, Makefile, requirements.
- Wire schemas v1: `sightline.event.v1`, `sightline.telemetry.v1`, MQTT topic tree, retention policy, evidence rule, fixtures.
- `hardware/dori_placement.py`: DORI rings (2025 rev thresholds incl. Validate 500), pitch-limited identify windows, placement verdicts, CLI. 10 tests pinned to the audited optics anchors.
- Perimeter simulator: house from scan JSON, virtual nodes sharing the placement math, actor paths, node-local tracks, schema-validated events and telemetry, procedural SVG thumbnails stamped SIMULATED, MQTT publishing with in-process fallback and JSONL log.
- Scenarios: quiet-night, car-prowler-0214 (deter fires 02:14:01), porch-pirate, party-arrivals, deer-3am, mail-daily.
- Live top-down web view (canvas, SSE, light theme) with deter flash on roofline segments and an event feed with thumbnails.
- Gateway: docker-compose (mosquitto, correlator, Frigate, Home Assistant), correlator skeleton with validated ingest and query, re-ID and story interfaces declared.
- Test suite: 18 passing (10 optics, 8 end-to-end sim).
