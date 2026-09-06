# Investor Memo: The Honest Venture Case

## Market

~$16B US residential security. ~30M monitored households. Incumbent economics: ADT acquires at ~$1,800 net SAC with 2.3 year payback and 13.1% gross attrition (Q2 2026 filings) while carrying ~$7.4B net debt; Vivint's creation cost was ~$2,150 with ~$300M/yr of door-to-door commissions (2019 Form 425). Retail monitoring sells for $30 to $80/mo against $2 to $6/mo wholesale cost (est. range; COPS SecureNet anchor $5.99/account/mo). SimpliSafe Active Guard at $49.99 to $79.99/mo and Deep Sentinel at $60 to $100/mo/camera (~$38M raised) prove premium demand for proactive monitoring and set the price umbrella we ship under at $19.99.

## The wedge

170K+ homes already have powered permanent roofline lighting (Trimlight 120K+, JellyFish 50K+, plus Gemstone, Oelo, EverLights). Every one has a 9 to 56V rail our retrofit tap node powers from, an owner who spent thousands on their roofline, and a dealer relationship that reaches them without a door knock. No security incumbent can see this base; their salesforce comp and their debt structure point them elsewhere. This is the beachhead: invisible cameras in lighting the customer already loves.

## Unit economics (modeled in econ/)

- Blended CAC: $285 (dealer attach $250 x 60%, inbound $450 x 25%, insurer-subsidized $150 x 15%).
- Marginal monitoring cost: $4.17/home/mo fully loaded (Guardian compute $0.42, support $0.75, storage; Shield adds the $5.99 wholesale station). Demo-measured compute alone: $0.09/home/mo at simulated volumes.
- Blended gross margin: 67.1%.
- Hardware sold at ~$400 margin per install, so net CAC after hardware margin is negative and subscription payback is immediate.
- LTV:CAC: 4.4x dealer-led, 6.5x insurer-led. Portfolio value modeled at 35x monthly RMR (market comps: RMR portfolios trade ~26x to 50x, Barnes).
- Plans: Core $0 forever (fully local, no cloud path exists), Plus $9.99, Shield $19.99 with central-station handoff. No contracts, ever.

## Why now

1. **AVS-01:** TMA's alarm scoring standard, ANSI-accredited 2023, IACP-ratified Oct 2024, gives machine-verified alarms an official grammar. Guardian scores AVS-01 level 3 on the flagship demo scenario today.
2. **Verified response:** Seattle ignored 96% of 13K false alarms in 2023; 94 to 98% of dispatches are false industry-wide. Unverified alarms are losing police response; verified events are becoming the only product that works.
3. **Agent cost curves:** around-the-clock agentic monitoring at $0.42/home/mo modeled compute vs $30 to $80/mo retail human monitoring.
4. **The lighting boom:** the 170K+ retrofit base exists now, Trimlight's network is PE-backed as of 2025 and hungry for RMR, and the trade labor to install new rail already works the roofline every December.

## Why us

- **Agentic-ops DNA.** The company itself runs on the agents in this repo: Guardian (monitoring), quote, QC, support, and dealer-GTM agents. The cost structure in this memo is not an aspiration; it is the operating system we already work in.
- **Utah channel proximity.** Ryan is local to Ogden, where Becklar/AvantGuard is headquartered (first monitoring call, a drive away), and to the permanent-lighting industry's home turf. The first partnerships are relationship-distance, not cold-outreach-distance.

## The three kill risks, plainly

1. **Platform bundling.** Ring ships Familiar Faces, Unusual Event Alert, Active Warnings in 2025 to 2026. Pre-committed trigger: if Ring/SimpliSafe bundle 24/7 agentic monitoring under $20/mo before we reach ~50K subscribers, we pivot to white-label licensing of the Guardian stack (`SIGHTLINE_WHITE_LABEL=1` in the repo, a config change, not a rewrite; $4/mo/account platform fee modeled at 89.5% margin in econ/). Mitigation before the trigger: local-first Core $0 positioning no cloud platform can copy, and insurer exclusivity.
2. **Re-ID and vision quality in the field.** Cross-node re-identification and identity-grade capture are demo-proven in controlled scenarios, not field-proven across weather, foliage, and thousands of roofline geometries. Mitigation: scan-derived factory aiming removes install-time aiming variance; pilot metros gate expansion; biometric face features are hard-gated in code for IL (BIPA), TX (CUBI), and Portland OR, so the compliance surface is engineered, not promised. Field re-ID performance is the number one thing pilots must prove.
3. **Contractor quality variance.** Converted seasonal crews are not W2 technicians. Mitigation: certification gates, QC agent review on every install, installer tiering, and 90-day callback tracking; callback rate is modeled at 4% vs 11% for the old model, and that modeled number must survive contact with real crews.

## What the demo proves today vs what only pilots can prove

**Demo, today:** Guardian produces an AVS-01 level 3 scored event on the flagship scenario; marginal compute measured at $0.09/home/mo at simulated volumes; the scan-to-kit flow, retrofit tap, and white-label switch exist in the repo and run.

**Only pilots can prove:** field re-ID accuracy on real perimeters, real dealer attach rates against the modeled 60% mix, real crew throughput against the 2.4 job-hour / 3-per-day ops-sim numbers, real callback rates against the 4% model, and central-station acceptance of the AVS-01 payload in production. The raise funds those pilots. Nothing in this memo asks an investor to believe a number the demo cannot show or a pilot cannot test.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
