"""Generate QC fixture photos: 5 per check (3 pass, 2 fail), synthetic
renders styled like installer phone photos, each carrying the qc-metadata
measurement block the mock vision layer reads.

  python3 make_fixtures.py     writes fixtures/<check>-<n>-<pass|fail>.svg

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).parent / "fixtures"
W, H = 320, 240


def _frame(inner: str, meta: dict, label: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<metadata id="qc">{json.dumps(meta)}</metadata>
<defs><filter id="g"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2"/>
<feColorMatrix values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0.05 0"/></filter>
<radialGradient id="v" cx="50%" cy="45%" r="75%"><stop offset="70%" stop-color="#000" stop-opacity="0"/>
<stop offset="100%" stop-color="#000" stop-opacity="0.3"/></radialGradient></defs>
<rect width="{W}" height="{H}" fill="#8d9297"/>
{inner}
<rect width="{W}" height="{H}" filter="url(#g)"/><rect width="{W}" height="{H}" fill="url(#v)"/>
<rect y="{H - 20}" width="{W}" height="20" fill="#000" opacity="0.45"/>
<text x="6" y="{H - 6}" font-family="monospace" font-size="10" fill="#fff">{label} · SIMULATED FIXTURE</text>
</svg>'''


def rail(tilt, var):
    y = 90
    mods = "".join(
        f'<rect x="{34 + i * (36 + (var / 3 if i % 2 else -var / 3))}" y="{y - 6}" width="9" height="13" rx="3" fill="#e8e4da"/>'
        for i in range(7))
    return (f'<rect y="40" width="{W}" height="70" fill="#b9bcb6"/>'
            f'<rect y="110" width="{W}" height="130" fill="#6f7a70"/>'
            f'<g transform="rotate({tilt} {W / 2} {y})">'
            f'<rect x="20" y="{y - 4}" width="280" height="9" fill="#3c4045"/>{mods}</g>'
            f'<line x1="20" y1="{y + 26}" x2="300" y2="{y + 26}" stroke="#d8524a" stroke-dasharray="6 4" stroke-width="1.6"/>')


def gasket(gap):
    return (f'<rect x="70" y="50" width="180" height="130" rx="14" fill="#2e3338"/>'
            f'<rect x="82" y="62" width="156" height="106" rx="10" fill="#3b4148"/>'
            f'<rect x="82" y="{62 + 50}" width="156" height="{max(gap * 6, 0.5)}" fill="#0c0e10"/>'
            f'<ellipse cx="160" cy="115" rx="60" ry="40" fill="#454c54"/>'
            f'<circle cx="160" cy="115" r="26" fill="#14171a"/><circle cx="152" cy="107" r="7" fill="#5a646e" opacity="0.7"/>')


def connector(latched, exposed):
    latch = "#3f8f5a" if latched else "#c2453f"
    copper = f'<rect x="196" y="118" width="{exposed * 7}" height="5" fill="#c98a3d"/>' if exposed > 0 else ""
    return (f'<rect y="140" width="{W}" height="100" fill="#5d6660"/>'
            f'<rect x="60" y="100" width="140" height="44" rx="8" fill="#e8e4da"/>'
            f'<rect x="70" y="110" width="26" height="24" rx="4" fill="{latch}"/>'
            f'<rect x="104" y="110" width="26" height="24" rx="4" fill="#3f8f5a"/>'
            f'<path d="M20 122 h40 M200 122 h80" stroke="#20242a" stroke-width="7"/>{copper}')


def aim(az_err, cant_err):
    return (f'<rect width="{W}" height="{H}" fill="#1b2434"/>'
            f'<circle cx="{W / 2}" cy="110" r="56" fill="none" stroke="#1d7fb0" stroke-width="2" stroke-dasharray="8 5"/>'
            f'<circle cx="{W / 2 + az_err * 6}" cy="{110 + cant_err * 8}" r="10" fill="none" stroke="#c07a10" stroke-width="3"/>'
            f'<line x1="{W / 2 + az_err * 6 - 18}" y1="{110 + cant_err * 8}" x2="{W / 2 + az_err * 6 + 18}" y2="{110 + cant_err * 8}" stroke="#c07a10"/>'
            f'<line x1="{W / 2 + az_err * 6}" y1="{110 + cant_err * 8 - 18}" x2="{W / 2 + az_err * 6}" y2="{110 + cant_err * 8 + 18}" stroke="#c07a10"/>'
            f'<text x="12" y="24" font-family="monospace" font-size="11" fill="#faf9f5">AIM VIEW · node-drive-mouth</text>')


def wiring(meter_v, relief):
    clamp = '<rect x="196" y="150" width="30" height="12" rx="3" fill="#3c4045"/>' if relief else ""
    return (f'<rect x="40" y="40" width="150" height="160" rx="8" fill="#d8d4cc"/>'
            f'<rect x="56" y="60" width="118" height="40" fill="#2e3338"/>'
            + "".join(f'<circle cx="{70 + i * 26}" cy="80" r="6" fill="#c0c4c8"/>' for i in range(4))
            + f'<path d="M190 156 q40 -10 90 -6" stroke="#20242a" stroke-width="6" fill="none"/>{clamp}'
            f'<rect x="210" y="60" width="84" height="56" rx="8" fill="#1b1e22"/>'
            f'<text x="222" y="94" font-family="monospace" font-size="20" fill="#7fd08f">{meter_v:.1f}V</text>')


CASES = {
    "rail_level_spacing": [
        (rail(0.4, 3), {"tilt_deg": 0.4, "spacing_var_pct": 3.0}, True),
        (rail(1.0, 5), {"tilt_deg": 1.0, "spacing_var_pct": 5.0}, True),
        (rail(1.4, 7.5), {"tilt_deg": 1.4, "spacing_var_pct": 7.5}, True),
        (rail(3.2, 4), {"tilt_deg": 3.2, "spacing_var_pct": 4.0}, False),
        (rail(0.6, 14), {"tilt_deg": 0.6, "spacing_var_pct": 14.0}, False),
    ],
    "gasket_seated": [
        (gasket(0.0), {"gap_mm": 0.0}, True),
        (gasket(0.2), {"gap_mm": 0.2}, True),
        (gasket(0.4), {"gap_mm": 0.4}, True),
        (gasket(1.2), {"gap_mm": 1.2}, False),
        (gasket(2.5), {"gap_mm": 2.5}, False),
    ],
    "connector_clicked": [
        (connector(True, 0), {"latch_engaged": True, "conductor_exposed_mm": 0.0}, True),
        (connector(True, 0.5), {"latch_engaged": True, "conductor_exposed_mm": 0.5}, True),
        (connector(True, 0.9), {"latch_engaged": True, "conductor_exposed_mm": 0.9}, True),
        (connector(False, 0), {"latch_engaged": False, "conductor_exposed_mm": 0.0}, False),
        (connector(True, 3.0), {"latch_engaged": True, "conductor_exposed_mm": 3.0}, False),
    ],
    "node_aim": [
        (aim(0.5, 0.3), {"azimuth_err_deg": 0.5, "cant_err_deg": 0.3}, True),
        (aim(2.0, 1.0), {"azimuth_err_deg": 2.0, "cant_err_deg": 1.0}, True),
        (aim(4.5, 1.8), {"azimuth_err_deg": 4.5, "cant_err_deg": 1.8}, True),
        (aim(9.0, 1.0), {"azimuth_err_deg": 9.0, "cant_err_deg": 1.0}, False),
        (aim(2.0, 4.0), {"azimuth_err_deg": 2.0, "cant_err_deg": 4.0}, False),
    ],
    "controller_wiring": [
        (wiring(0.0, True), {"meter_v": 0.0, "strain_relief": True}, True),
        (wiring(0.1, True), {"meter_v": 0.1, "strain_relief": True}, True),
        (wiring(0.3, True), {"meter_v": 0.3, "strain_relief": True}, True),
        (wiring(12.1, True), {"meter_v": 12.1, "strain_relief": True}, False),
        (wiring(0.0, False), {"meter_v": 0.0, "strain_relief": False}, False),
    ],
}


def main():
    OUT.mkdir(exist_ok=True)
    manifest = []
    for check, cases in CASES.items():
        for i, (inner, meta, expected) in enumerate(cases, 1):
            meta = dict(meta, check=check)
            tag = "pass" if expected else "fail"
            name = f"{check}-{i}-{tag}.svg"
            (OUT / name).write_text(_frame(inner, meta, f"{check} #{i}"))
            manifest.append({"file": name, "check": check, "expected_pass": expected})
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2))
    print(f"wrote {len(manifest)} fixtures + manifest")


if __name__ == "__main__":
    main()
