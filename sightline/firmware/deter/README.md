# SightLine deter pack

Reactive whole-house light deterrence on the existing LED track. The camera path never touches the LED data line (power-only tap, buffered pass-through); deterrence talks to whatever controls the lights, WLED first.

## Contents

- `wled/presets.json`: preset pack. 1 = zone-follow red/white strobe, 2 = quiet-hours amber sweep (less startle, still unmistakably reactive), 3 = welcome scene, 4 = all-clear return.
- `wled_push.py`: pushes the presets to a WLED device over its JSON API.
- HA automation lives in `gateway/homeassistant/config/packages/sightline_deter.yaml`: maps the triggering camera zone to LED segment ids, picks strobe vs quiet-hours by clock, holds for a configurable number of seconds, then returns to all-clear.

## Zone-follow model

The correlator (or the node's local reflex) publishes on `sightline/<site>/deter/cmd` with the zone. HA turns on ONLY the segments that face that zone. The rest of the house stays dark: the light itself points at where the person is, which reads as "it sees you" rather than "a floodlight tripped."

## Latency budget

Deter trigger must be under 1 s local. The edge reflex path (node decides, node fires its own segment via the bus) is the guarantee; the HA path is the whole-house follow. Measured numbers land in docs/guides/test-plans.md protocols.

## Push presets

```bash
python3 wled_push.py 192.168.1.50        # your WLED IP
```
