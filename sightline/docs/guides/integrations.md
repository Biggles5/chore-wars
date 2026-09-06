# Integrations: Today and Roadmap

## Works today

### Home Assistant (first class)

The gateway ships with Home Assistant included; the SightLine package is preinstalled. Everything SightLine knows shows up as HA entities: per-node presence, events, deter controls, arm mode, telemetry (including supply headroom).

MQTT topics and payload schemas are documented in `gateway/schemas/README.md`. Short version:

```
sightline/<site_id>/<node_id>/event        node -> gateway
sightline/<site_id>/<node_id>/telemetry    node -> gateway
sightline/<site_id>/deter/cmd              gateway -> nodes
sightline/<site_id>/gateway/story          correlator -> app
```

Anything that speaks MQTT can subscribe. On the Core plan all of this stays inside the house, which is the point.

### ONVIF / RTSP pass-through

Each camera node exposes standard streams so an existing NVR (Blue Iris, Synology, a rack NVR) can record SightLine cameras like any other camera. SightLine detection and deter keep running independently; the NVR just gets pixels. Native pixels only, same as the evidence path.

### Alexa and Google routines (via HA)

Through Home Assistant's Alexa and Google Assistant bridges: arm modes as scenes, deter and light controls as devices, announcements on events. This is routine-level integration, not camera feeds in the Alexa/Google apps (that is roadmap, below).

## Roadmap (all effort and cost figures est.)

| Item | What it gives | Effort (est.) | Cert cost (est.) | Notes |
|---|---|---|---|---|
| Matter bridge for lights | Roofline lighting controllable from any Matter app (Apple Home, Google Home, Alexa) | 2 to 3 eng-months | $3k to $8k fees | Lights only; Matter has no camera cluster worth targeting yet |
| HomeKit Secure Video | Camera feeds and clips in Apple Home with iCloud storage | 4 to 6 eng-months | MFi program fees | MFi plus HSV requirements; only ever over the gateway, nodes never talk to Apple directly |
| Google camera integration | Feeds in Google Home | 2 to 3 eng-months | Partner program, low fees | Partner program approval required |
| Amazon camera integration | Feeds in Alexa app / Echo Show | 2 to 3 eng-months | Partner program, low fees | Works with Alexa camera certification |

### Certification steps and costs (all est.)

| Step | Applies to | Cost (est.) | Time (est.) |
|---|---|---|---|
| CSA Alliance membership | Matter | $7k/yr | immediate |
| Matter certification (test house + fees) | Matter | $3k to $8k | 4 to 8 weeks |
| Apple MFi enrollment | HSV | modest annual fee | 2 to 4 weeks |
| HSV implementation + Apple review | HSV | eng time dominates | inside the 4 to 6 eng-months |
| Google / Amazon partner onboarding | camera integrations | low fees | 4 to 8 weeks each |

Sequencing: Matter lights first (cheapest, broadest reach), HSV second (highest homeowner pull, biggest lift). Cloud-side camera integrations only after Plus/Shield cloud infrastructure carries them; Core users lose nothing either way.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
