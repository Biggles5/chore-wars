# SightLine build and demo entry points.
# Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.

PY ?= python3
SCENARIO ?= quiet-night
SIM_DIR = sim/perimeter-sim

.PHONY: setup demo sim sim-headless correlator app gateway gateway-down test clean

correlator:
	cd gateway && $(PY) -m uvicorn correlator.app:app --port 8091

app:
	cd app/mobile && npm install --no-fund --no-audit && npm run dev

setup:
	$(PY) -m pip install -q fastapi uvicorn paho-mqtt jsonschema pytest

demo:
	@echo "SightLine demo: quiet-night scenario, live view at http://localhost:8090"
	cd $(SIM_DIR) && $(PY) -m perimeter_sim serve --scenario quiet-night

sim:
	@echo "SightLine sim: $(SCENARIO), live view at http://localhost:8090"
	cd $(SIM_DIR) && $(PY) -m perimeter_sim serve --scenario $(SCENARIO)

sim-headless:
	cd $(SIM_DIR) && $(PY) -m perimeter_sim run $(SCENARIO)

gateway:
	cd gateway && docker compose up -d

gateway-down:
	cd gateway && docker compose down

test:
	$(PY) -m pytest tests/ -q

clean:
	rm -rf $(SIM_DIR)/runs
	find . -name __pycache__ -type d -exec rm -rf {} + 2>/dev/null || true
