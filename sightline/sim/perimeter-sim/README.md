# perimeter-sim

A simulated house with virtual camera nodes that publish events exactly like real firmware: same MQTT topics, same schema-validated payloads, same DORI math (imported from `hardware/dori_placement.py`, not reimplemented).

## Run

```bash
python3 -m perimeter_sim list                       # scenarios
python3 -m perimeter_sim run quiet-night            # headless, writes runs/<id>/events.jsonl
python3 -m perimeter_sim serve --scenario car-prowler-0214   # live view at :8090
python3 -m perimeter_sim serve --scenario quiet-night --loop # restart forever (demo kiosk)
```

If an MQTT broker is reachable (localhost:1883, override with `SIGHTLINE_MQTT_HOST` / `SIGHTLINE_MQTT_PORT`, `make gateway` starts one), every message also goes to the broker. Without one, the in-process bus and the JSONL log carry the identical payloads, so the demo needs no Docker.

## Scenarios

- `quiet-night`: 8 hours, a passing car, a cat, a deer. Zero deter events. The baseline.
- `car-prowler-0214`: the flagship. Car stops at 2:10, prowler works the driveway, the identity channel captures at identify grade through the aimed chokepoint, deter fires at 2:14:01, prowler flees, car leaves.
- `porch-pirate`, `party-arrivals`, `deer-3am`, `mail-daily`.

## House scans

`scans/demo-house.json` is the default: a 16 x 13 m footprint, 6.1 m eaves (the hard case from the optics audit), three track nodes plus an eye-level door node, five roofline LED segments, named yard zones. The scan format is the same shape the real scan-to-quote flow produces, so a dealer scan drops straight in.

## What is honest and what is mocked

- DORI rings, pitch limits, identify windows: real math, shared with placement tooling.
- Detection: geometric (in FOV, above detect density). No ML in the sim.
- Confidence values and color histograms: deterministic synthetics. Histograms are stable per actor across nodes, which is exactly what the correlator's re-ID stub keys on.
- Thumbnails: procedural SVG stamped SIMULATED. `media.synthetic` is always true; nothing from the sim can enter an evidence path.
- Deter decision: lives here for Sprint 1, moves to the correlator in Sprint 2 (DECISIONS.md D-013). The bus topics are already final.
