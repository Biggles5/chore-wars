"""Watchtower: the proactive first-30-days support loop.

Watches telemetry for the classic post-install failure modes and opens a
fix ticket with the diagnosis and the exact remedy BEFORE the homeowner
notices. Every ticket routes through the support agent's rule table so the
remedy language is one source of truth.

Failure modes covered: voltage sag at the node (rail under 9.5V: run too
long or terminal overloaded), node offline (heartbeat gap), Wi-Fi weak at
the eave (RSSI under -75), loop storage degrading.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
from __future__ import annotations

import sys
import uuid
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "agents" / "support"))
from support import triage  # noqa: E402

HEARTBEAT_GAP_S = 120.0
FIRST_30_DAYS = timedelta(days=30)


class Watchtower:
    def __init__(self, install_dates: dict = None):
        """install_dates: site_id -> ISO date; sites in their first 30 days
        get the proactive treatment (all sites still get critical tickets)."""
        self.install_dates = install_dates or {}
        self.last_seen = {}        # (site, node) -> iso ts
        self.tickets = []
        self._open_keys = set()    # dedupe: one open ticket per (node, kind)

    def _in_first_30(self, site_id: str, now_iso: str) -> bool:
        d = self.install_dates.get(site_id)
        if not d:
            return True  # unknown install date: treat as new, err proactive
        try:
            return (datetime.fromisoformat(now_iso[:19])
                    - datetime.fromisoformat(d)) <= FIRST_30_DAYS
        except ValueError:
            return True

    def _open(self, site_id: str, node_id: str, kind: str, telemetry: dict,
              text: str) -> dict:
        key = (site_id, node_id, kind)
        if key in self._open_keys:
            return None
        self._open_keys.add(key)
        tri = triage(text, telemetry)
        ticket = {
            "ticket_id": f"t-{uuid.uuid4().hex[:8]}",
            "site_id": site_id, "node_id": node_id, "kind": kind,
            "opened_by": "watchtower (proactive)",
            "severity": tri["severity"],
            "diagnosis": tri["diagnosis"],
            "remedy": tri["steps"],
            "guides": tri["guides"],
            "escalate": tri["escalate"],
            "homeowner_notified": False,
            "note": "opened before the homeowner noticed; dealer sees it in the portal",
        }
        self.tickets.append(ticket)
        return ticket

    def observe(self, telemetry: dict):
        """Feed every telemetry message here. Opens tickets as rules trip."""
        site, node = telemetry["site_id"], telemetry["node_id"]
        ts = telemetry["ts"]
        self.last_seen[(site, node)] = ts
        if not self._in_first_30(site, ts):
            return
        power = telemetry.get("power") or {}
        if power.get("rail_v", 99) < 9.5:
            self._open(site, node, "voltage_sag", telemetry,
                       "proactive: rail voltage sag detected at node")
        if telemetry.get("wifi_rssi_dbm", 0) < -75:
            self._open(site, node, "wifi_weak", telemetry,
                       "proactive: weak wifi at the eave")
        storage = telemetry.get("storage") or {}
        if storage.get("loop_hours", 72) < 48:
            self._open(site, node, "loop_degrading", telemetry,
                       "proactive: loop storage under 48h")

    def sweep_offline(self, now_iso: str):
        """Call periodically: nodes silent past the heartbeat gap get a
        ticket even though they cannot tell us themselves."""
        try:
            now = datetime.fromisoformat(now_iso[:19])
        except ValueError:
            return
        for (site, node), ts in list(self.last_seen.items()):
            try:
                gap = (now - datetime.fromisoformat(ts[:19])).total_seconds()
            except ValueError:
                continue
            if gap > HEARTBEAT_GAP_S:
                self._open(site, node, "node_offline", {},
                           "proactive: node stopped reporting")

    def open_tickets(self, site_id: str = None) -> list:
        out = self.tickets
        if site_id:
            out = [t for t in out if t["site_id"] == site_id]
        return out
