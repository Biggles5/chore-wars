"""Camera-realistic synthetic frames for simulated events.

These render like real security-camera stills: IR night imagery with
white-hot subjects, film grain, vignette, OSD overlays (node, channel,
timestamp, REC), detection bounding boxes with confidence, and daylight
color grading for daytime events. Still fully procedural SVG: deterministic,
no image libraries, tiny in git.

Evidence rule stands: every frame carries a SIMULATED stamp and
media.synthetic=true. Realism is for the demo; nothing synthetic can ever
read as evidence (gateway/schemas/README.md).

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

W, H = 320, 240


def _seed(s: str) -> int:
    return int(hashlib.sha256(s.encode()).hexdigest()[:8], 16)


def _is_night(ts: str) -> bool:
    try:
        h = int(ts[11:13])
        return h >= 20 or h < 7
    except Exception:
        return True


# ---- subject renderers: white-hot IR at night, natural tones by day ----

def _person(x, y, s, night, rng):
    """A walking human figure with pose variation, not a pictogram."""
    body = "#e8e8e6" if night else "#4a4640"
    head = "#f4f2ee" if night else "#c8a37e"
    lean = (rng % 13) - 6
    stride = 6 + (rng % 7)
    return f'''<g transform="translate({x},{y}) scale({s}) rotate({lean / 3})">
      <ellipse cx="0" cy="34" rx="14" ry="3.5" fill="#000" opacity="0.35"/>
      <path d="M-{stride} 33 L-2 16 L0 8 L2 16 L{stride - 2} 33" stroke="{body}" stroke-width="4.6" fill="none" stroke-linecap="round"/>
      <path d="M0 8 L0 -8" stroke="{body}" stroke-width="7.5" stroke-linecap="round"/>
      <path d="M-1 -2 L-8 10 M1 -2 L9 7" stroke="{body}" stroke-width="3.6" stroke-linecap="round"/>
      <circle cx="0" cy="-13" r="5.2" fill="{head}"/>
      {f'<ellipse cx="0" cy="-2" rx="9" ry="13" fill="{body}" opacity="0.28"/>' if night else ''}
    </g>'''


def _vehicle(x, y, s, night, rng):
    body = "#d8d8d4" if night else "#5a6470"
    glass = "#9aa0a2" if night else "#2c3540"
    glow = '<ellipse cx="34" cy="8" rx="7" ry="4" fill="#fff" opacity="0.9"/><ellipse cx="34" cy="8" rx="14" ry="8" fill="#fff" opacity="0.25"/>' if night else ""
    return f'''<g transform="translate({x},{y}) scale({s})">
      <ellipse cx="0" cy="16" rx="42" ry="5" fill="#000" opacity="0.4"/>
      <path d="M-38 10 Q-38 -2 -26 -4 L-14 -12 Q0 -15 14 -12 L26 -4 Q38 -2 38 10 Z" fill="{body}"/>
      <path d="M-13 -10 Q0 -13 13 -10 L20 -4 L-20 -4 Z" fill="{glass}"/>
      <circle cx="-22" cy="11" r="7" fill="#1a1a1a"/><circle cx="-22" cy="11" r="3" fill="#555"/>
      <circle cx="22" cy="11" r="7" fill="#1a1a1a"/><circle cx="22" cy="11" r="3" fill="#555"/>
      {glow}
    </g>'''


def _animal(x, y, s, night, rng):
    body = "#e0dedb" if night else "#8a6f52"
    return f'''<g transform="translate({x},{y}) scale({s})">
      <ellipse cx="0" cy="18" rx="20" ry="3" fill="#000" opacity="0.35"/>
      <ellipse cx="0" cy="0" rx="16" ry="8" fill="{body}"/>
      <path d="M-12 6 L-13 17 M-6 7 L-6 17 M6 7 L6 17 M12 6 L13 17" stroke="{body}" stroke-width="2.6" stroke-linecap="round"/>
      <path d="M14 -4 Q20 -10 21 -16 M17 -5 Q23 -8 27 -9" stroke="{body}" stroke-width="2" fill="none"/>
      <circle cx="17" cy="-8" r="4.4" fill="{body}"/>
      <circle cx="19" cy="-9" r="0.9" fill="{'#fff' if night else '#2a2018'}"/>
    </g>'''


def _package(x, y, s, night, rng):
    face = "#c9c4bb" if night else "#b08d5f"
    top = "#d8d4cc" if night else "#c4a071"
    return f'''<g transform="translate({x},{y}) scale({s})">
      <ellipse cx="0" cy="13" rx="16" ry="3" fill="#000" opacity="0.35"/>
      <path d="M-14 -2 L0 -9 L14 -2 L14 10 L-14 10 Z" fill="{face}"/>
      <path d="M-14 -2 L0 -9 L14 -2 L0 4 Z" fill="{top}"/>
      <path d="M0 4 L0 10 M-7 -5.5 L-7 7" stroke="#8a8378" stroke-width="1.6"/>
    </g>'''


_SUBJECTS = {"person": _person, "vehicle": _vehicle, "animal": _animal,
             "package": _package, "unknown": _person}


def _scene(night: bool, zone: str, rng: int) -> str:
    """Background plate: sky band, structures, ground appropriate to zone."""
    if night:
        sky, far, ground, edge = "#0b0e0c", "#161a17", "#1e231f", "#2a302b"
    else:
        sky, far, ground, edge = "#b9c6cc", "#8e9a93", "#7d8579", "#98a094"
    houses = ""
    if zone in ("street", "driveway", "front-walk"):
        # neighbor house across the way
        houses = (f'<path d="M20 96 L70 70 L120 96 L120 128 L20 128 Z" fill="{far}"/>'
                  f'<rect x="38" y="104" width="14" height="12" fill="{sky}" opacity="0.8"/>'
                  f'<rect x="86" y="104" width="14" height="12" fill="{sky}" opacity="0.8"/>')
        drive = (f'<path d="M198 128 L262 128 L{W} 200 L{W} {H} L150 {H} Z" fill="{edge}"/>'
                 f'<path d="M226 128 L232 128 L{W - 60} {H} L{W - 110} {H} Z" fill="{ground}" opacity="0.55"/>')
    elif zone in ("porch",):
        houses = (f'<rect x="0" y="40" width="86" height="{H}" fill="{far}"/>'
                  f'<rect x="70" y="60" width="16" height="150" fill="{edge}"/>'
                  f'<rect x="8" y="70" width="40" height="70" fill="{sky}" opacity="0.55"/>')
        drive = f'<rect x="0" y="176" width="{W}" height="{H - 176}" fill="{edge}"/>'
    else:  # yards
        t1 = 40 + rng % 30
        houses = (f'<ellipse cx="{t1}" cy="110" rx="26" ry="34" fill="{far}"/>'
                  f'<rect x="{t1 - 3}" y="120" width="6" height="26" fill="{edge}"/>'
                  f'<ellipse cx="{260 + rng % 30}" cy="104" rx="30" ry="40" fill="{far}"/>'
                  f'<rect x="0" y="120" width="{W}" height="4" fill="{edge}" opacity="0.7"/>')
        drive = ""
    return (f'<rect width="{W}" height="96" fill="{sky}"/>'
            f'<rect y="96" width="{W}" height="{H - 96}" fill="{ground}"/>'
            f'{houses}{drive}')


def render_thumb(event: dict) -> str:
    obj = event.get("object", {}) or {}
    geo = event.get("geometry", {}) or {}
    cls = obj.get("class", "unknown")
    zone = geo.get("zone", "driveway")
    ts = event.get("ts", "")
    night = _is_night(ts)
    rng = _seed(event.get("event_id", "") + cls)

    # subject placement: distance drives scale and height in frame
    ground = geo.get("ground_m") or 10.0
    scale = max(0.55, min(2.4, 16.0 / max(ground, 3.0)))
    sx = 96 + (rng % 130)
    sy = int(132 + min(78, ground * 4.2))
    subject = _SUBJECTS.get(cls, _person)(sx, sy, scale, night, rng)

    # bounding box around the subject
    bw, bh = int(56 * scale), int(64 * scale)
    if cls == "vehicle":
        bw, bh = int(92 * scale), int(44 * scale)
    bx, by = sx - bw // 2, sy - int(bh * 0.72)
    conf = obj.get("confidence", 0)
    level = geo.get("dori_level", "")
    box_color = "#ff5f52" if cls == "person" else "#ffb454" if cls == "vehicle" else "#7fd08f"

    clock = ts[11:19] if len(ts) > 19 else ts
    date = ts[:10]
    node = event.get("node_id", "")
    channel = geo.get("channel", "wide").upper()
    pxm = geo.get("px_per_m", "")
    ir_badge = ('<circle cx="271" cy="17" r="3.5" fill="#c33"/>'
                '<text x="279" y="21" font-size="10" fill="#ddd">REC</text>'
                '<text x="236" y="21" font-size="10" fill="#9fd39f">IR</text>') if night else (
                '<circle cx="271" cy="17" r="3.5" fill="#c33"/>'
                '<text x="279" y="21" font-size="10" fill="#fff">REC</text>')
    grade = (f'<rect x="8" y="{H - 26}" width="{112 if level else 0}" height="18" rx="3" fill="#000" opacity="0.55"/>'
             f'<text x="14" y="{H - 13}" font-size="10" fill="#fff">{level.upper()} {pxm} px/m</text>') if level else ""
    mono = (f'<filter id="ir"><feColorMatrix type="matrix" '
            f'values="0.32 0.55 0.13 0 0.02  0.36 0.6 0.14 0 0.03  0.33 0.56 0.13 0 0.02  0 0 0 1 0"/></filter>') if night else "<filter id='ir'/>"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  {mono}
  <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="{rng % 97}" stitchTiles="stitch"/><feColorMatrix type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 {0.16 if night else 0.05} 0"/></filter>
  <radialGradient id="vig" cx="50%" cy="46%" r="72%">
    <stop offset="62%" stop-color="#000" stop-opacity="0"/>
    <stop offset="100%" stop-color="#000" stop-opacity="{0.55 if night else 0.28}"/>
  </radialGradient>
  <radialGradient id="irbeam" cx="50%" cy="40%" r="60%">
    <stop offset="0%" stop-color="#fff" stop-opacity="{0.10 if night else 0}"/>
    <stop offset="100%" stop-color="#fff" stop-opacity="0"/>
  </radialGradient>
</defs>
<g filter="url(#ir)">
  {_scene(night, zone, rng)}
  <rect width="{W}" height="{H}" fill="url(#irbeam)"/>
  {subject}
</g>
<rect width="{W}" height="{H}" filter="url(#grain)"/>
<rect width="{W}" height="{H}" fill="url(#vig)"/>
<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="none" stroke="{box_color}" stroke-width="1.6" opacity="0.95"/>
<rect x="{bx}" y="{by - 14}" width="{max(58, bw)}" height="13" fill="{box_color}" opacity="0.9"/>
<text x="{bx + 3}" y="{by - 4}" font-family="monospace" font-size="9" fill="#111">{cls} {int(conf * 100) if conf else ""}%</text>
<rect x="0" y="0" width="{W}" height="26" fill="#000" opacity="0.45"/>
<text x="8" y="17" font-family="monospace" font-size="11" fill="#fff">{node} · {channel}</text>
{ir_badge}
<rect x="0" y="{H - 22}" width="{W}" height="22" fill="#000" opacity="0.0"/>
<text x="{W - 8}" y="{H - 8}" font-family="monospace" font-size="11" fill="#fff" text-anchor="end" opacity="0.95">{date} {clock}</text>
{grade}
<text x="{W - 8}" y="17" font-family="monospace" font-size="9" fill="#ff8f86" text-anchor="end" opacity="0.0">.</text>
<g opacity="0.5"><text x="{W / 2}" y="{H / 2 + 4}" font-family="monospace" font-size="13" fill="#fff" text-anchor="middle" transform="rotate(-18 {W / 2} {H / 2})" letter-spacing="4">SIMULATED</text></g>
</svg>'''


def write_thumb(run_dir: Path, event: dict) -> str:
    thumbs = Path(run_dir) / "thumbs"
    thumbs.mkdir(parents=True, exist_ok=True)
    name = f'{event["event_id"][:8]}.svg'
    (thumbs / name).write_text(render_thumb(event))
    return f"thumbs/{name}"
