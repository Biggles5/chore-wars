# Market Share Plan: Three Fronts, In Order

Market frame: ~$16B US residential security, ~30M monitored households. We do not need a percent of that to matter. We need the 170K+ homes that already have a powered roofline rail, then the trades that install new rail, then the balance sheets that will subsidize the rest.

## Front 1: Retrofit the installed lighting base (SKU 1)

The base: Trimlight 120K+ homes (300+ dealers, PE-backed 2025), JellyFish 50K+, plus Gemstone, Oelo, EverLights. Total 170K+ retrofittable homes. The universal 9 to 56V power-only tap (docs/patent-notes.md, claim area 5) lets a node draw rail power while passing the incumbent controller's data through untouched, so SKU 1 installs on competitors' rail without replacing anything.

The math: these homeowners already paid $3K to $6K (est.) for permanent lighting, self-selected for curb-appeal spend, and are reachable through the dealer who installed them, not a door knock. Dealer attach CAC is $250 (modeled in econ/). A retrofit is a short visit on existing rail, not a full install, so it rides inside dealer service calls. At a 10% attach rate across the reachable base over 3 years (est.), Front 1 alone is ~17K subscribers.

## Front 2: New-install 48V rail (SKU 2 + Ops Engine)

The labor pool: Christmas-light crews and gutter crews already work the roofline and already own the ladders. The Ops Engine converts them: scan-derived kitting removes field measurement and cutting, snap-in rail and pre-terminated connectors remove wiring skill, auto-provisioning removes programming. Result: 2.4 job-hours per install and 3 installs/day per certified 2-person crew vs 8.5 job-hours and 1/day the old way (ops-sim). Installer keeps ~$840/day of $1,350 grossed (est.), which is the recruiting pitch. Callback rate modeled 4% vs 11%.

Capacity per metro: week 12 in a new metro reaches 109 installs/mo vs 27 under the old model (ops-sim). Front 2 is where subscriber growth compounds, because every new-install home is a subscription prospect at hardware-margin-funded CAC (~$400 hardware margin per install, net CAC negative, modeled in econ/).

## Front 3: Insurer and builder channels (subsidized CAC)

Templates already exist: State Farm put $1.2B into ADT (plus Google's $450M+) explicitly for predict-and-prevent; Lennar preinstalls Ring in new builds. Insurer-subsidized CAC is $150 (modeled in econ/) and carries the best economics we have: LTV:CAC 6.5x insurer-led vs 4.4x dealer-led (modeled in econ/). Builders get the 48V rail at construction stage, when roofline access is free. Front 3 scales last because it requires loss-reduction data from Fronts 1 and 2 to close.

## Eight-quarter subscriber targets

All targets (est.). Trajectory calibrated to the econ/ dealer-led model landing ~18K subs at month 36; the 8-quarter path below is the front-loaded portion of that curve. Mix: Front 1 dominant through Q4, Front 2 overtakes in year 2, Front 3 contributes from Q6.

| Quarter | Metros live | Install capacity/mo (ops-sim ramp) | New subs in quarter (est.) | Cumulative subs (est.) |
|---|---|---|---|---|
| Q1 | 1 | ramping to 109 by wk 12 | 150 | 150 |
| Q2 | 2 | ~140 | 350 | 500 |
| Q3 | 3 | ~250 | 600 | 1,100 |
| Q4 | 4 | ~360 | 900 | 2,000 |
| Q5 | 5 | ~470 | 1,300 | 3,300 |
| Q6 | 6 | ~580 | 1,700 | 5,000 |
| Q7 | 7 | ~690 | 2,000 | 7,000 |
| Q8 | 8 | ~800 | 2,300 | 9,300 |

Capacity check: metros are added quarterly; each reaches 109 installs/mo by week 12 (ops-sim), so quarterly install capacity always exceeds the new-sub target above (e.g. Q8: ~800/mo capacity, ~770/mo needed). Retrofit attaches (Front 1) need only service visits, not full install slots, so they sit on top of this capacity, which is where the slack in the table goes. The 9,300 at Q8 tracks to ~18K at month 36 on the econ/ dealer-led curve as later metros mature.

Every subscriber lands on the plan ladder: Core $0 forever (nothing leaves the house, no cloud path exists), Plus $9.99, Shield $19.99 with the wholesale central-station handoff. No contracts, ever. At 35x monthly RMR (portfolio value basis, modeled in econ/), each Shield subscriber is ~$700 of portfolio value on top of hardware margin.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
