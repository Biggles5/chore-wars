# Homeowner Setup Guide

What you do in the SightLine app from first open to a fully armed house. No tools required for any of it except the self-install path.

## 1. Onboarding (Setup tab)

1. Open the app, create your owner account, tap Setup.
2. Enter your roofline: total linear feet, number of corners, eave heights, and your lighting brand (Gemstone, Trimlight, JellyFish, or SightLine 48V rail).
3. A quote appears immediately. SKU 1 runs $1,299 to $1,799 installed (est.).
4. Pick a path:
   - Installer: a dealer schedules the visit and does everything in about 3 hours on the 48V system.
   - Self-install: the app walks you through the retrofit guide steps. Comfortable-with-a-ladder territory, all low voltage, never mains.

## 2. Privacy masks (mandatory, not skippable)

Setup will not complete until masks are set. This is by design.

- Walk each camera view with the installer (or with the app's mask editor on self-install). Look at what each camera actually sees.
- Mask every neighbor window and every neighbor yard. Masked areas are blacked out before any pixel is processed or stored.
- Masks are enforced on the device itself, not in the app or cloud. A masked region never exists anywhere.
- From the app you can only widen a mask. Narrowing a mask requires the owner PIN entered at the gateway, physically in your house. Nobody talks a mask down remotely.
- Audio is OFF by default and stays off unless you turn it on.

## 3. Arm modes and scenes

Ready-made modes, all editable:

- Night: perimeter armed, deter lighting live, indoors ignored.
- Away: everything armed, instant deter, notify all adults.
- Home: cameras record, deter off, no notifications for family faces.
- Party: detection on, deter off, lights run your party scene.
- Package watch: watches the porch, gentle light pulse and a notification on drop-off, deter only if the package moves toward the street.

Or use the natural-language designer: type what you want ("weeknights after 11, if someone lingers by the garage over 10 seconds, strobe the garage section and ping me") and it builds the scene. Review before saving; the reflex that fires deter lighting always runs locally in under 1 s.

## 4. Household sharing

- Invite members from Settings, Household. Adults get arm/disarm and live view; kids get presence-based automation only, no live view by default.
- Every member gets their own login. No shared passwords.
- Only the owner can change plans, delete footage, or touch privacy masks (widen from app, narrow at gateway with PIN).

## 5. Plans

| | Core | Plus | Shield |
|---|---|---|---|
| Price | $0 forever | $9.99/mo | $19.99/mo |
| Where footage lives | Your house only, nothing leaves it | Home + 60 day cloud backup | Home + 60 day cloud backup |
| Detection, deter, app, masks | Full | Full | Full |
| Cloud clip sharing, richer alerts | No | Yes | Yes |
| Professional monitoring path | No | No | Yes |

No contracts on any plan. Core is not a trial: on Core there is no cloud sync path at all, not a disabled one, an absent one. Everything above still works.

## If something looks wrong

- No events: check the gateway light, then Settings, System Health for node heartbeats.
- Deter feels slow: it should be well under 1 second. Anything slower, run Settings, System Health, Deter Test and contact support with the result.
- A camera sees something it should not: add a mask right now from the app (widening is always allowed).

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
