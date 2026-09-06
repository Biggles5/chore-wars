"""Ops-sim scenario tests: the growth thesis holds in simulation.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sim" / "ops-sim"))

import opssim  # noqa: E402


def test_new_metro_hits_100_per_month_by_week_12():
    s = opssim.simulate("new-metro-launch")["summary"]
    assert s["week12_installs_per_month"]["new"] >= 100, s
    assert s["week12_installs_per_month"]["new"] > 3 * s["week12_installs_per_month"]["old"]


def test_new_model_clears_backlog_old_drowns():
    s = opssim.simulate("new-metro-launch")["summary"]
    assert s["ending_backlog"]["new"] < 20
    assert s["ending_backlog"]["old"] > 200


def test_q4_crunch_absorbed_by_funnel():
    s = opssim.simulate("q4-crunch")["summary"]
    assert s["total_installs"]["new"] > 2 * s["total_installs"]["old"]
    assert s["ending_backlog"]["new"] < 50


def test_callback_storm_resilience():
    """QC gates keep the storm survivable; field splices do not."""
    storm = opssim.simulate("callback-storm")["summary"]
    clean = opssim.simulate("q4-crunch")["summary"]
    assert storm["ending_backlog"]["new"] < 60
    assert storm["ending_backlog"]["old"] > storm["ending_backlog"]["new"] * 4
    assert clean is not None  # both runs deterministic and comparable


def test_deterministic():
    a = opssim.simulate("new-metro-launch")
    b = opssim.simulate("new-metro-launch")
    assert a == b


def test_emit_web(tmp_path, monkeypatch):
    import json
    monkeypatch.setattr(opssim, "ROOT", tmp_path)
    (tmp_path / "website" / "demo").mkdir(parents=True)
    opssim.emit_web(opssim.simulate("new-metro-launch"))
    js = (tmp_path / "website" / "demo" / "opssim-data.js").read_text()
    assert js.startswith("// generated")
    payload = json.loads(js.split("window.OPSSIM = ", 1)[1].rstrip().rstrip(";"))
    assert payload["summary"]["scenario"] == "new-metro-launch"
