# Fleet Telemetry Dashboard Spec

Fleet health dashboard for SightLine operations, and the seed of the dealer portal. Data source: the sightline.telemetry.v1 topic (published by every node every 30 s), aggregated at the gateway, and synced upstream for Plus and Shield sites. Core (local-only) sites appear only if the owner opts in to anonymous health sync.

## Panels

### 1. Fleet map
- One marker per site.
- Green: healthy. All nodes reporting, no active alerts.
- Amber: degraded. At least one active alert, or one node missing but the site still covering.
- Red: offline more than 10 min. No gateway heartbeat, or all nodes silent.
- Click-through to the site's node grid.

### 2. Per-site node grid
- One row per node: power.rail_v, power.draw_w, temp_c, wifi_rssi_dbm, storage.loop_hours, used_pct, heater_on, uptime, fw_version.
- fw_version drift highlighting: any node not on the site's modal firmware version is flagged, any node below the fleet target version is flagged harder. Drift longer than 7 days opens an ops ticket.
- Sparkline per cell showing 24 h trend.

### 3. Alert rules

Each alert: threshold, evaluation window, action.

| Alert | Threshold | Window | Action |
|---|---|---|---|
| Rail undervoltage | power.rail_v below 9.5 V | 3 consecutive samples (90 s) | Amber site. Ticket: check tap, injection point, run length. Undervoltage is the top cause of "dead node" reports. |
| Sustained overdraw | power.draw_w above 10 W | 10 min sustained | Amber. Flag possible heater fault or short. If paired with temp rise, escalate to red and suggest remote power cycle. |
| Overtemperature | temp_c above 70 C | 2 consecutive samples | Red for that node. Throttle deter strobes on the node, ticket for enclosure or sun-load inspection. |
| Weak Wi-Fi | wifi_rssi_dbm below -75 | 15 min average | Amber. Ticket: relocate gateway or add repeater. Correlate with dropout history before dispatch. |
| Low loop retention | storage.loop_hours below 48 h | Any sample | Amber. Storage failing or misconfigured recording profile. Verify used_pct, schedule card health check. |
| Heartbeat gap | No telemetry for more than 2 min (4 missed publishes) | Immediate | Node marked silent. If all site nodes silent plus gateway silent more than 10 min, site goes red and owner is notified per plan. |

Alert lifecycle: raised, acknowledged, resolved, all timestamped. Auto-resolve when the metric clears the threshold for 2x its window.

### 4. Fleet rollups
- Firmware version distribution (pie + adoption curve per release, feeds OTA ring advancement decisions).
- Mean and p95 power.draw_w per hardware rev.
- Failure trends: alerts per 100 nodes per week, grouped by alert type and hardware rev. Feeds RMA return analysis and BOM cost-down notes.
- Heater duty cycle vs outside temperature by region (validates cold-climate design margin).

### 5. Dealer views
- Dealers see only sites they installed, scoped by installer ID bound at provisioning.
- Dealer panel set: their fleet map, per-site node grid, open alerts, firmware drift on their installs.
- No cross-dealer visibility, no video, no event content. Telemetry health only.
- Dealer alert routing: rail, Wi-Fi, and loop alerts go to the dealer first (they are install-quality issues); temperature and heartbeat alerts go to SightLine ops in parallel.

## Non-goals
- No event or video data on this dashboard. Health telemetry only. Event Stories live in the monitoring pipeline.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
