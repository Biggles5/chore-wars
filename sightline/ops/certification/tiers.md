# SightLine Installer Tiers and Scorecard

## Why tiering exists
Quality variance is the failure mode of every contractor network. One sloppy crew costs more in callbacks, warranty claims, and reputation than ten good crews earn. The scorecard is the mitigation: every job feeds it, every tier is earned from it, and the QC agent grades the same way for everyone.

## Scorecard schema
| Field | Type | Definition | Target |
|---|---|---|---|
| avg_install_hr | float | Rolling mean job-hours per single-story install | 2.4h target |
| qc_first_pass | float (0-1) | Share of QC gates passed on first submission | 85%+ by job 5; tier bars below |
| callback_90d | float (0-1) | Jobs generating a callback within 90 days | <5% |
| homeowner_rating | float (1-5) | Mean post-install rating | Tier bars below |
| jobs_done | int | Lifetime completed, commissioned jobs | Tier entry counts |

All rate metrics compute over rolling 90-day windows except jobs_done (lifetime).

## Tiers
### Certified (entry)
- Entry: passed the half-day course and the bench practical.
- Rev-share: 20% of plan revenue on your activated accounts.
- Queue: standard lead queue.

### Pro
- Entry: 20+ jobs, qc_first_pass >= 85%, callback_90d < 5%, homeowner_rating >= 4.5.
- Rev-share: 25%.
- Territory: first refusal on leads in your home zip.

### Elite
- Entry: 60+ jobs, qc_first_pass >= 90%, callback_90d < 3%, homeowner_rating >= 4.7.
- Rev-share: 30%.
- Territory: metro-wide first refusal, plus the demo-home program (SightLine-funded demo rig, featured in local marketing).

## Promotion and demotion
- Promotion: automatic at the start of the week after all bars are met. No application.
- Demotion: any tier bar missed across a full rolling 90-day window drops you one tier at the next weekly evaluation. One warning notice fires at day 60 of a failing window so there is time to correct.
- Floor: demotion never goes below Certified. Certification itself is revoked only for safety violations (meter discipline, mains contact) or certification-ethics violations (gaming QC photos).
- Cooldown: after a demotion, promotion back requires meeting the bars for a fresh 90-day window.

## Dispute process
1. File in the installer app within 14 days of the disputed job or rating.
2. Evidence reviewed: QC photos, telemetry, homeowner communication log. The QC agent's grade can be overturned by human review; telemetry (timestamps, commissioning data) is authoritative for time and callback disputes.
3. Ruling within 7 days. Upheld disputes recompute the scorecard retroactively, including any tier change that follows.
4. Ratings from homeowners with documented non-install grievances (pricing, scheduling by SightLine) are excluded on review.

## The deal in one line
The scorecard is public to you, the bars are fixed, the QC agent grades everyone identically, and the money follows the metrics: 20/25/30.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
