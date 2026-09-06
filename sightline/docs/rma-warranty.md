# RMA and Warranty Flow

Return, repair, and replacement policy for SightLine nodes and gateways, plus the serial scheme that makes it traceable.

## Serial number scheme

Format: SL-YYWW-FFFF-XXXXX

- SL: product prefix.
- YYWW: year and week of manufacture (e.g. 2634 = 2026, week 34).
- FFFF: factory code assigned per ODM line.
- XXXXX: monotonic sequence within that factory-week.

Placement, all three mandatory:
1. Laser-etched on the housing (visible without removing the node from the track).
2. Written to NVS at end-of-line test (readable over MQTT and by support tooling).
3. Printed with barcode on the carton.

The serial is bound to a site ID at provisioning. Support, warranty entitlement, OTA ring assignment, and epidemic-failure tracking all key off it. A serial whose etch, NVS, and carton records disagree fails outbound QA.

## Warranty terms

- Node: 3 years from provisioning date (activation, not purchase, subject to a 6 month shelf cap after ship).
- Gateway: 2 years (est.).
- Shield plan: extended coverage for the life of the active subscription, including advance replacement (below).
- Not covered: physical damage from impact or fire, unauthorized firmware, removal of the node from its provisioned rail system by a non-certified installer, damage from out-of-spec power injection.

## Support and RMA flow

### 1. Triage (telemetry first)
Most "dead node" tickets are rail power or Wi-Fi, not dead nodes. Before any RMA:
- Pull last known telemetry: power.rail_v, wifi_rssi_dbm, uptime, heartbeat history.
- rail_v low or absent at last report: dispatch as install issue (tap, injection point, run length), route to installing dealer.
- rssi weak with intermittent heartbeat: Wi-Fi issue, route to network fix.
- Healthy power and Wi-Fi with a hard stop in telemetry: candidate hardware failure, proceed.

### 2. Remote diagnostics
- Command a remote reboot and self-test over the MQTT ota/diag path.
- Check fw_version against known-bad releases before blaming hardware.
- Capture the diagnostic bundle to attach to the RMA record.

### 3. Replacement dispatch
- Shield: advance replacement. Replacement node ships immediately, provisioned to the site's serial record; defective unit returns in the same box, prepaid label. Site downtime target under 3 business days (est.).
- Plus and Core: cross-ship on card hold, or customer-return-first at customer choice.
- Replacement inherits the site binding; the failed serial moves to RMA state and is blocked from re-provisioning until analysis clears it.

### 4. Return analysis
- Every returned unit gets failure analysis: visual, power-on, NVS log pull, component-level where warranted.
- Findings tagged by failure mode against factory code and date code (the FFFF and YYWW fields exist for this).
- Analysis output feeds the production BOM cost-down notes: recurring failure modes justify component substitutions, added protection, or conformal coating changes, and quantify what each is worth per unit.

## ODM contract clauses

- DOA definition: unit fails end-to-end provisioning at a customer site, or fails within 30 days, with no install fault found in telemetry.
- DOA above 0.5% of a batch (est.): triggers 100% outbound screen of subsequent batches at ODM cost until two consecutive clean batches.
- DOA or field failure above 2% of a batch (est.): epidemic clause. ODM funds replacement units, freight both ways, and root-cause corrective action report within 15 business days. SightLine may hold acceptance of in-transit batches.
- All thresholds computed per batch keyed on YYWW + FFFF, which is why the serial scheme is contractual, not cosmetic.
- ODM must retain golden samples and EOL test logs per batch for 3 years.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
