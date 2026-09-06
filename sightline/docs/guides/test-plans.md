# Test Plans

Hardware and system verification protocols with explicit pass criteria. Software regression is separate: `make test` (48 tests) must be green before any protocol below counts.

## 1. Thermal soak and cold operation

Equipment: environmental chamber, node with telemetry logging, high-speed logging of SoC temperature.

| Test | Procedure | Pass criteria |
|---|---|---|
| Hot soak | 55 C chamber, 24 h, node running full pipeline (detect + stream + deter armed) | SoC stays under its throttle temperature the entire 24 h; zero resets; no frame-rate degradation |
| Heater function | Chamber to -30 C, node powered | Heater engages, lens and sensor area held above dew/frost point, node keeps detecting |
| Cold start | Soak node unpowered below -10 C, then apply power | Node boots (heater pre-warm allowed), reaches full operation; record time-to-operational |

Log telemetry throughout; the telemetry schema carries SoC temperature.

## 2. Ingress: IP66 spray per IEC 60529

- 12.5 L/min nozzle (12.5 mm), 3 min minimum, all angles, at spec distance per IEC 60529 second characteristic numeral 6.
- Pass: no water ingress on teardown, desiccant indicators unchanged, node fully functional after test.
- Run on a production-intent housing with glands torqued to the spec in the install guides, not finger-tight lab builds. Formal lab verification is covered in `compliance-path.md`.

## 3. Night DORI verification

- Place a resolution chart at the identify ring distance for the mounting height under test (from `python3 hardware/dori_placement.py`; at 20 ft eaves the identify window is 25 to 52 ft, so test at the far edge, 52 ft).
- Conditions: full dark, 850nm IR illumination only.
- Measure pixels per meter on the chart from captured native frames.
- Pass: >= 250 px/m (DORI Identify) at the identify ring distance, at 850nm. Record the margin, not just pass/fail.

## 4. Re-ID accuracy and bias

Panel: 20 subjects, each recorded day and night, crossing at least two camera nodes per session.

- Cross-camera match rate: fraction of crossings where the system links the same person across nodes.
- Pass: match rate >= 85% (est.) overall, day and night measured separately.

### Bias testing (mandatory, blocking)

- Recruit a balanced subject panel across skin tones (Monk or Fitzpatrick scale, documented).
- Measure match rate per skin-tone group, day and night.
- Report the deltas between best and worst performing group in every accuracy report; never publish an overall number without the parity table.
- Fail: parity gap > 5 percentage points. A failing gap blocks release regardless of the overall match rate.

Native pixels only throughout; no synthetic augmentation in the evaluation set. AI never fabricates imagery (State v. Puloka, 2024).

## 5. Deter latency

- Method: high-speed phone video (240 fps slow-mo) framing both the walk-in point and the deterrence strobe.
- Tester crosses the trigger line 20 times; for each, count frames from first foot across the line to first strobe frame. Frames / fps = latency.
- Pass: p95 < 1 s, measured entirely locally (network cable to the WAN pulled during the test to prove the reflex is edge-local).
- Repeat with `make sim SCENARIO=<name>` scenarios feeding the correlator to confirm software-path latency separately from optical-path latency.

## Reporting

One markdown report per protocol run: date, hardware revision, firmware version, raw numbers, pass/fail per criterion, and deviations. File them under `docs/hardware/` next to the design notes.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
