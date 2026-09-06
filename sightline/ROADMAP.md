# ROADMAP.md

Execution order and phase gates. A sprint is done when its gate demo runs clean from a fresh clone.

## Sprint 1: foundation and simulator [DONE 2026-09-06]
- Repo scaffold, root docs, Makefile.
- Versioned schemas: `sightline.event.v1`, `sightline.telemetry.v1` (JSON Schema, with fixtures).
- `hardware/dori_placement.py` with unit tests pinned to the audited optics numbers.
- Simulator core: house from JSON scan, virtual nodes with real DORI rings, actors with paths, synthetic events and thumbnails, MQTT-identical publishing with in-process fallback, scripted scenarios.
- Top-down live web view (canvas, light theme).
- Gateway docker compose boots: mosquitto, Frigate, correlator skeleton, Home Assistant.

**GATE: `make demo` runs quiet-night end to end.** Events flow from virtual nodes through the bus, validate against the schema, and render in the live view.

## Sprint 2: stories and the first two app screens [DONE 2026-09-06]
- Correlator: track maintenance, cross-camera re-ID (color-histogram stub behind a real re-ID interface), Event Story assembly, deter trigger via HA, REST + websocket for the app.
- Narrator agent in mock mode (Claude mode optional).
- App Home + Verified Event screens live against the sim.

**GATE: `sim run car-prowler-0214` renders a full story in the app with deter firing in the sim view.**

## Sprint 3: full app, quote agent, deter package, firmware skeleton [DONE 2026-09-06]
- App: Ask, Scenes, Onboarding/Scan-to-Quote.
- Quote agent: deterministic pricing engine, per-terminal power check, DORI plan.
- WLED preset pack + HA automation package (zone-follow strobe, quiet hours, privacy masks).
- ESP32-S3 PlatformIO firmware skeleton compiling in CI without hardware.

**GATE: full demo script clean, tests green.**

## Sprint 4: hardware, guides, compliance, pitch [DONE 2026-09-06]
- CAD exports (STL + STEP): node housing (Gemstone 30mm channel), universal retrofit clip, door node, bench fixture.
- bench_bom.csv and production_bom.csv. Wiring SVGs.
- All 8 guides, compliance docs, pitch assets, website/demo page.

**GATE: a stranger can clone, run the demo, print the housing, and order the bench BOM using only the repo.**

## Definition of done for the whole build
- `make demo` boots sim + gateway + app.
- The scripted 2:14 AM scenario produces a narrated verified event in the app in under 60 seconds of wall time.
- Every doc in section 3 of the build spec exists and is internally consistent.
- DECISIONS.md explains every assumption.
- Zero em dashes anywhere in the docs.
