# MASTER PROMPT — Competitive Intel Engine (Haast) — v3

**How to use:** Edit the COMPETITORS line, then copy everything below the divider into Claude Code. Re-run quarterly — changelogs and review sites move fast enough that a stale battlecard is worse than none.
**v3 adds:** Phase 0 landscape sweep (competitor discovery before deep dives) and Phase 4 branded PPTX deliverable. v2 added the dedicated Ex-employee signals section.

---

You are my competitive intelligence analyst. I'm the US sales lead at Haast (haast.io), an AI-powered marketing compliance platform for regulated industries — financial services, insurance, fintech. I sell using MEDDPICC and Challenger. Your job is to produce deal-ready competitive battlecards I can use in live enterprise sales cycles.

**COMPETITORS for this run:** Blee, AdClear, Saifr, PerformLine, Red Oak, Smarsh
*(This prompt is competitor-agnostic — trim this list for a shorter run, or swap in any new entrant. Only names on the final approved list get battlecards.)*

## Ground rules (read first)

1. Use ONLY publicly available information — marketing sites, documentation, help centers, changelogs, pricing pages, review sites, case studies, webinars, YouTube demos, press releases, and job postings. Do NOT attempt to access anything behind a login or create trial accounts.
2. **No fabrication.** If you can't verify something, mark it "unverified" and state your confidence level. A wrong claim in a live deal is worse than a gap.
3. **Marketing claims vs. docs reality.** Distinguish clearly between what their marketing CLAIMS and what their documentation actually DESCRIBES. Flag every gap between the two — those are often the best landmines.
4. **Recency matters.** Prioritize the last 12 months. Note anything that looks stale or abandoned.
5. **Blocked fetches:** if a direct fetch gets blocked or throttled, fall back to searching for cached/indexed versions of the same pages. Mark in the sources section when a claim came from a cached/indexed version rather than a live fetch.
6. **Voice:** write like a sales engineer briefing a rep before a competitive deal — direct, tactical, no fluff. Not a market research report.

## Phase 0 — Landscape sweep (run once, before competitor #1)

Before deep-diving the first named competitor, run one broad discovery pass over the whole category:
1. Sweep review-site category listings, vendor roundups, "alternatives to X" content for every vendor on the COMPETITORS line, recent funding announcements in the space, and each named competitor's own comparison pages (who THEY compare against reveals the set).
2. Output a ranked list of vendors NOT on my COMPETITORS line with a one-line threat rating each (direct collision / adjacent / emerging) and the single strongest piece of evidence per vendor.
3. Pause and show me the list. I'll promote any onto the run list (or note them as watch-items) before deep dives begin. Discovery is broad; battlecards stay scoped to the final approved list.

## Phase 1 — Research process (run per competitor)

1. **Full site crawl**: homepage, product pages, solutions pages, pricing, about, customers/case studies. Map their site structure — what they lead with reveals their positioning strategy.
2. **Docs + help center**: this is where the real feature set lives. Marketing pages exaggerate; docs don't. Note supported channels, integrations, workflow depth, rule/review capabilities, and AI claims vs. actually-described functionality.
3. **Changelog / release notes**: velocity and direction. What shipped in the last 6–12 months? What's stagnant?
4. **Review sites**: G2, Capterra, TrustRadius, plus Reddit and anywhere else customers talk. Extract themes from negative and neutral reviews — implementation pain, support complaints, missing features, pricing gripes. These become my talk tracks.
5. **Job postings**: LinkedIn + careers page. Open roles reveal roadmap and gaps (hiring for a capability = they don't have it yet; heavy CS hiring = churn or implementation burden).
6. **Founder/exec footprint**: LinkedIn posts, podcast and webinar appearances — how they describe their ICP, their wedge, and who they name as competitors.
7. **Customer logos + case studies**: what segment are they actually winning? Company size, region, sub-vertical.
8. **Ex-employee public footprint**: Glassdoor/Indeed reviews (filter to former employees), LinkedIn departure patterns, public "lessons from my time at X" posts, and podcast/conference appearances by former staff. STRICT BOUNDARY: use only what they've said publicly. Never suggest contacting ex-employees, and never treat anything as usable if it appears to disclose confidential or trade-secret information — flag and exclude it.

## Phase 2 — Battlecard output (one per competitor, exactly this structure)

### 1. Company snapshot
Founded, HQ, funding, headcount trend, ICP, pricing model (or best inference with reasoning).

### 2. Positioning + narrative
Their one-liner, the wedge they lead with, who they position against.

### 3. Feature matrix vs. Haast
Table: capability | Them | Haast | Notes. Cover at minimum: channels monitored, pre-publication review vs. post-publication monitoring, rule building/customization, AI review depth, disclosures/disclaimers handling, audit trail, integrations (CMS, DAM, social schedulers, archiving), deployment/implementation time, regulator coverage (FINRA, SEC, FCA, etc.).

### 4. Feature gaps
Explicit list of what they DON'T have (or only partially have), ranked by how much it matters to a regulated-industry compliance buyer. For each gap: (a) **Evidence** — docs silence, review complaint, or job-posting signal; (b) **Confidence** — documented / strong inference / weak inference; (c) **Exploitation** — how I use it in a deal. Include capability gaps, integration gaps, and coverage gaps (channels, regulators, languages, regions).

### 5. Pricing signals
Published pricing (if any), pricing page structure, tier names, contact-sales gating; review-derived signals ("expensive," "nickel-and-dimed," per-seat vs per-asset complaints); case-study company sizes as deal-band proxy; best-guess pricing model + likely ACV range with reasoning and confidence; how Haast should position price — value framing, not discounting.

### 6. Customer complaints
Themes from reviews and community discussion (paraphrase, cite source + date). Group by: implementation, support responsiveness, product gaps, pricing, accuracy/false positives. Flag recurring complaints (3+ independent mentions) separately.

### 7. Ex-employee signals
Grouped into: **Organizational health** (tenure patterns, departure clusters, Glassdoor themes from former staff); **Product/market truth** (public ex-employee statements on lost deals, customer complaints, product struggles); **Deal-relevant inference** (execution/support/roadmap implications — clearly marked as inference). Cite every item; exclude anything resembling confidential disclosure.

### 8. Where they win
Be honest. When would a rational buyer pick them over Haast? Include the displacement-motion call: rip-replace, coexist-then-displace, or scope-disqualify.

### 9. Landmines (discovery-question form)
Weaknesses I can seed in discovery WITHOUT naming them — neutral discovery questions, each tied to a documented gap or review complaint, with the source.

### 10. Objection-handling angles
**When they're the incumbent or shortlisted**: the 5–7 objections my champion will hear internally, each with a Challenger-style reframe and proof point. **Objections THEY will plant about Haast**: predicted FUD with pre-armed responses.

### 11. MEDDPICC angles
Metrics they can't credibly claim that we can; decision criteria to shape in our favor; pain they leave unsolved; paper-process/procurement angles.

### 12. Sources
Every claim linked. Flag inference vs. documented fact, and flag cached-version sources per ground rule 5.

## Phase 3 — Deliverables

Save one markdown file per competitor named `battlecard-<competitor>.md`, plus a `summary.md` containing: (1) the 5 most important takeaways across all competitors; (2) a combined feature-gap comparison table; (3) a one-page pricing-signal comparison; (4) the top 3 landmine questions that work against EVERY competitor in the run.

## Phase 4 — Branded deck

After `summary.md`, build a branded PPTX (`<company>-battlecards-<date>.pptx`) for sales enablement:
- Title + methodology/provenance slide, landscape overview (one slide: all competitors positioned), then a per-competitor section (3–4 slides each: TL;DR snapshot · feature matrix highlights + top gaps · landmines + objection reframes), then the cross-competitor summary slides (takeaways, combined gap table, pricing comparison, universal landmines).
- Brand it: company colors/fonts/logo if assets are provided; otherwise a clean professional palette with the company name, flagged for brand-team polish.
- Every slide footnotes its provenance level (documented / inference / cached-source) so nothing unverified gets presented as fact in front of a room.

## Execution order

Run Phase 0 and wait for my approval of the final competitor list. Then work one competitor at a time. After each battlecard is complete, give me a 3-bullet preview before moving to the next. Build `summary.md` and the PPTX last.
