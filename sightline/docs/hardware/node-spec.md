# Dual-sensor track node specification

The product in one module: a camera the street cannot see, with optics engineered so the native frame is evidence-grade.

## Sensors and optics

| Channel | Sensor | Lens | Job |
|---|---|---|---|
| Wide | 8MP (3840 px horizontal) | ~110 deg HFOV | overview, motion, tracking, zones |
| Identity | 12MP (4608 px horizontal) | ~60 deg HFOV, factory cant set from the scan | identify-grade capture at the chokepoint |
| IR | 850 nm array | matched to identity ring | night density (validated per test-plans.md) |

Why dual-sensor (the audited math, pinned in `hardware/dori_placement.py` tests): at a 6.1 m (20 ft) eave a 105 deg 8MP lens only reaches identify density inside 5.9 m, where downward pitch is 37 to 42 degrees and face recognition has already failed. The 60 deg identity channel reaches identify density at 13.3 m (8MP) / 16 m (12MP) where pitch is about 19 degrees. The wide channel watches everything; the identity channel is aimed math. The eye-level door node covers the one place eave optics never win.

## Factory cant from the scan

The scan-to-quote flow yields each node's mounting position and chokepoint. The identity channel's cant is set at the factory (or by the installer with the DORI tool) so the identify ring and the sub-30-degree pitch window land on that chokepoint. Aim window at 6.1 m eaves: 7.6 to 16 m ground distance.

## Compute and storage

- Edge-AI SoC, NDAA-eligible lineage. Candidates (est., tradeoffs): SigmaStar SSC377DE class (cheap, proven ISP, modest NPU), Ingenic T41 (strong NPU per dollar, smaller ecosystem), Ambarella CV25 class (best ISP + NPU, 2 to 3x the cost, reserve for a Pro SKU). Decision at EVT on night-ISP quality per dollar.
- On-node: person/vehicle/animal/package detection, track state machine, deter reflex. No cloud inference in the detection path, ever.
- microSD high-endurance, 72 h loop at full rate, per-node encryption.

## Electrical

- Input 9 to 56V (wide-input buck, >90% efficiency target, surge + reverse-polarity protected). One SKU taps every incumbent rail.
- Draw: ~7.5W continuous (est.), 12W ceiling budgeted (IR + heater duty + bursts). Power rules: docs/architecture/power.md.

## Mechanical and environmental

- Module <= 52 mm, sized to live inside the Gemstone 30 mm-lens channel line; universal clip adapts Trimlight and JellyFish profiles (parametric CAD: `hardware/cad/`).
- IP66. Operating -30 C to +55 C; heater engages below -10 C.
- Mechanical capture carries all load; VHB is a seal only, never structure.

## Door node

Eye-level jamb housing (110 x 16 x 24 mm), single sensor, same SoC family, same schemas. It exists because identification at the door is a solved geometry problem and the eave never beats it.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
