# SightLine Bench Practical

The certification exam. Same day as the course. Bench kit build per docs/guides/bench-build.md.

## The task
1. Install the bench kit: rail segments, one injection point, two nodes, gasketed joint, controller wiring. Time limit: 90 minutes from kit-open to last photo submitted.
2. Submit the 5 QC gate photos through installer mode, in order: rail_level_spacing, gasket_seated, connector_clicked, node_aim, controller_wiring.
3. Grading is by the QC agent, same thresholds as the field:
   - rail_level_spacing: tilt <= 1.5 deg, spacing variance <= 8%
   - gasket_seated: gap <= 0.5mm
   - connector_clicked: latch engaged, exposed conductor <= 1mm
   - node_aim: azimuth error <= 5 deg, cant error <= 2 deg
   - controller_wiring: meter <= 0.5V before work (photo of meter in frame), strain relief present
4. Mock commissioning run: walk the 30-point check (power 6, mechanical 6, optics 6, privacy 4, network+system 5, handoff 3) on the bench rig, including the privacy items (masks set on-device, audio confirmed off, owner PIN scripted) and the handoff script delivered to the proctor.

## Pass criteria
- All 5 gates pass first-try, or
- 4 gates pass first-try and the 5th passes on second-try (physical fix plus reshoot), and
- Build completed inside 90 minutes, and
- Mock commissioning run completed with zero skipped items.

## Grading rubric
| Component | Weight | Pass bar |
|---|---|---|
| 5 QC gates | Gate-by-gate | 5 first-try, or 4 + 1 second-try |
| Time | Hard limit | <= 90 min to last photo |
| Meter discipline | Hard requirement | Meter check performed and photographed before touching the terminal; skipping it is an automatic fail regardless of gates |
| Commissioning walk | Checklist | All 30 items addressed, privacy items verbatim |
| Handoff script | Proctor judgment | Masks, audio-off, owner PIN, plan explanation all present |

## On fail
- Failed gate(s): same-day retry of the failed gates only, after a physical fix. One retry round.
- Second fail (any gate failing twice, or more than one gate needing second-try beyond the allowance): full retake of the bench practical on another day. Course does not need to be repeated.
- Meter-discipline fail: full retake, no same-day retry. This is the one safety-culture line.
- Two full-practical fails: repeat the half-day course before a third attempt.

## What the QC agent is actually looking for
Photos graded to field standard: reference tag in frame, sharp focus, the measured feature clearly visible. A good build with a bad photo fails the gate. Redo etiquette applies: fix, then reshoot. Reshooting to hide a flaw is a certification-ethics violation and ends the session.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
