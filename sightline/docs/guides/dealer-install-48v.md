# Dealer Install Guide: 48V Rail (SKU 2)

Target: a complete single-story install in under 3 hours. The flow is scan, kit, rail, click, provision. The 48V system is a factory-cut rail with blind-mate keyed sockets and a 384W Class 2 supply, so on-site work is mounting and clicking, not wiring.

All times below are targets for a trained two-person crew on a typical single story. Example budget sums to 175 min, inside the 180 min promise.

## Flow with time targets

### 1. Scan: 15 min

- Walk the roofline with the app's scan flow: footage, corners, eave heights, obstructions.
- Confirm the pre-cut rail plan against reality. Any mismatch over a few inches, flag it now, not at step 3.
- Photograph the panel area and the planned supply location.

### 2. Quote accept: 5 min

- Review the generated plan and price with the homeowner in the app.
- Homeowner accepts on their own phone. No signature, no paper.

### 3. Rail cut and mount: 70 min

- Rail segments arrive factory-cut and labeled per the scan. On-site cuts should be trim cuts only.
- Mount clips per the plan spacing, hang rail segments, join with the keyed couplers. Keying makes reversed joins impossible; if a coupler will not seat, it is backwards or wrong segment, never force it.
- Dress the rail line level along the fascia. This is the longest step and the one homeowners see forever.

### 4. Node click-in: 15 min

- Camera nodes and the door node blind-mate into their keyed sockets. Push until the latch clicks, tug-test each.
- Sockets are position-keyed: a track node cannot seat in the door position.
- Nodes power from the rail through their 9-56V wide-input buck; there is nothing to wire at the node.

### 5. Supply and home run: 25 min

- Mount the 384W Class 2 supply at the planned location, run the home run to the rail feed point.
- Class 2 only. If the site wants the supply hardwired rather than plugged into an existing exterior outlet, that outlet work is an electrician's job, not yours.
- Power up. At a reference load of 3 track nodes, the door node, and 160 ft of LEDs, expect about 48% supply headroom on the telemetry page.

### 6. Provision and aim: 30 min

- Gateway online, nodes adopt automatically, firmware syncs.
- Run the aim check per node with the DORI tool (`python3 hardware/dori_placement.py --eave-ft <ft> --sensor 12mp --hfov 60`) and set each cant so the identify band covers the approach chokepoint. At 20 ft eaves that band is 25 to 52 ft from the wall.
- Set privacy masks with the homeowner standing next to you. Mandatory, see the QC list.

### 7. QC walk: 15 min

Total example: 15 + 5 + 70 + 15 + 25 + 30 + 15 = 175 min.

## QC checklist (do not leave without all boxes)

- [ ] Every rail clip and coupler torqued to spec, every node latched and tug-tested.
- [ ] Drip loops at the supply home run and any surface-mounted cable entry.
- [ ] Headroom reading from telemetry recorded on the work order (expect ~48% at the reference load; investigate anything under 20%).
- [ ] Deter test fire: walk-in at the chokepoint triggers the light response in under 1 s, verified by eye and logged by the gateway.
- [ ] Privacy masks set with the homeowner present: every camera view walked together, neighbor windows and yards masked. Masks are enforced on device.
- [ ] App handoff: homeowner logged in as owner, household members invited, arm modes explained, plan chosen (Core is $0 forever and fully local).
- [ ] Site photos of finished rail, supply, and panel area attached to the work order.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
