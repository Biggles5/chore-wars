# Phase 0 Bench Build

Goal: a working SightLine loop on your bench. One camera node, one gateway, one string of pixels, one app. When the exit checklist at the bottom passes, Phase 0 is done.

Time: one weekend if parts are in hand. Budget: ~$754 (est.), band $650 to $900 (est.).

## Safety, read first

- Everything on this bench is NEC Class 2 low voltage (12V). Never wire anything in this guide to mains. The only mains connection is the wall plug on the listed Class 2 supply, and you never open that supply.
- Fuse the bench 12V rail at 5A, inline, right at the supply output. A 12V short can still melt insulation and start a fire without a fuse.
- Unplug the supply before touching any splice. Verify 0V with the meter before you trust it.

## Step 1: Order the BOM

The full list is in `hardware/bom/bench_bom.csv`. Order it as-is. Key items and why:

| Part | Role |
|---|---|
| ESP32-S3 camera dev board (OV5640), x2 | The node firmware target, plus a spare |
| 8MP PoE reference camera | Wide-channel reference for Frigate and DORI validation |
| N100 mini PC (8GB/256GB) | Gateway: MQTT broker, Frigate, correlator, Home Assistant |
| Coral USB TPU | Edge inference for Frigate |
| 9-56V to 5V/3A buck, x3 | The universal tap regulator |
| WLED controller (ESP32) | Deter light target |
| WS2811 12V pixel strings, x2 | Bench stand-in for the roofline |
| WAGO 221 assortment | Every splice in these guides |
| 12V 5A Class 2 supply, x2 | Bench rail plus injection stand-in |
| microSD 128GB high endurance, x2 | 72 h loop testing |

Total on the sheet: $754.06 (est.). Every price in the CSV is an estimate.

## Step 2: Print the fixture and housings

Print in PETG, 0.2 mm layers, 4 perimeters, 40% infill. Files are in `hardware/cad/exports/`:

1. `bench_fixture.stl`: the baseboard that holds supply, bucks, WAGOs, and controller in one plane.
2. `track_node_housing_gemstone.stl`: the camera node housing you will reuse in the house pilot.
3. `door_node_housing.stl`: optional for Phase 0, print it if you have filament left.

Install M3 heat-set inserts in the housing bosses with a soldering iron at about 220 C. STEP files sit next to each STL if you need to modify anything.

## Step 3: Wire the 12V bench rail

Layout mirrors the retrofit tap diagram at `hardware/electronics/wiring/retrofit-tap-12v.svg`. Photos come later, so each step describes what the photo will show.

1. Mount the Class 2 supply on the fixture. Land its 12V output on the inline 5A fuse holder, then into the first WAGO. Photo: supply at far left, fuse holder immediately to its right, one red and one black 18 AWG lead leaving it.
2. Build the rail from WAGO 221-413s. One for 12V, one for GND. Photo: three WAGO 221-413s in a row, red 12V jumpers entering from the left, black returns below them.
3. Feed the buck. 18 AWG from the rail into the 9-56V buck input. The buck's 5V output feeds the ESP32-S3 camera board. Photo: buck centered, thin red/black 5V pair leaving the right side into the node housing.
4. Feed the WLED controller and the WS2811 string from the rail. Data line from the WLED controller to the string's data-in. Photo: green data wire running alone from controller to first pixel, power pair arriving separately from the rail.
5. Tap rule rehearsal, because it matters later: the node taps POWER ONLY. The WS2811 data line passes the node position untouched; the node buffers LED data inline but never loads the daisy chain. Photo: data wire passing the node housing with a small buffer board inline, no tee into the node's power harness.
6. Power on. Meter check: 12.0V at the rail, 5.0V at the buck output. Node draw stays under the 12W ceiling (check with the USB power meter on the 5V side; 12W at 12V is 1A at the rail).

Rules baked into this rail, same as production: one camera node per 5A/60W terminal, 12W ceiling per node, runs 75 ft or less on 18 AWG at 12V (longer runs use the injection kit, see `hardware/electronics/wiring/injection-kit.svg`).

## Step 4: Flash the ESP32-S3 node

1. `make setup` from the repo root (installs Python deps and PlatformIO).
2. Plug the ESP32-S3 board into the gateway PC over USB.
3. From `firmware/node/`: `pio run -t upload`
4. Open the serial monitor. You should see the node join Wi-Fi, then publish telemetry on `sightline/<site>/<node>/telemetry` every heartbeat.

`pio run` alone builds without flashing and is what CI runs.

## Step 5: Stand up the gateway

On the N100 mini PC (any recent Ubuntu or Debian):

1. Clone the repo, run `make setup`.
2. `make demo` boots the correlator on :8091, the simulator on :8090, and the app on :5173. Open the app, confirm simulated events flow. This proves the software path before hardware enters the picture.
3. For the real stack, from `gateway/`: `docker compose up -d`. That brings up Mosquitto, Frigate (with the Coral TPU passed through over USB), the correlator, and Home Assistant.
4. `make test` should pass all 48 tests on this machine.

Wire schemas and MQTT topics are documented in `gateway/schemas/README.md`.

## Step 6: Point the reference camera at a walk path

1. Mount the 8MP PoE camera on the fixture or a tripod, aimed at 3 to 5 m of clear floor you can walk repeatedly.
2. Add it to Frigate via its RTSP URL.
3. Mount the 850nm IR illuminator next to it for night runs.
4. Walk the path. A person detection should appear in Frigate, then land in the SightLine app as an event.

## Exit criteria: the Phase 0 demo checklist

Run this end to end with the room lights on, then again in the dark.

- [ ] Walk the path: a detection event lands in the app with a native-pixel frame attached.
- [ ] Deter preset fires the WS2811 string in under 1 s, measured locally (phone slow-mo of you crossing the line vs the strobe; the trigger is an edge reflex, no cloud round trip).
- [ ] Telemetry heartbeats from the ESP32-S3 node visible in the app or via `mosquitto_sub` on the telemetry topic.
- [ ] 72 h loop: node has run 3 days on the high-endurance microSD, loop writes verified (oldest segments aged out, newest readable).
- [ ] `make test`: 48/48 passing on the gateway.

All five green: Phase 0 complete. Next: `house-pilot.md`.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
