# SightLine gateway

The house brain: MQTT broker, Frigate, the SightLine correlator, and Home Assistant.

## Boot (requires Docker)

```bash
docker compose up -d
```

- mosquitto on :1883 (the simulator auto-publishes here when it is up)
- correlator on :8091 (`/health`, `/events`, `/telemetry`, `/ingest`, `/stories`)
- Frigate on :5000 (idle with the sim; real cameras enable in `frigate/config.yml`)
- Home Assistant on :8123 (SightLine package preloaded; point its MQTT integration at host `mosquitto`)

## Without Docker

The correlator runs standalone:

```bash
cd gateway && python3 -m uvicorn correlator.app:app --port 8091
```

It retries MQTT in the background and always accepts REST ingest at `POST /ingest` with the same schema validation as the bus path.

## Sprint status

Sprint 1: broker + skeleton correlator (ingest, validate, buffer, query). Sprint 2 adds tracks, cross-camera re-ID (interface already declared in `correlator/app.py`), Event Story assembly, the deter trigger via HA, and the app websocket. The Matter bridge design doc lands with `docs/architecture/` in Sprint 4.
