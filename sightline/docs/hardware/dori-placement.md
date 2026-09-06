# DORI placement math

The optics truth lives in code: `hardware/dori_placement.py`. This doc is the map to it, not a second copy of it.

## The model

Pixel density on a target at ground distance d: `h_px / (2 d tan(HFOV/2))`. Downward pitch to a 1.7 m face from an eave at height h: `atan((h - 1.7)/d)`. DORI thresholds (px/m): Validate 500 (2025 rev), Identify 250, Recognize 125, Observe 62.5, Detect 25. Face recognition holds to 30 degrees of pitch, degrades to unusable past 40.

## The audited anchors (pinned by tests/test_dori_placement.py)

| Setup | Identify reach | Pitch there | Verdict |
|---|---|---|---|
| 105 deg, 8MP, 6.1 m eave | 5.9 m | 37 to 42+ deg inside the ring | fails for identity |
| 60 deg, 8MP, 6.1 m eave | 13.3 m | ~19 deg | works |
| 60 deg, 12MP, 6.1 m eave | 16.0 m | ~15 deg | works, the identity channel |
| any lens, 6.1 m eave | n/a | 30 deg boundary at 7.6 m | aim window starts here |
| any lens, 3.05 m eave | n/a | benign beyond 2.4 m | 10 ft eaves are easy |

Aim window at 20 ft eaves: 7.6 to 16 m (25 to 52 ft) ground distance. The scan picks the chokepoint inside it; the factory sets the cant.

## Tools

```bash
python3 hardware/dori_placement.py --eave-ft 20 --sensor 12mp --hfov 60   # placement report
python3 hardware/dori_placement.py --eave-m 6.1 --sensor 8mp --hfov 110   # why wide fails
```

The simulator, the quote agent, and the install guides all import this module. There is no second implementation to drift.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
