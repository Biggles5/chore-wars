# Biometric law matrix

The jurisdictions where face-identification features are hard-gated in code. The gate is not a policy statement: `gateway/correlator/flags.py` serves the flags, `Guardian.face_id_allowed()` enforces them, and the app shows the user why. Informational, not legal advice; counsel reviews before any biometric feature ships anywhere.

## Hard gates (feature off, not offable)

| Jurisdiction | Law | What it does | SightLine behavior |
|---|---|---|---|
| Illinois | BIPA, 740 ILCS 14 (2008) | Biometric identifiers require informed written consent; private right of action; statutory damages per scan | Face recognition and Familiar Faces disabled. No biometric templates created, period. |
| Texas | CUBI, Bus. & Com. Code 503.001 | Consent required for biometric capture; AG enforcement up to $25K/violation | Same as Illinois. |
| Portland, OR | City Code 34.10 (2021) | Bans private-entity face recognition in places of public accommodation; broad reach, city-level | Same. City gate beats the state: `SIGHTLINE_CITY=Portland` with `SIGHTLINE_STATE=OR` triggers it. |

## Watchlist (review before enabling features in these markets)

| Jurisdiction | Why it is on the list |
|---|---|
| Washington | My Health My Data Act reaches biometric-adjacent data; AG active |
| New York City | Biometric Identifier Information Law: notice requirements for commercial establishments; residential reach untested |
| Baltimore, MD | Face recognition ordinance (private use restrictions, sunset provisions have shifted) |
| Colorado, Virginia, Connecticut | Comprehensive privacy laws treat biometrics as sensitive data requiring consent |
| Oregon (statewide) | Statute governs certain private facial recognition uses; Portland is stricter |

## What SightLine does everywhere, regardless

- No face databases exist in the product. Re-ID is per-site, ephemeral, appearance-based (not face-geometric), and ages out with the story.
- Familiar Faces, where lawful, stores the owner's own labels on the owner's gateway. Nothing enrolls anyone anywhere else.
- The evidence path never depends on biometrics: DORI-grade native frames are the product; a human identifies the person.
- Every gated market still gets the full product minus the gated feature. Nothing else degrades.

## Maintenance

This matrix is versioned with the code that enforces it. Any law change lands as a PR touching this file AND `flags.py` in the same commit, with an effective date. Tests in `tests/test_guardian.py` pin the three hard gates.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
