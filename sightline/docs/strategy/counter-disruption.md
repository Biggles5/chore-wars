# Counter-Disruption: How We Get Killed, and What We Do About It

Disruptors get disrupted. Three failure modes, each with named defenses, and one explicit, pre-committed pivot trigger so the decision is made now, calmly, instead of later, badly.

## Failure mode 1: Platform bundling

Ring is shipping Familiar Faces, Unusual Event Alert, and Active Warnings across 2025 to 2026. The clock is running. The kill scenario: Ring or SimpliSafe bundles 24/7 agentic monitoring under $20/mo, at Amazon distribution scale, before we have a defensible base.

**The trigger, in writing:** if Ring or SimpliSafe ships a 24/7 agentic monitoring bundle under $20/mo before we reach ~50K subscribers, we pivot to licensing the Guardian stack B2B2C. This is not a rewrite. In the repo it is literally `SIGHTLINE_WHITE_LABEL=1`, a config change. The pivot plan: white-label Guardian to lighting dealers and regional alarm companies who bring their own accounts, at a $4/mo/account platform fee modeled at 89.5% margin (modeled in econ/). Regional alarm cos hold accounts the platforms cannot reach and face the same wholesale-vs-retail squeeze we exploit; they become customers instead of casualties.

**Defenses before the trigger:**
- **Local-first privacy positioning.** Core $0, nothing leaves the house, no cloud path exists. This is structural, not marketing: a cloud platform funded by data and ads cannot credibly ship a no-cloud tier, and every Ring headline about footage sharing widens our lane.
- **RMR annuity economics.** At 67.1% blended gross margin and $4.17/home/mo marginal cost (modeled in econ/), we can profitably price under any bundler's retail floor while their $30 to $80/mo base anchors them high.
- **Insurer exclusivity.** The State Farm-template channel ($150 CAC, 6.5x LTV:CAC, modeled in econ/) can be locked with data-spec exclusivity that a platform selling everyone's data cannot sign.

## Failure mode 2: Hardware commoditization

The graveyard is the case study. Dropcam: great camera, absorbed by Nest, brand gone. Canary: hardware praised, no channel, faded. Latch: public via SPAC, collapsed under hardware margins. SmartRent: channel-dependent hardware, public-market repricing. Pattern: standalone smart hardware with no install trade, no recurring margin, and no channel dies when the hardware becomes a commodity.

**Defenses:**
- **Install-trade lock.** The Ops Engine plus the certified installer network is the hard-to-copy asset: scan-to-kit factory flow, 2.4 job-hour installs, 109/mo/metro capacity at week 12 (ops-sim), 4% modeled callback rate. A commodity camera does not come with 2-person certified crews on the roofline. Copying the node is easy; copying the trade takes years.
- **RMR annuity economics.** We are not a hardware company. Hardware carries ~$400 margin per install (modeled in econ/) and exists to make net CAC negative; the business is the subscription at 67.1% margin. Commoditized hardware makes our CAC cheaper, not our business weaker.
- **Patents as speed bumps, not walls.** Five filed claim areas (docs/patent-notes.md): rail-integrated dual-sensor node, scan-derived identity-channel aiming, detection-coupled zone-follow deterrence, cross-node perimeter re-identification with verified Event Story gating, and the universal 9 to 56V power-only tap. Plan for them to slow a copier 12 to 24 months (est.), not stop one. The moat is the trade and the channel; the patents buy time to dig it.

## Failure mode 3: Channel too slow

Dealers do not attach, installer certification lags, and the 8-quarter ramp in market-share-plan.md slips while the platform clock runs.

**Defenses:**
- **Multiple channels, staged.** Dealer attach (60% of mix, $250 CAC), inbound (25%, $450), insurer-subsidized (15%, $150), all modeled in econ/; no single channel is load-bearing. Builder construction-stage installs (Lennar template) add a fourth lane that bypasses dealers entirely.
- **Multiple labor pools.** Christmas-light, gutter, and landscape-lighting crews are separately recruitable; the Ops Engine's whole point is that certified labor is manufactured, not found.
- **The kill trigger doubles as the slow-channel exit.** If the channel is too slow to reach ~50K subs before an under-$20 platform bundle lands, the same white-label pivot applies, and a slow direct channel becomes the licensing customer list.

## The standing order

Track two numbers monthly: our subscriber count against the ~50K threshold, and platform bundle pricing against the $20/mo line. The day both conditions meet, `SIGHTLINE_WHITE_LABEL=1` ships within one quarter. No debate, no sunk-cost defense of the D2C motion. The trigger was written when we were calm.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
