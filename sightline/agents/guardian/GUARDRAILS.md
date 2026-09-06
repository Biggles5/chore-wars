# Guardian guardrails

What the autonomous monitoring agent may never do, no matter what it scores. The hard ones are enforced in code, not just written here.

1. **Never call 911 or any PSAP directly.** Dispatch authority belongs to the licensed central-station operator receiving the handoff. Guardian scores, verifies, and hands off. (Enforced: Guardian has no dialer, no PSAP integration surface; the only external call is the station webhook.)
2. **Never assert that a crime occurred.** Guardian reports observations with timestamps and grades: "verified person, driveway, deter fired, subject fled." Legal conclusions are for humans. (Enforced: handoff payload carries the guardrail line; narrator prompts ban accusation language.)
3. **No face identification in gated jurisdictions.** Illinois (BIPA), Texas (CUBI), and Portland, Oregon are hard-gated: the feature flag is off and `Guardian.face_id_allowed()` returns false regardless of configuration attempts. The jurisdiction matrix lives in docs/compliance/biometric-law-matrix.md and the flags endpoint serves it. (Enforced in code.)
4. **Never fabricate visual detail.** Guardian consumes structured story facts only, same as the narrator. It never describes clothing, race, gender, or objects that are not in the JSON. (Enforced: the payload is built from story fields; there is no free-generation path in mock mode, and Claude-mode prompts carry the ban.)
5. **Never deter on animals or during disarmed scenes.** Score 0 stories are dismissed; the policy engine cannot reach intervene from score 0 or 1. (Enforced: policy table.)
6. **Never suppress the owner.** Every intervene and handoff notifies the owner in the same motion. Guardian cannot opt the owner out of knowing.
7. **Never exceed the latency budget silently.** If scoring, intervention, or the handoff decision blows its budget (5 s / 10 s / 30 s), the event is escalated to notify+handoff conservatively and the miss is logged to telemetry.
8. **Never learn across homes.** Guardian's state is per-site. No cross-site identity, no fleet-wide behavioral profiles of people. Fleet learning happens on anonymized aggregate metrics only, per the privacy policy.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
