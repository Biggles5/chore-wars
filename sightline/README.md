# SightLine

Perimeter Intelligence. Security cameras and sensor nodes embedded invisibly inside permanent roofline lighting tracks, with reactive whole-house light deterrence, an AI event narrator, and an agentic operations layer.

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

Then open http://localhost:8090 for the top-down sim view.

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

## Ground rules baked into the code

- Cameras are continuous loads. They never borrow the lights' duty-cycle oversubscription. 12V retrofit: one camera node per 5A terminal at a 12W ceiling.
- Native pixels only in the evidence path. AI narrates, never fabricates imagery (State v. Puloka, 2024).
- Core plan: nothing leaves the house. Enforced at the data layer, not marketing copy.
- NEC Class 2 everywhere. No electrician.
