# SightLine app prototype

Functional React prototype, mobile-first at 390px, light theme only. Talks to the correlator over websocket and REST, and to the sim for the house map and thumbnails. Nothing here is a static mock: every screen renders live data.

## Run

```bash
npm install
npm run dev        # http://localhost:5173
```

Expects the correlator on :8091 and the sim on :8090 (vite proxies `/api`, `/ws`, `/sim`). Full demo from the repo root: see README, or run the three processes yourself:

```bash
cd gateway && python3 -m uvicorn correlator.app:app --port 8091
cd sim/perimeter-sim && python3 -m perimeter_sim serve --scenario car-prowler-0214 --loop
cd app/mobile && npm run dev
```

## Screens

- **Home**: narrator's latest one-liner, live house map (open-story zones highlighted, deter segments flashing), scene chips, live node tiles, recent stories with severity rails and verified badges.
- **Verified Event**: story header with dwell, deter banner with outcome, narrative, map, re-ID entity chips (cameras seen, best DORI grade), timeline with thumbnails, police export preview, Deter now (hits the gateway), Share clip and Send to monitoring (demo stubs; monitoring send enforces the native-pixels evidence rule).
- **Ask / Scenes / Setup**: Sprint 3.

Times always render in the house's clock (the event's own UTC offset), never the viewing browser's timezone (DECISIONS.md D-016).
