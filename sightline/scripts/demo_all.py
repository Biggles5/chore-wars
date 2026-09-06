#!/usr/bin/env python3
"""Boot the whole SightLine demo: correlator + simulator + app, one command.

  python3 scripts/demo_all.py [scenario]      (default car-prowler-0214)

Starts the correlator on :8091, the sim (looping) on :8090, and the app dev
server on :5173 (if npm and app/mobile/node_modules exist; run `make app`
once first, or it falls back to serving the built dist if present).
Ctrl-C tears everything down.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
import shutil
import signal
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENARIO = sys.argv[1] if len(sys.argv) > 1 else "car-prowler-0214"
PROCS = []


def spawn(name, cmd, cwd):
    p = subprocess.Popen(cmd, cwd=str(cwd))
    PROCS.append((name, p))
    return p


def wait_http(url, timeout_s=30):
    t0 = time.time()
    while time.time() - t0 < timeout_s:
        try:
            with urllib.request.urlopen(url, timeout=1) as r:
                if r.status == 200:
                    return True
        except Exception:
            time.sleep(0.5)
    return False


def shutdown(*_):
    print("\nshutting down")
    for name, p in PROCS:
        p.terminate()
    for name, p in PROCS:
        try:
            p.wait(timeout=5)
        except subprocess.TimeoutExpired:
            p.kill()
    sys.exit(0)


def ports_free():
    import socket
    busy = []
    for port in (8090, 8091, 5173):
        s = socket.socket()
        try:
            s.bind(("127.0.0.1", port))
        except OSError:
            busy.append(port)
        finally:
            s.close()
    return busy


def main():
    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    busy = ports_free()
    if busy:
        print(f"ports already in use: {busy}. Stop the other demo first "
              f"(or: pkill -f 'uvicorn correlator.app'; pkill -f 'perimeter_sim serve').")
        sys.exit(1)

    spawn("correlator", [sys.executable, "-m", "uvicorn", "correlator.app:app",
                         "--port", "8091", "--log-level", "warning"], ROOT / "gateway")
    if not wait_http("http://localhost:8091/health"):
        print("correlator failed to start"); shutdown()
    print("correlator  http://localhost:8091  up")

    spawn("sim", [sys.executable, "-m", "perimeter_sim", "serve",
                  "--scenario", SCENARIO, "--loop"], ROOT / "sim" / "perimeter-sim")
    if not wait_http("http://localhost:8090/site"):
        print("sim failed to start"); shutdown()
    print(f"sim view    http://localhost:8090  up ({SCENARIO}, looping)")

    app_dir = ROOT / "app" / "mobile"
    npm = shutil.which("npm")
    if npm and (app_dir / "node_modules").exists():
        spawn("app", [npm, "run", "dev", "--silent"], app_dir)
        wait_http("http://localhost:5173", 20)
        print("app         http://localhost:5173  up")
    elif npm:
        print("app: node_modules missing, running npm install first (one time)")
        subprocess.run([npm, "install", "--no-fund", "--no-audit"], cwd=str(app_dir), check=True)
        spawn("app", [npm, "run", "dev", "--silent"], app_dir)
        wait_http("http://localhost:5173", 20)
        print("app         http://localhost:5173  up")
    else:
        print("app: npm not found, skipping (sim view still shows the demo)")

    print("\nSightLine demo running. Open the app, watch the story assemble.")
    print("Ctrl-C to stop.")
    while True:
        time.sleep(1)
        for name, p in PROCS:
            if p.poll() is not None:
                print(f"{name} exited unexpectedly ({p.returncode})")
                shutdown()


if __name__ == "__main__":
    main()
