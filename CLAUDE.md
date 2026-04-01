# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Chore Wars is a single-file family chore tracking web app gamified for kids. It runs entirely from `index.html` (~1250 lines) — there is no build system, bundler, or server. Just open the file in a browser.

## Architecture

**Single-file app** (`index.html`) containing:
- Inline CSS styles in `<style>` block — minified, class-based utility styles with animations (`confFall`, `float`, `glow`, `fadeIn`)
- Firebase REST API (direct fetch to Realtime Database, no SDK scripts)
- React 18 + ReactDOM + Babel standalone loaded via CDN — JSX is transpiled in-browser
- Embedded base64 avatar images and SVG assets as `data:` URIs in a `<script>` block
- Sound effects engine (`SFX` object) using Web Audio API — plays tones for submit, approve, reject, habit, challenge, perfect, vote, coin events
- All application logic in a single `<script type="text/babel">` block

**Data layer** (`D` object): Abstraction over Firebase Realtime Database REST API with localStorage fallback. Methods: `set(path, val)`, `get(path)`, `on(path, cb)` (polling-based listener at 3s intervals). Firebase URL is hardcoded; `fbReady` flag controls whether Firebase or localStorage is used. localStorage keys are prefixed with `cw_`.

**Helper functions** for Firebase data normalization: `toArr(v)` converts Firebase objects back to arrays, `fixFam`, `fixHab`, `fixCfg` ensure correct data shapes after Firebase round-trips (Firebase converts arrays with gaps to objects).

**State structure (Firebase paths / localStorage keys):**
- `weeks/<weekKey>` — per-member, per-day chore/habit/bonus completion data
- `history` — lifetime earnings, weekly winners, activity feed, chat, challenges, extra chores, votes
- `config` — points values, allowance amounts, PIN, trip goal thresholds, monthly activities, weekly rewards
- `family` — array of family members (id, name, emoji, avatar, color, chores, group, title, pin)
- `habits` — array of trackable daily habits

**Components:**
- `ErrWrap` — React error boundary, prevents blank screen on crashes
- `Av` — Avatar component, renders base64 image or emoji fallback
- `RaceTimer` — Live countdown/stopwatch for challenge races
- `App` (line 217) — main component with all views, state, save helpers (`sW`, `sH`, `sC`, `sF`, `sHb`), scoring, and action handlers
- `MyDay` (line 1118) — child component for daily chore/habit tracking view with photo submission and parent approval workflow

**Views/routing** — `view` state switches between: `dash` (leaderboard/standings), `play` (My Day chores), `battle` (challenges), `earn` (allowance/earnings), `chat` (family chat), `quest` (streaks/badges/trip goals), `settings` (parent-only admin)

**Authentication** — Two-tier PIN system: parent PIN (`cfg.pin`) unlocks admin/settings mode; per-kid PINs (`member.pin`) for kid login. Lockout after 3 failed attempts (15 min). `me` state holds current user ID or `"_parent"`.

**Chore approval workflow** — Kids submit chores with photo proof (`status: "pending"`), parents approve/reject with optional rejection reason. Statuses: `none` → `pending` → `approved`/`rejected`. Rejected chores can be resubmitted.

**Scoring system:**
- `dP(mid, di)` — day points: chore completions × `cfg.chorePts` + habit points + daily bonus points
- `wP(mid)` — week points: sum of all day points + YM/YW weekly bonus. If all 6 days' chores are done, total multiplied by `cfg.multi`
- `cD(mid)` — count of complete days (all chores done)
- `skF(mid)` — current streak (consecutive complete days from today backwards)

**Key conventions:**
- Extremely terse variable names throughout (e.g., `sW` = save week, `sH` = save history, `wP` = week points, `dP` = day points, `cfg` = config, `FM` = family members, `HB` = habits)
- Default data constants: `DEF_FAM`, `DEF_HAB`, `DEF_CFG`, `BON` (bonuses), `LVS` (levels), `BGS` (badges), `CHALL` (challenge ideas), `RX` (reactions), `DAYS`
- Week key (`wkKey()`) is ISO date of Monday; day index (`dayI()`) is 0=Mon through 6=Sun (Sunday is day off, no chores)
- State mutations use deep clone via `JSON.parse(JSON.stringify(...))` then save to both React state and DB
- Real-time sync via polling (3s) when Firebase is active; localStorage mode has no live updates
- Historical week browsing via `histOff` (offset from current week) and `getOffWk()`

## Critical Syntax Rules

This app uses Babel Standalone 7.23.9 in-browser transpilation. The following constraints are **mandatory** for all code written in this project:

- **No arrow functions** — use `function(){}` everywhere
- **No `async`/`await`** — use `fetch().then()` chains
- **No optional chaining** (`?.`) — check each level explicitly
- **No `const` or `let`** — use `var` for all declarations
- **Firebase REST API only** — all DB calls go through `fetch` with `.then()` pattern via the `D` object
- **Always `toArr()` on Firebase data** before using array methods (`.map`, `.filter`, `.forEach`, etc.) — Firebase converts arrays with gaps to objects
- **Avatars via `injectAv()`** — base64 avatar strings are not stored in Firebase; `injectAv` must be called on family data every time it is loaded

## Development

No build, lint, or test commands. To develop:
1. Edit `index.html`
2. Open/refresh in browser
3. Firebase REST URL is at line 50 (`var FB=...`) — the app works offline with localStorage when `fbReady` is set to `false`
