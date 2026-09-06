"""CLI for the perimeter simulator.

  python -m perimeter_sim run <scenario>            headless, fast as possible
  python -m perimeter_sim serve --scenario <name>   live view at :8090
  python -m perimeter_sim list                      list scenarios

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import argparse
import copy
import time
from pathlib import Path

from .bus import Bus
from .engine import Engine
from .model import load_house
from .scenarios import SCENARIOS

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCAN = ROOT / "scans" / "demo-house.json"


def _run_dir(scenario: str) -> Path:
    stamp = time.strftime("%Y%m%d-%H%M%S")
    return ROOT / "runs" / f"{scenario}-{stamp}"


def cmd_run(args):
    scn = SCENARIOS[args.scenario]
    house = load_house(args.house)
    run_dir = _run_dir(scn.name)
    bus = Bus(run_dir)
    eng = Engine(scn, house, bus, run_dir)
    t0 = time.monotonic()
    eng.run_headless()
    wall = time.monotonic() - t0
    bus.close()
    print(f"scenario     {scn.name}")
    print(f"sim time     {scn.duration_s:.0f} s ({scn.start_clock} start)")
    print(f"wall time    {wall:.2f} s (headless)")
    print(f"bus          {bus.mqtt_status}")
    print(f"published    {bus.published} messages, all schema-valid")
    for etype in sorted(eng.counts):
        print(f"  {etype:<18} {eng.counts[etype]}")
    print(f"run dir      {run_dir}")


def cmd_serve(args):
    import uvicorn
    from .server import make_app

    scn = SCENARIOS[args.scenario]
    house = load_house(args.house)
    run_dir = _run_dir(scn.name)
    run_dir.mkdir(parents=True, exist_ok=True)
    bus = Bus(run_dir)

    def factory():
        return Engine(copy.deepcopy(scn), house, bus, run_dir)

    app = make_app(factory, house, scn, run_dir, loop=args.loop)
    print(f"SightLine sim: {scn.name} at {scn.start_clock}, "
          f"timescale {scn.timescale}x, view http://localhost:{args.port}")
    print(f"bus: {bus.mqtt_status}")
    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="warning")


def cmd_list(_args):
    for name, scn in SCENARIOS.items():
        print(f"{name:<20} {scn.start_clock}  {scn.description}")


def main():
    ap = argparse.ArgumentParser(prog="perimeter_sim")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_run = sub.add_parser("run", help="headless run, writes events.jsonl")
    p_run.add_argument("scenario", choices=sorted(SCENARIOS))
    p_run.add_argument("--house", default=str(DEFAULT_SCAN))
    p_run.set_defaults(fn=cmd_run)

    p_srv = sub.add_parser("serve", help="live view server")
    p_srv.add_argument("--scenario", default="quiet-night", choices=sorted(SCENARIOS))
    p_srv.add_argument("--house", default=str(DEFAULT_SCAN))
    p_srv.add_argument("--port", type=int, default=8090)
    p_srv.add_argument("--loop", action="store_true",
                       help="restart the scenario when it finishes")
    p_srv.set_defaults(fn=cmd_serve)

    p_ls = sub.add_parser("list", help="list scenarios")
    p_ls.set_defaults(fn=cmd_list)

    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
