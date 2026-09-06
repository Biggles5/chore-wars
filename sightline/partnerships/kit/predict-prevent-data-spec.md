# Predict and Prevent Data Spec v1

What an insurer partner receives, exactly. All flows are opt-in per policyholder. SightLine privacy policy is applied before anything leaves our side: masks enforced on-device, audio off by default, no face databases, re-ID is per-site and ephemeral.

## 1. Monthly per-cohort aggregates
Cohorts are anonymized groups (min cohort size enforced), never individual homes.

- Events by AVS-01 level (0-4 counts per cohort per month)
- Deter outcomes: fled vs stayed counts
- System-armed hours per cohort
- Mean response latencies (event to score, score to station handoff)

## 2. Incident-time attestation
On a claim, with policyholder consent: a signed attestation that the site had live coverage at timestamp T. Cryptographically signed, timestamped, machine-verifiable. No media, no event content, just the fact of coverage.

## 3. Claim export
On policyholder request only. The full claims package: AVS-01 scored story, native frames, chain of custody, police-readable narrative. Goes to the policyholder or their designee, not into any bulk feed.

## What is NEVER shared
- Video or images (outside a policyholder-initiated claim export)
- Per-person identity of any kind
- Per-home rhythms (arm/disarm times, occupancy patterns, schedules)
- Anything from Core-plan homes: no cloud path exists, the data is not collectable
- Face data: no face databases exist anywhere in the system

## Data schema

### cohort_monthly_aggregate
| Field | Type | Notes |
|---|---|---|
| cohort_id | string | Anonymized cohort key, min size enforced |
| period | string (YYYY-MM) | Reporting month |
| homes_active | int | Count of opted-in active systems |
| events_avs0 | int | AVS-01 level 0 count |
| events_avs1 | int | AVS-01 level 1 count |
| events_avs2 | int | AVS-01 level 2 count |
| events_avs3 | int | AVS-01 level 3 count |
| events_avs4 | int | AVS-01 level 4 count |
| deter_fled | int | Deter events with outcome fled |
| deter_stayed | int | Deter events with outcome stayed |
| armed_hours_total | int | Sum of system-armed hours in cohort |
| latency_event_to_score_ms_mean | int | Mean, milliseconds |
| latency_score_to_handoff_ms_mean | int | Mean, milliseconds |
| schema_version | string | "pp.agg.v1" |

### incident_attestation
| Field | Type | Notes |
|---|---|---|
| attestation_id | string | Unique per attestation |
| policy_ref | string | Carrier-side reference, supplied by carrier |
| timestamp_t | string (ISO 8601) | Incident time queried |
| coverage_live | bool | System live at T |
| plan_class | string | "plus" or "shield" only, never "core" |
| signature | string | Detached signature over payload |
| signed_at | string (ISO 8601) | Signing time |
| schema_version | string | "pp.attest.v1" |

### claim_export_manifest
| Field | Type | Notes |
|---|---|---|
| export_id | string | Unique per export |
| requested_by | string | "policyholder" (only valid value) |
| story_window_start | string (ISO 8601) | Event story start |
| story_window_end | string (ISO 8601) | Event story end |
| avs01_score | int | 0-4 |
| narrative_included | bool | Police-readable narrative |
| native_frames_count | int | Native frames only; simulated frames never attach |
| chain_of_custody_hash | string | SHA-256 over export contents |
| schema_version | string | "pp.claim.v1" |

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
