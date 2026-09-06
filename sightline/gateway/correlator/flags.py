"""Jurisdiction-aware feature flags, enforced in code.

The biometric matrix (docs/compliance/biometric-law-matrix.md) and the
audio-consent matrix drive what the stack may do per install location.
The gateway serves the flags; the app displays them; Guardian and the
correlator enforce them.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import os

# Face-identification gates. "PORTLAND-OR" is city-level: Portland's private
# facial-recognition ban is stricter than Oregon state law, so city beats state.
FACE_ID_GATED = {
    "IL": "Illinois BIPA (740 ILCS 14): biometric identifiers need written consent; private right of action",
    "TX": "Texas CUBI (Bus. & Com. Code 503.001): biometric identifiers need consent; AG enforcement",
    "PORTLAND-OR": "Portland City Code 34.10: private use of face recognition in places of public accommodation banned",
}

# All-party audio-consent states (mixed/unsettled treated as all-party, D-023)
AUDIO_ALL_PARTY = {"CA", "CT", "DE", "FL", "IL", "MD", "MA", "MI", "MT",
                   "NV", "NH", "OR", "PA", "VT", "WA"}


def jurisdiction() -> str:
    j = os.environ.get("SIGHTLINE_STATE", "UT").upper()
    city = os.environ.get("SIGHTLINE_CITY", "").upper()
    if j == "OR" and city == "PORTLAND":
        return "PORTLAND-OR"
    return j


def feature_flags() -> dict:
    j = jurisdiction()
    state = j.split("-")[-1] if "-" in j else j
    face_gated = j in FACE_ID_GATED or state in FACE_ID_GATED
    reason = FACE_ID_GATED.get(j) or FACE_ID_GATED.get(state)
    return {
        "jurisdiction": j,
        "face_recognition": {
            "enabled": not face_gated,
            "gated_reason": reason,
        },
        "audio": {
            "default": "off",
            "all_party_consent": state in AUDIO_ALL_PARTY,
            "warning": ("All-party consent state: every person recorded must consent. "
                        "Audio stays off unless you accept that responsibility."
                        if state in AUDIO_ALL_PARTY else
                        "One-party consent state. Audio still ships off by default."),
        },
        "familiar_faces": {
            "enabled": not face_gated,
            "note": "local labels only, never a shared database" if not face_gated
                    else "unavailable in this jurisdiction",
        },
    }


def branding() -> dict:
    white = os.environ.get("SIGHTLINE_WHITE_LABEL", "") == "1"
    return {
        "white_label": white,
        "name": os.environ.get("SIGHTLINE_BRAND", "Guardian" if white else "SightLine"),
        "brain": os.environ.get("SIGHTLINE_BRAIN_NAME", "Guardian"),
        "note": "licensing-pivot mode: set SIGHTLINE_WHITE_LABEL=1 and SIGHTLINE_BRAND. "
                "A config change, not a rewrite.",
    }
