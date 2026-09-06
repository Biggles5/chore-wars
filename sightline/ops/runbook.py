"""Installer runbook generator: kit in, guided job out.

Every step has a target time (they sum to the throughput model's job
hours), an AR/photo reference from the kit's overlay, and a QC gate where
one applies. The installer app walks these in order; the next step unlocks
when the QC agent passes the gate photo. The final step is auto-provision
plus the 30-point commissioning check. Warranty activates only when every
gate has passed.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "econ"))
import throughput as tp  # noqa: E402

COMMISSIONING_30 = [
    # power (1-6)
    "rail voltage at every node inside 9 to 56V window",
    "node draw under 10W sustained per telemetry",
    "terminal budget: LEDs + node ceiling under terminal watts",
    "injection points energized and inside voltage window",
    "controller terminals torqued and strain-relieved",
    "supply fused per Class 2 listing",
    # mechanical (7-12)
    "every node mechanically captured (pull test), VHB seal only",
    "gaskets seated with no visible gap at any housing joint",
    "glands torqued, drip loops on every entry",
    "rail/track sections coupled and aligned at every corner",
    "no exposed conductor anywhere on the run",
    "ladder damage walkaround: fascia, gutters, plants",
    # optics (13-18)
    "each identity channel aimed at its planned chokepoint azimuth",
    "cant angle within 2 degrees of plan",
    "chokepoint test frame at identify density (px/m readout)",
    "wide channel horizon level within 2 degrees",
    "IR illumination confirmed on night test frame or dark cloth test",
    "no obstruction (soffit lip, gutter) in any field of view",
    # privacy (19-22)
    "neighbor windows and yards masked with homeowner present",
    "masks verified in live view on every node",
    "audio confirmed OFF",
    "homeowner walked the mask editor and holds the owner PIN",
    # network + system (23-27)
    "every node on Wi-Fi with RSSI better than -70 dBm",
    "gateway discovered all nodes, heartbeats under 35s apart",
    "72h loop writing on every node (storage telemetry)",
    "deter test fire: zone-follow strobe observed under 1s local",
    "event test: walk test produces a story in the app",
    # handoff (28-30)
    "app installed for homeowner, scenes explained, arm modes set",
    "QC gate photos all passed and archived to the job record",
    "warranty activated; job marked complete in dealer portal",
]


def _gate(check: str, ref: str) -> dict:
    return {"qc_gate": check, "photo_ref": ref}


def runbook_from_kit(kit: dict) -> dict:
    brand48 = any(c["type"].startswith("48V") for c in kit["cut_list"])
    n_nodes = len(kit["cameras"])
    n_track = sum(1 for c in kit["cameras"] if c["kind"] == "track")
    steps = []

    def step(title, target_min, detail, ar=None, gate=None):
        s = {"n": len(steps) + 1, "title": title, "target_min": target_min,
             "detail": detail}
        if ar:
            s["ar_ref"] = ar
        if gate:
            s.update(gate)
        steps.append(s)

    step("Stage the kit against the pick sheet", 10,
         f'Verify every labeled piece: {", ".join(c["label"] for c in kit["cut_list"][:8])}'
         + ("..." if len(kit["cut_list"]) > 8 else "")
         + ". Missing label = stop, call support before the ladder goes up.",
         ar="segments")
    if brand48:
        step("Mount rail sections in labeled order", 55,
             "A1 outward. Corner couplers click; no tools on the bus. "
             "Level line per the AR guide as you go.",
             ar="segments",
             gate=_gate("rail_level_spacing", "full-segment photo, level visible"))
        step("Home-run the 48V supply", 20,
             "Supply location per plan; Class 2 only; fuse per listing.",
             gate=_gate("controller_wiring", "supply + first coupling photo"))
    else:
        step("Power down and verify at the controller", 8,
             "Kill the lighting supply, meter reads 0V at the terminal before "
             "anything else happens.",
             gate=_gate("controller_wiring", "meter on terminal photo"))
        step("Run tap harnesses per label", 30,
             "Power pair only into the WAGO 221s; the LED data line goes "
             "THROUGH the node's buffer, never spliced.",
             ar="segments",
             gate=_gate("connector_clicked", "open WAGO row photo before closing"))
    step(f"Seat {n_track} track node(s)", 12 * n_track if not brand48 else 5 * n_track,
         "Mechanical capture first (listen for it), gasket flat, gland torqued, "
         "drip loop formed." + ("" if brand48 else " VHB is a seal, never structure."),
         ar="nodes",
         gate=_gate("gasket_seated", "each node housing joint, close-up"))
    step("Aim each identity channel", 8 * n_track,
         "AR view shows the planned azimuth and cant per node; align the "
         "reticle to the chokepoint ring, lock the cant screw.",
         ar="chokepoint_rings",
         gate=_gate("node_aim", "app aim-view screenshot per node"))
    step("Mount and connect the door node", 12,
         "Jamb side per plan, slots level, gasketed 2-pin home.",
         ar="nodes",
         gate=_gate("gasket_seated", "door node seated photo"))
    step("Auto-provision and run the commissioning check", 18,
         "Power up. Nodes join, gateway discovers, the app runs all 30 points "
         "and shows red/green. Fix reds before the homeowner walkthrough.",
         gate={"qc_gate": "commissioning", "checklist": COMMISSIONING_30})
    step("Privacy masks with the homeowner", 12,
         "Mandatory. Walk every view together, mask neighbor windows and "
         "yards, hand over the owner PIN.")
    step("Homeowner walkthrough and handoff", 10,
         "Scenes, arm modes, the Guardian tab, how deter looks. Leave with "
         "the app on their phone and a test story in their history.")

    total_min = sum(s["target_min"] for s in steps)
    return {
        "schema": "sightline.runbook.v1",
        "site_id": kit["site_id"],
        "steps": steps,
        "total_target_min": total_min,
        "total_target_hr": round(total_min / 60.0, 1),
        "model_job_hr": tp.install_hours("new"),
        "gates_required_for_warranty": sorted({
            s["qc_gate"] for s in steps if "qc_gate" in s}),
        "ar_overlay": kit["ar_overlay"],
    }


if __name__ == "__main__":
    import json
    from scan_to_kit import kit_from_scan, load_sample
    rb = runbook_from_kit(kit_from_scan(load_sample(1)))
    print(json.dumps({k: rb[k] for k in
                      ("site_id", "total_target_hr", "model_job_hr",
                       "gates_required_for_warranty")}, indent=2))
    for s in rb["steps"]:
        print(f'{s["n"]}. [{s["target_min"]}m] {s["title"]}'
              + (f'  <gate:{s["qc_gate"]}>' if "qc_gate" in s else ""))
