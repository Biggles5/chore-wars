"""SightLine support agent: triage over telemetry + guides.

Deterministic rules first (telemetry explains most tickets before anyone
reads the words), guide citations second, escalation only when the rules
say human. Claude mode wraps the same rules output for tone; mock mode IS
the product behavior.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

ESCALATE_ALWAYS = ("fire", "smoke", "spark", "shock", "burn", "melt")

GUIDES = {
    "power": "docs/guides/retrofit-install-12v.md",
    "aim": "docs/guides/house-pilot.md",
    "setup": "docs/guides/homeowner-setup.md",
    "integrations": "docs/guides/integrations.md",
    "install48": "docs/guides/dealer-install-48v.md",
}


def _telemetry_findings(t: dict) -> list:
    """Rule table over a node telemetry snapshot. Order = severity."""
    f = []
    if not t:
        f.append(("no_telemetry",
                  "Node is not reporting at all: check the tap and the terminal "
                  "budget before anything else.", GUIDES["power"], False))
        return f
    rail = (t.get("power") or {}).get("rail_v")
    draw = (t.get("power") or {}).get("draw_w")
    if rail is not None and rail < 9.5:
        f.append(("rail_low",
                  f"Rail at the node is {rail}V, under the 9.5V floor: the run is "
                  "too long or the terminal is overloaded. Fit the injection kit.",
                  GUIDES["power"], False))
    if draw is not None and draw > 10:
        f.append(("draw_high",
                  f"Node draw {draw}W sustained is over the 10W watch line "
                  "(12W ceiling): check heater state and IR duty.", GUIDES["power"], True))
    if t.get("temp_c", 0) > 70:
        f.append(("temp_high",
                  f"Board temp {t['temp_c']}C: verify the housing seats in the "
                  "channel (the track is the heatsink) and the vent path.", None, True))
    if t.get("wifi_rssi_dbm", 0) < -75:
        f.append(("wifi_weak",
                  f"Wi-Fi at {t['wifi_rssi_dbm']} dBm is too weak for reliable "
                  "streams. Control keeps working over the bus pair; move the AP "
                  "or add the mesh node.", GUIDES["integrations"], False))
    storage = t.get("storage") or {}
    if storage.get("loop_hours", 72) < 48:
        f.append(("loop_short",
                  f"Loop holds {storage['loop_hours']}h, under the 48h watch line: "
                  "microSD is degrading. RMA the card class per docs/rma-warranty.md.",
                  None, False))
    return f


def triage(ticket_text: str, telemetry: dict = None) -> dict:
    """Returns diagnosis, steps, guide refs, and an escalation decision."""
    text = (ticket_text or "").lower()
    if any(w in text for w in ESCALATE_ALWAYS):
        return {"severity": "critical", "escalate": True,
                "diagnosis": "Possible electrical safety issue.",
                "steps": ["Tell the customer to power off the lighting supply now.",
                          "Escalate to a human immediately. Do not troubleshoot further."],
                "guides": [], "mode": "mock"}

    # telemetry None = not provided (guide from the words);
    # telemetry {} = the node is silent (that IS the finding)
    findings = [] if telemetry is None else _telemetry_findings(telemetry)
    steps, guides, escalate = [], [], False
    for _key, msg, guide, esc in findings:
        steps.append(msg)
        if guide and guide not in guides:
            guides.append(guide)
        escalate = escalate or esc

    if not findings:
        if any(w in text for w in ("aim", "blurry", "identify", "face")):
            steps.append("Re-run the aim: python3 hardware/dori_placement.py with the "
                         "eave height, confirm the chokepoint sits inside the aim window, "
                         "re-cant the identity channel.")
            guides.append(GUIDES["aim"])
        elif any(w in text for w in ("mask", "privacy", "neighbor")):
            steps.append("Masks widen from the app; narrowing needs the owner PIN at "
                         "the gateway. Walk the mask editor in the Scenes tab.")
            guides.append(GUIDES["setup"])
        elif any(w in text for w in ("alexa", "google", "homekit", "matter", "home assistant", "nvr", "onvif")):
            steps.append("Integration paths and their current status are in the guide.")
            guides.append(GUIDES["integrations"])
        else:
            steps.append("Pull the node telemetry snapshot from the app (Settings > "
                         "Node health) and re-run triage with it; most issues are "
                         "power or Wi-Fi and telemetry shows which.")
            guides.append(GUIDES["setup"])

    severity = ("high" if escalate else
                "medium" if findings else "low")
    return {"severity": severity, "escalate": escalate,
            "diagnosis": "; ".join(s.split(":")[0] for s in steps[:2]),
            "steps": steps, "guides": guides, "mode": "mock"}
