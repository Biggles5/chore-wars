# Retrofit Install: Existing Roofline Lighting (12V and JellyFish)

SightLine nodes retrofit onto permanent roofline LED tracks that are already on the house. The universal rules, then per-brand notes, then the budgeting worksheet and injection decision tree.

## Universal rules (every brand)

- NEC Class 2 only. Never mains. Kill low-voltage power at the controller before touching anything, verify 0V with a meter.
- One camera node per 5A/60W terminal. Node budgeted at a 12W ceiling.
- Tap POWER ONLY. The node buffers the LED data line inline and never loads the WS2811-family daisy chain.
- Runs 75 ft or less on 18 AWG at 12V. Longer: injection kit (`hardware/electronics/wiring/injection-kit.svg`).
- The node's 9-56V wide-input buck accepts any of these systems' rails.
- Wiring diagram: `hardware/electronics/wiring/retrofit-tap-12v.svg`. Clips: `hardware/cad/exports/retrofit_clip_<brand>.stl`.

## Gemstone (12V)

- Controller: GEM40012-4 class. Class 2 400W kit = 4 terminals x 5A/60W. Limits per terminal: 75 linear ft or 100 lights. Bulbs 0.96W max, 30mm, IP67.
- Tap at the terminal block, power pair only, one node per terminal. Full step-by-step including gland torque and drip loops is in `house-pilot.md`.
- Clip: `retrofit_clip_gemstone.stl`.

## Trimlight (12V)

- 12V system, UCS1903 data protocol. UCS1903 is WS2811-family: same power rules, and the node's data buffer handles it, pass-through untouched except the inline buffer.
- The controller carries FCC ID 2ATV8TRIMLIGHT and is made by Shenzhen Sperll. Connector pigtails vary by production run, so match connector pigtails on site: bring the pigtail assortment, cut in WAGO 221s only where the run is concealed, and keep the factory connector on anything visible or serviceable.
- Clip: `retrofit_clip_trimlight.stl`.

## JellyFish (48V)

- 48V rail with a proprietary 4-wire redundant data scheme.
- Power: fine. The node's 9-56V buck takes the 48V rail directly. Same tap-power-only discipline, same 12W node ceiling (at 48V that is only 0.25A).
- Data: hands off. The 4-wire redundant data line must pass through untouched. Never tap, cut, or buffer the data pair. The node does not sit inline on JellyFish data; it clips beside the track and takes power only. Deter lighting effects on JellyFish route through the integration layer, not the wire.
- Clip: `retrofit_clip_jellyfish.stl`.

## Terminal budgeting worksheet

One row per controller terminal. LED watts = linear ft x 0.8 W/ft, based on 0.96W max bulbs at 9 in spacing (est.). Node adds 12W (its budget ceiling). Verify against `python3 hardware/electronics/power_budget.py`.

| Terminal | LED linear ft | LED watts (ft x 0.8) | Node on this terminal? (+12W) | Total W | Under 60W? |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

Worked example: 60 ft of LEDs = 48W. Add a node: 60W. That is at the limit, not under it. Move the node to a lighter terminal or split the LED run.

## Injection decision tree

Work through this per node drop, top to bottom. First rule that fires wins.

1. Is the node's power run over 75 ft on 18 AWG at 12V? Yes: injection kit. No: continue.
2. Does the terminal total (worksheet above) stay under 60W with the node's 12W included? No: move the node to another terminal. If no terminal has room: injection kit with its own Class 2 supply.
3. Measured voltage at the node under load below 9V (long thin legacy wiring)? Yes: injection kit, even under 75 ft. No: continue.
4. Is this a JellyFish 48V rail? Voltage drop is rarely the issue at 48V; injection is only for terminal wattage, not distance, in almost all cases.
5. None fired: direct tap, no injection.

Injection kit wiring: `hardware/electronics/wiring/injection-kit.svg`. The kit adds a fused Class 2 feed near the node; it joins power only and grounds common with the LED system.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
