# Network architecture

Wi-Fi 6 primary, wired bus pair as the control fallback, and offline behavior that never leaves the house blind.

## Primary: Wi-Fi 6

Nodes join the home 2.4/5 GHz network (Wi-Fi 6 radios: OFDMA keeps a 4-node fleet polite on congested spectrum). Streams are gateway-only: RTSP never crosses the router to the internet. Provisioning: first boot raises a node AP (`SightLine-<serial>`), the installer app pushes credentials, node joins and drops the AP.

## Fallback: the bus data pair

Both rails carry a data pair (the retrofit tap buffers the LED pair through; the 48V rail has its own). When Wi-Fi is down, the pair carries a low-rate control channel (deter commands, heartbeats, event headers at reduced rate). Video does not fit; it stays on the loop until Wi-Fi returns. The reflex path (detect -> local deter) never needed the network at all.

## Mesh AP node (concept, not committed)

A node SKU variant that doubles as a Wi-Fi 6 mesh AP: the roofline is the best AP real estate on the house, and the power problem is already solved. This turns "the cameras need Wi-Fi" into "the cameras improve the Wi-Fi." Requires a second radio and hits thermal margins at the SoC-per-node budget, so it stays a documented concept until the temperate-SKU thermals are measured.

## Offline behavior

| Condition | Behavior |
|---|---|
| Wi-Fi down | loop keeps recording; deter reflex intact; control over bus pair; events queue (bounded ring, oldest dropped) and redeliver on reconnect |
| Gateway down | loop + reflex intact; nodes hold events; app shows last-known state with an honest OFFLINE banner |
| Internet down | everything works except cloud sync and remote app access; LAN app access unaffected |
| Power cut | lights and nodes share the fate of the rail; on restore, nodes boot in < 20 s (est.) and re-arm the previous scene |

## Addressing and discovery

Gateway advertises via mDNS (`sightline-gateway.local`). Nodes find the broker from provisioning config, fall back to mDNS. The app talks to the gateway on the LAN by default; remote access (Plus/Shield) rides the cloud relay with end-to-end TLS.
