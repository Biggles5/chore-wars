# SPRINT-REPORT: Sprint 3

Date: 2026-09-06. Gate: full demo script clean, tests green. **Gate met: `make demo` boots correlator + sim + app in one command, 48 tests green.**

## What works

- `make demo`: one command, three services, port-guarded, clean teardown on Ctrl-C. The 2:14 AM scenario produces a narrated verified event in the app about 35 to 40 s after boot (under the 60 s definition-of-done budget).
- All four app screens live: Home, Verified Event, Ask (cited answers with tappable story chips), Scenes (active scene, tap-to-paint deter zones, natural-language scene designer, enforced privacy mask list), Setup (scan inputs to kit, price, per-terminal power check, DORI coverage rings). Browser-verified with Playwright.
- Quote agent: 160 ft Gemstone home lands $1,701 installed (in the SKU 1 band), 110 ft home $1,343; long runs and heavy LED terminals correctly flag injection kits; 48V rail quotes 2.9 hr install with 47.8% supply headroom. All numbers marked estimates, all math from the shared modules.
- Power module: 12W at 12V over 75 ft of 18 AWG computes 0.96V drop (the audited rule holds); the 9 to 56V buck window guards absurd runs; one-node-per-terminal enforced.
- WLED deter pack + HA automation: zone to segment mapping, strobe vs quiet-hours by clock, hold-then-all-clear, welcome scene on disarmed arrivals.
- Firmware skeleton: schema-exact payloads, watchdog, OTA hook, provisioning AP, motion state machine, camera gated for CI.

## What's mocked or deferred

- Firmware compile is CI-verified by the shipped workflow template, not verified in this container: the build environment's proxy blocks the PlatformIO registry (D-019). `pio run` with pinned espressif32@6.7.0 is the command; the workflow runs it on every firmware change once activated.
- Ask and scene-designer are deterministic keyword engines in mock mode; Claude modes exist as gateway env switches and were not exercised in CI (no key).
- Zone painting is tap-to-toggle on named zones, not freehand polygons (called in Sprint 2 risks; scope held).
- HA automation is authored and packaged but not executed against a live HA in this environment (no Docker daemon).

## Exact commands

```bash
cd sightline && make setup
make demo                     # everything: correlator + sim (2:14 AM loop) + app
make test                     # 48 tests
make sim SCENARIO=quiet-night # any scenario into the same stack
```

## Top 3 risks going into Sprint 4

1. **The Sprint 4 gate is a stranger test.** Clone, run, print, order. Every doc has to carry its own context; the repo currently assumes the reader watched it get built. The guides need to be written against the artifacts, not from memory.
2. **CAD without a physical Gemstone channel in hand.** The 30mm channel interface dimensions come from published specs (est.); the parametric models must expose every mating dimension as a named parameter so the first test print calibrates fast.
3. **BOM realism.** Bench BOM prices drift; production BOM at $33 to $47 needs honest cost-down notes, not hand-waving, or the pitch assets inherit fiction.

---

# SPRINT-REPORT: Sprint 2

Date: 2026-09-06. Gate: car-prowler-0214 renders a full story in the app with deter firing in the sim view. **Gate met, verified in a real browser.**

(Sprint 1 report is preserved below.)

## What works

- Full pipeline, three processes, zero Docker: sim (:8090) feeds the correlator (:8091) which feeds the app (:5173) over websocket. `make correlator`, `make sim SCENARIO=car-prowler-0214`, `make app`.
- The correlator stitches node-local tracks into site-level entities (histogram re-ID: car and prowler stay separate, three party guests stay three people), assembles Event Stories with timeline beats, severity, verified flag, and deter outcome (fled/stayed from post-deter behavior), and runs the narrator on story close.
- The app renders it live: Home (narrator one-liner, house map with deter segments flashing, live tiles, story list) and Verified Event (deter banner "They left immediately", narrative, re-ID chips "person, 3 cameras, identify", timeline with thumbnails, police export preview). Verified with Playwright against the running stack: every gate element present, screenshots on file.
- Deter Now button hits the gateway. Send to Monitoring enforces the evidence rule: it refuses simulated frames with the reason.
- Narrator mock is deterministic and guardrailed: cites frame timestamps, invents nothing, flags simulated frames as not-evidence. Claude mode ships behind SIGHTLINE_NARRATOR_MODE=claude with automatic fallback. 5 eval fixtures.
- 29 tests green in about 2 s.

## What's mocked

- Re-ID is color-histogram cosine (threshold 0.95) over deterministic sim histograms. Real embeddings drop in behind `HistReID`'s two-method interface. Day/night robustness is untested by construction.
- Narrator claude mode is written but not exercised in CI (no API key in the build environment). The mock output passes the same eval assertions.
- Ask, Scenes, Onboarding/Scan-to-Quote screens are Sprint 3 stubs behind the tab bar.
- Deter reflex still originates at the edge (sim), by design now (DECISIONS.md D-015); the correlator records it and can command deter itself from the app.
- Share clip is a demo stub. Frigate and HA remain idle against the sim.

## Exact commands

```bash
cd sightline && make setup
# terminal 1
make correlator
# terminal 2
make sim SCENARIO=car-prowler-0214
# terminal 3
make app
# open http://localhost:5173 (app) and http://localhost:8090 (sim view)
make test
```

## Top 3 risks going into Sprint 3

1. **The quote agent's power math has to be exactly right.** Per-terminal budgeting (5A/60W Gemstone rules, 12W camera ceiling, 75 ft runs, injection decision) is dealer-facing; an error strands an install. The pricing engine must share one power module with docs/architecture/power.md, same discipline as the DORI module.
2. **Scenes needs a real zone-painting model.** Freehand zone painting on the house map, mapped to camera FOVs and LED segment ranges, is the hardest UI in the app. Cutting scope to polygon-tap-and-name for Sprint 3 keeps the demo honest.
3. **Firmware skeleton must actually compile in CI.** PlatformIO pulls toolchains at build time; the offline story needs a pinned platform version and a documented `pio run` path, or the "compiles without hardware" claim is hollow.

---

# SPRINT-REPORT: Sprint 1

Date: 2026-09-06. Gate: `make demo` runs quiet-night end to end. **Gate met.**

## What works

- `make demo` boots the simulator on quiet-night and serves the live top-down view at http://localhost:8090: house, FOV wedges, identity-channel identify rings, actors moving, deter segments flashing, event feed with thumbnails, sim clock, armed state, bus status.
- `make sim SCENARIO=car-prowler-0214`: car stops at 2:10, prowler works the driveway, the identity channel captures him at identify grade (467 px/m, 27 deg pitch) through the factory-aimed chokepoint, deter fires at 02:14:01 on seg-front and seg-east, prowler flees, car leaves.
- `make sim-headless SCENARIO=<name>`: full night simulates in under half a second, writes schema-validated JSONL. Six scenarios.
- Every published message validates against the v1 schemas at publish time. Quiet-night publishes about 3,900 messages (46 events plus telemetry), zero deter. Animals never deter. Disarmed modes never deter.
- DORI math is one module shared by placement tooling and the sim, pinned by tests to the audited anchors: 105 deg 8MP identify 5.9 m (fails at a 20 ft eave, pitch 37+), 60 deg 8MP 13.3 m at 19 deg pitch, 12MP 16 m, 30 deg pitch boundary 7.6 m, 10 ft eave benign beyond 2.4 m.
- Correlator boots standalone or in Docker, subscribes to the site topic tree, validates, buffers, serves `/health`, `/events`, `/telemetry`, REST `/ingest` (rejects bad payloads with the exact schema error).

## What was mocked (Sprint 1 state)

- Detection geometric, no ML. Confidence and histograms deterministic synthetics.
- Deter decision inside the sim (now D-015: edge reflex by design).
- Thumbnails procedural SVG stamped SIMULATED; `media.synthetic: true` enforced by tests.
- Frigate and Home Assistant configured but idle; compose validated, full stack not booted in this build environment (no Docker daemon), correlator exercised directly.

## Top 3 risks called at Sprint 1 (status after Sprint 2)

1. Story assembly quality: addressed, tests cover multi-entity stitching; day/night re-ID robustness still open.
2. Deter latency budget: reframed as edge reflex + gateway judgment (D-015); real-bus latency measurement still owed in Sprint 3 with the HA/WLED path.
3. App contract drift: prevented; story.v1 schema landed before any UI.
