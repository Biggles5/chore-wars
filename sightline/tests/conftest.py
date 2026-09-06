"""Test isolation: never let the suite talk to a live broker or correlator.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
"""
import os

# Closed ports fail instantly, keeping the suite deterministic and fast even
# when a dev has the demo stack running.
os.environ["SIGHTLINE_MQTT_HOST"] = "127.0.0.1"
os.environ["SIGHTLINE_MQTT_PORT"] = "1"
os.environ["SIGHTLINE_CORRELATOR_URL"] = "http://127.0.0.1:1"
