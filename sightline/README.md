# SightLine

An agentic security intelligence company. The brain (working name: Guardian) scores, verifies, deters, narrates, and hands off; invisible roofline hardware inside permanent lighting tracks is its delivery vehicle; a certified-contractor Ops Engine is how it scales. Every event is AVS-01 scored and video-verified before anyone is bothered with it, monitoring runs at single-digit dollars of marginal cost, and installs take a certified two-person crew under three hours.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved. Not for publication.

## What this is

A complete, runnable, demo-ready foundation:

- **Simulator** (`sim/perimeter-sim/`): a virtual house with virtual camera nodes that publish events exactly like real firmware. Scripted scenarios (car prowler at 2:14 AM, porch pirate, quiet night). Top-down live web view.
- **Gateway** (`gateway/`): MQTT broker, Frigate, Home Assistant, and the SightLine correlator (event ingest, cross-camera re-ID, Event Stories).
- **App prototype** (`app/mobile/`): React, mobile-first, wired to the correlator.
- **Hardware** (`hardware/`): dual-sensor node design, DORI placement math, CAD, BOMs.
- **Firmware** (`firmware/`): ESP32-S3 node skeleton plus the WLED deter preset pack.
- **Agents** (`agents/`): narrator, quote, support, dealer GTM. All run in deterministic mock mode with zero external services.

Everything runs end to end on a laptop with no physical hardware.

## Run the demo in 3 commands

```bash
cd sightline
make setup        # installs python deps (fastapi, uvicorn, paho-mqtt, jsonschema, pytest)
make demo         # boots the simulator on the quiet-night scenario, opens the live view
```

Then open http://localhost:8090 for the top-down sim view. `make demo` also prints the scenario's AVS-01 verdict, Guardian's simulated cost per home per month (target under $6), and the ops-sim week-12 install rate under the old model vs the Ops Engine.

Other scenarios:

```bash
make sim SCENARIO=car-prowler-0214
make sim SCENARIO=porch-pirate
make sim SCENARIO=party-arrivals
```

Headless run (writes validated event JSONL to `sim/perimeter-sim/runs/`):

```bash
make sim-headless SCENARIO=quiet-night
```

Full live demo (three terminals, no Docker needed):

```bash
make correlator                        # gateway brain on :8091
make sim SCENARIO=car-prowler-0214     # sim + live view on :8090
make app                               # app prototype on :5173
```

Open http://localhost:5173: watch the 2:14 AM story assemble, deter fire, and the narrator write it up, live.

Full gateway stack (broker + Frigate + correlator + Home Assistant, requires Docker):

```bash
make gateway
```

Tests:

```bash
make test
```

## Repo map

See `ROADMAP.md` for phase gates, `DECISIONS.md` for every assumption made and why, and `CHANGELOG.md` for history. Directory layout matches the master build spec: `docs/`, `hardware/`, `firmware/`, `gateway/`, `sim/`, `app/`, `agents/`, `cloud/`, `website/`, `tests/`.

## The three disruptions (and where each lives)

1. **Acquisition**: no door-knocking, no contracts. Dealer, inbound, and insurer channels model to $285 blended CAC against the incumbents' $1,800 to $2,150 (`econ/unit_economics.py`, thresholds enforced in `tests/test_econ_thresholds.py`).
2. **Monitoring**: Guardian scores every story on AVS-01, dismisses the noise, intervenes with the lights, and hands verified events to a wholesale central station. Marginal cost $4.17/home/month modeled fully loaded (`agents/guardian/`, cost meter in the app's Guardian tab).
3. **Install throughput**: the scan measures, the factory cuts, the connector wires, the runbook knows, the QC agent supervises. Certified crews run 3 installs/day; a metro's capacity is a recruitment funnel (`ops/`, `sim/ops-sim/`, dealer dashboard in `website/dashboard/`).

Strategy docs: `docs/strategy/`. Partner-facing kit: `partnerships/kit/`. The licensing pivot (kill trigger: a platform bundles agentic monitoring under $20 before 50K subs) is `SIGHTLINE_WHITE_LABEL=1`: a config change, not a rewrite.

## Ground rules baked into the code

- Cameras are continuous loads. They never borrow the lights' duty-cycle oversubscription. 12V retrofit: one camera node per 5A terminal at a 12W ceiling.
- Native pixels only in the evidence path. AI narrates, never fabricates imagery (State v. Puloka, 2024).
- Core plan: nothing leaves the house. Enforced at the data layer, not marketing copy.
- NEC Class 2 everywhere. No electrician.
