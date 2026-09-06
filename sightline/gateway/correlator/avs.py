"""AVS-01 alarm scoring for Event Stories.

Implements the TMA AVS-01 0 to 4 scale (ANSI-accredited 2023, IACP-ratified
Oct 2024) over the story's structured facts, so every story the correlator
emits is dispatch-grade by construction. Verified-response jurisdictions
(Seattle model) act on scored, video-verified events; this is the score.

Level semantics used here:
  0  no call for service (nothing, animal, disarmed expected activity)
  1  call for service, no additional information (unverified motion)
  2  confirmed human presence on the property
  3  threat to property (human + property-threat indicators)
  4  threat to life (never emitted by simulation; requires indicators the
     sim cannot produce, e.g. forced entry while occupied, weapon)

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

PROPERTY_THREAT_ZONES = {"driveway", "porch", "front-walk", "side-yard-w", "back-yard"}


def score_story(story: dict, armed: bool = True) -> dict:
    """Returns the avs object: score, confidence, rationale."""
    entities = story.get("entities", [])
    classes = {e["class"] for e in entities}
    humans = "person" in classes
    vehicles = "vehicle" in classes
    verified = bool(story.get("verified"))
    deter = story.get("deter", {}) or {}
    zones = [z for z in story.get("zones", []) if z != "street"]
    dwell = story.get("dwell_s") or 0

    # confidence: best person frame confidence proxy via verified + multi-node
    nodes = story.get("nodes", [])
    conf = 0.55
    if verified:
        conf += 0.25
    if len(nodes) >= 2:
        conf += 0.1
    if deter.get("fired"):
        conf += 0.05
    conf = round(min(conf, 0.98), 2)

    if not entities or classes <= {"animal"}:
        return {"score": 0, "confidence": conf,
                "rationale": "No human presence. "
                             + ("Animal activity only." if "animal" in classes
                                else "No classified subjects.")}

    if not humans and not vehicles:
        return {"score": 0, "confidence": conf,
                "rationale": "No human or vehicle presence classified."}

    if not armed:
        return {"score": 0, "confidence": conf,
                "rationale": "Human presence during a disarmed period: expected activity, no call for service."}

    if humans and not verified:
        return {"score": 1, "confidence": conf,
                "rationale": "Possible human presence, not verified to AVS-2 evidence bar "
                             "(no identify-grade frame or multi-camera confirmation)."}

    if not humans and vehicles:
        s = 1 if not zones else 2
        return {"score": s, "confidence": conf,
                "rationale": "Vehicle on the property"
                             + (f" in {', '.join(zones)}" if zones else "")
                             + ", no confirmed human presence on foot."}

    # verified human from here
    threat_bits = []
    if deter.get("fired"):
        threat_bits.append(f"deterrence fired at {deter.get('ts', '')[11:19]}"
                           + (", subject fled" if deter.get("outcome") == "fled" else
                              ", subject did not leave" if deter.get("outcome") == "stayed" else ""))
    if "package" in classes:
        threat_bits.append("package interaction on the porch")
    if dwell >= 60 and zones:
        threat_bits.append(f"{int(dwell)}s dwell in {', '.join(zones[:2])}")
    if vehicles:
        threat_bits.append("associated vehicle present")

    if threat_bits:
        evidence = ("native frames on the gateway" if story.get("evidence_exportable")
                    else "frames on the gateway (simulated in this demo)")
        return {"score": 3, "confidence": conf,
                "rationale": "Verified human presence with property-threat indicators: "
                             + "; ".join(threat_bits)
                             + f". Video-verified, {evidence}."}
    return {"score": 2, "confidence": conf,
            "rationale": "Confirmed human presence on the property"
                         + (f" ({', '.join(zones[:2])})" if zones else "")
                         + ", video-verified, no property-threat indicators yet."}
