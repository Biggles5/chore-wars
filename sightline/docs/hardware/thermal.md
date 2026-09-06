# Thermal design notes

The aluminum lighting channel is the heatsink. That is the quiet advantage of living in the track.

## Budget

- Dissipation: ~7.5 W continuous (est.), 12 W ceiling. The node body couples to the channel through the mechanical capture surfaces with a thermal pad; the channel's extrusion area dwarfs what a standalone camera housing gets.
- Hot bound: +55 C ambient in direct sun-soaked track. SoC throttle margin verified by the 24 h soak (docs/guides/test-plans.md). IR duty is the biggest swing load at night; capture bursts are seconds.
- Cold bound: -30 C. Heater film engages below -10 C ambient (sensor fog and microSD write floor are the constraints before the silicon is). Heater duty is inside the 12 W ceiling by budget, which is why the ceiling is 12 W and not 9.

## Rules

1. Thermal pad between housing spine and channel is mandatory on install (the guides call it out); VHB never sits in the thermal path.
2. The temperate SKU drops the heater film (saves cost, see production BOM); climate is chosen at quote time from the install ZIP.
3. Telemetry reports `temp_c` and `heater_on` every 30 s; the fleet dashboard alarms at 70 C sustained (docs/telemetry-dashboard-spec.md).

## Open items for EVT

Measure channel-coupled vs free-air delta on the bench rig (bench-build.md has the fixture); validate the pad choice at the 55 C soak; characterize IR-on night steady state. Replace every number above with the measured ones.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
