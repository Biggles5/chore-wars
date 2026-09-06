# Hardware

- `dori_placement.py`: the optics truth. DORI rings, pitch windows, placement verdicts. Tests pin it to the audited anchors.
- `electronics/power_budget.py`: the power truth. Drop tables, terminal checks, injection rules, 48V headroom.
- `electronics/wiring/`: retrofit tap, 48V bus, injection kit (SVG).
- `cad/sightline_cad.py`: parametric CadQuery for the track node housing (Gemstone 30mm channel), universal retrofit clips (Gemstone/Trimlight/JellyFish), door node, bench fixture. Real exports committed in `cad/exports/` (STL to print, STEP for ODMs). Rebuild: `pip install cadquery && python3 cad/sightline_cad.py`.
- `bom/bench_bom.csv`: the ~$754 (est.) Phase 0 order list. `bom/production_bom.csv`: the $33 to $47 at 25K path with cost-down notes.

Specs live in `docs/hardware/` (node-spec, dori-placement, thermal). Install procedures live in `docs/guides/`.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
