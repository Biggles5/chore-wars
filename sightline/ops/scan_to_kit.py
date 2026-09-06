"""Scan-to-kit: the Ops Engine's core pipeline. One scan in, everything a
factory and an installer need out.

Input:  sightline.scan.v1 (ops/schemas/, 3 samples in ops/samples/)
Output: measured model, kit BOM + price (via the quote engine: one price
        book, one power module, one optics module), factory cut list with
        segment labels (A1..N), connector map, power-injection plan,
        DORI camera placement with identity-channel aim angles, and the
        AR overlay data file the installer app consumes.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import json
import math
import string
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "hardware"))
sys.path.insert(0, str(ROOT / "hardware" / "electronics"))
sys.path.insert(0, str(ROOT / "agents" / "quote"))
import dori_placement as dp  # noqa: E402
import power_budget as pb  # noqa: E402
import quote as quote_engine  # noqa: E402

import jsonschema  # noqa: E402

SCAN_VALIDATOR = jsonschema.Draft202012Validator(
    json.loads((Path(__file__).parent / "schemas" / "scan.v1.schema.json").read_text()))

FT = 0.3048
RAIL_STOCK_FT = 8.0          # factory rail sticks (SKU 2) (est.)
CONNECTOR_EVERY_FT = 25.0    # retrofit tap harness service loop spacing (est.)


def _seg_len(seg) -> float:
    return math.dist(seg["from"], seg["to"])


def _seg_facing(seg) -> float:
    """Outward normal (compass, 0=N/+y, cw). Front wall (y=0, x increasing)
    faces south (180)."""
    if "facing_deg" in seg and seg["facing_deg"] is not None:
        return seg["facing_deg"]
    dx = seg["to"][0] - seg["from"][0]
    dy = seg["to"][1] - seg["from"][1]
    # left-hand normal of the walk direction points outward for a
    # counterclockwise footprint traversal
    nx, ny = dy, -dx
    return round(math.degrees(math.atan2(nx, ny)) % 360, 1)


def measured_model(scan: dict) -> dict:
    segs = []
    for seg in scan["segments"]:
        segs.append({
            "id": seg["id"], "from": seg["from"], "to": seg["to"],
            "length_ft": round(_seg_len(seg), 1),
            "eave_ft": seg["eave_ft"], "facing_deg": _seg_facing(seg),
        })
    return {
        "site_id": scan["site_id"],
        "roofline_ft": round(sum(s["length_ft"] for s in segs), 1),
        "corners": len(segs),
        "eave_heights_ft": sorted({s["eave_ft"] for s in segs}, reverse=True),
        "segments": segs,
        "variance_note": "photogrammetry ~2.6% vs tape; cut list carries +2% length margin",
    }


def cut_list(model: dict, brand: str) -> list:
    """Factory cut list, labeled A1..N, ready for the kit pick sheet."""
    cuts = []
    letters = string.ascii_uppercase
    for i, seg in enumerate(model["segments"]):
        need = seg["length_ft"] * 1.02  # scan variance margin
        if brand == "none":
            sticks = math.ceil(need / RAIL_STOCK_FT)
            for n in range(sticks):
                piece = min(RAIL_STOCK_FT, need - n * RAIL_STOCK_FT)
                cuts.append({
                    "label": f"{letters[i]}{n + 1}",
                    "segment": seg["id"],
                    "length_ft": round(piece, 1),
                    "type": "48V blind-mate rail",
                    "note": "factory cut, bus pre-terminated both ends",
                })
        else:
            cuts.append({
                "label": f"{letters[i]}1",
                "segment": seg["id"],
                "length_ft": round(need, 1),
                "type": "tap harness (18 AWG, power only + data buffer loop)",
                "note": "pre-cut to segment length, labeled to the plan",
            })
    return cuts


def _nearest_segment(model: dict, pos) -> dict:
    best, best_d = None, 1e9
    for seg in model["segments"]:
        mid = [(seg["from"][0] + seg["to"][0]) / 2, (seg["from"][1] + seg["to"][1]) / 2]
        d = math.dist(mid, pos)
        if d < best_d:
            best, best_d = seg, d
    return best


def camera_plan(scan: dict, model: dict) -> list:
    """One track node per scan chokepoint, mounted on the nearest segment,
    identity channel aimed at the chokepoint with the cant computed from
    the shared optics module. Plus the door node."""
    plan = []
    for cp in scan.get("chokepoints", []):
        seg = _nearest_segment(model, cp["pos"])
        # mount at the segment point closest to the chokepoint
        ax, ay = seg["from"]
        bx, by = seg["to"]
        px, py = cp["pos"]
        t = max(0.12, min(0.88, ((px - ax) * (bx - ax) + (py - ay) * (by - ay))
                          / max(_seg_len(seg) ** 2, 1e-6)))
        mount = [round(ax + t * (bx - ax), 1), round(ay + t * (by - ay), 1)]
        ground_ft = math.dist(mount, cp["pos"])
        eave_m = seg["eave_ft"] * FT
        ground_m = ground_ft * FT
        pitch = dp.pitch_deg(eave_m, ground_m)
        density = dp.px_per_m(dp.SENSORS_H_PX["12mp"], 60, ground_m)
        window = dp.identify_window(eave_m, dp.SENSORS_H_PX["12mp"], 60)
        in_window = window.exists and window.near_m <= ground_m <= window.far_m
        aim_az = round(math.degrees(math.atan2(px - mount[0], py - mount[1])) % 360, 1)
        plan.append({
            "node_id": f"node-{cp['id']}",
            "kind": "track",
            "segment": seg["id"],
            "mount_pos_ft": mount,
            "chokepoint": cp["id"],
            "aim": {
                "azimuth_deg": aim_az,
                "cant_down_deg": round(pitch, 1),
                "ground_distance_ft": round(ground_ft, 1),
                "px_per_m_at_chokepoint": round(density, 1),
                "dori_at_chokepoint": dp.dori_level_at(dp.SENSORS_H_PX["12mp"], 60, ground_m),
                "pitch_ok": pitch <= dp.PITCH_USABLE_DEG,
                "in_identify_window": bool(in_window),
                "identify_window_ft": [round(window.near_m / FT, 1),
                                       round(window.far_m / FT, 1)]
                if window.exists else None,
            },
        })
    if scan.get("door"):
        plan.append({"node_id": "node-door", "kind": "door",
                     "segment": None, "mount_pos_ft": scan["door"]["pos"],
                     "chokepoint": "door",
                     "aim": {"azimuth_deg": 180.0, "cant_down_deg": 0.0,
                             "ground_distance_ft": 6.0,
                             "px_per_m_at_chokepoint": 500.0,
                             "dori_at_chokepoint": "validate",
                             "pitch_ok": True, "in_identify_window": True,
                             "identify_window_ft": [2.0, 52.4]}})
    return plan


def connector_map(model: dict, cameras: list, brand: str) -> list:
    """Every connection on the job, numbered, with its connector type.
    Tool-free gasketed connectors kill the field splice."""
    out = []
    n = 1
    for cam in cameras:
        if cam["kind"] == "door":
            out.append({"n": n, "at": "door jamb", "type": "M12 gland + gasketed 2-pin",
                        "connects": "door node to nearest soffit feed"})
        elif brand == "none":
            out.append({"n": n, "at": f'{cam["segment"]} @ {cam["mount_pos_ft"]}',
                        "type": "blind-mate rail socket (keyed)",
                        "connects": f'{cam["node_id"]} clicks into the rail'})
        else:
            out.append({"n": n, "at": f'{cam["segment"]} @ {cam["mount_pos_ft"]}',
                        "type": "WAGO 221-413 x2 (power) + inline data buffer",
                        "connects": f'{cam["node_id"]} tap, power only, data passes through'})
        n += 1
    if brand == "none":
        for i, seg in enumerate(model["segments"]):
            out.append({"n": n, "at": f'{seg["id"]} corner',
                        "type": "rail-to-rail corner coupler (gasketed)",
                        "connects": "next segment"})
            n += 1
    return out


def kit_from_scan(scan: dict) -> dict:
    """The whole pipeline. This is what the quote agent, the installer
    runbook, and the AR overlay all consume."""
    SCAN_VALIDATOR.validate(scan)
    model = measured_model(scan)
    brand = scan["brand"]
    q_brand = "sightline48" if brand == "none" else brand
    cameras = camera_plan(scan, model)
    ctrl = scan.get("controller") or {}
    n_track = sum(1 for c in cameras if c["kind"] == "track")
    price = quote_engine.quote(
        roofline_ft=model["roofline_ft"], corners=model["corners"],
        eave_heights_ft=model["eave_heights_ft"], brand=q_brand,
        led_load_w_per_terminal=ctrl.get("led_load_w_per_terminal", 40.0),
        node_run_ft=min(75.0, model["roofline_ft"] / max(len(cameras), 1)),
        n_track_override=n_track)
    cuts = cut_list(model, brand)
    return {
        "schema": "sightline.kit.v1",
        "site_id": scan["site_id"],
        "model": model,
        "cameras": cameras,
        "cut_list": cuts,
        "connector_map": connector_map(model, cameras, brand),
        "power": price["power"],
        "price": {k: price[k] for k in
                  ("kit", "hardware_total", "install", "total_installed",
                   "install_time_hr", "in_sku1_band", "under_3hr_target")},
        "dori_plan": price["dori_plan"],
        "ar_overlay": ar_overlay(model, cameras, cuts),
        "all_estimates": True,
    }


def ar_overlay(model: dict, cameras: list, cuts: list) -> dict:
    """The data file the installer app's AR/photo view consumes: everything
    positioned in the scan's site frame, feet."""
    return {
        "schema": "sightline.ar.v1",
        "frame": "site-ft",
        "segments": [{"id": s["id"], "from": s["from"], "to": s["to"],
                      "labels": [c["label"] for c in cuts if c["segment"] == s["id"]]}
                     for s in model["segments"]],
        "nodes": [{"id": c["node_id"], "pos": c["mount_pos_ft"],
                   "azimuth_deg": c["aim"]["azimuth_deg"],
                   "cant_down_deg": c["aim"]["cant_down_deg"]} for c in cameras],
        "chokepoint_rings": [
            {"node": c["node_id"], "center": c["mount_pos_ft"],
             "identify_window_ft": c["aim"]["identify_window_ft"]}
            for c in cameras if c["aim"]["identify_window_ft"]],
    }


def load_sample(n: int) -> dict:
    return json.loads((Path(__file__).parent / "samples" / f"house-{n}.json").read_text())


if __name__ == "__main__":
    for i in (1, 2, 3):
        kit = kit_from_scan(load_sample(i))
        print(f'{kit["site_id"]}: {len(kit["cameras"])} nodes, '
              f'{len(kit["cut_list"])} cuts, ${kit["price"]["total_installed"]}, '
              f'{kit["price"]["install_time_hr"]} hr')
