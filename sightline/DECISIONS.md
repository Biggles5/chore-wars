# DECISIONS.md

Every assumption made while building, dated, with reasoning. Section 0 of the master build spec wins over anything here. Tensions are noted where they exist.

## 2026-09-06 (Sprint 1)

### D-001: Monorepo lives inside the chore-wars repository, under `sightline/`
This session's GitHub scope is `biggles5/chore-wars` and the designated push branch is `claude/chores-wars-impact-check-xpsj0r`. Building in a `sightline/` subdirectory keeps the Chore Wars app (`index.html`) untouched, which was the standing instruction. When SightLine gets its own repo, `git filter-repo --path sightline/` or a plain copy migrates it cleanly. Nothing in SightLine references chore-wars files.

### D-002: `make` over `just`
`make` ships on every mac and Linux box a dealer or investor might clone on. `just` is nicer but adds an install step, which violates the "3 commands" bar. Makefile targets are thin wrappers over python and docker compose so nothing is trapped in make syntax.

### D-003: Demo runs without Docker; Docker is the full-stack path
The Sprint 1 gate is "make demo runs quiet-night end to end." Requiring Docker Desktop for the first-run demo would fail on locked-down laptops. So the simulator carries an in-process event bus with the exact MQTT topic layout and payloads, plus a JSONL event log, and serves its own web view. When a real broker is reachable (localhost:1883 by default, `SIGHTLINE_MQTT_HOST` to override) the sim publishes to it identically. `make gateway` boots the real broker + Frigate + correlator + Home Assistant via docker compose.

### D-004: 12MP identity sensor assumed 4608 x 2592
"12MP" is ambiguous. 4000 x 3000 (4:3, 12.0MP) gives an identify reach of 13.9 m at 60 degrees, which does not match the audited 16 m figure. 4608 x 2592 (16:9, 11.9MP, the common "12MP" security SKU, e.g. IMX515 class) gives 15.96 m, which matches. So 4608 horizontal pixels is the working assumption for the identity channel. Recorded in `hardware/dori_placement.py` and pinned by tests.

### D-005: DORI density computed on ground distance, target face at 1.7 m
The audited numbers (105 deg 8MP identify at 5.9 m with pitch 37 to 42 inside it, 60 deg 8MP at 13.3 m with pitch about 19 at the edge, pitch 30 boundary at 7.6 m for a 6.1 m eave) reproduce exactly when pixel density is horizontal_pixels / (2 * d * tan(HFOV/2)) with d as ground (horizontal) distance, and pitch as atan((eave - 1.7) / ground_distance). The pitch values pin d as ground distance: atan(4.4 / 5.9) = 36.7 degrees matches the audited "37" at the 5.9 m ring edge. Face height 1.7 m (est.) lands the 30 degree boundary at 7.62 m. Line-of-sight distance is derived for reporting. Thin-lens, distortion-free approximation; real lens tables replace it in Phase 1 without changing the interface.

### D-006: Event schema is versioned by filename and by a `schema` field in every payload
`gateway/schemas/event.v1.schema.json`, and every event carries `"schema": "sightline.event.v1"`. Consumers reject what they do not recognize instead of guessing. Same for telemetry.

### D-007: Simulator timescale
Real scenarios span minutes to hours. The sim runs on a configurable timescale (default 60x for timed scenarios, quiet-night compresses 8 hours into about 50 s wall time at 600x). Event timestamps are simulated wall-clock time (the scenario's clock, e.g. 02:14), not the developer's laptop time, so stories and the app read correctly.

### D-008: Synthetic thumbnails are procedural SVG
No image libraries, no binary assets, fully deterministic, tiny in git. Each event's `media.thumb_ref` points to an SVG rendered from the event geometry (class silhouette, node id, timestamp, DORI level). `media.native_pixels` is `true` only on real hardware; the sim marks frames `"synthetic": true` so nothing synthetic can ever masquerade as evidence. This is the evidence-policy rule enforced at the schema level from day one.

### D-009: Correlator is a skeleton in Sprint 1
Sprint 1's gate needs the gateway to boot, not to stitch stories. The correlator ships as a FastAPI service with health, ingest, recent-events, and an MQTT subscriber, with the track/story interfaces stubbed and typed so Sprint 2 fills them in without moving files.

### D-010: CadQuery (decided in Sprint 4, as leaned)
CadQuery 2.8 over OpenSCAD: native STEP export (ODMs need STEP; OpenSCAD cannot produce it natively) and python parametrics that share the repo toolchain. `hardware/cad/sightline_cad.py` builds all four part families and exports STL + STEP; the exports in `hardware/cad/exports/` are real CadQuery output, committed so a stranger can print without installing the CAD stack. Channel mating dimensions are published-data estimates exposed as named parameters; the first test print calibrates them.

### D-011: Python 3.11 stdlib + 5 pinned deps for the whole Sprint 1 runtime
fastapi, uvicorn, paho-mqtt, jsonschema, pytest. Nothing else. Keeps `make setup` under 30 seconds and the offline story honest.

### D-012: Sim web view uses Server-Sent Events, not websockets
SSE is one-directional state streaming, which is all the top-down view needs, works through the same FastAPI app, and needs zero client libraries. The app prototype (Sprint 2) gets a websocket from the correlator, where bidirectional matters (Deter now button).

## 2026-09-06 (Sprint 2)

### D-014: Sim-to-correlator HTTP bridge for the no-Docker path
Without a broker the correlator would sit blind. The sim bus grew a fourth sink: POST to the correlator's `/ingest` when one is reachable (SIGHTLINE_CORRELATOR_URL). The correlator dedupes by event_id, so when a broker IS present and both paths deliver, nothing double-counts. thumb_refs are rewritten to absolute sim-view URLs on this path so the app can render thumbnails (SIGHTLINE_SIM_BASE).

### D-015: Node-local deter stays; the correlator records and can also command
The deter latency budget is <1 s local. That argues for the edge owning the reflex (node/sim decides, fires, publishes deter.fired) with the correlator recording it into the story and able to issue its own deter over `sightline/<site>/deter/cmd` (app Deter Now). This mirrors the real firmware plan: reflex at the edge, judgment at the gateway. Supersedes the "moves entirely to the correlator" wording of D-013.

### D-016: App times render in the house's clock, never the browser's
Event timestamps carry the site's UTC offset. The app formats from the ISO string itself instead of `new Date().toLocaleTimeString()`, so a 2:14 AM prowler reads 2:14 AM from any timezone. Found the hard way: the dev browser (UTC) showed 8:10 AM.

### D-017: One identity-grade beat per entity
Beat generation keyed on per-entity level transitions flapped when multiple nodes at different DORI grades interleaved (about 80 duplicate beats in one story). An entity now gets exactly one "identity-grade capture" beat, from whichever node lands it first. Best-frame tracking still upgrades continuously.

### D-018: uvicorn needs the `websockets` package for WS routes
FastAPI's `@app.websocket` silently 404s under uvicorn without the `websockets` (or wsproto) protocol package. Pinned in requirements. Found in live testing, invisible in TestClient.

## 2026-09-06 (Sprint 4)

### D-023: Audio-law matrix treats mixed and unsettled states as all-party
Where state audio-consent law is mixed or unsettled (Connecticut, Delaware, Michigan, Nevada, Oregon, Vermont), the in-app behavior uses the strictest reading (all-party warning). Legal exposure is asymmetric: over-warning costs nothing, under-warning costs everything. The matrix is informational input for counsel, not legal advice, and says so.

### D-024: Cloud API is a contract skeleton with in-memory stores
`cloud/api/main.py` defines the routes, auth shape, plan gating (Core cannot sync by 403 AND by absence of a client, defense in depth), and the verified-alerts-only monitoring dispatch. Real persistence, real auth, and the mTLS webhook come with the first cloud deployment; the tests pin the contract now so the gateway sync client can be written against it.

### D-025: i18n ships as a working stub, not a full extraction
`src/i18n.js` + `locales/es.json` prove the mechanism (tab bar and status chips localize by browser language). Full string extraction across screens is scheduled work; doing it now would churn every screen file while the UI is still moving.

## 2026-09-06 (Sprint 3)

### D-019: Firmware compile is CI-verified, not container-verified
This build environment's network policy blocks api.registry.platformio.org (proxy 403), so the espressif32 toolchain cannot download here. The firmware pins platform espressif32@6.7.0 and libraries, and `ci/firmware-build.yml` is a ready GitHub Actions workflow that runs `pio run` on every firmware change. The claim is "compiles in CI with no hardware"; the workflow is the proof mechanism, activated when SightLine gets its own repo (workflows are shipped as templates in `ci/`, not enabled on this shared repo).

### D-020: Quote agent price book tuned to the playbook bands
Track node $279, door node $179, gateway $199, retrofit install $249 + $79/node (all est.). These land the reference homes inside the SKU 1 $1,299 to $1,799 installed band and the 48V rail under 3 install hours for a 160 ft single story. The engine flags every output as estimates; the BOM cost-down work in Sprint 4 owns reconciling these retail targets against the $33 to $47 production BOM.

### D-021: 48V LED load estimated at 0.85 duty for headroom math
Lights are duty-cycle oversubscribed by every incumbent's design; cameras never are (counted at full continuous draw). The 45% headroom target computes LED load at 0.85 duty (est.) and cameras at 100%. Worst-case all-white-all-on is still within supply, just below the 45% comfort target, and the quote surfaces both.

### D-022: Ask and scene-designer agents run gateway-side
The app calls `/ask` and `/scenes/design` on the correlator rather than shipping agent logic client-side: the gateway owns event memory (Core plan: nothing leaves the house), so the answering has to happen where the data lives. Claude modes are gateway env switches (SIGHTLINE_ASK_MODE, SIGHTLINE_NARRATOR_MODE); the app UI is identical in both modes.

### D-013: Deter logic lives in the sim for Sprint 1, moves to the correlator in Sprint 2
The view needs to show deter zones firing now. The sim carries a placeholder rule (person or vehicle dwelling inside the identify ring during armed hours triggers zone-follow deter). Sprint 2 replaces this with the correlator issuing deter commands over `sightline/<site>/deter/cmd`, and the sim just obeys the bus. The topic and payload are already final so nothing downstream changes.
