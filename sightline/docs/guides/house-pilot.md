# House Pilot: Two Nodes on a Real Gemstone Track

Goal: two printed camera nodes running on a live Gemstone roofline for 30 nights, with real measurements. Prerequisite: `bench-build.md` exit checklist passed.

## What you are installing

- Two `track_node_housing_gemstone` nodes (printed, from Phase 0) clipped to the track with `retrofit_clip_gemstone` clips (`hardware/cad/exports/`).
- Power tapped from the Gemstone controller, a GEM40012-4 class unit: 12V, Class 2, 400W kit as 4 terminals at 5A/60W each, 75 linear ft or 100 lights per terminal, 0.96W max bulbs.
- Everything stays NEC Class 2. You never touch mains. If your controller wiring looks unusual, stop and get an electrician.

## Power-tap procedure (per node, on a GEM40012-4 terminal)

Wiring reference: `hardware/electronics/wiring/retrofit-tap-12v.svg`.

1. Kill 12V at the controller first. Unplug the controller's supply or switch its breaker. Never tap live.
2. Verify with the meter. 0V DC across the terminal you are tapping. Trust the meter, not the switch.
3. Pick the terminal. One camera node per 5A/60W terminal, no exceptions. The node is budgeted at a 12W ceiling, so run the numbers: LED load on that terminal plus 12W must stay under 60W. Use the worksheet in `retrofit-install-12v.md` if the terminal is heavily loaded.
4. Tap POWER ONLY. Splice the node's 18 AWG power pair onto the terminal's 12V and GND with WAGO 221s. Do not touch the LED data conductor at the controller.
5. Data pass-through, buffered, inline. At the node's position on the track, the WS2811-family data line enters the node's buffer and exits re-driven. The node never loads the daisy chain and never originates LED data outside a deter command. Downstream pixels must behave identically before and after.
6. Check the run length. Node drop 75 ft or less on 18 AWG at 12V. Longer: use the injection kit (`hardware/electronics/wiring/injection-kit.svg`).
7. Gland torque. M12 glands on the housing: hand-tight plus a quarter turn with the wrench, cable should not rotate when twisted by hand. Do not crush the jacket.
8. Drip loop. Every cable dips below its gland entry before rising into the housing. Water follows the wire; make it fall off before the entry.
9. Restore 12V. Meter the node's buck output (5.0V), confirm the LED string runs normally end to end, confirm node telemetry appears at the gateway.

Repeat for node two on a different terminal.

## Aiming the identity channel (DORI)

DORI thresholds: 250 px/m Identify, 125 Recognize, 62.5 Observe, 25 Detect (the 2025 revision adds Validate at 500). Two constraints set your aim window at a 20 ft (6.1 m) eave:

- Too close: camera pitch exceeds the 30 degree face-recognition limit until 7.6 m (25 ft) of ground distance.
- Too far: the 60 degree 12MP identity channel holds identify density (250 px/m) out to 16 m (52 ft).

So at 20 ft eaves the window is 25 to 52 ft from the wall. At 10 ft eaves anything beyond 2.4 m (8 ft) is fine.

1. Run the tool for your eave height:

   ```
   python3 hardware/dori_placement.py --eave-ft 20 --sensor 12mp --hfov 60
   ```

2. Chalk the driveway. Mark the near line (25 ft) and far line (52 ft) from the wall below the node. The band between them is where identification happens.
3. Aim the cant at the chokepoint. Find where anyone approaching must pass (driveway throat, gate, front walk) and put it centered in the chalk band. Set the housing cant so the chokepoint sits mid-frame.
4. Verify with a test frame at night. IR on, stand a helper at the chokepoint, pull a frame, measure face pixel height. At 250 px/m a face spans roughly 40 to 50 px vertically. If short, re-aim or accept Recognize instead of Identify and write it down.

## 30-night measurement protocol

Fixed conditions: same reference walk path (through the chalk band, past the chokepoint), same tester, same clothing every night. Walk it once per night after dark.

- Pixel density: pull the night's best frame of the reference walk, measure px/m at the chokepoint.
- False positives: count deter or person events that night with no person present (animals, headlights, weather).
- Deter latency, stopwatch method: phone slow-mo (240 fps if available) framing both the tester and the roofline. Count frames from first foot inside the trigger line to first deter strobe. Frames / fps = latency. Target under 1 s local.
- Weather: one line, since rain, fog, and snow drive both IR performance and false positives.

### Nightly log template

Copy this table into `docs/guides/pilot-log.md` and add one row per night.

| Night | Date | px/m at chokepoint | Ref walk detected? | Deter latency (s) | False positives | Weather | Notes |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| ... | | | | | | | |
| 30 | | | | | | | |

### Pilot pass criteria

- Reference walk detected 30/30 nights.
- Median px/m at the chokepoint >= 250.
- Deter latency p95 < 1 s.
- False positives trending down after the first week of tuning (target under 1 per night by night 30 (est.)).

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
