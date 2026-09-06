# AVS-01 reference summary

The TMA AVS-01 alarm validation scoring standard: ANSI-accredited 2023, IACP-ratified October 2024. It exists because 94 to 98% of alarm dispatches are false and verified-response jurisdictions (Seattle model: 96% of 13K calls ignored in 2023) now act only on scored, verified events. SightLine implements it in the correlator so every Event Story is dispatch-grade by construction (`gateway/correlator/avs.py`).

## The scale, as implemented

| Level | Standard meaning | SightLine trigger |
|---|---|---|
| 0 | No call for service | Nothing, animals only, or expected activity during a disarmed scene |
| 1 | Call for service, no additional information | Possible human, below the verification bar (no identify-grade frame, no multi-camera confirmation) |
| 2 | Confirmed human presence | Verified person on the property (identify-grade capture or 2+ node confirmation) |
| 3 | Threat to property | Verified human plus threat indicators: deter fired, package interaction, extended dwell in protected zones, associated vehicle |
| 4 | Threat to life | Indicators the simulator never produces (forced entry while occupied, weapon). Reserved; escalation policy hands off immediately |

Confidence accompanies every score (verification quality, node corroboration), plus a human-readable rationale a central-station operator can read to a dispatcher verbatim.

## Operational consequences

- Guardian's escalation policy keys on the score: 0 dismiss, 1 watch, 2 notify, 3 intervene or hand off, 4 hand off (`agents/guardian/guardian.py`).
- The central-station payload (`sightline.dispatch.v1`) leads with the score; the mock receiver, like a real one, refuses anything under 2.
- Marketing never outruns the standard: "verified" in SightLine copy means AVS-2 or better, nothing softer.

## Certification path

TMA membership, then AVS-01 conformance assessment for the scoring implementation alongside the receiving station's own accreditation. Budget: membership and assessment in the low five figures (est.), timeline one to two quarters (est.), coordinated with the wholesale-station partner who already operates under it.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
