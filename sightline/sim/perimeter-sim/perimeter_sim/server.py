"""Live web view server for the simulator.

Serves the top-down canvas view, a Server-Sent Events stream of state
snapshots and events, and the run's thumbnails. This same view embeds in
website/demo.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import json
import queue
import threading
import time
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

WEB_DIR = Path(__file__).resolve().parents[1] / "web"
MAX_SIM_STEP = 0.5  # never integrate more than this much sim time at once


class Broadcaster:
    def __init__(self):
        self._clients = []
        self._lock = threading.Lock()

    def subscribe(self) -> queue.Queue:
        q = queue.Queue(maxsize=500)
        with self._lock:
            self._clients.append(q)
        return q

    def unsubscribe(self, q):
        with self._lock:
            if q in self._clients:
                self._clients.remove(q)

    def push(self, msg: dict):
        with self._lock:
            clients = list(self._clients)
        for q in clients:
            try:
                q.put_nowait(msg)
            except queue.Full:
                pass


def site_payload(house, scenario) -> dict:
    return {
        "site_id": house.site_id,
        "name": house.name,
        "scenario": {"name": scenario.name, "description": scenario.description,
                     "start_clock": scenario.start_clock, "armed": scenario.armed,
                     "timescale": scenario.timescale},
        "footprint": house.footprint,
        "eave_m": house.eave_m,
        "segments": house.segments,
        "zones": house.zones,
        "nodes": [
            {
                "id": n.id, "kind": n.kind, "pos": list(n.pos),
                "facing_deg": n.facing_deg,
                "channels": [
                    {"name": c.name, "sensor": c.sensor, "hfov_deg": c.hfov_deg,
                     "boresight_deg": c.boresight_deg, "rings": c.rings_ground_m}
                    for c in n.channels
                ],
                "deter_segments": n.deter_segments,
            }
            for n in house.nodes
        ],
    }


def make_app(engine_factory, house, scenario, run_dir: Path, loop: bool = False) -> FastAPI:
    """engine_factory() returns a fresh Engine wired to the bus. The pacing
    thread drives it; with loop=True the scenario restarts when done."""
    app = FastAPI(title="SightLine perimeter sim")
    bcast = Broadcaster()
    state = {"engine": engine_factory()}
    state["engine"].bus.add_listener(
        lambda topic, payload: bcast.push({"kind": "event", "topic": topic,
                                           "payload": payload}))

    def pace():
        last = time.monotonic()
        next_snap = 0.0
        while True:
            now = time.monotonic()
            wall_dt = min(now - last, 0.25)
            last = now
            eng = state["engine"]
            sim_dt = wall_dt * eng.scn.timescale
            while sim_dt > 0 and not eng.done:
                step = min(sim_dt, MAX_SIM_STEP)
                eng.tick(step)
                sim_dt -= step
            if now >= next_snap:
                bcast.push(eng.snapshot())
                next_snap = now + 0.1
            if eng.done and loop:
                time.sleep(2.0)
                state["engine"] = engine_factory()
                state["engine"].bus.add_listener(
                    lambda topic, payload: bcast.push({"kind": "event", "topic": topic,
                                                       "payload": payload}))
                last = time.monotonic()
            time.sleep(0.05)

    threading.Thread(target=pace, daemon=True).start()

    @app.get("/")
    def index():
        return FileResponse(WEB_DIR / "index.html")

    @app.get("/site")
    def site():
        return JSONResponse(site_payload(house, scenario))

    @app.get("/events")
    def events():
        return JSONResponse(state["engine"].recent)

    @app.get("/stream")
    def stream():
        q = bcast.subscribe()

        def gen():
            try:
                yield f"data: {json.dumps(state['engine'].snapshot())}\n\n"
                while True:
                    try:
                        msg = q.get(timeout=15)
                        yield f"data: {json.dumps(msg)}\n\n"
                    except queue.Empty:
                        yield ": keepalive\n\n"
            finally:
                bcast.unsubscribe(q)

        return StreamingResponse(gen(), media_type="text/event-stream")

    app.mount("/run", StaticFiles(directory=str(run_dir)), name="run")
    return app
