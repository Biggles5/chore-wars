# Privacy architecture

Privacy is load-bearing here: 72% of buyers say they have privacy concerns about cameras (Parks). The answers below are structural, not settings.

## Neighbor masks, enforced at setup

- Mask setup is a mandatory onboarding step: the installer (or self-installing owner) walks each camera view and masks neighbor windows, doors, and yards before the system arms.
- Masks are enforced on device: masked pixels are zeroed at the sensor pipeline, before encoding, before the loop. Masked regions are never stored anywhere, so no later actor (us, police, a subpoena, a hacker) can recover them.
- Masks can be widened from the app freely. Narrowing or deleting one requires the owner PIN at the gateway, on purpose: the easy direction is always more privacy.

## Audio: off by default

Audio capture ships disabled. Enabling it surfaces a state-specific consent warning driven by `docs/compliance/audio-law-matrix.md` (all-party consent states get the strongest warning). No audio ever rides an evidence export unless it was lawfully captured and the owner explicitly includes it.

## Data retention

Node loop 72 h; gateway local, owner-capped (default 90 days (est.)); cloud only on Plus/Shield, 60 days, delete-on-demand. Full table: data.md.

## Core = nothing leaves the house

The $0 forever plan has no cloud path in the build. Detection, stories, narration (mock mode), deterrence, the app on your LAN: all of it runs locally. Upgrading to Plus adds sync; it never adds obligation: no contracts anywhere (the anti-Vivint position, and the FTC's $20M Vivint settlement is why the position sells).

## No face databases

Re-ID stitches one night's story from color/embedding features, per site, ephemeral. There is no enrollment, no gallery, no cross-site matching, and nothing to sell. We do not do facial recognition against external databases, period.

## The owner sees everything

Every access (support session, export, law-enforcement process, mask change) is logged to the owner in the app. Law-enforcement requests require legal process, and the owner is notified unless the process legally forbids it.
