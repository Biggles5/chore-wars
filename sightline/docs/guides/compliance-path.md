# Compliance Path

What it takes to sell SightLine legally in the US, in the order to do it. Every cost and duration below is an estimate and marked (est.).

## 1. FCC Part 15: intentional radiator

The node radiates (Wi-Fi), so it is an intentional radiator under Part 15.

- Module-based approach (recommended): build on a pre-certified Wi-Fi module and inherit its grant. That saves a full certification cycle; what remains is unintentional-radiator testing of the whole product plus label and integration requirements per the module grant.
- Full certification (if we ever ship custom RF): ~$8k to $15k and 6 to 10 weeks (est.) at a test lab.
- Either way: FCC ID labeling, Part 15 statement in the docs, and no antenna changes outside the module grant.

## 2. ETL or UL listing: the Class 2 lighting system

- Reference standard: UL 2108 (low-voltage lighting systems) for the rail, supply pairing, and nodes-on-track; the supply itself must already be a listed Class 2 unit.
- Cost ~$15k to $30k, 8 to 16 weeks (est.), plus ongoing factory follow-up inspections.
- ETL and UL marks are equivalent for AHJ acceptance; pick on lab availability and price.
- Why it matters: dealers pulling permits and any AHJ conversation start with "is it listed". Class 2 throughout keeps the install out of licensed-electrician territory in most jurisdictions, which protects the sub-3-hour install.

## 3. NDAA Section 889: silicon selection

Section 889 bars federal agencies (and pulls many municipalities and school districts along) from buying covered surveillance equipment.

- Rule: no Hikvision, Dahua, or Huawei silicon lineage anywhere in the video path. That includes rebadged sensors and SoCs; lineage, not logo, is what counts.
- Action: pick the SoC and image sensor with a documented supply chain, keep a signed supplier attestation and provenance file for every silicon component in the DHR.
- Payoff: keeps federal-adjacent and many municipal customers open, and it is a sales line consumer competitors cannot always match. Costs nothing extra if done at part selection; very expensive to retrofit later.

## 4. IP66: lab verification

- The internal spray protocol in `test-plans.md` is engineering verification. Marketing an IP66 rating credibly means an accredited lab run per IEC 60529 (dust chamber for the 6, 12.5 L/min jets for the second 6).
- Bundle it with the ETL/UL campaign at the same lab to share fixtures and time.

## Timeline and cost summary (all est.)

Sequence assumes module-based FCC and one lab for safety plus ingress. Some stages overlap; the wall-clock total below reflects that.

| Stage | Cost (est.) | Duration (est.) | Depends on |
|---|---|---|---|
| Pre-certified Wi-Fi module selection + 889 silicon documentation | internal time | 2 weeks | final BOM |
| FCC unintentional radiator testing + labeling (module path) | $3k to $6k | 3 to 5 weeks | DVT hardware |
| ETL/UL listing to UL 2108 reference | $15k to $30k | 8 to 16 weeks | DVT hardware |
| IP66 lab verification per IEC 60529 | $3k to $6k | 2 to 4 weeks | same lab, overlaps ETL |
| Contingency (retests, sample rebuilds) | $5k | absorbed | |
| Total | ~$26k to $47k | ~4 to 6 months wall clock | |

If the module path fails (custom antenna, grant conditions unmet), add $8k to $15k and 6 to 10 weeks (est.) for full FCC certification and re-plan around it.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
