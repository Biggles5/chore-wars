# SightLine Installer Certification Quiz

25 questions, 4 options each. Passing score is set in practical.md context: quiz is a learning check before the bench practical. Answer key at the bottom.

**1.** Which of these is done on site during a SightLine install?
A. Cutting rail segments to length
B. Splicing conductors to extend a run
C. Clipping factory-cut rail segments into position
D. Drilling node housings for cable entry

**2.** How many nodes may be connected to a single 5A terminal?
A. One
B. Two, if total wattage is under 12W
C. Three, with an approved splitter
D. As many as fit under the 75 ft run limit

**3.** What is the wattage ceiling per run?
A. 5W
B. 12W
C. 18W
D. 48W

**4.** What is the maximum run length on 18AWG cable?
A. 50 ft
B. 75 ft
C. 100 ft
D. 120 ft, if the run has a drip loop

**5.** Before touching a terminal, your meter must read:
A. Exactly 0V
B. <= 0.5V
C. <= 5V
D. <= 48V, since the system is low voltage

**6.** The maximum allowed gasket gap at any point is:
A. 0.5mm
B. 1mm
C. 1.5mm
D. 2mm

**7.** What is the correct role of VHB tape in the rail system?
A. Primary structural attachment
B. Seal only; mechanical capture carries the load
C. Backup structure if a clip fails
D. Temporary hold until adhesive cures

**8.** Where does the low point of a drip loop belong?
A. Above the gland, to keep cable tension
B. Below the gland, so water drips off before the entry
C. Level with the gland
D. Anywhere, as long as the gland is torqued

**9.** The rail_level_spacing gate passes when:
A. Tilt <= 1.5 deg and spacing variance <= 8%
B. Tilt <= 5 deg and spacing variance <= 8%
C. Tilt <= 1.5 deg and spacing variance <= 15%
D. Tilt <= 2 deg and spacing variance <= 10%

**10.** The maximum azimuth error for node aim is:
A. 1.5 deg
B. 2 deg
C. 5 deg
D. 8 deg

**11.** Why does cant error matter at only 2 deg?
A. It voids the Class 2 rating
B. It tilts the scene across the frame and degrades DORI grade at zone edges
C. It doubles power draw
D. It breaks the gasket seal on the node

**12.** DORI stands for:
A. Detect, Observe, Recognize, Identify
B. Distance, Optics, Resolution, Illumination
C. Detect, Orient, Record, Identify
D. Direction, Observation, Range, Image

**13.** The AR reticle in installer mode exists to:
A. Measure run length to the controller
B. Put the node's aim inside the azimuth and cant window at capture time
C. Verify the meter reading photographically
D. Check gasket compression optically

**14.** Privacy masks are:
A. Applied in the cloud after the first week of footage
B. Optional, at the homeowner's request
C. Enforced on-device at setup, before commissioning completes
D. Applied by the monitoring station operator

**15.** The default state of audio capture is:
A. On, with a homeowner opt-out
B. On outdoors, off indoors
C. Off, owner can enable it
D. Off on Core, on for Plus and Shield

**16.** Which statement about the Core ($0) plan is true?
A. It uploads only AVS-01 level 3+ events to the cloud
B. It has no cloud path at all; data stays local
C. It shares anonymized aggregates with insurers
D. It includes station handoff at reduced priority

**17.** Which is the correct list of the 5 QC gates?
A. rail_level_spacing, gasket_seated, connector_clicked, node_aim, controller_wiring
B. rail_level_spacing, gasket_seated, drip_loop, node_aim, meter_check
C. rail_torque, gasket_seated, connector_clicked, node_focus, controller_wiring
D. rail_level_spacing, vhb_coverage, connector_clicked, node_aim, controller_wiring

**18.** The connector_clicked gate requires:
A. Latch engaged and exposed conductor <= 1mm
B. Latch engaged and exposed conductor <= 5mm
C. Hand-tight fit and dielectric grease applied
D. Latch engaged and heat-shrink over the joint

**19.** The QC agent rejects your gasket photo. Correct next step:
A. Reshoot from a tighter angle so the flaw is out of frame
B. Fix the physical issue, then reshoot
C. Submit the same photo with a note explaining the flaw
D. Skip the gate and flag it for the warranty desk

**20.** Warranty on a SightLine install requires:
A. All 5 QC gates passed
B. At least 4 of 5 gates passed
C. Only the electrical gate passed
D. A licensed electrician's sign-off

**21.** The target job time and daily volume for a certified 2-person crew on single-story homes is:
A. 2.4 job-hours, 3 jobs/day
B. 4 job-hours, 2 jobs/day
C. 1.5 job-hours, 4 jobs/day
D. 8 job-hours, 1 job/day

**22.** The 30-point commissioning check breaks down as:
A. Power 6, mechanical 6, optics 6, privacy 4, network+system 5, handoff 3
B. Power 10, mechanical 10, optics 10
C. Power 5, mechanical 5, optics 5, privacy 5, network 5, handoff 5
D. Electrical 15, everything else 15

**23.** SightLine forwards an event to the monitoring station only when:
A. Any motion is detected in an armed zone
B. AVS-01 score >= 2 with video verification
C. AVS-01 score is exactly 4
D. The homeowner taps "request dispatch" in the app

**24.** Which statement matches the Guardian guardrail?
A. Guardian calls 911 directly on level 4 events
B. Guardian asserts a crime when confidence exceeds 0.9
C. Guardian never calls 911 and never asserts a crime; the operator holds dispatch authority
D. Guardian dispatches automatically unless an operator cancels within 60s

**25.** Expected QC first-pass rate by job 5 is:
A. 50%+
B. 70%+
C. 85%+
D. 100%, or certification is revoked

## Answer key
1. C: kits are factory-cut; no cutting, splicing, or drilling on site.
2. A: one node per 5A terminal, no exceptions.
3. B: 12W ceiling per run.
4. B: 75 ft maximum on 18AWG; longer fascia needs another injection point.
5. B: meter must read <= 0.5V before any work on a terminal.
6. A: gasket gap <= 0.5mm anywhere.
7. B: VHB is seal, not structure; mechanical capture comes first.
8. B: the low point sits below the gland so water sheds before the entry.
9. A: tilt <= 1.5 deg plus spacing variance <= 8%.
10. C: azimuth error <= 5 deg.
11. B: cant tilts the scene and degrades DORI grade at zone edges.
12. A: Detect, Observe, Recognize, Identify.
13. B: the reticle puts aim inside the 5 deg azimuth / 2 deg cant window.
14. C: masks are enforced on-device at setup, mandatory.
15. C: audio is off by default; only the owner enables it.
16. B: Core has no cloud path; nothing leaves the home.
17. A: the five gates are rail_level_spacing, gasket_seated, connector_clicked, node_aim, controller_wiring.
18. A: latch engaged and exposed conductor <= 1mm.
19. B: fix first, then reshoot; never frame a flaw out of the photo.
20. A: warranty requires all gates passed.
21. A: 2.4 job-hours single story, 3 jobs/day.
22. A: power 6, mechanical 6, optics 6, privacy 4, network+system 5, handoff 3.
23. B: only verified events, score >= 2 with video verification, are forwarded.
24. C: Guardian never calls 911, never asserts a crime; operator holds authority.
25. C: 85%+ first-pass by job 5 is the expected ramp.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
