#!/usr/bin/env python3
"""Push the SightLine preset pack to a WLED device.

  python3 wled_push.py <wled-ip>

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
import json
import sys
import urllib.request
from pathlib import Path

PRESETS = json.loads((Path(__file__).parent / "wled" / "presets.json").read_text())


def push(ip: str):
    for pid, preset in PRESETS.items():
        if pid.startswith("_"):
            continue
        body = dict(preset)
        body.pop("_comment", None)
        body["psave"] = int(pid)
        req = urllib.request.Request(
            f"http://{ip}/json/state", data=json.dumps(body).encode(),
            headers={"content-type": "application/json"})
        with urllib.request.urlopen(req, timeout=5) as r:
            ok = r.status == 200
        print(f"preset {pid} ({preset.get('n')}): {'ok' if ok else 'FAILED'}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    push(sys.argv[1])
