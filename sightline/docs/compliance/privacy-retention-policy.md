# SightLine Privacy and Retention Policy

This is the policy as it ships. It is not marketing copy. Where the policy says a thing cannot happen, the architecture makes it impossible, not merely disabled.

## 1. Core Plan: Nothing Leaves the House

On the Core plan ($0, forever), no video, audio, image, event, story, or metadata leaves the home. This is not a toggle. There is no cloud upload path in Core firmware. No endpoint, no credential, no dormant code path. A Core system cannot exfiltrate footage because the capability does not exist on the device.

- All processing (detection, verification, narration) runs on the node and gateway.
- Remote viewing on Core is direct, local-network only.
- Upgrading to Plus or Shield is an explicit owner action that provisions the cloud path at that moment, never before.

## 2. On-Node Retention

- Each node keeps a rolling 72-hour loop of its own footage, encrypted at rest, overwritten continuously.
- The loop never leaves the node except when the owner exports a clip or a verified event is committed to the gateway.

## 3. Gateway Retention (All Plans)

- The gateway retains verified events, narrated stories, and associated native-pixel clips locally.
- Retention cap is user-set. Default: 90 days (est.). Owner can shorten to 24 hours or extend to the gateway's storage limit.
- When the cap is reached, oldest events are deleted first, automatically and irrecoverably.

## 4. Cloud Retention (Plus and Shield Only)

- Cloud stores verified events, stories, and owner-flagged clips only. Never the raw 72-hour loop. Never continuous video.
- Retention: 60 days, then automatic deletion.
- Delete on demand: owner-initiated deletion completes across all cloud systems, including backups, within 72 hours.
- No contracts. Cancel any time; on cancellation, cloud data is deleted on the same 72-hour clock and the system continues to work fully on Core.

## 5. What We Will Never Do

- We will never sell customer data. Not footage, not events, not metadata, not derived analytics. Ever.
- We do not build or contribute to facial recognition databases. No enrollment, no matching against external galleries.
- Re-identification (recognizing "the same person seen earlier tonight") is per-site and ephemeral: embeddings live on the gateway, are scoped to that one home, and expire with the event window. They are never uploaded, pooled, or compared across sites.
- The AI narrator describes what the native pixels show. It never fabricates, enhances, or synthesizes imagery. Evidence exports are native pixels only (see State v. Puloka, 2024: courts reject AI-enhanced frames).

## 6. Audio

- Audio capture is OFF by default on every SKU and every plan.
- Enabling audio requires an explicit owner action, per node, with an in-app legal warning driven by the owner's state (see the audio law matrix).
- Audio, when enabled, follows the same retention rules as video and the same Core no-cloud guarantee.

## 7. Privacy Masks

- Privacy masks are enforced at the sensor, on device. Masked regions are zeroed before encoding; masked pixels are never captured into the loop, never processed, never recoverable.
- Mask setup is mandatory during installation. The system will not arm until the owner has reviewed mask coverage for neighbor windows, neighbor yards, and public sidewalk beyond the property line.

## 8. Breach Notification

- If a breach affects customer data, we notify affected owners within 72 hours of confirmation, with plain-language scope: what was exposed, whose, and what we are doing.
- Core customers have no cloud data to breach. We will say so plainly in any incident report.

## 9. Law Enforcement Requests

- We disclose customer data only in response to valid legal process (warrant, subpoena, court order) reviewed by counsel.
- Every law enforcement request touching an owner's data is logged to that owner and visible in-app, unless a court order legally prohibits notice, in which case we notify the moment the prohibition lapses.
- We do not offer law enforcement a portal, bulk access, or warrantless "emergency" sharing programs.
- Core plan: we hold nothing to disclose. Requests for Core-plan footage go to the owner, because only the owner has it.

## 10. Changes to This Policy

- Material changes require in-app notice 30 days before effect.
- We will never weaken the Core no-cloud guarantee, the no-sale commitment, or on-device mask enforcement by policy update. Those are architectural commitments.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
