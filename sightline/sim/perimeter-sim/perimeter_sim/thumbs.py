"""Procedural SVG thumbnails for simulated events.

Deterministic, no image libraries, tiny. Every thumbnail is stamped
SIMULATED so synthetic frames can never be mistaken for evidence
(see gateway/schemas/README.md, evidence rule).

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

from pathlib import Path

PAPER = "#FAF9F5"
INK = "#1B2434"
AMBER = "#C07A10"
BLUE = "#1D7FB0"
GREEN = "#1E8A63"
RED = "#C24545"

_SILHOUETTES = {
    "person": ('<circle cx="80" cy="34" r="11" fill="{c}"/>'
               '<rect x="68" y="46" width="24" height="34" rx="8" fill="{c}"/>'
               '<rect x="70" y="80" width="8" height="22" fill="{c}"/>'
               '<rect x="82" y="80" width="8" height="22" fill="{c}"/>'),
    "vehicle": ('<rect x="40" y="58" width="80" height="24" rx="8" fill="{c}"/>'
                '<rect x="56" y="44" width="48" height="18" rx="6" fill="{c}"/>'
                '<circle cx="60" cy="86" r="8" fill="{ink}"/>'
                '<circle cx="100" cy="86" r="8" fill="{ink}"/>'),
    "animal": ('<ellipse cx="80" cy="66" rx="26" ry="13" fill="{c}"/>'
               '<circle cx="104" cy="52" r="8" fill="{c}"/>'
               '<rect x="62" y="76" width="5" height="18" fill="{c}"/>'
               '<rect x="92" y="76" width="5" height="18" fill="{c}"/>'
               '<path d="M106 46 l5 -10 M110 48 l8 -7" stroke="{c}" stroke-width="3"/>'),
    "package": ('<rect x="58" y="52" width="44" height="34" rx="3" fill="{c}"/>'
                '<path d="M58 66 h44 M80 52 v34" stroke="{paper}" stroke-width="3"/>'),
    "unknown": '<circle cx="80" cy="62" r="24" fill="{c}"/>',
}

_CLASS_COLOR = {"person": RED, "vehicle": AMBER, "animal": GREEN,
                "package": BLUE, "unknown": INK}


def render_thumb(event: dict) -> str:
    obj = event.get("object", {}) or {}
    geo = event.get("geometry", {}) or {}
    cls = obj.get("class", "unknown")
    color = _CLASS_COLOR.get(cls, INK)
    sil = _SILHOUETTES.get(cls, _SILHOUETTES["unknown"]).format(
        c=color, ink=INK, paper=PAPER)
    label = f'{cls} {geo.get("dori_level", "")} {geo.get("px_per_m", "")} px/m'
    ts = event.get("ts", "")[11:19]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="160" height="120" viewBox="0 0 160 120">
<rect width="160" height="120" fill="{INK}"/>
<rect x="4" y="4" width="152" height="112" fill="none" stroke="{AMBER}" stroke-width="1" opacity="0.5"/>
{sil}
<text x="8" y="16" font-family="monospace" font-size="9" fill="{PAPER}">{event.get("node_id", "")} {ts}</text>
<text x="8" y="112" font-family="monospace" font-size="9" fill="{PAPER}">{label}</text>
<text x="118" y="16" font-family="monospace" font-size="9" fill="{RED}">SIMULATED</text>
</svg>'''


def write_thumb(run_dir: Path, event: dict) -> str:
    thumbs = Path(run_dir) / "thumbs"
    thumbs.mkdir(parents=True, exist_ok=True)
    name = f'{event["event_id"][:8]}.svg'
    (thumbs / name).write_text(render_thumb(event))
    return f"thumbs/{name}"
