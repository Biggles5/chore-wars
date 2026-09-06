# CHANGELOG

## 0.5.0 (2026-09-06) Addendums 1 + 2: the Brain and the Ops Engine

- Realistic synthetic camera frames (IR night stills with OSD, grain, bounding boxes; daylight grading) replacing the pictograms, still SIMULATED-stamped.
- AVS-01 scoring in the correlator (story.avs, additive); Guardian agent: escalation policy, latency budgets, cost meter, nightly report, code-enforced guardrails, mock central-station receiver that refuses sub-AVS-2 events.
- Jurisdiction feature flags in code (IL/TX/Portland-OR face gates), white-label licensing pivot as env config, biometric matrix + AVS-01 reference + monitoring-license checklist in compliance.
- econ/: unit economics with encoded kill thresholds (CAC < $1,000 at $285 blended; marginal monitoring < $6 at $4.17; margin > 60% at 67.1%; 8% attrition floor), 3 scenario HTML reports, throughput model (2.4 hr installs, learning curves, recruitment funnel, seasonality).
- Ops Engine: scan.v1 + 3 sample houses, scan-to-kit (cut lists, connector maps, injection plans, aim angles, AR overlay, price with one source of truth), capacity/scheduling engine, installer runbook with QC gates + 30-point commissioning, QC agent (25 fixtures, 25/25), watchtower proactive tickets, certification package, dealer dashboard.
- ops-sim: 26-week metro simulation, 3 scenarios; week-12: 109/mo vs 27/mo, backlog 0 vs 486; chart embedded in the demo page.
- App: Guardian tab (night report, cost-of-protection meter, insurance export surface, jurisdiction flags), installer mode with live QC gating.
- `make demo` prints the AVS-01 verdict, Guardian cost per home per month, and the opssim week-12 comparison.
- Strategy docs (disruption thesis, market share plan, partnerships, counter-disruption, investor memo, ops disruption) and the partnerships kit.
- 127 tests green including every encoded threshold.

## 0.4.0 (2026-09-06) Sprint 4

- CAD: CadQuery parametric models with real committed exports (STL + STEP): track node housing (Gemstone 30mm channel), universal retrofit clips for three brand profiles, door node, bench fixture.
- BOMs: orderable bench_bom.csv (~$754 est.) and production_bom.csv ($33 to $47 at 25K with cost-down notes).
- Wiring SVGs: 12V retrofit tap, 48V blind-mate bus, injection kit.
- Architecture docs complete: system (with the 2:14 sequence + latency budgets), power, data, network, security, evidence-policy (Puloka, chain of custody), privacy; Matter bridge roadmap.
- All 8 guides: bench build, house pilot (30-night protocol), 48V dealer install (175 min flow), 12V retrofit per brand, homeowner setup, integrations, test plans (incl. re-ID bias gate), compliance path.
- Compliance: FCC/ETL/NDAA/IP66 checklists, privacy + retention policy, 50-state + DC audio-consent matrix.
- Pitch: investor one-pager, dealer pitch, HOA approval packet template.
- Ops + IP docs: OTA pipeline with rollback, telemetry dashboard spec, RMA + serial scheme, monitoring-center payload spec, insurance one-pager, trademark alternates + knockout search, provisional patent notes (5 claim areas).
- Agents: support triage (telemetry-first rules, safety escalation) and dealer GTM (ICP, enrichment schema, 3-touch sequences in Ryan's voice, booking flow), 5 evals each.
- Cloud API skeleton: plans, Core sync refusal, Plus/Shield sync, verified-alerts-only monitoring dispatch, tested.
- Website demo page embedding the live sim + app. App accessibility pass (focus rings, reduced motion, 44px targets) + Spanish i18n stub.
- 63 tests green.

## 0.3.0 (2026-09-06) Sprint 3

- Quote agent: deterministic scan-to-kit engine over shared power_budget + dori_placement modules; SKU 1 band and 48V sub-3-hour checks; 5 eval fixtures.
- `hardware/electronics/power_budget.py`: voltage drop tables, per-terminal checks (one node per terminal, 12W ceiling, 75 ft rule, 9 to 56V buck window), injection decisions, 48V rail headroom.
- Gateway endpoints: `/ask` (chat over event memory, mock + Claude), `/quote`, `/scenes` (+ natural-language designer), manual deter publishes on MQTT.
- App: Ask, Scenes (zone painting, scene designer, enforced privacy masks), Setup/Scan-to-Quote (kit, price, power check, DORI coverage rings). All browser-verified live.
- WLED preset pack (zone-follow strobe, quiet-hours, welcome, all-clear) + HA zone-to-segment deter automation package.
- ESP32-S3 firmware skeleton: schema-exact MQTT publishing, heartbeat, watchdog, OTA hook, provisioning AP, motion state machine; pinned platform; CI workflow template (registry blocked in this build env, see D-019).
- `make demo` boots correlator + sim + app with one command.
- 48 tests green.

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
