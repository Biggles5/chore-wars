# SightLine Installer Certification: Half-Day Course

6 modules, 4 hours total. Bench practical follows same day (see practical.md). Quiz (see quiz.md) is taken after module 6.

## Module 1: Why this install is different (30 min)
No measuring. No cutting. No splicing. The kit arrives factory-cut to the scanned roofline. Your job is placement, capture, connection, aim, and proof.

Learning goals:
- Explain the factory-kit model: scan drives the cut list, every rail segment is labeled to its fascia run.
- Know what is never done on site: cutting rail, splicing conductors, drilling nodes.
- Know the day shape: 2.4 job-hours single story, 3 jobs/day for a 2-person crew.

Pass signal: trainee can lay out a kit against a plan sheet and identify every segment's position in under 5 minutes, and states the three nevers unprompted.

## Module 2: Class 2 electrical + the terminal rules (45 min)
Class 2 low voltage, never mains. The rules are few and absolute.

Learning goals:
- One node per 5A terminal. No doubling, ever.
- 12W ceiling per run. Know the node wattage and count before connecting.
- 75 ft maximum run on 18AWG. Longer fascia means another injection point.
- The injection tree: how power injection points are laid out and why balance matters.
- Meter-verify before touching: <= 0.5V on the meter before any work on a terminal. This is also QC gate 5 territory (controller_wiring: meter <= 0.5V before work + strain relief).

Pass signal: trainee sizes a 3-run injection tree from a plan sheet correctly (terminals, wattage, run lengths) and demonstrates the meter check with correct probe placement, twice.

## Module 3: Mechanical + weatherproofing (45 min)
Water is the warranty killer. The rail system is designed so that discipline, not skill, keeps it out.

Learning goals:
- Capture first: mechanical capture before any adhesive. VHB is seal, not structure.
- Gasket discipline: seated continuously, gap <= 0.5mm anywhere (QC gate 2: gasket_seated).
- Glands: torque to spec, one cable per gland, no sealant substitutes.
- Drip loops on every cable entry, low point below the gland.
- Rail level and spacing: tilt <= 1.5 deg, spacing variance <= 8% (QC gate 1: rail_level_spacing).

Pass signal: trainee assembles a bench gasket joint that passes the 0.5mm feeler check and explains, in one sentence, why VHB alone is a failed install.

## Module 4: Optics + aiming (40 min)
A perfectly sealed node aimed wrong is a returned kit.

Learning goals:
- DORI in plain language: detect, observe, recognize, identify, and which grade each zone needs.
- The aim window: azimuth error <= 5 deg, cant error <= 2 deg (QC gate 4: node_aim).
- The AR reticle in installer mode: line the reticle, hold, capture.
- Why cant matters: 2 deg of cant tilts the story window across the frame and degrades DORI grade at the zone edge.

Pass signal: trainee aims a bench node into the reticle window on the first hold, within 5 deg azimuth and 2 deg cant, three times in a row.

## Module 5: Privacy + homeowner handoff (30 min)
Privacy is enforced by the product, delivered by you.

Learning goals:
- Mandatory masks: enforced on-device at setup, before commissioning completes. Not optional, not later.
- Audio off by default. It stays off unless the owner turns it on.
- Owner PIN: set by the owner, not the installer, during the walkthrough.
- The walkthrough script: masks shown, plan explained (Core $0 local-only, Plus, Shield), app handed off, questions invited.
- What never exists: face databases, off-site re-ID, any cloud path on Core.

Pass signal: trainee delivers the full walkthrough script from memory to a role-playing "homeowner" without skipping masks, audio, or PIN.

## Module 6: The app runbook + QC gates (50 min)
The QC agent grades your photos. Learn to pass first try.

Learning goals:
- Photo standards: framing, focus, lighting, the reference tag in frame.
- The 5 gates and their thresholds: rail_level_spacing (tilt <= 1.5 deg, spacing var <= 8%), gasket_seated (gap <= 0.5mm), connector_clicked (latch engaged, exposed conductor <= 1mm), node_aim (azimuth <= 5 deg, cant <= 2 deg), controller_wiring (meter <= 0.5V before work, strain relief present).
- Redo etiquette: fix the physical issue first, then reshoot. Never reshoot to game the frame.
- Commissioning: the 30-point check (power 6, mechanical 6, optics 6, privacy 4, network+system 5, handoff 3) and the warranty rule: warranty requires all gates passed.

Pass signal: trainee submits 5 bench gate photos and passes at least 4 on first grading, and can name every commissioning category and its count.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
