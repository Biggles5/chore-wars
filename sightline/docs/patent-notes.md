# Provisional Patent Support Notes

Input for patent counsel. Not legal advice, not claims. Plain-language descriptions of what we believe is novel, for counsel to convert into a provisional filing. Incumbent baseline throughout: lights-only permanent roofline tracks (Trimlight-class) and standalone security cameras (Ring/floodlight-class). Nobody ships both in one rail.

## Claim area 1: Dual-sensor camera node integrated in a powered permanent lighting rail

Summary: A camera node that mounts inside a decorative/permanent roofline LED track and draws power from the rail itself, containing two imaging channels in one track module: a wide overview sensor for detection and tracking, and a narrow identity channel aimed to capture identify-grade frames.

Believed novel: Lights-only tracks carry no sensing at all. Standalone cameras are separate fixtures with their own mounts, power, and visual footprint. The combination (camera hidden in the light rail form factor, powered by the rail, with a two-channel wide-plus-identity optical design in a single track module) is not found in either incumbent line.

Figures: hardware/cad/exports/track_node_housing_gemstone.step (housing and dual-aperture geometry), hardware/electronics/wiring/rail48-bus.svg (rail power and data bus the node sits on).

## Claim area 2: Scan-derived identity-channel aiming

Summary: The identity channel's cant (its fixed aiming angle within the housing) is computed per-home from a 3D scan of the property before manufacture or at kitting, so that when the installer places the node at its planned rail position, the identify ring and pitch window land on a chosen chokepoint (gate, walkway, driveway throat) with no field aiming.

Believed novel: Standalone cameras are aimed by hand at install and drift. Lights-only tracks have nothing to aim. Factory-setting a per-site optical cant from a home scan, turning aiming into a manufacturing parameter instead of an install skill, appears to be new in residential security.

Figures: hardware/cad/exports/track_node_housing_gemstone.step (cant seat in housing), docs/architecture/system.md sequence diagram (scan-to-provisioning flow).

## Claim area 3: Detection-coupled zone-follow deterrence

Summary: The detection zone map is bound to LED segment ranges on the same rail, so when an entity is tracked moving along the perimeter, the strobe/deter lighting follows it segment by segment. The house itself visibly tracks the intruder.

Believed novel: Floodlight cams switch one lamp on at one spot. Lights-only tracks play preset patterns with no sensing input. Closing the loop (detection position mapped continuously to addressable segment ranges so deterrence follows the target along the roofline) exists in neither incumbent category.

Figures: hardware/electronics/wiring/rail48-bus.svg (segment addressing on the bus), docs/architecture/system.md sequence diagram (detect-to-deter event path).

## Claim area 4: Cross-node re-identification on a residential perimeter

Summary: Multiple nodes on one home hand off and re-identify the same entity as it moves between fields of view, and the gateway correlator stitches those observations into one verified Event Story (sightline.story.v1) with verification requiring identify-grade capture or multi-node confirmation.

Believed novel: Re-identification exists in commercial multi-camera VMS deployments, so counsel should frame narrowly: the residential-perimeter application on rail-mounted co-calibrated nodes (known fixed geometry from the rail and the home scan), producing a consumer-grade verified/unverified distinction that gates monitoring hand-off, is the asserted contribution. Standalone consumer cameras alert per-camera and do no entity stitching.

Figures: docs/architecture/system.md sequence diagram (correlator assembling a story from multiple node events).

## Claim area 5: Universal 9 to 56 V power-only tap with buffered data pass-through

Summary: A retrofit tap that lets a SightLine node draw power from an existing third-party LED rail across a 9 to 56 V input range, while buffering and passing through the rail's own data signal untouched, so the incumbent lighting controller keeps working and the node is electrically invisible to it.

Believed novel: Existing retrofit approaches replace the controller or the string. A power-only tap that is protocol-agnostic on the data line (buffered pass-through, no interpretation, no injection) across the full common LED voltage range enables install onto competitors' installed base. Compare and distinguish the Celebright in-string conversion patent (2026), which converts the string rather than passively tapping it.

Figures: hardware/electronics/wiring/retrofit-tap-12v.svg (tap circuit), hardware/electronics/wiring/injection-kit.svg (power injection variant).

## Prior-art search pointers for counsel

- Ring, Arlo, Eufy floodlight and spotlight cameras: light plus camera in one fixture, single lamp, no rail, no zone-follow. Establishes the standalone baseline to distinguish.
- Trimlight (and Jellyfish, Gemstone, EverLights) patents and filings on permanent roofline track, channel extrusions, and controllers: the lights-only baseline. Check for any sensing claims hiding in their portfolios.
- Celebright in-string conversion patent (2026): closest known art for claim area 5; distinguish tap vs conversion.
- WLED and open addressable-LED ecosystems: public prior art on segment addressing and effects; relevant to claim area 3, where the novelty is the detection coupling, not segment control itself.
- Commercial VMS re-identification literature and patents (claim area 4): survey to find the narrowest defensible framing.
- General search: CPC classes around G08B 13 (intrusion detection), H05B 47 (light source control responsive to conditions), F21S 4 (light strings/tracks).

## Claims-drafting cautions

1. Do not claim "camera plus light" broadly; floodlight cams anthologize that. Tie claims to the rail/track integration and rail power.
2. Do not claim re-identification per se; claim the perimeter-rail configuration and the verified-story gating.
3. Avoid claiming LED segment control alone; WLED-class prior art is thick. The detection-to-segment mapping is the inventive link.
4. Keep the 9 to 56 V range in a dependent claim; a range alone is easy to design around, the buffered pass-through behavior is the core.
5. File before any public demo, dealer pitch, or crowdfunding page goes live; provisional first, disclosures after.
6. Capture the scan-to-cant toolchain (claim area 2) as method claims as well as apparatus claims.
7. Record inventor contributions now (Ryan Brown, plus anyone else who touched the concepts) to keep inventorship clean.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
