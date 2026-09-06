# SightLine Compliance Checklists

Working checklists for hardware certification and supply-chain compliance. Owner column assigns a named human or agent; Status is one of: Not started, In progress, Blocked, Done.

## 1. FCC Part 15 (Module Strategy)

Strategy: use pre-certified radio modules (Wi-Fi/BLE, sub-GHz) with their own FCC IDs to limit our scope to unintentional-radiator testing on the host device.

| # | Step | Owner | Status |
|---|------|-------|--------|
| 1 | Select radio modules with valid modular grants (single-modular, not limited-modular where avoidable) | HW lead | Not started |
| 2 | Pull each module's FCC grant and confirm host integration conditions (antenna type, gain limits, co-location) | HW lead | Not started |
| 3 | Verify our antenna choices match the grant's approved antenna list or fall under same-type lower-gain rule | HW lead | Not started |
| 4 | Confirm no simultaneous-transmission scenario voids modular grants; if co-located, plan co-location assessment | RF consultant | Not started |
| 5 | Run pre-scan for unintentional radiated emissions on node, door node, and gateway (Class B limits) | Test lab | Not started |
| 6 | Fix any margin failures (shielding, filtering, layout spins) before formal test | HW lead | Not started |
| 7 | Formal Part 15B test at accredited lab; obtain test report for each SKU | Test lab | Not started |
| 8 | File Supplier's Declaration of Conformity (SDoC), designate US responsible party | Compliance owner | Not started |
| 9 | Label each product: FCC statement, "Contains FCC ID: XXXX" per module | Compliance owner | Not started |
| 10 | Add Part 15 compliance statement to user documentation and packaging | Docs agent | Not started |
| 11 | Archive grants, reports, and SDoC in the compliance vault with revision control | Compliance owner | Not started |

## 2. ETL Class 2 System Listing (UL 2108 Reference)

Target: ETL listing for the low-voltage lighting-and-camera track system evaluated against UL 2108 (low voltage lighting systems), powered by NEC Class 2 supplies.

| # | Step | Owner | Status |
|---|------|-------|--------|
| 1 | Confirm every power supply SKU is a listed NEC Class 2 source (100 VA max, energy limited) | HW lead | Not started |
| 2 | Map system architecture for the lab: supply, 48V rail, track, nodes, door node, gateway | HW lead | Not started |
| 3 | Engage Intertek for a preliminary design review against UL 2108 | Compliance owner | Not started |
| 4 | Verify wire gauges, connectors, and track conductors meet ampacity and temperature ratings at max load | HW lead | Not started |
| 5 | Run abnormal tests: short circuit, overload, single-fault conditions on rail and nodes | Test lab | Not started |
| 6 | Verify enclosure flammability ratings (V-0 or per-standard) for node and gateway housings | HW lead | Not started |
| 7 | Confirm wet-location suitability for roofline components (ties to IP66 checklist below) | HW lead | Not started |
| 8 | Submit samples and construction data package; complete witness testing | Compliance owner | Not started |
| 9 | Resolve any variation notices; respin hardware if required | HW lead | Not started |
| 10 | Obtain ETL listing, apply ETL mark, and register in Intertek directory | Compliance owner | Not started |
| 11 | Set up follow-up service (factory inspections) with the CM | Ops | Not started |
| 12 | Publish installer-facing doc: Class 2 wiring rules, no electrician required, what voids the listing | Docs agent | Not started |

## 3. NDAA Section 889 Silicon Compliance

Goal: document full SoC and sensor lineage so no covered-entity silicon (Huawei, ZTE, Hikvision, Dahua, Hytera, and affiliates) is anywhere in the BOM. This unlocks government-adjacent buyers, insurers, and dealers who serve federal employees.

| # | Step | Owner | Status |
|---|------|-------|--------|
| 1 | Enumerate every camera SoC, ISP, image sensor, radio, and MCU in both SKUs | HW lead | Not started |
| 2 | Trace each part's manufacturer of record and fab lineage; document corporate ownership | Supply chain | Not started |
| 3 | Screen the full BOM against the FCC Covered List and Section 889 entity list, including subsidiaries | Compliance owner | Not started |
| 4 | Obtain written non-covered-entity attestations from each silicon vendor | Supply chain | Not started |
| 5 | Verify image sensors (8MP wide, 12MP identity, door node) are from non-covered vendors with signed lineage docs | HW lead | Not started |
| 6 | Audit CM and sub-assembly suppliers for substitution risk; lock approved-vendor list, no unapproved swaps | Supply chain | Not started |
| 7 | Add contractual clause: any BOM substitution requires re-screening before production | Legal | Not started |
| 8 | Screen firmware and SDK provenance (no covered-entity SDKs or binary blobs) | FW lead | Not started |
| 9 | Produce a signed Section 889 compliance letter for dealers and channel partners | Compliance owner | Not started |
| 10 | Re-screen the BOM at every hardware revision and annually at minimum | Compliance owner | Not started |

## 4. IP66 Verification

Roofline nodes and track-mounted hardware must survive dust-tight and powerful-water-jet conditions for the life of the install.

| # | Step | Owner | Status |
|---|------|-------|--------|
| 1 | Define which assemblies claim IP66: roofline node, door node, track couplers; gateway is indoor, excluded | HW lead | Not started |
| 2 | Design review of all seals, gaskets, cable glands, and lens interfaces against IP66 requirements | HW lead | Not started |
| 3 | Verify lens and LED window materials for UV stability (roofline sun exposure, 10-year target) | HW lead | Not started |
| 4 | Prototype dust chamber test (IP6X: talcum, 8 hours, vacuum) on 5 units per assembly | Test lab | Not started |
| 5 | Prototype water jet test (IPX6: 12.5 mm nozzle, 100 L/min, 3 min, all angles) on 5 units per assembly | Test lab | Not started |
| 6 | Thermal cycling pre-conditioning (-30 C to +60 C) before repeat ingress test to catch seal fatigue | Test lab | Not started |
| 7 | Post-test teardown: inspect for moisture, dust, corrosion at connectors and sensor cavities | HW lead | Not started |
| 8 | Fix failures, respin gaskets or housings, re-run full sequence | HW lead | Not started |
| 9 | Third-party IP66 certification test at accredited lab; obtain report | Test lab | Not started |
| 10 | Add production line water-ingress sampling plan (AQL-based) with the CM | Ops | Not started |
| 11 | Document field service rule: any opened node gets a new gasket kit, never reseated | Docs agent | Not started |

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
