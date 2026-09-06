# Matter bridge design (roadmap doc)

Make the lights first-class citizens of every ecosystem; bring the cameras along where the ecosystem deserves them.

## Lights as Matter devices

The gateway runs a Matter bridge exposing each roofline segment as a Matter Extended Color Light. Scenes (welcome, holiday, all-clear) map to Matter scenes. Deter stays OUT of Matter's reach: no third-party ecosystem can trigger or suppress a deter, and a Matter "turn everything off" during an active deter is deferred until the hold ends (safety and liability: the strobe is a security actuator, not a light).

- Implementation: `python-matter-server` or the connectedhomeip SDK bridge example on the gateway (est. 6 to 10 eng-weeks to demo grade).
- Certification: CSA membership ($7k/yr Adopter (est.)) + certification per product (test lab, $10k to $25k (est.), 6 to 10 weeks).

## Camera integrations (roadmap, effort-estimated)

| Target | Path | Effort (est.) | Notes |
|---|---|---|---|
| Home Assistant | ships now (native package + MQTT + RTSP) | done | reference integration |
| ONVIF/NVR | Profile S pass-through from gateway | 2 to 3 wks | metadata (Profile M) later |
| Alexa | Ring-free skill: doorbell + camera feed via gateway cloud | 6 to 8 wks | requires Plus/Shield relay |
| Google Home | camera + events via Smart Device Management API | 6 to 8 wks | SDM approval cycle adds calendar time |
| HomeKit Secure Video | HAP + HSV over the gateway (video never to our cloud, which fits HSV's model perfectly) | 4 to 6 months | MFi program; the privacy story aligns, the effort is real |
| Matter cameras | spec still maturing; watch 1.4+ | n/a | revisit when camera clusters stabilize |

## Sequencing call

Lights bridge first (it sells: whole-house lighting in Apple/Google/Alexa with zero extra hardware), HA-native cameras as the power-user path, HSV when headcount allows. Nothing here blocks the core product; all of it compounds it.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
