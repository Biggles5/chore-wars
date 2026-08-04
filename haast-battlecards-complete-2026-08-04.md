# BATTLECARD: Blee (blee.com)

**Run date:** 2026-08-04 · **Refresh by:** 2026-11-04 (quarterly) · **Prepared for:** Haast US sales
**Provenance note (read once):** direct page fetches were blocked by the research environment's egress proxy for most sites this run, so the bulk of claims below are sourced from search-engine-indexed/cached versions of the cited pages (per ground rule 5). Every such claim is tagged **[cached]**. Before quoting anything *verbatim* in front of a prospect, spot-check the live page — flagged again in §12.

---

## TL;DR for the 2-minute pre-call read

Blee is a ~25-person, YC S22, NYC seed-stage startup with a genuinely impressive US fintech logo wall (Rocket Mortgage, Marqeta, Public, NerdWallet, Betterment) and a pre-publication review wedge embedded in marketing tools (Figma, Asana, Jira, Google Docs). Their attack on us is "Haast is Australian." Their soft underbelly: **no public docs, no security/trust page, no SOC 2 evidence, no changelog, no reviews anywhere, a monitoring claim their own customer PR never substantiates, and "recordkeeping" positioning with zero 17a-4/WORM substance.** You will win on post-publication monitoring, regulatory archiving depth, enterprise implementation rigor, and proof (AWS-published case study, published customer case studies). You will lose speed-shootouts at fintechs that only want pre-publish review inside Figma.

---

## 1. Company snapshot

| Item | Finding | Confidence |
|---|---|---|
| Founded | 2022, Y Combinator S22 (note: one third-party profile says "W23" — that's wrong; W23 is competitor Warrant's batch) | Documented |
| HQ | New York City; building an SF engineering presence (SF-only AI Engineer role) | Documented [cached] |
| Founder/CEO | Guy Shahar — ~5 yrs marketing ops leadership at Adobe, ex-McKinsey, Israeli Intelligence Corps; sole founder. CRO: Omri Chosnek | Documented [cached] |
| Funding | $500K YC pre-seed (Aug/Sep 2022) is the only *disclosed* round. ~$2.8M total per rlegaltech500 + PitchBook, corroborated by Cardumen Capital listing Blee in its portfolio. No raise ever press-released — they are not marketing on funding | $500K documented; $2.8M strong inference |
| Headcount | ~15 (YC, stale) → 23 (Tracxn, Jan 2026) → 27 (LinkedIn-derived). Trend: steady seed-stage growth, 15→mid-20s over ~18 months | Strong inference (converging third-party counts) |
| Revenue | ~$1.5M ARR (2024) per two third-party estimates; never confirmed by Blee | Weak inference — unverified |
| ICP | Compliance officers + in-house legal at US fintech/finserv; marketing velocity is the pitched benefit. Stated ambition into insurance, healthcare/pharma, CPG, travel, life sciences — **no non-fintech logo exists yet** | Documented [cached] |
| Pricing model | No pricing page; "flexible pricing plans… contact for a customized quote." Sales-led, annual enterprise contracts (their YC page: "pledged or paid, long-term contracts" — note the "pledged" hedge). Inferred ACV: tens of thousands of dollars (arithmetic on unverified ~$1.5M ARR ÷ "dozens" of customers) | Model: strong inference. ACV: weak inference |

**Momentum read:** all five logo announcements landed May–Dec 2025 (Rocket case study May, Marqeta Jun, Public Jul, NerdWallet Sep, Betterment Dec). **Zero customer or partnership announcements found in 2026 (Jan–Aug).** Either the pipeline went quiet or they stopped announcing — both worth probing. The 2026 content engine pivoted to GC/legal-ops thought leadership (webinar recaps, "GC-led innovation" posts), suggesting a move toward the legal buyer. [Documented absence, cached]

## 2. Positioning + narrative

- **One-liner:** "The AI-first marketing compliance platform that gives you complete control and oversight over all your content." (Older indexed title: "Smart, Fast, and Collaborative Marketing Compliance Reviews" — they repositioned from "reviews tool" to "AI-first platform.") [Documented, cached]
- **The wedge:** pre-publication AI review embedded where marketers already work — "marketing teams continue working in Jira, Asana, Workfront, Salesforce, Figma, Google Docs… compliance teams review everything centrally in Blee." Human-in-the-loop framing: AI pre-reads everything, flags what marketing can self-fix before compliance looks. [Documented, cached]
- **Founder narrative:** the "AI content tsunami" — AI explodes content volume (test 50–100 versions, hyper-personalization), compliance review is the bottleneck, so review must move "to the source of business activities" (Law://WhatsNext podcast, Nov 2025). [Documented, cached]
- **Repositioning in flight:** a Webflow staging site titled "AI-powered Communications Review and Recordkeeping" + LinkedIn blurb now saying the same + job-page copy saying "Compliance AI Enterprise Platform." They're stretching beyond marketing review toward communications review/recordkeeping — Smarsh-adjacent language without archiving substance (see §4). [Weak-to-strong inference, cached]
- **Who they position against:** head-to-head SEO pages vs **Haast**, Warrant, Norm AI, Hadrius, Red Marker; roundups that include PerformLine. Their template on every page: concede the rival a narrow niche → cite the rival's *website silence* as a product gap ("not documented," "creates uncertainty") → present Blee's specific numbers against that silence → conclude "Blee suits organisations of all sizes." The niche they assign us: "Australian-based teams requiring localized compliance workflows." [Documented, cached]

## 3. Feature matrix vs. Haast

Haast column = Haast's public claims (haast.io, cached) — sanity-check against the internal deck before using numbers.

| Capability | Blee | Haast | Notes |
|---|---|---|---|
| Pre-publication review | **Yes — core strength.** AI pre-read, routing, permissions, approvals, embedded in creation tools | Yes | Parity on paper; Blee's embedding story is slicker for marketing-led evals |
| Post-publication monitoring | **Claimed** ("always-on monitoring… continuously scans website, product pages, social channels, partner content") but **never substantiated**: no docs, no customer PR describes it in production, competitor pages say live content goes unmonitored, and Shahar's own wedge framing is pre-publish. Marqeta PR mentions "monitoring capabilities" in passing — only trace found | **Yes — core strength.** Continuous monitoring of live web + FB/IG/LinkedIn/X/YouTube | **The #1 landmine.** Make them demo it on live content in the eval |
| Channels/media | Documents, web/product pages, social, partner/affiliate content, video (video-analysis agent), Figma designs, emails (claimed in comparison articles). Email + paid-ads *monitoring*: unverified | Text, images, PDFs, docs, long-form video, web, social channels | Roughly comparable claims; Blee's video claim rests on the "15 agents" marketing |
| Rule building / customization | "Legal engineers work with your team to build rules" — **service-assisted, not self-serve**. Competitor Warrant claims Blee ships **no preloaded FINRA/SEC/FTC/ADA rule libraries** (customers upload their own guidelines). No compliance-SME hiring observed → no proprietary reg-rule corpus being built | Pre-configured regulator agents (FINRA, FTC, FCA) + bespoke frameworks via legal implementation team + self-serve per-asset rule config (Equity Trustees: 80+ custom rules encoded) | Their "legal engineering team" is a services layer; probe change-turnaround SLAs |
| AI review depth | "15 specialised AI agents per review," "85–95% accuracy on genuine risks," "custom LLM per client." All self-claims from their own SEO articles; zero methodology, benchmark, or third-party validation. "Custom LLM per client" is almost certainly fine-tuning/RAG, not a custom model | AI agents trained on regulatory frameworks, tuned to org risk tolerance; AWS-published case study (Amazon Bedrock) | Their numbers are unaudited marketing; our AWS case study is third-party-published |
| Disclosures/disclaimers | Real-time flagging vs "sources of truth" (third-party profile). No explicit disclosure-library / auto-insertion feature found | Claimed handling within review workflows | Both thin publicly — verify Haast side internally before leaning on it |
| Audit trail | "Complete audit trails with timestamped records of every review, approval, and content version" + retroactive rule application claims | Full audit trail claims | Paper parity — differentiate on 17a-4 (next row) |
| Regulatory recordkeeping (17a-4 / FINRA 4511 / WORM) | **Nothing.** Despite "Recordkeeping" repositioning, zero 17a-4/WORM/books-and-records claims found anywhere; no archiving-vendor integrations (Global Relay, Smarsh) named. "Recordkeeping" = review audit logs, not regulatory archiving | Check internal positioning — if we integrate with archiving vendors or make 17a-4-adjacent claims, this is a clean kill shot vs their broker-dealer/RIA logos (Public, Betterment) | **Documented absence.** Their own customers are FINRA-regulated |
| Integrations | Jira, Asana, Workfront, Salesforce, Figma, Google Docs/Drive, Dropbox, Monday.com, Workday, Wrike, Word. **Not found:** CMS, DAM, social schedulers, Slack, archiving vendors | Figma, Office365, Workfront, Google Docs, + API/native connectors | Blee wins breadth of PM-tool logos; nobody has archiving/CMS/DAM story publicly — first to build one wins the row |
| Deployment time | Conflicting: "2–4 weeks" (one Blee article + Puntt), "6–10 weeks" (their own vs-Haast page). Their attack says Haast = 8–12 weeks | 8–12 weeks bespoke, with out-of-the-box regulator agents live from day one | **Use their inconsistency.** If their rep says 2–4 weeks, their own vs-Haast page says 6–10 |
| Regulator coverage | Claims SEC, FINRA, FTC, all 50 state insurance depts, ADA, platform ad policies (Google/Meta/LinkedIn), "50 states plus UK, EU, Asia, MENA." CFPB/FDIC/FCA: not found. International claim has zero non-US evidence (no non-US logo, no international hires) | FINRA, FTC, FCA pre-configured + ASIC/ACCC heritage (genuine multi-jurisdiction operating history) | Their international line is aspirational; ours is operational. Flip their geography attack |
| Security posture | **No SOC 2 claim, no security/trust page found** — for a vendor serving PayPal-class logos, striking. (They are hiring a Security Engineer at $170–200K — building it now) | Check internal — if Haast has SOC 2, table it early in every deal | Documented absence [cached] |
| Proof/validation | No G2/Capterra/TrustRadius presence, no HN launch, no Reddit footprint. Proof = 5 logo PRs + 1 self-published case study (Rocket, 67% faster reviews, corroborated by a Rocket employee on a CLOC panel) | AWS-published case study, Equity Trustees case study, Telstra/Aviva, $6M US-expansion raise (May 2025) | Their proof is press releases; ours includes third-party-published material |

## 4. Feature gaps (ranked by weight for a regulated-industry compliance buyer)

1. **Post-publication monitoring unproven in production.**
   (a) Evidence: marketing claims "always-on monitoring" [cached: blee.com], but no docs exist to describe it, no customer announcement describes it in use (all five describe pre-publish review workflows; Marqeta PR alone mentions "monitoring capabilities" in passing), Haast's and Warrant's comparison pages both state live content goes unmonitored (adversarial sources), and Shahar's own narrative is entirely pre-publish.
   (b) Confidence: strong inference (claim documented; substance absent everywhere it should appear).
   (c) Exploitation: force a live-content demo in the eval — "show us yesterday's Instagram post being caught." Structure POC success criteria around post-publish detection latency. If it's real but shallow, it dies in the POC; if it's vapor, it dies in the demo.

2. **No regulatory recordkeeping substance (17a-4/WORM/books-and-records).**
   (a) Evidence: zero 17a-4/WORM claims anywhere despite "Recordkeeping" repositioning [documented absence, cached]; no archiving integrations named. Their marquee logos (Public = broker-dealer, Betterment = RIA) live under SEA 17a-4/FINRA 4511.
   (b) Confidence: documented absence.
   (c) Exploitation: bring the buyer's books-and-records owner into the eval. Ask how review records get to the compliant archive. Blee has no public answer.

3. **No preloaded regulatory rule libraries; setup depends on their "legal engineers."**
   (a) Evidence: their own copy — "legal engineers work with your team to build rules" [cached]; Warrant's claim that customers upload their own guidelines (adversarial); zero compliance-SME/regulatory-content job postings ever observed; Haast's counter-page: "rule configuration is more complex and requires input from other teams" (adversarial).
   (b) Confidence: strong inference (their own copy + posting mix; rival claims corroborate).
   (c) Exploitation: rule-change turnaround. "FINRA issues new guidance Tuesday — what's your process and SLA to have rules updated, and is a vendor services ticket in the loop?" Also scale math: a ~25-person company's legal-engineering bench vs. an enterprise's rule-change volume.

4. **No public documentation, help center, changelog, or security/trust page at all.**
   (a) Evidence: docs.blee.com and help.blee.com are NXDOMAIN (live DNS check — one of the few non-cached facts this run); no indexed help center; no changelog; no SOC 2 mention; a third-party profile explicitly notes "no public security documentation… despite serving regulated industries."
   (b) Confidence: documented absence.
   (c) Exploitation: procurement/vendor-due-diligence angle. Compliance buyers diligence vendors like regulators diligence them. "Ask each vendor for their public documentation, trust center, and SOC 2 report on day one." Also means every capability claim is un-checkable — push the eval to proof-by-demo.

5. **Insurance vertical is aspirational.**
   (a) Evidence: "50 state insurance departments" claimed [cached], but zero insurance logos, zero insurance case studies, no insurance-domain hires.
   (b) Confidence: documented absence of proof.
   (c) Exploitation: in insurance deals, demand insurance references. They have none to give.

6. **International coverage is a line on a webpage.**
   (a) Evidence: "50 states plus UK, EU, Asia and MENA" [cached] vs. no non-US logo, no international roles, no FCA-specific content.
   (b) Confidence: strong inference.
   (c) Exploitation: for any buyer with UK/EU entities, make FCA financial-promotions coverage a scored criterion and ask both vendors for an FCA-regulated reference. We have operating history in multiple jurisdictions; they have a sentence.

7. **No CMS/DAM/social-scheduler/archiving integrations.**
   (a) Evidence: integration lists are all PM/design/doc tools; targeted searches for CMS, DAM, scheduler, Global Relay/Smarsh integrations returned nothing [documented absence, cached].
   (b) Confidence: documented absence (of claims).
   (c) Exploitation: map the buyer's actual content supply chain (CMS publish step, DAM as source of truth, Sprinklr/Hootsuite for social). Every unsupported hop = manual upload = the exact workflow tax Blee claims to eliminate.

8. **Enterprise GTM is embryonic.**
   (a) Evidence: hiring their **founding** AE, first pre-sales SE, first PMM, and a Security Engineer simultaneously (2025–26 postings) [cached]; "pledged or paid" contracts hedge on the YC page.
   (b) Confidence: documented postings; strong inference on implications.
   (c) Exploitation: don't say "they're small." Ask about named CSM/support model, SLAs, security-review turnaround, reference calls with 12+ month customers. A founder-led vendor stalls on all four.

## 5. Pricing signals

- **Published pricing:** none. No pricing page exists. "Flexible pricing plans… contact for a customized quote." [Documented absence, cached]
- **Marketplace/procurement presence:** not on Vendr, Spendflo, NachoNacho, or AWS Marketplace. No review-site pricing fields (no listings). No press-reported deal sizes. [Documented absence]
- **Structure signals:** YC page says "long-term contracts"; they frame rival Warrant as the "usage-based, budget-constrained smaller teams" option → Blee sells annual enterprise contracts, demo-gated. Per-seat vs per-asset split: unknown. [Strong inference]
- **Their pricing FUD line:** "enterprise-grade compliance democratically accessible **without enterprise-exclusive pricing**" — an insinuation that rivals (us included) overprice, backed by no published number of their own. [Documented, cached]
- **Best-guess model + ACV:** sales-led annual SaaS; if the unverified ~$1.5M ARR (2024) across "dozens" of customers is roughly right, blended ACV lands in the **$30K–$75K** band, with marquee logos likely above it. Confidence: **weak** — arithmetic on two unverified numbers. Do not quote; use only to calibrate expectations.
- **How to position price:** never race them down. Frame TCO: (1) their price buys pre-publish review; monitoring, archiving-grade records, and multi-jurisdiction coverage are absent or unproven, so the buyer still needs budget for those; (2) "legal engineers build your rules" = a services dependency priced into renewal leverage; (3) a quietly-funded ~25-person sole-founder vendor carries continuity risk that procurement prices in — multi-year discount asks, source-code escrow, SLA teeth. Sell certainty per dollar, not dollars.

## 6. Customer complaints

**Independent complaint volume is zero.** No G2, Capterra, TrustRadius, GetApp, Software Advice, or Product Hunt listing exists (searches returned only name collisions: Bleeper, Bleesk, Bleez, Bleemeo, Bleexo). No HN thread, no Reddit mention in fintech/compliance/regtech subs. All public "customer voice" is vendor PR or competitor content. [Documented absence — ~14 searches logged]

- **What this means for talk tracks:** you cannot cite Blee customer complaints — don't invent any. Reframe the absence itself: "For any vendor on your shortlist, can you find a single independent customer review? For Blee the answer is currently no — every public data point is a press release they wrote."
- **Closest critique-shaped content** (single, adversarial sources — background only, never cite as "customer feedback"): Haast's comparison page (6–10 week implementation; live content unmonitored; rule config needs other teams) and Warrant's (no preloaded rule libraries).
- **Their own concession:** "85–95% accuracy on genuine risks" implicitly concedes a 5–15% miss/false-positive band, self-reported, methodology-free. [Documented, cached]

## 7. Ex-employee signals

- **Organizational health:** effectively no signal exists — expected for a sub-30-person company. No Glassdoor page for this Blee (collisions only). An Indeed page ("Blee", 4.0 rating, minimal content) could not be confirmed as this company — excluded. No public departure patterns, no "ex-Blee" profiles surfaced in public search, no "my time at Blee" posts. [Documented absence]
- **Product/market truth from former staff:** none available.
- **Deal-relevant inference (clearly marked as inference):** the absence cuts both ways — no disgruntled-employee ammo for us, but also no independent window into execution. The only org-health facts available are structural: sole founder, ~25 people, first-ever AE/SE/PMM hires happening now. Use §4 gap 8 (GTM maturity) instead of ex-employee angles for this competitor.
- Boundary note: nothing encountered resembled confidential disclosure; nothing was excluded on that basis except the unconfirmable Indeed page.

## 8. Where they win (honest)

- **US fintech, marketing-led eval, pre-publish-only scope.** If the buyer is a growth-stage fintech whose pain is "compliance reviews slow our marketing team down inside Figma/Asana," Blee's embedding story + fintech logo wall (Rocket, Marqeta, Public, NerdWallet, Betterment) is genuinely strong and the references are peer-perfect.
- **Fintech peer-proof beats us there.** Rocket's 67% review-time claim is corroborated by a Rocket employee appearing on a CLOC panel — that's a real reference customer, not vapor.
- **Speed-to-value optics.** If they quote 2–4 weeks against our 8–12 and the buyer doesn't scrutinize, they win the "time to first value" line.
- **Deals where the champion is a marketing leader, not compliance.** Blee's UX pitch is built for marketing's experience; ours leads with compliance depth.
- **Price-sensitive mid-market.** A seed-stage vendor hungry for logos can underbid; if the deal is a procurement-led price shootout on pre-publish review only, disqualify or reframe scope early.
- **Disqualify/reframe rule:** if the buyer has (a) no post-publish risk surface they care about, (b) no 17a-4-style records obligation in scope, and (c) US-only footprint — Blee is a rational choice and the deal is only winnable on risk/continuity grounds. Reframe to the full content-risk lifecycle or move on fast.

## 9. Landmines (discovery-question form — never name Blee)

1. Ask: **"Once content is live — on your site, your partners' sites, social — what continuously checks that it still complies, and how would you know if something changed?"** → Their monitoring claim is unsubstantiated in docs and customer PR (§4.1).
2. Ask: **"When a regulator or auditor asks for your review records, do those need to live in your books-and-records archive — and how would a review tool feed that?"** → No 17a-4/WORM/archiving-integration substance (§4.2).
3. Ask: **"When rules change — new FINRA guidance, a state bulletin — who updates your rule set, how fast, and can your own team do it without a vendor services ticket?"** → "Legal engineers build your rules"; no preloaded libraries per rival claims (§4.3).
4. Ask: **"How important is it that a vendor's claims are checkable — public documentation, a trust center, SOC 2 on request, independent reviews — before you rely on them for a regulated function?"** → None of the four exists publicly (§4.4).
5. Ask: **"How many reference customers in *your* sub-vertical (insurance / UK-regulated / bank) will each vendor put on the phone?"** → Fintech-only logo wall; insurance and international are claims without proof (§4.5–4.6).
6. Ask: **"Can we see the full content journey in the demo — from your CMS/DAM/scheduler through review to publish — using your actual stack, not a file upload?"** → No CMS/DAM/scheduler integrations found (§4.7).
7. Ask: **"What implementation timeline is each vendor committing to in writing, and what's their reference base for that number?"** → Their own content says both 2–4 and 6–10 weeks (§3, deployment row).

## 10. Objection-handling angles

**When Blee is shortlisted or the incumbent — what your champion will hear inside:**

1. *"Blee is built for US fintech; Haast is Australian."* → Reframe: "Geography isn't the risk — coverage depth is. Haast ships pre-configured FINRA and FTC agents and has operated under some of the world's strictest marketing-compliance regimes (ASIC/ACCC) — regulator-portability is the point. Meanwhile, the 'US-native' vendor has no public documentation of its US rule libraries at all; their own partner Warrant says customers upload their own guidelines. Ask both vendors to show their FINRA rule coverage live." (Their attack is an absence-of-evidence gambit that our own site already contradicts — haast.io documents FINRA/FTC agents and Figma/Office365/Workfront/Google Docs integrations.)
2. *"Blee deploys in 2–4 weeks; Haast takes 8–12."* → Reframe: "Their own vs-Haast page says 6–10 weeks — get the commitment in writing. Our 8–12 weeks includes encoding your actual policy manual (Equity Trustees: 80+ custom requirements) with regulator agents live from day one. Fast onboarding of generic rules just means your reviewers re-litigate every flag later."
3. *"Rocket Mortgage/Marqeta/Betterment use them."* → Reframe: "Great logos — all announced within a seven-month window in 2025, all describing pre-publish review. Ask for a reference that's been live 12+ months, and one that uses post-publication monitoring in production. Also ask why there hasn't been a customer announcement since December 2025."
4. *"They're cheaper."* → Reframe: TCO story from §5 — their price covers a slice of the lifecycle; monitoring, archiving-grade records, and multi-jurisdiction are absent or unproven, and rule maintenance is a services dependency. "Cheaper per feature-you-actually-get" usually inverts.
5. *"Their AI is more advanced — 15 agents, 85–95% accuracy, custom LLM per client."* → Reframe: "Those numbers appear only in their own SEO articles — no methodology, no benchmark, no third-party validation. Haast's AI architecture is documented in an AWS-published case study. Make both vendors run *your* content corpus in the POC and measure precision/recall yourselves — we'll agree to that in writing."
6. *"Marketing prefers their workflow."* → Reframe: "Embedding review where marketers work matters — and we do it (Figma, Office365, Workfront, Google Docs). But the buyer here is compliance: marketing convenience with an unmonitored post-publish surface just moves the risk downstream of the approval click."
7. *"They're a fast-moving startup; big platforms are slow."* → Reframe: "Fast-moving is unverifiable without a changelog — they don't publish one. What's verifiable: sole founder, ~25 people, first-ever AE and PMM being hired now, no SOC 2 evidence, no trust center. For a system of record in a regulated function, ask procurement what vendor-continuity terms they'd require — then price those in."

**FUD they will plant about Haast — pre-armed responses:**

| Their line (documented from their vs-Haast page [cached]) | Your response |
|---|---|
| "Australian tool; case studies and blog are all ASIC/ACCC" | "Multi-jurisdiction by design — FINRA/FTC/FCA agents ship pre-configured; AU heritage means we cut our teeth under aggressive enforcement. Here's the US coverage demo." Then show it — the attack dies on contact with a demo |
| "US regulatory depth undocumented — creates uncertainty" | Flip it: they have NO public docs of any kind — no docs site (their docs/help subdomains don't even resolve), no trust page, no changelog. We'll put rule coverage on screen; ask them to do the same |
| "8–12 week implementation vs our 6–10" | Two-week delta buys 80+ custom-encoded rules and a legal implementation team vs. CSMs configuring presets. Also surface their 2–4 week claim elsewhere — which number is real? |
| "Upload-based workflow, no Figma/PM integrations specified" | Factually false per our own site (Figma, Office365, Workfront, Google Docs, API). Demo the Figma flow; note their claim was 'not specified on the website,' not 'doesn't exist' — that's their evidentiary standard for everything |
| "Audit trail depth not specified; no retroactive rule application" | Show the audit trail in the demo. Then ask them for their 17a-4 story — their 'recordkeeping' has no regulatory-archiving substance |
| "AI architecture not disclosed — agents, accuracy, learning mechanism unknown" | "Agent-count marketing isn't a quality metric — it's a criterion they invented because only they publish one. Our architecture is in a published AWS case study. POC on your corpus decides this row" |

## 11. MEDDPICC angles

- **Metrics:** we can anchor metrics they can't credibly claim — % of *live* estate continuously monitored (they can't demo it), time-to-detection of non-compliant live content, multi-jurisdiction rule coverage counts, POC precision/recall on the buyer's own corpus (they've never published a methodology). Their metrics (67% faster reviews, 85–95% accuracy) are self-published; make third-party-verifiable measurement a deal norm.
- **Decision criteria to install:** (1) full-lifecycle coverage — pre-publish AND post-publish — demoed live; (2) regulatory recordkeeping path (17a-4-grade) documented; (3) self-serve rule administration with change-SLA; (4) vendor diligence pack — SOC 2, trust center, public docs, independent references; (5) written implementation commitment with reference backing. Blee fails or struggles on all five today.
- **Pain they leave unsolved:** everything after the approval click — live-estate drift, partner/affiliate content that bypassed review, regulator-ready records, and any non-US obligation. Sell the compliance officer their 2 a.m. fear: "the approved version isn't what's live."
- **Paper process / procurement:** their friction, our leverage — no SOC 2 evidence or trust center (security review stalls), sole-founder ~25-person continuity risk (business-continuity and escrow clauses), "pledged or paid" contract hedging, no marketplace presence (no pre-negotiated paper), services-dependent rule setup (scope-creep risk in the SOW). Arrive with our security pack on day one and make "vendor diligence completeness" a scored criterion.
- **Champion risk note:** if the champion is in marketing, Blee's pitch is aimed at them. Build the compliance/legal economic buyer early; that's whose risk register we own.

## 12. Sources

Provenance: **[cached]** = search-engine-indexed/cached content of the cited page (direct fetch blocked by research-environment proxy — ground rule 5). **[live-DNS]** = observed DNS behavior during fetch attempt. Adversarial = competitor-authored, treat as claims not facts. All accessed 2026-08-04.

**Blee-owned** (all [cached]):
- Homepage/positioning/monitoring claims: https://www.blee.com/
- About (team, ex-FTC-Chairwoman advisor claim): https://www.blee.com/about-us
- vs-Haast page (attack lines, 6–10 wk claim): https://www.blee.com/resources/articles/blee-vs-haast-best-marketing-compliance-software-for-2025
- Other comparison/SEO pages (15 agents, 85–95%, custom LLM, integrations, regulator lists, 2–4 wk claim): blee.com/resources/articles/ and /blogs/ — blee-vs-warrant, blee-vs-norm, blee-vs-hadrius, blee-vs-red-marker, top-marketing-compliance-software-providers-in-2025, the-best-ai-marketing-compliance-tools-for-financial-services-insurance-in-2025
- Customer posts: /blogs/rocket-mortgage-cuts-marketing-review-time-by-67-with-blees-compliance-ai (May 19 2025), /blogs/blee-partners-with-public (Jul 7 2025), NerdWallet post (Sep 22 2025), /blogs/blee-partners-with-betterment-to-scale-trustworthy-financial-communication (Dec 1 2025)
- Staging reposition: https://blee-kral.webflow.io/ ("AI-powered Communications Review and Recordkeeping")
- App login: https://vettr.blee.com/ · docs.blee.com + help.blee.com NXDOMAIN [live-DNS]

**Company data** (all [cached]): ycombinator.com/companies/blee (+/jobs: AI Engineer, SWE/Full-Stack Founding, comp bands) · workatastartup.com/companies/blee (6 open roles, "pledged or paid" quote) · tracxn.com/d/companies/blee ($500K; 23 emp Jan 2026) · rlegaltech.com/vendors/blee ($2.8M/~24 emp/~$1.5M ARR — sole source, contains a batch error; also "no public security documentation" critique; unverified PayPal logo) · cardumencapital.com/investments/blee (investor corroboration) · crunchbase/pitchbook/cbinsights/rocketreach/extruct profiles · linkedin.com/company/weareblee (27 emp)

**Founder** (all [cached]): lawwhatsnext.substack.com/p/the-ai-content-tsunami-with-guy-shahar (Nov 19 2025) · finovate.com/videos/finovatespring-2024-blee · cloc.org "Can AI Protect Your Brand?" (Rocket's Roxanne Worosz on panel — corroborates Rocket relationship) · fintechcouncil.org AFC press release (Aug 7 2025, Shahar quote) · linkedin.com/in/guy-shahar posts

**Adversarial/competitor sources** (claims, not facts; all [cached]): haast.io/blog/haast-vs-blee (6–10 wk, "live content unmonitored," rule-config complexity — note snippet contained a YC-batch error) · hellowarrant.com/blog/warrant-vs-blee (no preloaded rule libraries) · puntt.ai/blog/punttai-vs-blee-marketing-compliance (2–4 wk figure)

**Haast baseline** (all [cached]): haast.io home/about/case-studies/equity-trustees · haast.io/blog/best-marketing-compliance-software (FINRA/FTC/FCA agents) · aws.amazon.com/solutions/case-studies/haast-case-study/ · fintech.global (May 8 2025, $6M US-expansion raise)

**Review-site absence** (documented negative results): G2, Capterra, TrustRadius, GetApp, Software Advice, Product Hunt — no listing for this Blee (collisions: Bleeper, Bleesk, Bleez, Bleemeo, Bleexo). No HN thread (Algolia + /from?site=blee.com blocked; no indexed thread exists). No Reddit mentions in r/fintech, r/compliance, r/RegTech. ~14 searches logged in research notes.

**⚠ Before quoting verbatim in a live deal:** re-fetch blee.com's vs-Haast page and homepage from an unrestricted network to confirm exact current wording — this entire run is cached-source per ground rule 5, and their site copy has demonstrably shifted at least once (homepage retitle, staging reposition).
# BATTLECARD: Adclear (adclear.ai)

**Run date:** 2026-08-04 · **Refresh by:** 2026-11-04 (quarterly) · **Prepared for:** Haast US sales
**Identity note:** this is Adclear Ltd, London (founded 2024) — NOT the discontinued German "AdClear" ad-blocker (SEVEN Networks) or "AdClarity." Both collisions pollute review-site and Glassdoor results; findings from those pages were excluded.
**Provenance note:** direct fetches were blocked by the research environment's egress proxy this run, so nearly all claims are sourced from search-engine-indexed/cached versions of the cited pages (ground rule 5) — tagged **[cached]**. Live DNS checks are the exception, tagged **[live-DNS]**. Spot-check live pages before quoting verbatim in a deal; specifics in §12.

---

## TL;DR for the 2-minute pre-call read

Adclear is an 8-person, ~$3.4M-raised London startup that has genuinely won the UK "finprom" wedge: FCA-native positioning, real tier-1 UK logos (Lloyds teams, IG UK&I, PensionBee), an FCA AI-programme credential, a RegTech of the Year award (UK FinTech Awards 2026), and — unlike Blee — a real public docs site and claimed ISO 27001/SOC 2 Type II. In the UK, do not fight their FCA story head-on. Everywhere else: their US coverage is a homepage list plus one customer (NinjaTrader, Apr 2026) plus one blog post — no US docs, no US entity, no US hires; their post-publication monitoring was a *roadmap item in their own Nov 2025 seed PR* and its documented scope is web/affiliate/Discord/Telegram; their headline metrics contradict each other in their own materials; and 8 people cannot support US enterprise accounts. They frame Haast as a "horizontal enterprise platform" vs their "finprom specialist" — a frame that collapses against their own 15-regulator/"100+ bodies" breadth claim.

---

## 1. Company snapshot

| Item | Finding | Confidence |
|---|---|---|
| Founded | 2024, London (LinkedIn says 2023 — likely incorporation vs launch). Origin story: a founder's family member spent 30+ years regulating radio ads, called ~40% of the work repetitive; the team built a genAI POC on radio ad rules, then pivoted to financial services | Documented [cached] |
| Founders | Doni Hoti (CEO — LSE public policy, ex-Euronext), **Joe Jordan (CCO = Chief COMMERCIAL Officer** — ex-VC associate at Supernode Global, co-founded a student staffing startup; **not ex-FCA, not ex-compliance**), Cameron Ward (CTO — spacecraft engineering, ex-Focal/Trayport/Arqit) | Documented [cached] |
| Funding | £510K pre-seed (Jan 2025 — Haatch, Force Over Mass, Founders Capital) + £2.1M/$2.75M oversubscribed seed (Nov 13 2025 — led by Outward VC, with AFG Partners, Tenity; angels Dan Cobley/ClearScore and Keith Grose/Coinbase UK via a16z scout fund). Total ~$3.4M | Documented [cached] |
| Headcount | **8 at seed announcement (Nov 2025)**; LinkedIn band 2–10; all job postings London-only; job applications go to joe@adclear.ai (founder-screened hiring) | Documented [cached] |
| Traction | "ARR grown 10x since Jan 2025" — no absolute figure anywhere; base was pre-seed-stage ten months earlier, so likely small. 15,000+ ads processed claim (Jan 2025) | Claim documented; magnitude unverified |
| ICP | Marketing + compliance teams at FCA-regulated finance brands — fintech, neobank, trading/CFD/spread-betting, crypto, lending; first insurance logo Jul 2026 (Marshmallow). Dual-sided pitch: marketing gets speed, compliance gets audit trail | Documented [cached] |
| Pricing model | No pricing page. "Based on volume and workflow configuration," ROI model built at demo, "payback in under 5 months," 6-week pilot structure. Inferred: sales-led annual SaaS; blended ACV £20K–£60K (fintech £15–30K, bank/broker £75K–150K+); total ARR likely under ~£1.5M | Model documented [cached]; ACV weak inference |
| Credentials | FCA AI & Innovation Programme graduate; **RegTech of the Year, UK FinTech Awards 2026** (Apr 23 2026 — winners page confirms, though their own earlier copy cited an unnamed award); claims ISO 27001, SOC 2 Type II, **Cyber Essentials Plus** (a UK-market tell) | Award documented; certs claimed, no public evidence |

## 2. Positioning + narrative

- **One-liner:** "FinProm Compliance Platform for Finance Brands" / "Financial Promotions Compliance, in Seconds." Product page title is literally "Real-Time **FCA** Ad Review." [Documented — SERP titles]
- **Wedge:** pre-publication AI review of financial promotions for UK/FCA-regulated marketing teams, embedded in Slack and Figma, with "compliance-in-the-loop" framing — "applies your compliance rules without inventing them; your compliance team can edit the rule logic directly." [Documented, cached]
- **Narrative:** AI-speed marketing vs manual compliance review — "isn't just inefficient, it's risky" (Jordan). Regulators "showing their teeth" (FCA finprom crackdown, Consumer Duty, cryptoasset promotion rules) creates the urgency. They position against *manual review*, not named vendors, in press. [Documented, cached]
- **Against Haast specifically:** comparison-page-style copy surfaced framing "Adclear's financial promotions specialism" vs "Haast's horizontal enterprise compliance platform" as an "honest 2026 comparison." URL couldn't be confirmed (site blocks fetches) — **verify with a browser and capture it**; if real, they're the only competitor in this run actively comparing against Haast from the UK side. Also positions vs Hadrius ("US-only" vs their "UK and US regimes") and Blee (peer framing). [Cached, moderate confidence]
- **Expansion arc:** UK fintech bottom-up (first client Plum) → UK enterprise (Lloyds teams, IG) → verticals (insurance via Marshmallow, Jul 2026) → geographies (EU/US "recently expanded" Nov 2025; APAC/MENA "coming months" — no evidence shipped since). [Documented, cached]

## 3. Feature matrix vs. Haast

Haast column = Haast public claims (haast.io); verify against internal deck.

| Capability | Adclear | Haast | Notes |
|---|---|---|---|
| Pre-publication review | **Yes — core strength.** Upload → auto-assessment vs org policies + reg rules → reviewer sign-off; annotation/inline/sticky comments; escalations, evergreens, claims substantiation, self-approvals; substantiated by real public docs (docs.adclear.ai "Adclear Manual") | Yes | Their docs actually back the review workflow — stronger substantiation than Blee's |
| Post-publication monitoring | **Shipped but young and narrow.** Was explicitly *roadmap* in their own Nov 2025 seed PR ("will fund… post-publication compliance monitoring for affiliates and finfluencers"). Docs now show monitoring of websites, affiliate sites, social, **Discord, Telegram**. No monitoring case study, no coverage spec (cadence, historical footprint, remediation). NinjaTrader deal (Apr 2026) covers influencer/affiliate content | **Founding capability** — continuous monitoring of live web + FB/IG/LinkedIn/X/YouTube | Do NOT say "they don't monitor" — say "less than a year old, no reference, scope it in the POC." The Discord/Telegram angle shows their crypto/trading DNA |
| Channels | Review: "any channel — email, social, TV, radio, PPC, product screens, websites," Google/Meta ads, OOH, influencer/affiliate. Monitoring: web/affiliate/social/Discord/Telegram only (docs) | Text, image, PDF, docs, long-form video, web, social | Their review-channel breadth claim exceeds their monitoring scope — probe the delta |
| Rule building | Compliance team "can edit the rule logic directly" + separate partner workspaces with dedicated rule sets (affiliate use case). Regulator rule content: no compliance-SME team — 8 people, no ex-regulator, no reg-content hires | Pre-configured FINRA/FTC/FCA agents + legal implementation team + self-serve per-asset config | Their self-serve rule-editing claim is real differentiation vs Blee; their rule *content* bench is 3 founders deep |
| AI review depth | Real-time feedback, automated claims evaluation, positional comments, learns from reviewer decisions. "Regulatory changes reflected within 24 hours" — mechanism described nowhere; implausible as a systematic SLA across "100+ bodies" for an 8-person team | Regulator-trained agents, AWS-published architecture case study | Attack the 24-hour claim with one question: "walk me through the pipeline" |
| Disclosures/disclaimers | Claims-substantiation feature in docs; no dedicated disclosure-library feature found | Claimed within review workflows | Both thin publicly |
| Audit trail | Claimed throughout + docs substantiate review records; no 17a-4/WORM/books-and-records claims, no archiving-vendor integrations | Full audit trail claims | Same 17a-4 landmine as Blee — and Adclear sells to brokers (IG, NinjaTrader, Freetrade) |
| Integrations | **Slack, Figma** (customers run it inside both), REST API + webhooks for HubSpot, Braze, Contentful, headless CMS, DAM. Not claimed: social schedulers, Jira/Asana/Monday, archiving vendors | Figma, Office365, Workfront, Google Docs, API | Their CMS/martech story (HubSpot/Braze/Contentful) is actually broader than Blee's — don't run the Blee integration attack here |
| Deployment | 6-week pilot (policy import → workflow mapping → parallel run); no hard go-live claim; "payback <5 months" | 8–12 weeks bespoke, regulator agents live day one | Their "seconds" review speed vs 6-week pilots is a mild inconsistency; weaker attack than vs Blee |
| Regulator coverage | Claims FCA, Consumer Duty, MiFID II, MiCA, ASA/CAP, SEC, FINRA, CFTC, FTC, MAS, ASIC, FSCA, CySEC, CSSF, CVM/BACEN, "100+ bodies mapped" (full list gated in customer-only "Regulations Hub"). **Their own Nov 2025 PR: EU/US "recently expanded," APAC/MENA "coming months."** Zero SEC/FINRA content in docs; one US customer; US content = one blog post (Jun 2026) | FINRA/FTC/FCA pre-configured + ASIC/ACCC operating heritage | **FCA-deep, elsewhere-shallow.** The breadth list is the attack surface: depth is evidenced only for FCA |
| Security/certs | ISO 27001 + SOC 2 Type II + Cyber Essentials Plus claimed; **no trust-center URL, auditor, or certificate scope public** (trust./security. subdomains don't resolve [live-DNS]) | Verify Haast's certs internally and table them | They beat Blee here on paper; ask for report scope + date |
| Proof/validation | 2 real case studies (Plum: 88% faster/18x output; InvestEngine: 520 hrs/week), 12+ named logos, award, FCA programme. Zero independent reviews anywhere (no G2/Capterra/TrustRadius/PH/Trustpilot/Reddit/HN) | AWS-published case study, Equity Trustees, Telstra/Aviva, $6M raise | Their proof is stronger than Blee's but still 100% company-controlled narrative |

## 4. Feature gaps (ranked for a regulated-industry compliance buyer)

1. **US regulatory depth is a list, not a capability.**
   (a) Evidence: their own seed PR (Nov 2025) says EU/US coverage "recently expanded" [documented, cached]; docs contain zero SEC/FINRA content; no US case study; one US customer (NinjaTrader, Apr 2026); no US entity, office, or job posting; first US-regime blog post Jun 29 2026.
   (b) Confidence: strong inference from converging documented absences.
   (c) Exploitation: in any US deal, make FINRA 2210 depth a scored, demo-verified criterion — filing workflows, principal-approval concepts, retail-communication categories, test content with known 2210 violations. A rule layer built FCA-first will show its seams live.

2. **Post-publication monitoring is <1 year old with no reference and narrow documented scope.**
   (a) Evidence: roadmap item in their own Nov 2025 funding PR [documented]; docs scope = websites/affiliates/social/Discord/Telegram; no monitoring case study or coverage spec anywhere.
   (b) Confidence: documented (roadmap timing) + strong inference (immaturity).
   (c) Exploitation: POC criteria — live-estate scale test (full domain crawl + all social channels), detection latency, change detection, remediation workflow, historical footprint. Ask for a monitoring reference customer; they have none public.

3. **8 people. All in London.**
   (a) Evidence: "expand its current 8-strong team" in their own seed PR [documented]; every job posting London (Founding Engineer £70–90K, Founders Associate £27–30K, Growth Marketer £30–45K, Senior AI Engineer); applications to joe@adclear.ai; no US/EU roles.
   (b) Confidence: documented.
   (c) Exploitation: US enterprise support reality — timezone coverage, named CSM, security-questionnaire turnaround, SLA depth, who answers at 2pm ET. Also roadmap-vs-capacity: EU+US+APAC+MENA expansion, monitoring build-out, and insurance vertical on an 8-person team and $3.4M.

4. **No regulatory brain-trust on payroll.**
   (a) Evidence: CCO is Chief *Commercial* Officer (ex-VC, not ex-FCA); CTO from spacecraft/energy-trading tech; no compliance-SME or regulatory-content roles ever posted; origin story is radio-ads genAI POC pivoted to finance.
   (b) Confidence: documented (bios, posting history).
   (c) Exploitation: "Who at each vendor owns regulatory interpretation when the FCA/FINRA position is ambiguous — and what's their background?" Contrast with Haast's legal implementation team (and note Saifr/Red Oak run ex-regulator benches — relevant when they're also in the deal).

5. **The "24-hour regulatory updates" claim has no visible machinery.**
   (a) Evidence: appears on homepage only [cached]; no docs page, blog, or press explains the pipeline; implausible as systematic SLA across "100+ bodies" at their size.
   (b) Confidence: documented absence of substantiation.
   (c) Exploitation: discovery question — "when a rule changes, what's the update process, who validates it, and is there an SLA in the contract?" Push to contract language; marketing claims evaporate there.

6. **No regulatory archiving (17a-4/WORM) story — while selling to brokers.**
   (a) Evidence: no 17a-4/WORM/books-and-records claims; no Global Relay/Smarsh integrations; customer base includes IG, NinjaTrader, Freetrade (all under books-and-records regimes).
   (b) Confidence: documented absence.
   (c) Exploitation: same records-path landmine as Blee — "how do review decisions get into your compliant archive?"

7. **Certifications claimed without public evidence.**
   (a) Evidence: ISO 27001/SOC 2 Type II/Cyber Essentials Plus asserted on homepage [cached]; no auditor, scope, cert number, or trust-center URL; trust./security. subdomains don't resolve [live-DNS].
   (b) Confidence: documented absence of evidence (certs may well be real — Vanta-style attainment is feasible).
   (c) Exploitation: soft probe, not an accusation: "ask every vendor for the SOC 2 report and ISO scope on day one." If real, fine; if scoped narrowly (common for young companies), procurement finds it.

8. **Metrics don't reconcile internally.**
   (a) Evidence: "review times drop over 90%" vs "88%" in the same materials; "first-time approvals triple to 90%+" vs Flagstone case at 77.5% and IG's press metric being "87% *within target timeframes*" (an SLA stat, not first-time approval); Plum story told as 5 days→1 day AND 10 days→same-day in different outlets; "-44% cost per review" with no source at all; "18x output" is one customer's best case promoted to a platform stat.
   (b) Confidence: documented inconsistencies.
   (c) Exploitation: "walk me through the 44%" — then propose measuring both vendors on the buyer's corpus in the POC with agreed definitions.

## 5. Pricing signals

- **Published pricing:** none. No /pricing page exists. Site copy: "pricing is based on volume and workflow configuration," tailored ROI model at demo, "most customers see payback in under 5 months." [Documented, cached]
- **Sales motion:** book-a-demo only; 6-week structured pilot (policy import → workflow mapping → parallel run); no free trial or self-serve. [Documented, cached]
- **Procurement footprint:** nothing on Vendr/Spendflo/AWS Marketplace; no press-reported contract sizes. [Documented absence]
- **Best-guess model + ACV:** volume-based annual SaaS. Blended ACV £20K–£60K; fintech deals £15–30K; bank/broker enterprise plausibly £75K–150K+; total ARR likely under ~£1.5M given a 10x-from-tiny-base claim on a £2.1M seed. Confidence: **low-medium** — triangulated from stage, logo mix, UK regtech comparables. Don't quote figures; use for calibration.
- **How to position price:** they will likely undercut on sticker in any US deal (hungry seed-stage, land-grab mode, weak pound-dollar dynamics). Don't discount into it. Frame: (1) their price buys FCA-shaped review + young monitoring — US depth, monitoring scale, and archiving path still need budget; (2) an 8-person London vendor in a US enterprise stack carries support and continuity costs procurement can quantify (timezone SLAs, escrow, security-review friction); (3) volume-based pricing invites growth-penalty math — model the buyer's content volume at year 3 and compare. Sell certainty per dollar.

## 6. Customer complaints

**Zero independent complaint data exists.** No G2, Capterra, TrustRadius, GetApp, Software Advice, Product Hunt, or Trustpilot listing (searches returned only the ad-blocker and AdClarity collisions); no Reddit or HN threads; no critical press. All customer voice is vendor-site testimonials and vendor-supplied press quotes. [Documented absence]

- **Usable reframe (same as Blee, and it's honest):** "For each shortlisted vendor, can you find one independent customer review? For this one the public record is 100% company-authored."
- **Watch-list for next quarterly run:** first negative Glassdoor/G2 entries, any churn signals from the early fintech cohort (Plum, Yonder, Creditspring renewals would be coming up), and whether the "UK's biggest neobank" ever gets named.
- Their own numbers concede review imperfection nowhere — unlike Blee's 85–95% accuracy band, Adclear publishes no accuracy/false-positive figure at all. Absence of an accuracy claim is its own probe: "what precision/recall will you commit to on our corpus?"

## 7. Ex-employee signals

- **Organizational health:** effectively zero signal — expected at 8 people, 2 years old. The only Glassdoor "AdClear" employer with reviews (2 reviews, 5.0) lists Berlin HQ — that's the unrelated German ad-blocker; excluded. No Indeed presence attributable to Adclear Ltd. No visible departures, alumni, or "my time at" posts. [Documented absence]
- **Product/market truth from former staff:** none available.
- **Deal-relevant inference (marked as inference):** at this headcount there *are* no ex-employees to speak of — org-health intelligence is structural, not testimonial: sole-digit headcount, founder-screened hiring (applications to the CCO's personal address), below-market cash comp with equity weighting (£27–30K Founders Associate), all consistent with disciplined but very thin operating capacity. Use §4 gaps 3–4 instead of ex-employee angles.
- Boundary note: nothing resembling confidential disclosure was encountered; the Berlin-HQ Glassdoor profile was excluded as misattributed, not as confidential.

## 8. Where they win (honest)

- **UK deals, full stop, are hard to win against them right now.** FCA AI-programme credential + RegTech of the Year (UK FinTech Awards 2026) + Lloyds/IG/PensionBee logos + FCA-native content engine + UK certifications (Cyber Essentials Plus) — for a UK-HQ'd fintech buying finprom review, they are the safe local choice.
- **High-velocity fintech/trading/crypto marketing teams** — Slack/Figma-native workflow, "seconds" review speed, Discord/Telegram monitoring (nobody else in this run covers those channels), partner/affiliate workspaces. If the buyer's pain is influencer/affiliate content volume, their NinjaTrader story lands.
- **Consumer Duty-driven UK insurance/lending deals** — Marshmallow gives them a beachhead reference we should not pretend away.
- **Price-led evals** — seed-stage land-grab pricing beats us on sticker.
- **Disqualify/reframe rule:** UK-only buyer + finprom-only scope + price-sensitive = their kill zone; qualify hard or reframe to multi-jurisdiction/full-lifecycle early. US-led buyer, FINRA obligations, enterprise procurement = our kill zone; accelerate and force depth-proof.

## 9. Landmines (discovery-question form — never name Adclear)

1. Ask: **"For your US content, how important is it that the vendor's FINRA and SEC rule coverage is documented and referenceable — not just listed on a website?"** → US depth is a homepage list; docs have zero SEC/FINRA content; one US customer since Apr 2026 (§4.1).
2. Ask: **"How long has each vendor's post-publication monitoring been in production, at what scale, and can they name a reference using it?"** → Monitoring was on their seed-round roadmap in Nov 2025; no reference, no coverage spec (§4.2).
3. Ask: **"What does support look like in your timezone — named contacts, SLAs, escalation — and how many people actually staff it?"** → 8 people, all London (§4.3).
4. Ask: **"When regulatory guidance is ambiguous, whose regulatory expertise at the vendor makes the interpretation call — and what's their background?"** → No ex-regulator or compliance SME on the team; commercial co-founder runs accounts (§4.4).
5. Ask: **"When a regulation changes, what's the documented process and contractual SLA for updating rules — not the marketing claim, the contract language?"** → "24 hours" appears nowhere but the homepage (§4.5).
6. Ask: **"How do approved-content records reach your books-and-records archive, and which archiving systems does each vendor integrate with?"** → No 17a-4/archiving story despite broker customers (§4.6).
7. Ask: **"Can we agree that headline metrics get re-measured on our own content during the pilot, with definitions we set?"** → Their 90%/88%/77.5%/44% numbers don't reconcile (§4.8).

## 10. Objection-handling angles

**When Adclear is shortlisted or incumbent — what your champion will hear:**

1. *"They're the FCA specialists — award-winning, FCA-programme graduates."* → Reframe: "Genuine UK credentials — and that's exactly the question: specialist *where*? Their own funding release says EU/US coverage was 'recently expanded'; their documentation contains no SEC or FINRA material at all. For a US book of business, ask the specialist question in reverse: show us the FINRA 2210 depth, live."
2. *"They cover 100+ regulatory bodies — more than anyone."* → Reframe: "Count the evidence, not the list: every public case study is FCA-regime; the full regulator list is gated in a customer-only hub; APAC/MENA were 'coming months' in their own PR. A 3-founder, 8-person team cannot maintain 100+ regimes at examination depth. Coverage lists are free; ask both vendors to run your corpus under *your* regulators."
3. *"They monitor published content too — full lifecycle, same as anyone."* → Reframe: "Monitoring shipped within the last year — it was a roadmap line in their November 2025 funding announcement — and their documentation scopes it to websites, affiliates, Discord and Telegram. Haast's monitoring is a founding capability across the full social estate. Make both vendors monitor your actual live footprint for two weeks of the pilot and compare what gets caught."
4. *"They're cheaper and faster to start — pilots in 6 weeks, reviews in seconds."* → Reframe: TCO + growth math from §5: volume-based pricing compounds with content growth; US support from London has hidden costs; and 'seconds' is review latency, not time-to-value — their own pilot is six weeks, ours delivers configured regulator agents on go-live.
5. *"Lloyds and IG use them."* → Reframe: "Look at the scope words: 'marketing teams at' Lloyds; IG is a UK&I rollout. These are team-level UK deployments, not enterprise contracts. Ask for a reference matching your profile — US entity, enterprise scale, monitoring in production. There is exactly one named US customer, signed April 2026."
6. *"They're SOC 2 and ISO certified."* → Reframe: "Good — request the SOC 2 report and ISO scope on day one, as you should from us too. Theirs has no public trust center, auditor, or scope statement; young-company certifications are often narrowly scoped. Let the reports speak."
7. *"They're the momentum player — 10x ARR, award, new logos monthly."* → Reframe: "10x from an undisclosed base ten months after a £510K pre-seed is a small absolute number. Momentum is real — so is the load: EU, US, APAC, MENA, monitoring, and insurance, all on 8 people and $3.4M. Ask which commitments in *your* contract survive that math."

**FUD they will plant about Haast — pre-armed responses:**

| Their likely line (from their documented framing) | Your response |
|---|---|
| "Haast is a horizontal enterprise platform; we're finprom specialists — depth beats breadth" [their comparison framing, cached] | "They claim 15+ regulators and 100+ bodies on the same homepage — specialist and everything-everywhere don't coexist. Haast ships regulator-specific agents (FINRA/FTC/FCA), so 'horizontal' ≠ generic. And your compliance risk doesn't stop at ads — comms, disclosures, and live-estate drift are the same buyer's problem, which a finprom-only tool leaves open" |
| "We're FCA-native; Haast is Australian" | In UK deals, concede their FCA home turf and move the frame to lifecycle + multi-entity coverage. In US deals, mirror it: "we're both non-US vendors — one of us has FINRA/FTC agents in production, a US expansion funded with $6M, and an AWS-published architecture; the other has one US customer and a blog post" |
| "Enterprise platforms take months; we deploy pilots in 6 weeks" | "Our 8–12 weeks encodes your policy manual with a legal implementation team; their 6-week pilot imports your rules — *you* supply the regulatory content. Ask what's actually configured at their go-live and who maintains it" |
| "Reviews in seconds vs legacy workflows" | Review latency is table stakes for every AI vendor in this category, us included. Move the metric to precision/recall on the buyer's corpus — they publish no accuracy figure at all |
| "We're certified (ISO/SOC 2/Cyber Essentials Plus)" | Match with Haast's security pack (verify internally first) and request theirs with scope + date. No public trust center exists on their side |
| "Award-winning: RegTech of the Year" | "UK FinTech Awards — a UK-market award for a UK-market product. Relevant if you're buying for the UK; ask what it evidences for FINRA coverage" |

## 11. MEDDPICC angles

- **Metrics:** anchor on what they can't measure or won't commit to — precision/recall on the buyer's corpus (they publish no accuracy number), % of live estate under continuous monitoring with detection latency (no monitoring reference exists), US rule-coverage depth demonstrated on FINRA 2210 test content, contractual rule-update SLAs (their 24-hour line is homepage-only). Offer to put our numbers in the pilot success criteria in writing.
- **Decision criteria to install:** (1) documented + demo-verified US regulator depth; (2) monitoring maturity — production references, scope spec, scale test; (3) vendor regulatory expertise on staff; (4) support model in buyer's timezone with named humans; (5) evidence-backed metrics with agreed definitions; (6) records path to compliant archive. They struggle on all six in a US enterprise context.
- **Pain they leave unsolved:** US regulatory examination readiness; live-estate assurance at enterprise scale; non-promotional regulated content; the "who interprets the grey areas" question; books-and-records integration.
- **Paper process / procurement:** our leverage — no public trust center or audit evidence (security review friction), 8-person London vendor supporting US enterprise (SLA/timezone/continuity clauses; escrow), volume-based pricing (growth-penalty modeling), no marketplace paper (procurement starts from scratch). Their leverage — certifications on paper (if reports check out), fast pilot paper, hungry pricing; counter with diligence depth, not speed.
- **Champion note:** their pitch is dual-sided (marketing speed + compliance control) and lands well with UK-style compliance officers. In US deals, elevate to the CCO/GC with examination-readiness framing — that's terrain their team composition can't contest.

## 12. Sources

Provenance: **[cached]** = search-engine-indexed/cached content (direct fetch blocked — ground rule 5); **[live-DNS]** = DNS resolution observed during fetch attempts. Adversarial items flagged. Accessed 2026-08-04.

**Adclear-owned** (all [cached]): adclear.ai home (metrics, regulator list, 24h claim, certs, pricing copy, Regulations Hub) · /product ("Real-Time FCA Ad Review"; pre+post claim; channels) · /about · /insights + blog posts (finfluencer-marketing-sec-finra-compliance Jun 29 2026; fca-annual-report-2025-26; Allica/Yonder podcast posts) · /case-studies/how-adclear-helped-plum-cut-approval-times · /case-studies/how-investengine-saves-over-520-hours-a-week · /adclear/founding-engineer + /founders-associate (comp bands) · /adclear/resouces/resources (typo'd production slug) · docs.adclear.ai (Adclear Manual: /introduction, /user-guide/compliance/reviewing-campaigns, /dashboard — review workflow, self-approvals, monitoring scope incl. Discord/Telegram) · status.adclear.ai · jobs.ashbyhq.com/adclear (Growth Marketer)
**Subdomain findings** [live-DNS]: docs/status/app/api/help resolve (help dormant on super.so); changelog, trust, security do NOT resolve.

**Funding/press** (all [cached]): fintech.global 23 Jan 2025 (pre-seed £510K) + 13 Nov 2025 (seed; **"post-publication monitoring" as roadmap; EU/US "recently expanded"; APAC/MENA "coming months"; "8-strong team"**) + 20 Jul 2026 (Marshmallow) · tech.eu, ffnews, techfundingnews, fxnewsgroup, cityam ("dodge FCA fines"), financialit, thepaypers, uktechnews, cfotech (seed variants) · haatch.com investment note · outwardvc.com why-we-invested + in-conversation-with-adclears-founders · tenity.com · foxwilliams.com (deal counsel, 27 Nov 2025)

**Customer deals** (all [cached]): finextra.com/pressarticle/108744 (IG — **UK&I rollout scope; "87% within target timeframes"**) · finextra.com/pressarticle/109341 + financemagnates + tradeinformer + channellife (NinjaTrader — only named US customer; influencer/affiliate/OOH) · itbrief.co.uk + cmotech.uk (Flagstone — 2d→8h; **77.5% first-time approval**) · regtechanalyst + insurance-edge + itbrief (Marshmallow Jul 2026) · thepaypers (Intelligent Lending Group)

**Founders/company** (all [cached]): preseednow.com/p/adclear (origin story) · fintechforum.de Doni Hoti Q&A (3 Dec 2025) · fintechprofile.com Joe Jordan (CCO = commercial; ex-Supernode Global) · LinkedIn founder/company pages · ukfintechawards.co.uk/2026-winners + /shortlist-2026 (RegTech of the Year, Apr 23 2026) · tracxn/pitchbook/cbinsights/crunchbase profiles

**Competitive mapping** (all [cached]): cbinsights.com/compare/adclearai-vs-red-oak-compliance-solutions · cbinsights.com/company/haast/alternatives-competitors (lists Adclear as top Haast competitor) · adclear.ai vs-Haast comparison copy — **URL unconfirmed, verify live** · hellowarrant.com roundup (Adclear absent) · g2.com/products/adclear-adclear (miscategorized as DAM — noted, not used)

**Excluded collisions:** AdClear GmbH ad-blocker (Glassdoor E1973457 Berlin-HQ profile, ZoomInfo, SoftwareSuggest, Slashdot, allaboutcookies.org) · AdClarity (G2/Capterra/GetApp) · "AdClear Digital Marketing" (India) · CB Insights "New York, founded 2022" datapoint (conflated entity).

**⚠ Verify live before quoting in a deal:** (1) the "Adclear vs Haast" comparison page — capture URL + exact wording; (2) current homepage metric set (88 vs 90+ has already drifted once); (3) whether APAC/MENA coverage ever shipped; (4) the extended customer names circulating in snippets (NatWest, Monzo, Scottish Widows, Kraken, Coinbase) — all unverified, do NOT repeat them.
# BATTLECARD: Saifr (saifr.ai)

**Run date:** 2026-08-04 · **Refresh by:** 2026-11-04 (quarterly) · **Prepared for:** Haast US sales
**Provenance note:** direct page fetches were blocked by the research environment's egress proxy this run — claims are sourced from search-engine-indexed/cached versions of cited pages (ground rule 5), tagged **[cached]**. Competitor-authored sources (Luthor, Sedric) are tagged **[competitor]** — verify before using externally. Spot-check live pages before quoting verbatim; list in §12.

---

## TL;DR for the 2-minute pre-call read

Saifr is the pedigree play: a Fidelity Labs-incubated, FMR-owned "brand" (not an independent company) selling pre-publication AI review trained on 15–20 years of Fidelity's internal compliance corpus, fronted by ex-SEC/FINRA staff attorneys and a "Grammarly for compliance" story. Real strengths: multimodal review (text/image/video/audio), SOC 2 Type 2, an SEC 17a-4-compliant storage claim, FINRA filing assistance, and enterprise distribution embeds (Microsoft, Adobe, ServiceNow, Superhuman). Beatable because: **no post-publication monitoring of live marketing content** (their "continuous monitoring" is adverse-media screening of *people*), **US-only regulator coverage** (zero FCA/ASIC/EU evidence), **their models not your rules** (no self-serve rule authoring for marketing review), **zero named customers anywhere**, **no net-new product since May 2024**, and a **Fidelity conflict-of-interest question** their own privacy policy hands you. They don't name competitors and have no vs-pages — you can define the comparison frame first.

---

## 1. Company snapshot

| Item | Finding | Confidence |
|---|---|---|
| Structure | **Not an independent company.** Per their own privacy policy: "a standalone brand representing a subset of services provided by Fidelity Labs, LLC and Saifr.ai LLC, subsidiaries of FMR LLC" (Fidelity Investments' parent). Built from ~2020 inside Fidelity Labs; publicly launched Jan 24, 2022 | Documented [cached] |
| HQ / CEO | Boston; CEO Vall Herard (NYC-based, "co-founder" framing despite corporate ownership; Crain's NY Notable Leaders in Finance 2025) | Documented [cached] |
| Funding | No external funding — Fidelity-funded (Tracxn/Crunchbase: no rounds). Acquired Giant Oak's GOST platform Feb 2024 (adverse media screening), terms undisclosed | Documented [cached] |
| Headcount | ~30 (Tracxn, May 2026) vs 51–200 band (ZoomInfo/LinkedIn); staff often carry Fidelity Labs affiliations so counts are muddy. Best read: ~30–60 dedicated | Weak-medium (vendor estimates) |
| Customers | **Zero named customers.** Anonymized case studies only ("fintech platform with $4T+ AUM on platform," 50 seats, live Dec 2022; "large financial services firm"). 6sense telemetry: ~11 identifiable companies (8 US), skew wealth/investment mgmt/life insurance | Documented (absence + telemetry) |
| ICP | Enterprise/mid-enterprise US financial services: asset managers, broker-dealers, wealth platforms, fintechs distributing regulated products; deliberate second beachhead in life insurance & annuities (Jun 2025 insurance agent) and banks/AML via ServiceNow. Not an SMB/RIA motion | Strong inference |
| Pricing model | No public pricing; contact-sales. Third-party "$500/month starting" figure traces to competitor Luthor's buyer guide — unreliable. Best guess: annual enterprise SaaS, seats + usage hybrid; ACV ~$50K–$250K+, lighthouse deals higher | Model strong inference; figures low-medium |
| Products | SaifrReview (pre-pub workflow), SaifrScan (Office add-ins/REST APIs), SaifrScreen (adverse media/sanctions — from GOST), Saifr eComms (comms surveillance, May 2024), insurance review agent (Jun 2025) | Documented [cached] |

## 2. Positioning + narrative

- **One-liner:** "Saifr redefines how compliance operates with advanced AI technology, the right data, and deep industry expertise." Street version: **"Grammarly for compliance"** — real-time compliance spell-check inside authoring tools, pre-publication. [Documented, cached]
- **The moat claim (their whole pitch):** models trained on "tens of millions of compliance-reviewed data records" — "20+ years of work by thousands of marketing and compliance experts," seeded with 15+ years of Fidelity's internal compliance-reviewed documents. Herard's line: generic LLMs hallucinate in regulated domains; "only partner with AI providers operating on robust and proprietary data." [Documented, cached]
- **Accuracy claims (note the drift):** site copy says AI "identifies as much as 90% of what a human reviewer would"; Herard says "93% to 95% as effective as a human compliance officer" in interviews. No published methodology for either. [Documented, cached]
- **2024→2026 repositioning:** from "RegTech tools" to **"AI agents for compliance"** — boilerplate in every recent release. Strategy is "agents embedded everywhere": Azure AI Foundry + M365 E5 (May 2025), Adobe GenStudio (Mar 2025), ServiceNow FSO (Jun 2025), Superhuman/ex-Grammarly Go agent (Jan 2026, private preview, GA "late Q1 2026"). The bet: AI-generated content explodes review volume; Saifr becomes the guardrail inside other platforms. [Documented, cached]
- **Who they position against:** nobody by name. They frame competition as manual review and generic LLMs. **No vs-pages, no competitor mentions, no Haast mentions anywhere.** Challengers (Luthor, Sedric, Blee) name Saifr; Saifr names no one. You can define the head-to-head frame before they do. [Documented absence]

## 3. Feature matrix vs. Haast

Haast column = public claims (haast.io, AWS case study); verify internally.

| Capability | Saifr | Haast | Notes |
|---|---|---|---|
| Pre-publication review | **Yes — core strength.** Create→review→approve→file workflow (SaifrReview) + point-of-creation checks (SaifrScan add-ins, APIs, partner embeds); suggested compliant language and disclosure recommendations | Yes | Mature; don't attack the review workflow itself |
| Post-publication monitoring of live marketing content | **No.** SaifrReview/Scan are pre-pub. Their "continuous monitoring" language = SaifrScreen (adverse media on *people/entities*) and eComms (surveillance of *archived* communications) — not live web/social content monitoring. Two independent third-party guides state they lack live website monitoring [competitor, corroborates absence in Saifr's own materials] | **Yes — founding capability**: continuous monitoring of live websites + social + partner channels | **The #1 landmine — and buyers will conflate their monitoring language. Force precision: "monitoring of what, exactly?"** |
| Channels/media | Text, images, video (MP4), audio with built-in transcription — genuinely multimodal | Text, images, PDFs, docs, long-form video, web | **Don't lead with channel breadth — theirs is real.** Lead with lifecycle position |
| Rule building / customization | **Their models, their tuning loop.** Saifr's data-science team updates models when regs change; only documented client-specific adaptation is "risk relevancy models" for SaifrScreen (not marketing review). No self-serve rule authoring found for SaifrReview | Bespoke org frameworks + self-serve per-asset rule config + legal implementation team (Equity Trustees: 80+ custom rules) | Killer question: "Whose interpretation of FINRA 2210 is in the model — yours or Fidelity's — and who encodes MY style guide?" |
| AI review depth | 90% / 93–95% efficacy claims, no methodology; human-in-the-loop SME validation claimed | Regulator-trained agents; AWS-published architecture (Bedrock); POC-measurable | Their number drifts between their own materials — push to measured POC |
| Disclosures/disclaimers | **Yes — documented strength**: recommends needed disclosures, drafts with proper disclosures included | Claimed within review workflows | Parity-to-their-advantage on paper; check Haast internal depth before contesting |
| Audit trail / recordkeeping | **Strong on paper**: tracks entry→approval→filing, storage claimed **SEC 17a-4 compliant**, FINRA filing assistance | Full audit trail | **First competitor in this run with a real records story — do NOT run the Blee/AdClear 17a-4 landmine here.** Verify their claim's scope in deals instead |
| Integrations | Microsoft (Azure AI Foundry, M365 E5), Adobe GenStudio, ServiceNow FSO, Superhuman Go (private preview Jan 2026), Pinpoint (2023), Office add-ins, REST APIs. No archiving-vendor partnership (Smarsh/Global Relay) announced; no CMS/DAM/scheduler/PM-tool claims | Figma, Office365, Workfront, Google Docs + API | Their embed list is enterprise-impressive but new and partly pre-GA — ask for production references per integration |
| Deployment | No public implementation-time claim; enterprise POC-heavy motion (data-science sales engineers on staff); Fidelity-grade procurement | 8–12 weeks with regulator agents live day one | Their silence on timelines lets you anchor the number |
| Regulator coverage | **US only**: FINRA 2210, SEC 482, SEC Marketing Rule; insurance (state/NAIC-style) since Jun 2025; AML side covers AMLD6/BSA/OFAC (screening, not marketing). **Zero FCA/ASIC/EU marketing-rule evidence anywhere**; a blog arguing "principles transcend jurisdictions" is positioning, not coverage | FINRA + FTC + FCA agents; live deployments under ASIC (Telstra, Equity Trustees, Zurich ANZ) and FCA (Aviva) regimes | Multi-jurisdiction buyers: Saifr is single-regime by evidence |
| Security | SOC 2 Type 2 (SaifrReview + SaifrScreen, annual audit) | Table Haast's pack | Parity play; check their eComms SOC 2 scope |
| Proof/validation | Zero named customers; anonymized gated case studies; awards from 2023–2024 only (A-Team, AI Breakthrough); no analyst-report placement found; Kitces publicly questioned efficacy at launch (Mar 2022) | AWS-published case study (500+ hrs saved, 80%+ productivity, 4x capacity), named logos (Telstra, Aviva, Zurich ANZ, Equity Trustees), $6M US-expansion raise (May 2025) + **$12M Series A led by Peak XV w/ DST Global Partners (Apr 2026)**, Zurich Innovation Champion 2024 | "Proven" should mean referenceable deployments, not parent-company logo |

## 4. Feature gaps (ranked for a regulated-industry compliance buyer)

1. **No post-publication monitoring of live marketing content.**
   (a) Evidence: absent from all Saifr materials [documented absence, cached]; SaifrReview/Scan documented as pre-pub only; "continuous monitoring" refers to adverse-media screening (people) and archived-comms surveillance; two third-party guides state no live website monitoring [competitor, x2].
   (b) Confidence: high (multi-source convergence).
   (c) Exploitation: the conflation is the trap — in evals, make them answer "after content is approved and published, what watches it?" Structure POC with live-estate drift detection. Their suite breadth ("we monitor continuously!") dissolves under the precise question.

2. **US-only regulatory coverage.**
   (a) Evidence: every named rule is US (FINRA 2210, SEC 482, Marketing Rule); zero FCA/ASIC/MiFID references across site, PR, and third-party coverage; ~73% of identified customers US (6sense); no international roles posted.
   (b) Confidence: medium-high (consistent absence).
   (c) Exploitation: any buyer with UK/EU/APAC entities — make multi-jurisdiction coverage a scored criterion with regime-specific test content. Haast operates FCA (Aviva) and ASIC (Telstra, Equity Trustees, Zurich ANZ) deployments today.

3. **Their model, their rules — no customer rule authoring for marketing review.**
   (a) Evidence: FAQ describes Saifr's teams fine-tuning/validating models when regulations change; client-specific adaptation documented only for SaifrScreen; no self-serve rule/lexicon authoring found for SaifrReview.
   (b) Confidence: medium (docs silence + consistent third-party characterization).
   (c) Exploitation: "Fidelity's 20 years of data" cuts both ways — it's *Fidelity's* risk appetite and house style baked into the model. Ask: "How does my firm's policy manual, style guide, and risk tolerance get encoded — and is that my team's control or the vendor's data-science backlog?"

4. **Zero named customers, zero independent reviews.**
   (a) Evidence: no logo anywhere; case studies anonymized and gated; no G2/Capterra/TrustRadius listings (Slashdot/SourceForge profiles: 0 reviews); no analyst-report placement found.
   (b) Confidence: documented absence.
   (c) Exploitation: "Ask each vendor for three named, referenceable customers in your segment — and check which vendors have any independent review footprint at all." Haast tables named enterprise references; Saifr structurally can't (or won't).

5. **Platform stagnation behind the partnership noise.**
   (a) Evidence: last net-new products May 2024 (eComms) and Feb 2024 (SaifrScreen via acquisition); Aug 2025–Aug 2026 window contains only distribution embeds and thought leadership; no 2025 press archive indexed; last awards 2024; Superhuman agent still private preview Jan 2026.
   (b) Confidence: strong inference (public record pattern).
   (c) Exploitation: "Ask for the last six months of release notes for the review product itself." Big-company incubation pace vs your funded startup cadence. Announced integrations ≠ shipped outcomes.

6. **The Fidelity question.**
   (a) Evidence: their privacy policy states Saifr "may share information, including personal information, with other Fidelity Labs, LLC companies"; the data-moat pitch itself advertises that the corpus derives from Fidelity's asset/wealth business; their FAQ pre-empts the custody question but no public statement addresses customer-data segregation from Fidelity. No documented case of a firm refusing Saifr on these grounds — this is a *question*, not a fact.
   (b) Confidence: high on the citable hooks; no evidence of actual buyer resistance.
   (c) Exploitation: diligence framing only, never an accusation: "Your unreleased campaigns and compliance judgments flow through a vendor owned by FMR LLC — has legal reviewed the data-handling and IP terms, including the inter-affiliate sharing language in their privacy policy?" Works hardest on asset managers, BDs, and wealth platforms that compete with Fidelity for the same clients.

7. **Sales organization still being built.**
   (a) Evidence: open posting for **VP, Head of SaaS Sales (North America), reporting to the CEO** — i.e., no seated NA sales head at posting time; pre-sales via "data science sales engineers."
   (b) Confidence: medium (single posting, search-indexed).
   (c) Exploitation: not a talk track — a tell. Expect inconsistent sales execution, slow follow-ups, POCs run by data scientists. Outrun them on responsiveness and deal energy.

8. **No CMS/DAM/scheduler/PM-tool integrations; no archiving distribution partner.**
   (a) Evidence: integration list is authoring/platform embeds (Microsoft/Adobe/ServiceNow/Superhuman); nothing for content-ops stack; eComms positioned to integrate with archiving "generically," no named partner.
   (b) Confidence: documented absence of claims.
   (c) Exploitation: map the buyer's content supply chain; every unsupported hop is manual.

## 5. Pricing signals

- **Published pricing:** none; no pricing page exists in their site structure at all. Demo/contact-sales only. [Documented, cached]
- **Marketplace/procurement:** no Vendr/Spendflo/AWS/Azure/GCP marketplace listing found (notable given the Microsoft partnership — the agent is in Azure AI Foundry's model catalog, not a transactable marketplace SKU as far as public evidence shows). [Documented absence]
- **Third-party figure:** "$500+/month starting, for $100M+ AUM orgs" — traces solely to competitor Luthor's buyer guides [competitor]; if real, likely a minimal SaifrScan/API SKU, not a deal price. Do not repeat as fact.
- **ACV proxies:** 50-seat deployment at a $4T-AUM platform; ~11 identifiable customers total (revenue concentration); Fidelity-grade security/procurement posture; competitor positioning as "the expensive enterprise option, cost-prohibitive for small/mid RIAs" [competitor].
- **Best-guess model + ACV:** annual enterprise SaaS, seats (Review) + usage (Scan/API) hybrid, negotiated per firm. **ACV band ~$50K–$250K+, lighthouse deals into high six figures.** Confidence: medium on model, low-medium on band.
- **How to position price:** Saifr won't be the cheap option — price is rarely their FUD, pedigree is. Two angles: (1) **paying for the parent, not the product** — part of the premium buys the Fidelity halo; ask what it buys in *your* deployment (whose team supports you, what SLAs, how many people actually work on this product); (2) **lifecycle-per-dollar** — their spend covers pre-publication only; the live estate still needs a monitoring answer, which with Saifr means a second vendor. On procurement: expect their motion to be slow and Fidelity-shaped; a faster, cleaner paper process is a real Haast advantage — use mutual action plans to make speed visible.

## 6. Customer complaints

**No public complaint data exists.** Zero reviews on every major platform (Slashdot/SourceForge profiles exist with 0 reviews — the only listings anywhere); no Reddit/HN practitioner threads; LinkedIn activity is Saifr's own posts; conference presence is as speaker/sponsor, not discussed vendor. [Documented absence]

- **Only critique-shaped public content:**
  - **Kitces (Mar 2022, independent)**: questioned whether AI tools like Saifr can catch risky content reliably enough — an efficacy skepticism from the most-read advisor-tech commentator. Old, but citable as an independent voice where nothing else exists.
  - **Luthor buyer guides [competitor, single source family]**: enterprise pricing prohibitive for small/mid RIAs; implementation requires internal resources; US-centric; no bundled CCO-expert support; limited post-publication monitoring. Treat as hypotheses, not customer voice.
- **Reframe for deals:** same as the whole AI cohort — "vendor-controlled narrative only; ask for independent proof." For Saifr add: four years on the market, still not one named customer.

## 7. Ex-employee signals

- **Organizational health:** not measurable from public sources — and structurally obscured: Saifr staff are Fidelity Labs/FMR employees, so any Glassdoor/Indeed reviews are buried inside Fidelity Investments' tens of thousands and can't be attributed. No Saifr-specific review page exists. No public departure patterns or "formerly at Saifr" commentary surfaced. [Documented limitation]
- **Product/market truth from former staff:** none found.
- **Deal-relevant inference (marked as inference):** the one visible signal is *retention*, not attrition — Giant Oak's leadership (Harsh Pandya → Head of Product; Jon Elvin → Strategic Risk Advisor) stayed and remain publicly active post-acquisition. Read: the AML/screening line has stable leadership; no visible leadership bleed to exploit. Use §4 gaps 5 and 7 (platform pace, unfilled sales leadership) instead of ex-employee angles.
- Boundary note: nothing resembling confidential disclosure was encountered.

## 8. Where they win (honest)

- **Conservative enterprise buyers who want the safest name in the room.** "Fidelity-backed, ex-SEC/FINRA attorneys, SOC 2, 17a-4 storage" clears vendor-risk committees that would flag any startup — including us. If the buying committee is risk-first and reference-optional, Saifr wins the comfort vote.
- **Microsoft/ServiceNow/Adobe-standardized enterprises.** If the buyer's IT strategy is "everything through our existing platforms," Saifr's embeds are a genuine wedge — the compliance check shows up inside tools already procured.
- **US-only asset managers and broker-dealers with pre-publication-only scope** — their home turf: FINRA 2210/SEC Marketing Rule review with filing assistance, multimodal content, disclosure drafting.
- **Life insurance & annuities (US)** — the Jun 2025 insurance agent plus Fidelity's insurance-relevant corpus; they're investing here deliberately.
- **AML/adverse-media adjacency** — if the buyer wants marketing review AND screening from one vendor, their suite argument has substance (even though the pieces are stapled).
- **Disqualify/reframe rule:** US-only + pre-pub-only + platform-standardized + risk-committee-driven = Saifr's kill zone; reframe to lifecycle coverage and named-reference proof or expect a pedigree loss. Multi-jurisdiction, live-monitoring, or rule-control requirements = your kill zone; force those criteria early.

## 9. Landmines (discovery-question form — never name Saifr)

1. Ask: **"Once marketing content is approved and live — on your site, social, partner pages — what continuously checks it, and how would you catch post-approval edits or stale disclosures?"** → No live-content monitoring exists; their "monitoring" is people-screening and archived-comms surveillance (§4.1).
2. Ask: **"When a vendor says their AI is 'trained on 20 years of compliance data' — whose risk appetite and house style is in that training data, and how does *your* policy manual get encoded and updated, by whom?"** → Fidelity's corpus, Saifr's tuning loop, no self-serve rule authoring (§4.3).
3. Ask: **"Which non-US regulators does each vendor cover with evidence — rule packs, references, live deployments — not principles?"** → US-only by all evidence (§4.2).
4. Ask: **"How many *named* reference customers will each vendor provide, and can you find a single independent review of them anywhere?"** → Zero named customers in four years; zero reviews (§4.4).
5. Ask: **"Can each vendor share the last six months of release notes for the review product — not partnership announcements?"** → Platform stagnant since May 2024; noise is distribution embeds (§4.5).
6. Ask: **"If a vendor is owned by a firm you compete with, what data-handling, IP, and affiliate-sharing terms would your legal team need to see?"** → FMR ownership + privacy-policy inter-affiliate sharing language (§4.6). Deploy only with buyers who actually compete with Fidelity.
7. Ask: **"For each integration a vendor advertises, is it GA with production customers, or announced/preview?"** → Superhuman agent private preview; ask for per-integration references (§3, §4.5).

## 10. Objection-handling angles

**When Saifr is shortlisted or incumbent — what your champion will hear:**

1. *"They're Fidelity — nobody gets fired for buying Fidelity."* → Reframe: "You're not buying Fidelity; you're buying a ~30–60-person brand inside Fidelity Labs, with no named customers after four years and a sales leadership role still being filled. The safety you want is *evidence*: named references, an AWS-published case study, measurable POC results — we'll put all three on the table this week. Also worth asking legal: the affiliate data-sharing language in their privacy policy, given you compete with their parent."
2. *"Trained on 20 years of Fidelity compliance data — no one can match that."* → Reframe: "That corpus is one firm's historical interpretations — Fidelity's risk appetite, not yours. The question that matters in 2026 isn't whose archive is older; it's who encodes *your* policies fastest and lets *your* team control the rules. That's architecture, not archaeology — and it's measurable in a two-week POC on your content."
3. *"Ex-SEC and FINRA attorneys built it."* → Reframe: "Genuine expertise — concede it. Then ask where it lives: in their internal model-tuning backlog, or in rules your team controls? And ask what FINRA expertise covers when your UK entity's financial promotions are the exposure — their coverage evidence stops at the US border."
4. *"They're a full suite — review, screening, surveillance."* → Reframe: "Three products for three different buyers (marketing compliance, AML, surveillance) — one of them acquired, none of them monitoring your live marketing estate. Suite breadth that skips the highest-exposure gap — published content drifting out of compliance — is breadth in the wrong direction."
5. *"They're embedded in Microsoft and ServiceNow — that's our stack."* → Reframe: "Embeds are checkpoints at creation — valuable, and we integrate with the authoring stack too. But ask for a named production customer per integration (one was still in private preview in January 2026), and ask what happens after the content leaves Word. Compliance risk lives on your website and social channels, not in the draft."
6. *"90%+ as effective as a human reviewer."* → Reframe: "Their own numbers move — 90% on the site, 93–95% in interviews, no methodology for either. Precision and recall get measured on *your* corpus with agreed definitions in the pilot, and we'll commit to that in writing. Push both vendors to."
7. *"They're 17a-4 compliant and SOC 2 — startups aren't."* → Reframe: don't contest what's true; match it. Table Haast's security pack and records story immediately (verify internal 17a-4/archiving posture first — see note in §3). Then move the frame back to lifecycle and jurisdictions where their paper doesn't reach.

**FUD they will plant about Haast — pre-armed responses:**

Saifr doesn't name competitors publicly, so expect *implication* rather than direct attack — pedigree criteria designed to age out startups:

| Their implied line | Your response |
|---|---|
| "Generic LLMs hallucinate; only proprietary-data vendors are safe" (their standing thesis) | Haast isn't a wrapped generic LLM — regulator-specific agents, architecture published in an AWS case study, tuned to each org's frameworks (80+ custom rules at Equity Trustees). And 'proprietary data' here means one firm's archive; ask how it learns *your* firm |
| "We're built by compliance people; startups are built by engineers" | Haast's implementation runs with legal/compliance teams (GC-level engagement documented); measured outcomes, not résumés: 500+ hours saved, 80%+ productivity gain in the AWS-published study |
| "Foreign startup risk — will they be here in five years?" | $12M Series A led by Peak XV with DST Global Partners (Apr 2026) on top of the $6M US-expansion round (May 2025); named enterprise customers on three continents. Then mirror gently: after four years, ask them for one named customer |
| "We're the enterprise-safe choice — SOC 2, 17a-4, Fidelity infrastructure" | Match the security pack, then the diligence flip: "safe" includes data governance — review the inter-affiliate sharing terms with legal, given the parent competes with you |

## 11. MEDDPICC angles

- **Metrics:** own what they can't measure — % of live estate continuously monitored, time-to-detection of post-publication drift, multi-jurisdiction rule coverage demonstrated on regime-specific test content, POC precision/recall with agreed definitions (their 90/93/95% claims have no methodology), named-reference count. Offer written commitment to POC measurement.
- **Decision criteria to install:** (1) full-lifecycle coverage demoed live; (2) non-US regulator evidence (not principles); (3) customer-controlled rule authoring with change SLAs; (4) named references in the buyer's segment; (5) release-note velocity on the review product; (6) data-governance terms review (affiliate sharing). Saifr fails or strains on all six.
- **Pain they leave unsolved:** post-approval drift on the live estate; non-US obligations; "our policies, not Fidelity's" encoding; the second-vendor problem for monitoring; speed of product evolution.
- **Paper process / procurement:** their friction — Fidelity-shaped contracting (likely slow, rigid paper through FMR entities; inference), inter-affiliate data terms your legal team will actually want to negotiate, no marketplace paper found despite the Microsoft story. Your leverage — faster security review turnaround, cleaner DPA, mutual action plan that makes their pace visible. Their leverage — enterprise-grade paper that clears risk committees; don't promise what Haast's pack can't match, verify first.
- **Champion note:** Saifr's buyer gravity is the CCO/vendor-risk committee. Your champion needs ammunition for the risk conversation (security pack, references, Series A, AWS study) more than the feature conversation. Arm them for the meeting you're not in.

## 12. Sources

Provenance: **[cached]** = search-engine-indexed/cached content (direct fetch blocked — ground rule 5). **[competitor]** = competitor-authored, verify before external use. Accessed 2026-08-04.

**Saifr-owned** (all [cached]): saifr.ai — home, /saifrreview, /saifrreview-insurance, /saifrscreen (+trust-screening), /saifrecomms, /solutions-landing-page, /partners (+/microsoft-azure, /servicenow, /superhuman), /about, /faqs (custody FAQ; model-training/tuning descriptions), **/privacy-policy (FMR-subsidiary structure; inter-affiliate sharing language)**, /client-support, /fair-use-policy (gated developer docs referenced), /case-studies, /careers (**VP Head of SaaS Sales NA posting**), /press + 2022/2023/2024 archives (no 2025 archive indexed), blog (saifrs-mission, "startup with 15 years of experience," 2026-trends, FINRA-report commentary, video/audio reviews, "principles transcend jurisdictions") · insights.saifr.ai (anonymized case studies: fintech platform $4T+ AUM/50 seats; finserv firm; "From Caution to Action" survey) · SaifrReview data sheet PDF (Feb 2025)

**Fidelity/Saifr PR** (all [cached]): newsroom.fidelity.com — launch (Jan 24 2022), Giant Oak GOST acquisition (Feb 20 2024) · businesswire — offerings expansion/eComms (May 7 2024), Superhuman integration (Jan 13 2026; **private preview, GA "late Q1 2026"**), NSCP keynote (2023), Pinpoint (Apr 2023) · prnewswire — Adobe GenStudio (Mar 2025), Microsoft agent (May 20 2025), ServiceNow (Jun 12 2025), insurance AI agent (Jun 30 2025), adverse-media launch (May 2024), AI Breakthrough award (2024)

**Independent/trade** (all [cached]): kitces.com AdvisorTech March 2022 (efficacy skepticism) · a-teaminsight.com (CEO buy-vs-build interview; GOST coverage; marcomms due-diligence piece) · thefr.com (Herard "93–95%" quote) · investmentnews.com + financial-planning.com (launch; "Grammarly for compliance" comparison) · Eye on AI #235, Compliance Podcast Network, Authority Magazine, pulse2.com, globalfintechseries (Herard interviews) · store.servicenow.com SERI listing (230K+ sources, 23B+ webpages — most concrete public spec) · crainsnewyork.com (Herard 2025) · NSCP speaker pages (Herard, Pandya)

**Data vendors** (estimates; all [cached]): tracxn (30 employees May 2026; no funding rounds) · zoominfo (51–200) · 6sense (~11 customers, industry mix) · crunchbase · theorg.com

**Competitor-authored** (all [cached] [competitor]): luthor.ai buyer guides ($500/mo figure; "cost-prohibitive for RIAs"; "no live website monitoring"; "no CCO support") · sedric.ai performline-alternatives ("emphasizes pre-publication review… FINRA 2210, SEC Marketing Rule")

**Review-site absence** (documented negatives): no G2/Capterra/TrustRadius/GetApp/SoftwareAdvice/ProductHunt listings; slashdot.org + sourceforge.net Saifr profiles with 0 reviews; no Reddit/HN threads surfaced.

**Haast baseline** (all [cached]): aws.amazon.com/solutions/case-studies/haast-case-study/ · morningstar.com PR (Apr 2026 — **$12M Series A, Peak XV, DST Global Partners**) · fintech.global (May 2025, $6M) · itbrief.com.au + financialnewswire.com.au (Equity Trustees, Telstra/Aviva/Zurich ANZ) · haast.io case studies.

**⚠ Verify live before quoting in a deal:** (1) the 17a-4 compliance claim's exact scope on their current SaifrReview page; (2) whether the VP SaaS Sales NA role is still open (tell may expire); (3) Superhuman agent GA status; (4) the privacy-policy inter-affiliate sharing wording (quote it exactly or not at all); (5) any new FCA/international coverage since this run.
# BATTLECARD: PerformLine (performline.com)

**Run date:** 2026-08-04 · **Refresh by:** 2026-11-04 (quarterly) · **Prepared for:** Haast US sales
**Provenance note:** direct fetches were blocked by the research environment's egress proxy — claims sourced from search-engine-indexed/cached versions of cited pages (ground rule 5), tagged **[cached]**. Employee-review quotes are Glassdoor excerpts via search index — attribute as *employee* testimony, never as customer complaints. Competitor-authored items tagged **[competitor]**. Verify-live list in §12.

---

## TL;DR for the 2-minute pre-call read

PerformLine is the 19-year incumbent of US consumer-finance marketing compliance: omni-channel monitoring (web, social, **calls, messages**, email, documents — now "AI responses"), the Kraken crawler, 1.1B+ lifetime observations, "6 of the top 10 US banks," and a real moat in bank-fintech/BaaS partner monitoring. It is also a company mid-transition: founder Alex Baydin left the CEO seat Jan 2026 for an operator with exit experience, M33 Growth injected more capital "for AI expansion," two CFOs churned in a year, and employees describe an under-invested product propped up by manual CS heroics. **Their genAI pre-publication product is weeks old (July 13, 2026)** — you are genAI-native competing against a genAI retrofit. Do NOT say "they have no AI" (real Bedrock LLM work exists) or "they're US-only" (a UK/FCA customer story exists). Win by moving the scoresheet from *coverage* (their criteria) to *judgment* — accuracy, false-positive rates, pre-pub depth, self-serve rules, multi-jurisdiction reasoning.

---

## 1. Company snapshot

| Item | Finding | Confidence |
|---|---|---|
| Founded / HQ | 2007, Morristown NJ. Founder Alex Baydin (CEO 2007–2025, now board) | Documented [cached] |
| Leadership (new) | **CEO Chris Calhoun since Jan 5, 2026** — ex-CEO Americas of Treasury Intelligence Solutions, "guided a successful transaction in 2024." CFO churn: Kristie Goodgion (Nov 2024) → Jim Corr (Feb 2026). CTO Byron Lee (2021, ML background). CRO John Zanzarella + VP Product Margaret Tuohy ("AI innovation") Apr 2025 | Documented [cached] |
| Funding/ownership | Lightly capitalized: ~$6.4–9.7M disclosed equity over its life + $5M debt (2019); M33 Growth strategic investment May 2021 + **additional M33 money Jan 2026 "for AI product expansion"** (amounts undisclosed). Acquired LashBack (email compliance) Jul 2022. Bootstrapped to ~$20M ARR per founder interviews (~2022) | Documented [cached]; ARR from founder interview |
| Exit posture | Operator CEO with transaction experience + growth-equity investor ~5 years into hold + CFO refresh = classic pre-liquidity-event professionalization. **Inference, medium confidence** — no sale-process reporting exists | Inference |
| Headcount | ~39 (2021) → 53 (Dec 2022) → ~69–89 (2026, now incl. Asia/Oceania — offshore hiring signal). Slow growth; no layoffs found | Medium (data vendors) |
| Revenue | Estimates $12.7M–$19M (Growjo/RocketReach/Prospeo) vs founder's ~$20M ARR claim | Weak (estimates) |
| ICP | Enterprise US consumer finance: partner/sponsor banks overseeing fintech programs (dedicated BaaS page), mortgage, cards, BNPL; secondary: insurance, credit unions, gig, higher ed. AE job posting confirms: enterprise FS, 6+ month deal cycles | Documented [cached] |
| Pricing model | No public pricing; per-channel/module packaging (each channel is a separate product). Est. ACV ~$40K–$150K+, big multi-channel bank deals $200K+ (inference from revenue ÷ ~100–300 accounts). No Vendr/Spendflo benchmarks exist | Model strong inference; band medium-low |

## 2. Positioning + narrative

- **One-liner (post-rebrand):** homepage title is now "**AI** Marketing Compliance Software for Growth" — the AI-led rebrand is recent. Fuller frame: "end-to-end marketing compliance automation, from review of material before publication to discovery and continuous monitoring" across web, email, social, calls, messages; "full-lifecycle Marketing Compliance-as-a-Service." [Documented, cached]
- **The wedge:** omni-channel breadth + discovery at scale (Kraken crawler; email harvested from "hundreds of thousands of live consumer inboxes" via LashBack) + curated regulatory rulebooks (CFPB/FTC/OCC/FDIC/FINRA bulletins) + partner/affiliate oversight + dedicated CSM service layer + tenure ("15+ years," 1.1B observations, 6 of top 10 US banks). [Documented, cached]
- **The criteria they install are all incumbent-shaped** — breadth, historical volume, service headcount, tenure, ROI arithmetic ("1,214 hours saved monthly," "90% faster reviews"). Conspicuously absent from their own buyer's guide: accuracy/precision, false-positive rate, time-to-first-value, pre-pub turnaround, model quality, marketer UX, multi-jurisdiction reasoning. **They sell coverage, not judgment — hand the buyer the other scoresheet.** [Documented, cached]
- **CFPB-deregulation narrative:** they've pivoted content hard to "states are stepping up" (their own analysis: "67% of enforcement actions from state agencies"), FTC activity, private litigation, and AI risk — repositioning UDAAP budgets away from CFPB fear. Test in discovery whether the buyer's budget survived that transition. [Documented, cached]
- **Community moat:** COMPLY Summit since 2014 (now their Client Summit + "Kraken Compliance Awards"); regulators speak there (CA DFPI, 2025). Real relationship glue — budget for it in displacement deals. [Documented, cached]
- **Who they name:** nobody. They frame competition as manual review + point tools. The asymmetry: Sedric, Warrant, Fintel Connect, Blee (and Haast's roundup) all publish "PerformLine alternatives" content — challengers targeting the incumbent's search terms. No Haast mentions by PerformLine; a SourceForge auto-generated "Haast vs PerformLine" page exists. [Documented, cached]

## 3. Feature matrix vs. Haast

| Capability | PerformLine | Haast | Notes |
|---|---|---|---|
| Post-publication monitoring | **Yes — the historic core strength.** Kraken crawler; web/social/partner/affiliate discovery at scale; 200+ fintech partners monitored for one bank; screenshots/transcripts as audit record | Yes — continuous live web + social monitoring | The one competitor in this run where post-pub is THEIR home turf. Fight on monitoring *intelligence* (context vs lexicon noise), not existence |
| Pre-publication review | Legacy: Document Review (~2021) + Pre-Publication Review — **pass/fail scoring on the same rulebook engine**, OCR/transcription, partner email submission. GenAI version — **"Pre-Publication Scanner" — launched Jul 13, 2026**, "advancing to context-aware AI analysis" (tacit admission the prior product wasn't) | **Core strength** — AI review with regulator agents + org-specific rules, in production for years | Their v1-genAI vs your mature product. Demand pre-pub bake-off on real creative |
| Channels | Web, social (TikTok/X/LinkedIn/FB/IG/YouTube, paid+organic), **calls (100% coverage claim), messages/chat**, email, documents, + **AI Response Monitor** (May 2026 — monitors ChatGPT/Gemini/Claude/Copilot answers about the brand) | Text, image, PDF, docs, long-form video, web, social | **Calls + messages are real capabilities Haast doesn't match — don't deny; reframe as adjacency + invoice line-items** |
| AI depth | Real but recent: Bedrock prompt-engineering in production (AWS blog Jul 2025); "semantic evaluation grounded in client source-of-truth docs"; philosophy "AI when it makes sense, deterministic rules where auditability is non-negotiable" = **core engine remains rules/lexicon** (Apr 2025 headline improvement: +3,500 terms/phrases) | GenAI-native; AWS-published architecture; agents per regulator | "GenAI-native vs genAI-retrofit, retrofit dated July 2026." Never "they have no AI" |
| Rule building | PerformLine-curated rulebooks; "specialists work with each client to refine, optimize and prioritize" (their own competitor page) — **vendor-tuned, not self-serve**; their copy concedes pre-built rules "can lead to false positives" | Self-serve per-asset rule config + legal implementation team | Their accuracy depends on perpetual vendor services — ops burden + lock-in |
| False-positive control | Structural weakness of lexicon scoring, conceded in their own materials ("too many rules at once can create overwhelming noise"); employee reviews describe manual compensation | Contextual AI review; measure in POC | Phrase from THEIR docs; no independent customer testimony exists — don't invent it |
| Regulator coverage | CFPB/UDAAP core, FTC, OCC, FDIC, FINRA (2210 rulebooks claimed), TCPA, fair lending, racial-bias monitoring; multi-language (ES/NL/FR/DE); **FCA = rulebook customization for one UK/BNPL story, not local reasoning; no ASIC/EU evidence.** No SEC Marketing Rule/investment-adviser depth found | FINRA + FTC + FCA agents; ASIC-native heritage; investment/wealth depth | They're consumer-finance deep; investment-marketing and true multi-jurisdiction are thin |
| Audit trail | Screenshots, transcripts, remediation records; findings management workflows | Full audit trail | Parity on paper; no 17a-4 claims found on their side either |
| Integrations | Asana, Jira, Monday, Smartsheet, Workfront, HubSpot, Salesforce; API ambiguous (sources conflict) | Figma, Office365, Workfront, Google Docs, API | They beat the AI startups here; probe API depth |
| Deployment | No public claim; Warrant alleges "months" [competitor]; 19-year enterprise motion with CSM-heavy onboarding | 8–12 weeks, regulator agents live day one | Anchor the number first |
| Security | SOC 2 Type 2 claimed only by an unreliable third-party aggregator — **no trust page, no first-party claim found** | Table Haast's pack | Odd gap for a bank vendor; soft diligence probe |
| Docs/transparency | **No public docs** (help.performline.com doesn't resolve), no trust page, no pricing; support is human-mediated (CSMs, "Tuesday Tutorials") | Check Haast posture | Same transparency landmine as the startups — surprising for a 19-year vendor |
| Proof/reviews | Named logos real (Cross River, Cadence, Republic, Bread Financial, Upstart, PREMIER Bankcard; TD/Rocket/Benchmark as summit speakers) — but **near-zero authentic review footprint**: Capterra listing still under legacy name "PerformMatch" with no reviews; no TrustRadius; G2 rating unverifiable/thin; SpotSaaS "4.5/458" unreliable — do not cite | AWS case study, named enterprise logos, $12M Series A (Peak XV, Apr 2026) | "19 years in market — find one verifiable customer review" |

## 4. Feature gaps (ranked for a regulated-industry compliance buyer)

1. **GenAI pre-publication review is three weeks old.**
   (a) Evidence: Pre-Publication Scanner PR dated Jul 13, 2026; its own language ("advancing to context-aware AI analysis") concedes the prior pre-pub product wasn't context-aware; legacy pre-pub is rulebook pass/fail scoring.
   (b) Confidence: high (their own press releases).
   (c) Exploitation: insist on a pre-publication bake-off with the buyer's real creative — nuanced claims, layered disclosures, video. A v1 retrofit against your production system, measured on precision/recall, is the cleanest technical win available in this run.

2. **Accuracy depends on vendor-tuned lexicons — noise is structural.**
   (a) Evidence: their own copy concedes pre-built rules create false positives and that specialists must continually "refine, optimize and prioritize"; +3,500-terms announcement is a lexicon fingerprint; Glassdoor employees describe "manual solutions to placate clients and prevent churn."
   (b) Confidence: high on mechanism (their materials); employee testimony corroborates; no customer reviews exist either way.
   (c) Exploitation: discovery on alert volume and tuning cadence: "How many flags per week does your team triage today, and who tunes the rules when noise spikes — your team or vendor services?" Then structure the POC to count false positives per 100 assets, both vendors, same corpus.

3. **Investment-marketing depth is thin.**
   (a) Evidence: gravity is UDAAP/CFPB consumer finance; FINRA 2210 rulebooks claimed but zero SEC Marketing Rule / IA performance-advertising / fund-marketing workflow evidence found.
   (b) Confidence: medium (absence of evidence — probe, don't assert).
   (c) Exploitation: in wealth/asset-management deals, run regime-specific test content (performance advertising, hypothetical returns, testimonials under the Marketing Rule). Their rulebooks were built for lenders, not advisers.

4. **Multi-jurisdiction is customization, not capability.**
   (a) Evidence: one UK/FCA BNPL customer story ("rulebooks customizable to comply with FCA regulations"); no ASIC/EU/ESMA evidence; multi-language limited to 4 European languages; Asia/Oceania staff are an offshore-cost signal, not GTM.
   (b) Confidence: high on US-centric positioning.
   (c) Exploitation: **never say "US-only" — you'll get corrected with the BNPL story and lose credibility.** Say: "US platform with FCA rulebook customization — ask for local regulatory *reasoning* and in-region references under FCA and ASIC." Haast has both.

5. **Product under-investment, per their own employees.**
   (a) Evidence: Glassdoor (3.6/5, 46 reviews): "lack of investment in technology causing them to lag behind client expectations"; "product is average, CS makes up for shortfalls with around-the-clock high-touch support"; "turnover is constant"; bonuses "not paid out fully, year after year"; company "overreacts to losing clients" with monthly reorgs.
   (b) Confidence: medium-high (multiple consistent employee reviews) — **frame as employee testimony, never as customer complaints.**
   (c) Exploitation: don't quote Glassdoor in front of prospects. Use it to shape strategy: push live product demos over slideware, ask who maintains hand-tuned rulebooks given turnover, and expect the CSM relationship layer — not the product — to be the real displacement obstacle.

6. **Transition risk: new CEO, new CFO (x2), new money, retrofit in flight.**
   (a) Evidence: CEO change Jan 2026 explicitly tied to AI expansion; CFO churn; M33 top-up; exit-experienced operator profile.
   (b) Confidence: documented events; exit-posture reading is inference.
   (c) Exploitation: procurement framing — "mid-transition vendors reprioritize roadmaps; ask what happens to your feature commitments and your CSM if the company is sold in 18 months." Contrast with Haast's Series A trajectory (fresh capital, founder-led, growth phase).

7. **No public docs, no trust page, no verifiable review footprint — after 19 years.**
   (a) Evidence: help subdomain NXDOMAIN; no first-party SOC 2 claim found; Capterra listing still under the legacy "PerformMatch" name with no reviews; no TrustRadius listing.
   (b) Confidence: documented absences.
   (c) Exploitation: the diligence-completeness criterion works even against the incumbent: "ask every vendor for public docs, a trust center, and independent reviews." An unmanaged 19-year-old review footprint reads as complacency.

## 5. Pricing signals

- **Published pricing:** none — custom quote only across every directory; a free trial (no credit card) per GoodFirms. [Documented, cached]
- **Packaging:** per-channel modules (web, call, message, email, social, documents, AI Response Monitor, Pre-Pub Scanner are separate products) → **module-stacking economics**. The full-lifecycle invoice is the pressure point: "ask what omni-channel + pre-pub actually costs, all modules in."
- **Procurement footprint:** no Vendr/Spendflo benchmarks — consistent with high-touch direct sales, not marketplace transactions. [Documented absence]
- **Perception data (competitor-sourced, flag it):** a bank found them "too complex and expensive" and switched (Fintel Connect's story) [competitor]; "positioned for enterprise budgets… earlier-stage fintechs look for different commercial models" (Sedric) [competitor].
- **Best-guess model + ACV:** annual subscription, per channel/module + scan volume, services bundled; **ACV ~$40K–$150K+, large multi-channel bank deals $200K+; entry rarely below ~$25–30K.** Confidence: medium-low (revenue ÷ account-count arithmetic).
- **How to position price:** their sticker for monitoring-only may undercut you; their *full-lifecycle* sticker (all modules + the new AI products) likely won't. Force the all-in comparison. Second lever: their price embeds a perpetual services layer (rulebook tuning, CSM heroics) — Haast's finite implementation + product-absorbed scale (AWS case study: 4x capacity) is the TCO story. Third: renewal risk — module stacking plus a possible ownership change is exactly when procurement demands price protection; offer multi-year rate locks they may not match mid-exit-process.

## 6. Customer complaints

**No authentic customer-review corpus exists** — the 19-year incumbent has effectively zero verifiable reviews on G2/Capterra/TrustRadius (Capterra shell under a legacy product name; discarded two inflated aggregator figures as unreliable). Complaint themes below are assembled from competitor switching stories, PerformLine's own copy, and employee reviews — labeled accordingly:

- **"Enterprise-priced / too complex for what smaller teams use"** — clears the 3-source bar with a bias caveat (two competitor sources + structural quote-only pricing): Fintel's bank-switch story; Sedric's "enterprise budgets" framing. Usable as a discovery theme, attributed carefully.
- **Detection-not-prevention heritage** — two competitor sources + PerformLine's own July 2026 Scanner launch as tacit confirmation (you don't launch a pre-pub AI product in year 19 if pre-pub was solved).
- **Alert noise / rules-maintenance burden** — Fintel's "information overload" + PerformLine's own false-positive concession. Their fix is more vendor services — the lock-in angle.
- **Product under-investment / churn-fighting via manual labor** — Glassdoor employees only; powerful but internal; use for strategy, not quotes.
- Positives to respect: employees praise the CS culture; customers renew on relationships; the COMPLY community creates genuine loyalty.

## 7. Ex-employee signals

First competitor in this run with real signal. All from public Glassdoor/Indeed review content; no individuals identified; nothing confidential.

- **Organizational health:** Glassdoor 3.6/5 (46 reviews), 66% recommend, comp 3.3/5. Themes: **constant turnover "from leadership team to ICs"**; below-market comp; **bonuses "not paid out fully, year after year"** (repeated missed plans); reactive reorgs after client losses ("systems, department structure, KPIs, product priorities… changing every month or quarter"); hard to grow vertically. Balanced by: remote-first, good work-life balance, well-liked founder-CEO (pre-transition), culture 4.0. Indeed: 4.5/13 (thin).
- **Product/market truth:** the two most deal-relevant excerpts — "lack of investment in technology causing them to lag behind client expectations… employees consistently need to overcompensate with **manual solutions to placate clients and prevent churn**" and "the **product is average**, CS does their best to make up for any shortfalls with around-the-clock high-touch support."
- **Deal-relevant inference (marked as inference):** (1) the automation has a manual backstage — in bake-offs, insist on live unscripted runs, not curated samples; (2) hand-tuned rulebook knowledge is fragile under constant turnover — continuity-of-service questions land; (3) the CS layer generates real switching-cost goodwill — displacement campaigns need an executive-level risk narrative, not just a feature win; (4) leadership churn at the top (founder out, 2 CFOs) plus IC turnover below suggests execution wobble during exactly the period they must ship an AI replatform.
- No public "my time at PerformLine" essays or ex-staff podcast appearances found; LinkedIn tenure analytics not accessible publicly (gap).

## 8. Where they win (honest)

- **Bank-fintech/BaaS partner oversight at scale.** Monitoring 200+ fintech partners for a sponsor bank is their signature motion — discovery breadth, affiliate scraping, and remediation workflows built for it. If that's the buyer's core problem, they're the safest pick today.
- **Call and message monitoring.** 100%-of-calls coverage, scorecards, higher-ed/mortgage call stories. Haast doesn't match this — if voice compliance is in scope, coexist or step aside.
- **Consumer-finance UDAAP depth + regulator relationships.** Rulebooks built from CFPB/FTC/OCC/FDIC actions, state-regulator relationships (DFPI at their summit), racial-bias monitoring. A mortgage lender or card issuer buying UDAAP coverage gets real substance.
- **Incumbency + community.** 6-of-top-10-banks claim, COMPLY summit loyalty, dedicated CSMs, award refresh (Banking Tech USA 2026). Enterprise compliance teams renew relationships.
- **Discovery of unknown-unknowns.** "You can't review what you can't find" — Kraken + LashBack inbox network is a genuine differentiator vs every AI-native vendor including Haast.
- **Disqualify/reframe rule:** buyer = sponsor bank with hundreds of partners + call-center compliance + UDAAP lens → their kill zone; coexistence ("keep PerformLine for calls/partners, Haast for content lifecycle") beats head-on displacement. Buyer = content-velocity pain, pre-pub bottleneck, investment-marketing rules, multi-jurisdiction → your kill zone; force the accuracy/pre-pub scoresheet.

## 9. Landmines (discovery-question form — never name PerformLine)

1. Ask: **"When you evaluate AI review, will you measure precision and recall on your own content — and how long has each vendor's AI review actually been in production?"** → Their genAI pre-pub scanner shipped Jul 13, 2026 (§4.1).
2. Ask: **"How many alerts does your team triage per week today, and who tunes the rules when the noise gets bad — your team, or vendor services on their timeline?"** → Lexicon noise + vendor-tuned rulebooks, conceded in their own copy (§4.2).
3. Ask: **"If we added up every module — each channel, pre-publication, the new AI features — what does the all-in annual cost look like, and which modules are extra?"** → Per-channel stacking economics (§5).
4. Ask: **"For your investment products, can the vendor demonstrate SEC Marketing Rule and performance-advertising review on real adviser content — not just lending disclosures?"** → Consumer-finance rulebooks, no IA depth found (§4.3).
5. Ask: **"Outside the US, do you need local regulatory reasoning and in-region references — or is 'customizable rulebooks' enough?"** → FCA customization vs native coverage (§4.4).
6. Ask: **"How would a change of vendor ownership or leadership affect your roadmap commitments and named support team — and what protections would you want in the contract?"** → Founder exit, operator CEO, PE top-up, CFO churn (§4.6).
7. Ask: **"Can you find a single verifiable customer review of each shortlisted vendor on G2, Capterra, or TrustRadius?"** → 19 years, effectively zero authentic reviews; Capterra still lists a legacy product name (§4.7).

## 10. Objection-handling angles

**When PerformLine is the incumbent or shortlisted — what your champion will hear:**

1. *"They've done this 19 years — 1.1 billion observations, 6 of the top 10 banks."* → Reframe: "Observation counts measure crawler output, not review quality — and their own materials concede rules-based scoring produces false positives that need perpetual specialist tuning. The question for 2026 isn't who crawled the most pages since 2007; it's whose AI reads *your* content most accurately today. That's measurable in two weeks on your corpus — let's make both vendors sign up for it."
2. *"They already monitor our partners and calls — why add a vendor?"* → Reframe: "Keep what works. Calls and partner discovery are their strength. The gap is everything upstream: your content volume is exploding and their pre-publication AI shipped in July 2026. Run Haast on the content lifecycle — pre-publish review plus live-estate monitoring — alongside their call coverage, and compare the invoice to stacking their modules."
3. *"They just launched AI — Pre-Publication Scanner, AI Response Monitor."* → Reframe: "Real, and telling: a new CEO was hired in January 2026 explicitly to accelerate an AI roadmap that was behind, and the pre-pub scanner is a v1 launched in July. Haast's AI review has been the product since day one, with an AWS-published architecture and named enterprise deployments. Ask both vendors: how long in production, which referenceable customers, what measured accuracy?"
4. *"Switching costs — our team knows their platform, our CSM is great."* → Reframe: "The CSM is great partly because the platform needs one — their model is high-touch service compensating for a rules engine. Also worth asking: with the founder out of the CEO seat, new capital, and an operator CEO with exit experience, will that CSM and roadmap look the same in 18 months? Get continuity commitments in writing — from both of us."
5. *"They're the safe choice for a bank — regulators speak at their conference."* → Reframe: "Their regulator relationships are real, in US consumer finance. If your risk surface includes investment products, UK/EU entities, or AI-generated content velocity, 'safe' means the vendor built for those — FINRA/FTC/FCA agents, live multi-jurisdiction deployments (Aviva, Zurich ANZ, Equity Trustees), and a $12M Series A funding the US build-out."
6. *"They cover channels you don't — calls, texts, consumer inboxes."* → Concede and contain: "Correct, and if voice is in scope we'll say so plainly — keep them for calls. Now price that honestly: each channel is a separate module on their invoice. For the content lifecycle — where your volume is growing 10x — compare depth, not breadth."
7. *"Their price came in lower."* → Reframe: "Compare all-in: their quote is usually monitoring-first; add pre-publication, the AI modules, and every channel, then add the services layer that tunes rulebooks forever. Haast's implementation is finite and the product absorbs volume growth — 4x capacity in the AWS-published case study. And in a vendor mid-ownership-transition, ask for multi-year price protection — we'll offer it."

**FUD they will plant about Haast — pre-armed responses:**

| Their likely line (from their installed criteria) | Your response |
|---|---|
| "AI startups are unproven — we have 19 years and billions of observations" | AWS-published case study (500+ hours saved, 80%+ productivity, 4x capacity); Telstra, Aviva, Zurich ANZ, Equity Trustees in production; $12M Series A led by Peak XV (Apr 2026). Then flip: their genAI products are dated May–July 2026 — who's actually unproven at AI review? |
| "They don't cover calls or messages" | True today — and if that's your deciding requirement, we'll say so. But scope the invoice: those are separate modules on their side. For marketing-content compliance — the budget under pressure — depth beats channel count |
| "They can't match our consumer-finance rulebooks" | Their rulebooks are curated lexicons (+3,500 terms was their 2025 headline); Haast encodes your policies with contextual AI and covers FINRA, FTC, and FCA as agents. In a POC on your content, count the false positives per hundred assets — lexicons lose that fight |
| "We monitor what ChatGPT says about your brand — they don't" | Novel and clever — it's discovery of talk *about* you. Your bigger 2026 exposure is the AI content *you* produce at scale, pre-publication. Ask which vendor's core product handles that, and since when |
| "Young foreign vendor risk" | Mirror it precisely: founder just left their CEO seat, two CFOs in a year, PE investor five years into its hold, exit-experienced operator installed. Vendor-stability questions cut both directions — put continuity terms in both contracts |

## 11. MEDDPICC angles

- **Metrics:** false positives per 100 assets (POC-measured — their structural weakness), pre-pub review turnaround on complex creative, precision/recall with agreed definitions, % of live estate monitored with contextual (not lexicon) analysis, time-to-value (their deployments allegedly "months" [competitor]; yours committed in writing). Avoid competing on observation counts and channel tallies — that's their scoresheet.
- **Decision criteria to install:** (1) AI review accuracy measured on buyer corpus; (2) production maturity of genAI capability (months vs years); (3) self-serve rule control with change SLAs vs vendor-services tuning; (4) all-in module pricing transparency; (5) investment-marketing and multi-jurisdiction depth with references; (6) vendor-continuity protections given ownership transition. They fail or strain on all six; they'd install breadth/tenure/service instead — get your sheet in first.
- **Pain they leave unsolved:** content-velocity bottleneck pre-publication (their own July 2026 PR admits manual review "can't keep up"), false-positive triage load, investment-adviser marketing rules, non-US reasoning, and the marketer experience (Warrant's critique: built for compliance teams, not marketers [competitor]).
- **Paper process / procurement:** their friction — quote-only per-module pricing (invites all-in cost exposure), no marketplace paper, no public trust page or first-party SOC 2 claim found (diligence drag for a bank vendor, worth verifying), ownership-transition risk clauses. Your leverage — transparent bundle, multi-year price lock, faster security pack, continuity commitments. Their leverage — existing MSAs at incumbent accounts and procurement inertia; in renewals-timed deals, start 6+ months before their renewal date.
- **Champion note:** their real defense at incumbent accounts is the CSM relationship and the COMPLY community. Your champion needs an executive-level story (risk coverage evolution, AI-era readiness, TCO) — a feature comparison alone won't dislodge a beloved CSM.

## 12. Sources

Provenance: **[cached]** = search-engine-indexed/cached content (direct fetch blocked — ground rule 5). **[competitor]** = competitor-authored. **[employee]** = Glassdoor/Indeed review content. Accessed 2026-08-04.

**PerformLine first-party** (all [cached]): performline.com — home ("AI Marketing Compliance Software" title), /why-performline/ (1.1B observations, 6-of-top-10-banks), /company/about-us/, product pages (/products/pre-publication/, /web-monitoring/, /social-media-monitoring/, /call-monitoring/, /message-monitoring/, /email-monitoring/, /omni-channel-monitoring/, /ai-response-monitor/, documents), /rulebooks/, /integrations/, industry pages (/industry/fintech/, /baas/, /insurance/, /gig-companies/), /customer-stories/ + content.performline.com (global BNPL US+UK / FCA-customization story; call-monitoring stories), blog: competitor-alternative page ("1,214 hours," false-positive concession), choosing-the-right-marketing-compliance-software (CSM as criterion #1), state-regulators post ("67% state enforcement"), CFPB roundups, flexible-AI post ("deterministic rules where auditability is non-negotiable") · complysummit.com · help.performline.com NXDOMAIN [live-DNS]

**Press releases** (all [cached]): PRWeb — **Calhoun CEO + M33 top-up (Jan 5, 2026, 302652006)**, **AI Response Monitor (May 4, 2026, 302760898)**, **Pre-Publication Scanner (Jul 13, 2026, 302823191)**, rulebook +3,500 terms (2025, 302423470), exec expansion (Apr 2025, 302429048), Goodgion CFO (Nov 2024, 302305624), Byron Lee CTO (Jun 2021), M33 investment (May 2021), LashBack acquisition (Jul 2022), Document Review launch (~2021, 17828893), 2025 Client Summit/Catalysts (302479243), Kraken Awards 2023/2024 · Banking Tech Awards USA 2026 win (performline.com blog + informaconnect)

**AI reality** (all [cached]): aws.amazon.com/blogs/machine-learning — "How PerformLine uses prompt engineering on Amazon Bedrock to detect compliance violations" (~Jul 25, 2025)

**Employee voice** [employee] [cached]: glassdoor.com/Reviews/PerformLine-Reviews-E829235.htm (3.6/5, 46 reviews; all quoted excerpts) · indeed.com/cmp/Performline/reviews (4.5/13, thin)

**Review-site absence** (documented negatives, [cached]): Capterra p/159651 listed as legacy "PerformMatch," no reviewer feedback; no TrustRadius listing; G2 product/seller/alternatives pages exist but no retrievable rating (alternatives list misclassified as social listening — thin footprint); SoftwareSuggest "no reviews yet"; TechnologyCounter 0.0/unclaimed; SpotSaaS "4.5/458" and a "Capterra 4.6/5,302" search artifact **rejected as unreliable — do not cite**; FeaturedCustomers (43 references) is vendor-curated

**Competitor-authored** (all [cached] [competitor]): sedric.ai/blog/performline-alternatives ("detection after publication" heritage; "enterprise budgets") · hellowarrant.com warrant-vs-performline ("built for compliance teams, not marketers"; "months" deployments) · fintelconnect.com/blog/performline-competitors ("too complex and expensive" bank-switch story; "information overload")

**Company data** (all [cached]): tracxn ($9.68M/7 rounds; headcount trend) · pitchbook 51544-99 ($6.38M equity) · crunchbase · growjo/rocketreach/prospeo/leadiq (revenue/headcount estimates; Asia/Oceania footprint) · sramanamitra.com (bootstrapped-to-$20M-ARR interview series) · builtin AE/CSM postings (enterprise FS ICP, 6+ month cycles) · outcomecapital.com (Series A) · Titan Cloud Shortsleeve bio (board)

**Haast baseline** (all [cached]): aws.amazon.com/solutions/case-studies/haast-case-study/ · prnewswire 302737540 + legaltechnology.com + siliconangle.com (Apr 2026 — $12M Series A, Peak XV, DST Global Partners, Airtree; 4.5x growth, zero churn company-reported) · itbrief.com.au + businessnewsaustralia.com (Telstra, Aviva, Zurich ANZ, Equity Trustees, Future Super) · haast.io case studies

**⚠ Verify live before quoting in a deal:** (1) Pre-Publication Scanner capability depth — get a demo teardown, the PR is 3 weeks old; (2) G2/Gartner Peer Insights actual ratings (fetch-blocked; assumed thin); (3) whether SOC 2 exists first-party (aggregator-only claim, and that aggregator also misattributed a "Greenboard Go AI engine" to them); (4) COMPLY Summit 2026 status; (5) any sale-process news — the exit-posture read is inference and staleness-sensitive.
# BATTLECARD: Red Oak (redoak.com, formerly redoakcompliance.com)

**Run date:** 2026-08-04 · **Refresh by:** 2026-11-04 (quarterly — **sooner if the MirrorWeb merger closes**) · **Prepared for:** Haast US sales
**Provenance note:** direct fetches blocked by the research environment's egress proxy — claims sourced from search-engine-indexed/cached versions of cited pages (ground rule 5), tagged **[cached]**. Competitor-authored claims tagged **[competitor]**. Verify-live list in §12.

---

## TL;DR for the 2-minute pre-call read

Red Oak is the advertising-review **workflow** incumbent for US investment firms — AdMaster DNA, bi-directional FINRA AREF filing (their fortress), 17a-4-native records, ~1,800–2,300 claimed client firms including most top-20 asset managers, now PE-fueled (Mainsail, $51M, 2023) and rolling up into a "Compliance Connectivity Platform" (SiteQuest 2024, 4U 2025). **The defining fact of this quarter: on July 28, 2026 they announced a merger with MirrorWeb — MirrorWeb's CEO takes over, Red Oak's CEO becomes an advisor, and the combined stack won't be integrated for 12–24 months.** That's your displacement window. Their "AI Review" (Jan 2025) is a real but shallow LLM feedback layer — GPT-3.5/4 prompts configured by their implementation team, bolted in front of the human workflow, no published accuracy. Recommended motion: **coexist-then-displace** — don't fight the FINRA-filing plumbing; own the review intelligence and live-estate monitoring, and let their workflow commoditize underneath you. Two things NOT to say: "they have no AI" (falsifiable) and "they have no post-publication monitoring" (they do — but it's rep surveillance/archiving, not live marketing-estate re-review). And don't attack their support — it's genuinely loved.

---

## 1. Company snapshot

| Item | Finding | Confidence |
|---|---|---|
| Founded / HQ | March 2010, Austin/Cedar Park TX, by **three** ex-practitioners: Cathy Vasilev (supervisory systems at a hybrid BD/RIA), Stephen Pope, Rick Grashel (tech, ex-Dell) | Documented [cached] |
| Ownership | **Mainsail Partners** growth equity — $51M, June 2023 (their only institutional round). Bolt-ons: SiteQuest (Mar 2024), 4U Platform (Apr 2025). **Definitive merger agreement with MirrorWeb announced Jul 28, 2026** — terms undisclosed, not confirmed closed | Documented [cached] |
| Leadership | PE playbook, C-suite almost fully replaced 2024–26: Dave Dutch CEO (May 2024 → advisor post-merger), **Romir Bosu (MirrorWeb CEO) to lead combined company**; CRO/CCO/CMO/COO all new since 2024; **Kirk Sadler CPO (Feb 2026, ex-Mitratech, "led orgs through six acquisitions")**. Founders: Vasilev → Chief Engagement Officer, Pope → board/Chief Solutions Architect | Documented [cached] |
| Headcount | ~116 (Tracxn, Apr 2026, incl. 4U); roughly doubled since the 2023 investment; merger will roughly double again. Inc. 5000 seven straight years | Medium (aggregators) |
| Scale claims | Inconsistent across their own materials: "1,800+ firms" (2023–25) / "2,300+ firms" (2025 site) / "1,550+ regulated firms, $62T AUM" (combined merger PR). "19 of top 20 US asset managers, 17 of top 20 global." **The inconsistency is a usable diligence needle** | Documented claims [cached] |
| ICP | US broker-dealers, asset managers (deepest penetration), RIAs down to single-state advisors, mutual funds, banks, insurers (since 2023). Enterprise ad-review specialist — NOT the small-RIA all-in-one category (Kitces commentary puts SmartRIA there) | Documented [cached] |
| Pricing model | Quote-only; annual firm-level subscription; modular (ad review core + AI Review, disclosure mgmt, supervision, registration, 4U add-ons); likely AUM/size-tiered. Hypothesis bands: small RIA $5–20K, mid BD/insurer $25–75K, large AM $100K+ (several hundred K multi-module). Blended-average math (~$9M est. revenue ÷ ~2,000 firms ≈ $4–5K) implies a long tail of small accounts under a few six-figure logos | Structure medium; bands low — validate in win/loss |
| Go-live claim | "4–8 weeks" (via comparison snippet); self-service workflow admin positioning | Weak-medium [cached] |
| Security | SOC 2: **no public evidence found either way** — treat as unknown, ask in deals. AI stack disclosed on directory listing: "ChatGPT 3.5 Turbo and GPT-4 on Microsoft Azure" | Documented gap / [cached] |

## 2. Positioning + narrative

- **One-liner:** "the global advertising review software of choice in the financial services industry" → now "**Compliance Connectivity Platform**" — "the only modern compliance ecosystem that connects every stage of content creation, review, distribution, and surveillance." Post-merger: "no rival platform connects the full lifecycle, from the moment content is created through to its final archive." [Documented, cached]
- **The wedge:** built-by-compliance-practitioners workflow depth + FINRA plumbing. Bi-directional AREF integration ("file over 95% of advertising material with FINRA directly," auto-retrieves comment letters, "saves 30 minutes per filing") + "100% books and records compliant" 17a-4/WORM storage — including, smartly, **AI Review outputs stored 17a-4-compliant**. [Documented, cached]
- **AI narrative — deliberately conservative, and it's FUD scaffolding:** "**Compliance-Grade AI™**," "precision not prediction," "transparent, auditable AI," "no time-consuming model training." Their content warns about FINRA's GenAI risk guidance. Every phrase is engineered to install anti-genAI-startup decision criteria. Execs on record: "AI won't replace compliance teams"; SVP Product on AI Review: "additive solution that enhances efficiency without compromising regulatory integrity or **disrupting existing workflows**" — the workflow is the product; AI must not threaten it. [Documented, cached]
- **The criteria they install are workflow/records/trust criteria** — practitioner pedigree, client counts, 17a-4, FINRA connectivity, configurability, "35% faster approvals / 70% fewer touches" (a routing metric recycled since ~2020). **None of their criteria touch review quality, catch-rate, live-channel coverage, or review-effort reduction** — score the deal on those and they're playing away. [Documented pattern, cached]
- **Who they name:** nobody — classic incumbent. Meanwhile Warrant runs a dedicated vs-Red-Oak page, Blee/Sedric/Luthor/Greenboard/RegFin all target them as "the legacy incumbent… document-centric tools built for a pre-AI world" [competitor]. **Zero Haast mentions anywhere** — you can define the frame first.
- **Community/events:** NSCP fixture (Vasilev speaks), FINRA Advertising Regulation Conference sponsor, own conference "**Accelerate 2026**" (Austin, co-branded with 4U + MirrorWeb, open to non-clients — worth attending for roadmap intel).

## 3. Feature matrix vs. Haast

| Capability | Red Oak | Haast | Notes |
|---|---|---|---|
| Review workflow (routing/versioning/approvals) | **Core strength.** Configurable parallel workflows, video/audio annotation, lexicon pre-check, full-text search, Word add-in, Seismic/Aprimo/Workfront integrations | Workflow exists but isn't the wedge | Don't fight this early — coexist (§8) |
| FINRA filing | **Fortress.** Bi-directional AREF, 95% direct-filing claim, comment-letter retrieval | Not a Haast capability | Concede; position review layer as feeding their filing pipe |
| 17a-4 / books & records | **Native**, incl. AI Review outputs in 17a-4 store | Verify Haast posture internally | Second competitor (after Saifr) where the records landmine does NOT work |
| AI review depth | **Real LLM, shallow layer**: AI Review (Jan 2025, beta through 2024) = GPT-3.5/4 prompts on the rules engine, giving submitters pre-submission feedback on promissory/misleading language. **Prompts configured by Red Oak's implementation team at onboarding.** No published accuracy/catch-rate; no regulator-corpus agents; humans still review everything | GenAI-native regulator agents (FINRA/FTC/FCA), per-finding citations, org-tuned; AWS-published architecture | Never say "no AI." Say: "a vendor-configured prompt layer to reduce back-and-forth — ask to see and version the review logic yourself, and ask for the catch-rate" |
| Post-publication monitoring | **Exists — but it's rep surveillance + archiving**: SiteQuest website monitoring, social supervision module (Jan 2025: LinkedIn/Meta/IG/X), affiliate/influencer monitoring (Oct 2024), comms capture (SMS/Slack/Teams/Zoom/WhatsApp), MirrorWeb archiving + "Mira" conduct-risk AI post-merger | **Continuous AI re-review of the firm's own live marketing estate** — rate change/reg change/product pull → finds every live page/PDF/post now non-compliant | **The precise gap**: FINRA-3110-style supervision of what reps post ≠ compliance re-review of your own live estate. Make the buyer articulate which problem they're solving |
| Channels | Documents/submissions core; video/audio in *annotation* and *capture*, no evidence of AI compliance review of video/audio content | Text, image, PDF, docs, long-form video AI review + live web/social | Probe video-review depth in demos |
| Disclosures | Smart Review (2020) disclosure management — "800K potentially missed disclosures flagged" in a year | Disclosure handling in review workflows | Genuine strength of theirs; don't dismiss |
| Regulator coverage | US only: FINRA/SEC/17a-4 anchors. **No FCA/ASIC/EU product capability found.** MirrorWeb adds UK archiving DNA — expect UK noise within 12 months, but archiving ≠ finprom review | FINRA + FTC + FCA agents; ASIC-native; live UK/AU enterprise deployments | Haast's ANZ/UK turf is uncontested by them today |
| Implementation | 4–8 weeks claimed; self-service workflow admin; AI prompts vendor-configured | 8–12 weeks with regulator agents live day one | Their number is smaller; reframe on what's actually configured at go-live |
| Support | **Genuinely loved** — every independent-ish source praises responsiveness (<1hr ticket claims, high NPS/low churn claims) | Compete, don't attack | Attacking support will backfire; it's their most consistent positive theme |
| Proof/reviews | ~Zero independent review footprint (no G2/Capterra/TrustRadius; 3 five-star Serchen reviews; vendor-curated FeaturedCustomers). No named customers — testimonials anonymized | AWS case study, named logos, $12M Series A (Peak XV, Apr 2026) | Same review-vacuum reframe as the whole category |
| Corporate state | **Mid-merger**: 3 M&A events in 30 months; CEO seat passing to merger partner; brands not unified; integration ahead | Single product, single roadmap, fresh Series A | The stability argument now cuts against the incumbent |

## 4. Feature gaps (ranked for a regulated-industry compliance buyer)

1. **AI Review is a vendor-configured prompt layer, not an AI reviewer.**
   (a) Evidence: their own pages — LLM + prompt engineering for pre-submission feedback; "prompts… configured as part of the implementation led by the Red Oak team"; stack disclosed as GPT-3.5/4 on Azure; no accuracy/catch-rate published anywhere; humans still perform every review.
   (b) Confidence: high (their materials).
   (c) Exploitation: two questions dismantle it — "Can your team see, edit, and version the AI's review logic yourselves?" and "What catch-rate will they commit to on your corpus?" Then run the bake-off. Also flip their black-box FUD: vendor-configured prompts you can't inspect *are* the black box.

2. **No continuous compliance re-review of the live marketing estate.**
   (a) Evidence: monitoring stack is rep-surveillance/capture (SiteQuest, social supervision, comms archiving, Mira conduct-risk) — nothing re-reviews the firm's own published content against current rules when rates/regs/products change.
   (b) Confidence: medium-high (product-scope evidence; do NOT overstate — they will demo "monitoring").
   (c) Exploitation: scenario question — "Your advertised rate changed last Tuesday. Which system tells you every live page, PDF, and social post that's now wrong?" Their stack has no answer; it archives the problem instead.

3. **Merger/integration risk — right now.**
   (a) Evidence: definitive agreement Jul 28, 2026; MirrorWeb CEO takes over; Red Oak CEO to advisor; brands run separately "as the joint customer experience is built out"; third acquisition in 30 months; CPO hired specifically for acquisition integration; client counts already inconsistent across their own materials.
   (b) Confidence: high on facts; integration-drag reading is inference.
   (c) Exploitation: procurement questions — "Which entity is on the contract? Whose roadmap survives integration? What are the SLAs during re-platforming?" Time displacement campaigns to their renewal + integration milestones. This window closes; use it this cycle.

4. **US-only regulatory reasoning.**
   (a) Evidence: all anchors FINRA/SEC/17a-4; no FCA/ASIC/EU capability found; "global" means global clients on US rules.
   (b) Confidence: medium-high.
   (c) Exploitation: multi-jurisdiction buyers — demand regime-specific reasoning and in-region references. Note MirrorWeb's Manchester base will let them *claim* UK soon; pre-empt by distinguishing archiving DNA from financial-promotions review.

5. **Review-effort economics unchanged in five years.**
   (a) Evidence: headline ROI (35% faster approvals / 70% fewer touches) recycled since ~2020 — measures routing, not review effort; AI Review's benefit statement is "less back-and-forth," i.e., humans still review everything.
   (b) Confidence: high on the claims record.
   (c) Exploitation: reframe the metric — cost per reviewed asset and reviewer hours per 100 assets, measured in the POC. A workflow tool can't move those numbers; an AI reviewer can (AWS case study: 500+ hours saved, 4x capacity).

6. **Marketer experience.**
   (a) Evidence: competitor-authored but consistent across 3+ sources — "built for compliance teams, not marketers," "document vault," low marketer adoption with work leaking to email/spreadsheets [competitor]. No independent reviews exist to confirm or refute.
   (b) Confidence: low-medium as fact; high as the consensus challenger narrative.
   (c) Exploitation: don't assert it — test it. Ask the buyer's *marketing* team to demo-drive both tools and score submission experience. If the narrative is true, they'll say it themselves.

7. **No public docs, no trust page, SOC 2 unknown, no named customers.**
   (a) Evidence: no public KB/docs; production app is date-stamped ("Red Oak v2026.0711.3" — active releases, but no public changelog); SOC 2 unverifiable; testimonials anonymized.
   (b) Confidence: documented absences.
   (c) Exploitation: the standard diligence-completeness criterion works even here.

## 5. Pricing signals

- **Published pricing:** none — quote-only, phone number on directories. No Vendr/Spendflo benchmarks. No review-site pricing fields (no listings). [Documented absence]
- **Structure:** annual firm subscription, modular add-ons (AI Review, disclosure, supervision modules, registration, 4U), "unlimited workflows at no extra cost" as a sweetener, likely AUM/size tiers given "single-state advisor to top-20 asset manager" spread. [Medium confidence]
- **Hypothesis bands (validate in win/loss, do not quote):** small RIA $5–20K; mid BD/insurer $25–75K; large asset manager $100K+ to several hundred K multi-module. Blended-average arithmetic suggests a long tail of small cheap accounts beneath a few six-figure logos.
- **No pricing complaints found anywhere** — genuinely no signal, either direction.
- **How to position price:** the fight isn't sticker, it's *what the money buys*. Their spend buys routing + filing + records; review labor stays constant (their own metrics prove it). Haast's spend reduces review labor per asset and adds live-estate assurance — TCO on reviewer hours, not license lines. In coexist deals, price Haast as the intelligence layer, not a workflow replacement — smaller ask, faster yes, and it avoids waking the incumbent defense. Merger angle: procurement should demand price protection and assignment clauses before signing anything with a company mid-merger — friction you don't have.

## 6. Customer complaints

**Independent complaint volume: effectively zero.** No G2/Capterra/TrustRadius/GetApp/Gartner PI listings at all; Serchen has ~3 uniformly five-star reviews; FeaturedCustomers is vendor-curated; Info-Tech snippets are positive (time savings, support, onboarding). Reddit was crawler-blocked this run — a coverage gap, not proof of silence. [Documented]

- **Competitor-authored negative themes (label them as such if ever used):** "clunky UX / document vault / rigid workflows" (3+ competitor sources — flagged but all adversarial); "built for compliance, not marketers → adoption leaks to email/spreadsheets" (3 competitor sources); "manual checklists, static rules, slow at scale" (2 sources). Long-implementation claims are contested (vendor says 4–8 weeks; some snippets praise easy onboarding) — don't use.
- **Genuine positive theme to respect: support.** Multiple quasi-independent sources + vendor NPS/churn claims align. Do not build talk tracks attacking their service.
- **Reframe:** "2,300 claimed clients and not one review on G2, Capterra, or TrustRadius — the public record of this vendor is entirely their own marketing. Ask for referenceable proof, and put both vendors' claims through the same POC."

## 7. Ex-employee signals

- **Organizational health:** very thin public signal — Glassdoor ~2–5 reviews (culture 5.0, senior management 3.2 — only soft negative, sample too small to lean on; "no opportunities for advancement — typical small company"); Indeed reviews overwhelmingly positive and read pre-PE-era ("best company I ever worked for," "owners are extremely nice"). [Documented, low-n]
- **Product/market truth from former staff:** none found — no essays, podcasts, or public commentary by identifiable ex-employees.
- **Deal-relevant inference (marked as inference):** the churn story is at the **top, not the bottom** — founder-CEO out (2024), near-complete C-suite turnover 2024–26, CEO seat now passing to the merger partner's chief. Rank-and-file looks stable and loyal. Implication: institutional product knowledge persists (their delivery won't wobble quickly), but **strategy continuity is the soft spot** — roadmap promises made by executives who may not be there after integration. Aim continuity questions at the executive layer, not the delivery layer.
- Job-posting tells: engineering ad admits "mixed or transitioning technology stacks" (.NET + inherited Java); AI skills sought are Copilot-style *tooling* use, not ML engineering — no ML-scientist roles ever observed. Consistent with prompts-on-rules-engine reality. Boundary note: nothing confidential encountered.

## 8. Where they win (honest)

- **FINRA filing automation + 17a-4 workflow as the primary requirement.** Their fortress. If the buyer's pain is filing volume and books-and-records workflow with light review volume, let them have it or coexist — don't bleed cycles.
- **Top-20 asset managers with a decade of embedded workflow.** Deep configurations, trained reviewer teams, filing history. Rip-replace here fails; the coexist wedge (§ below) is the only path.
- **Conservative CCOs who want "Compliance-Grade AI™."** Their anti-black-box narrative lands with buyers whose board just read FINRA's GenAI warnings. If the buying committee's top criterion is "AI that can't surprise us," their story is built for it — counter with auditability-of-AI (per-finding citations, human sign-off) rather than AI enthusiasm.
- **One-throat-to-choke platform buyers (post-merger).** Once MirrorWeb integrates, "create→review→distribute→supervise→archive from one vendor" will genuinely appeal to consolidation-minded enterprises — in ~12–24 months. Beat the clock.
- **Support-and-relationship renewals.** Their service reputation is real; incumbent renewals defended by beloved support teams are hard to flip on features alone.
- **The coexist-then-displace motion (recommended default):** sell "keep your Red Oak workflow and FINRA filing — add Haast as the review intelligence and live-estate layer." Avoids the migration/records objection, lands fast, and every quarter widens the intelligence gap until their workflow is a commoditized routing utility at renewal. Rip-replace only at light-usage mid-market accounts, or anywhere their AI Review add-on is actively being evaluated — beat it *before* it lands, because "we already have AI" blocks the door afterward.

## 9. Landmines (discovery-question form — never name Red Oak)

1. Ask: **"Can your own team see, edit, and version the logic your AI reviewer applies — or is it configured by the vendor's implementation team at onboarding?"** → Their prompts are vendor-configured; buyers can't inspect the review logic (§4.1).
2. Ask: **"What accuracy or catch-rate will each vendor commit to in writing, measured on your content?"** → No published AI Review accuracy exists (§4.1).
3. Ask: **"When a rate changes or a regulation updates, what tells you — same day — every live page, PDF, and post that's now non-compliant?"** → Their monitoring is rep surveillance/archiving, not live-estate re-review (§4.2).
4. Ask: **"Has your reviewer workload per asset actually gone down with your current tooling — or has routing just gotten smoother?"** → Their five-year-old ROI stats measure routing, not review effort (§4.5).
5. Ask: **"If a vendor is mid-merger, which entity signs your contract, whose roadmap survives, and what SLA and assignment protections do you need?"** → MirrorWeb merger, announced Jul 28, 2026, not closed (§4.3).
6. Ask: **"Will your marketing team actually work inside the tool — can they demo-drive the submission experience before you buy?"** → The marketer-adoption critique, tested rather than asserted (§4.6).
7. Ask: **"For your non-US entities, does the vendor reason under FCA or ASIC rules — or apply US rulebooks globally?"** → US-only reasoning (§4.4).

## 10. Objection-handling angles

**When Red Oak is the incumbent or shortlisted — what your champion will hear:**

1. *"They were built by compliance officers — they know this world."* → Reframe: "They do — and what they built in 2010 was a routing-and-filing system, which is still what it is. The 2026 question is review intelligence: whose AI reads your content against current FINRA, FTC, and FCA rules with citations your team controls? Their AI answer is a prompt layer their implementation team configures. Keep their plumbing if you like it; add the intelligence."
2. *"Nineteen of the top 20 asset managers use them."* → Reframe: "For workflow and filing — and note their own materials can't agree whether it's 1,550, 1,800, or 2,300 firms. Ask the sharper question: how many of those firms have reduced reviewer hours per asset? Their headline metric has been '35% faster approvals' since 2020 — routing efficiency, not review capacity. We'll commit to measured review-effort reduction in the pilot."
3. *"They have AI now — AI Review, Compliance-Grade AI™."* → Reframe: "Real, and worth examining: GPT-3.5/4 prompts configured by their team at onboarding, giving submitters feedback before humans review everything anyway — with no published catch-rate. 'Compliance-grade' should mean you can see the logic, version it, and measure it. Put both AIs on your corpus for two weeks and count."
4. *"They monitor post-publication too — websites, social, and soon archiving with MirrorWeb."* → Reframe: "That stack watches what your *reps* post and archives your comms — supervision. Different problem from: 'our advertised rate changed; which of our own 4,000 live pages is now wrong?' That's continuous re-review of your live estate, which is Haast's founding capability and absent from theirs."
5. *"17a-4, FINRA filing — startups can't do our records."* → Concede + reframe: "Keep that plumbing — genuinely good. Haast's review outputs are auditable, exportable records that feed your filing and archiving systems; we're not asking you to move your books. The gap isn't records storage — it's what never gets caught before it's stored." (Verify Haast's 17a-4/archiving-integration posture internally before extending this.)
6. *"Now's not the time to change — they're merging, the platform's getting bigger."* → Flip it: "Merging is exactly when to de-risk: third acquisition in 30 months, the CEO seat passing to the merger partner, brands not yet unified, roadmaps to be reconciled. Adding Haast as the review layer *doesn't* touch their workflow — it hedges you against their integration timeline while they sort it out."
7. *"Their support is fantastic."* → Agree and redirect: "It is — consistently praised, and we're not asking you to give it up. The question is whether great support on a workflow tool solves a review-capacity problem. It can't; only review intelligence moves that number."

**FUD they will plant about Haast — pre-armed responses:**

| Their likely line (from their documented narrative) | Your response |
|---|---|
| "GenAI is a black box — FINRA itself warns about it. Our AI is precision, not prediction — no model training on your data" | "Their AI is prompts their team configures that you can't inspect — that's the actual black box. Haast shows the rule citation behind every finding, keeps humans in the approval loop, and nothing publishes without sign-off. FINRA's guidance asks for *governed* AI, which is an audit-trail question — ours is AWS-published. And they sell LLM review too now; the category question isn't whether to use genAI, it's whose is measurable" |
| "Built by compliance officers; startups don't know FINRA" | Haast ships FINRA/FTC/FCA agents validated in production at Aviva, Zurich ANZ, Equity Trustees, Telstra — regulated tier-ones. Expertise is testable: same corpus, both tools, count the catches |
| "2,000+ firms, 16 years — we're the safe choice" | "Safe" is under revision: merger announced July 2026, new controlling CEO from the merger partner, integration ahead. Haast: $12M Series A led by Peak XV (Apr 2026), single product, single roadmap. Ask both vendors for continuity commitments in writing |
| "We're end-to-end now — create to archive, one vendor" | Announced, not integrated: MirrorWeb still trades under its own brand while the "joint customer experience is built out." One-vendor value arrives only after integration succeeds; your compliance exposure is now. Best-of-need beats someday-suite |
| "They can't file with FINRA or store 17a-4" | Correct on filing — keep Red Oak's pipe, we feed it. On records: auditable exportable outputs into your archive (confirm Haast specifics internally). The buyer's records system doesn't need replacing; their review capacity does |

## 11. MEDDPICC angles

- **Metrics:** reviewer hours per 100 assets (their metrics never touch it), AI catch-rate/precision on the buyer's corpus (they publish none), time-to-detection of live-estate drift (no capability), % of review logic visible/versionable by the buyer's team (theirs: vendor-configured prompts). Concede routing metrics — don't compete on "% faster approvals."
- **Decision criteria to install:** (1) measurable AI review accuracy with written commitment; (2) buyer-controlled, versionable review logic; (3) live-estate re-review capability demoed on the buyer's real site; (4) marketer-experience score from the marketing team's own demo-drive; (5) vendor-continuity and assignment protections given merger status; (6) multi-jurisdiction reasoning where relevant. Their sheet (pedigree/scale/17a-4/filing) is strong — get yours scored first or alongside, never accept theirs alone.
- **Pain they leave unsolved:** review capacity (humans still read everything), live-estate drift, marketer adoption leakage to email/spreadsheets [competitor-sourced — test it], non-US reasoning, and now integration uncertainty.
- **Paper process / procurement:** their friction — mid-merger contracting entity/assignment questions, modular add-on quotes that balloon, SOC 2 status unverifiable publicly, no marketplace paper. Your leverage — coexist positioning shrinks the ask (intelligence layer, not platform swap → smaller line item, shorter security review, no migration project), price protection they'll struggle to match mid-transaction, and speed. Their leverage — existing MSAs, beloved support, and the FINRA-filing dependency; never let the deal be framed as "replace the filing system."
- **Champion note:** the CCO's attachment is to the *records/filing safety* and the support relationship — reassure both explicitly before differentiating. The marketing leader is your natural second champion (their tool is not built for marketers — let marketing say it). Post-merger, exec-level uncertainty is your entry point to the economic buyer: "hedge the integration."

## 12. Sources

Provenance: **[cached]** = search-engine-indexed/cached content (direct fetch blocked — ground rule 5). **[competitor]** = competitor-authored. Accessed 2026-08-04.

**Red Oak first-party** (all [cached]): redoak.com — home ("2,000+ firms," top-20 claims), /our-story/ (founders), /ai-review/ + redoakcompliance.com/aireviewmodule (LLM + prompt engineering; vendor-configured prompts; 17a-4 storage of AI results), AI Review launch PR (Jan 7, 2025), /resources/articles/ai-in-compliance-precision-not-prediction/ ("Compliance-Grade AI™" scaffolding), FINRA GenAI-risk articles, supervision suite pages (SiteQuest/internet supervision/social media), /rulebooks-era AdMaster pages, /integrations/ (Seismic, Aprimo, Workfront, Word add-in), testimonials (anonymized), Accelerate 2026 event pages, admaster-prod.redoakcompliance.com login ("Red Oak v2026.0711.3")

**M&A / ownership / leadership** (all [cached]): globenewswire.com (Mainsail $51M, Jun 29 2023 — "1,800+ firms"; SiteQuest acquisition Mar 5 2024; AREF integration 2016) · prnewswire.com — **MirrorWeb merger (Jul 28, 2026, 302835903 — "1,550+ firms, $62T AUM," Bosu CEO, Dutch to advisor)**, Oct 2025 MirrorWeb partnership (302594827), Dutch CEO (302132508), Newbold-Knipp COO (302603504), Sadler CPO (302682277, ex-Mitratech), Lubansky SVP Product (302144891), Smart Review 2020 (301068857 — 800K disclosures) · fintech.global (4U acquisition Apr 2025; merger analysis Jul 28 2026; exec hires) · mainsailpartners.com portfolio/news · mirrorweb.com merger blog · citybiz/pulse2 merger coverage · einpresswire (Inc 5000 7th year — "2,300+ firms"; RegTech100; FT list; Registration Management module Oct 2024)

**Reviews/community** (all [cached]): serchen.com (3 five-star reviews; phone-for-quote) · featuredcustomers.com/vendor/red-oak-compliance (vendor-curated, 13–14 references) · infotech.com/softwarereviews listings (positive snippets) · slashdot.org/software/p/Red-Oak-Software (**AI stack: "ChatGPT 3.5 Turbo and GPT4 on Microsoft Azure"**; AdMaster praise quote) · G2/Capterra/TrustRadius/GetApp/SoftwareAdvice/Gartner PI: **no listings found** (domain-restricted searches) · fintech.kitces.com directory entry; SmartRIA/RightCapital Kitces-report recaps (category positioning) · glassdoor EI_IE2556012 (~2–5 reviews) · indeed reviews (positive, pre-PE era) · regfin.com pricing guide (category custom-pricing norms) · Reddit: crawler-blocked — coverage gap, not absence

**Competitor-authored** (all [cached] [competitor]): hellowarrant.com warrant-vs-red-oak ("legacy," "document vault," "not built for marketers," "manual checklists") + best-tools roundup · blee.com top-providers roundup ("built over a decade ago… rarely loved by teams who create content") · sedric.ai ("document-centric tools built for a pre-AI world") · luthor.ai RIA tools roundup (neutral) · Greenboard-adjacent comparison (4–8 week go-live; "deeper penetration in marketing compliance")

**Haast baseline** (all [cached]): aws.amazon.com/solutions/case-studies/haast-case-study/ · prnewswire 302737540 ($12M Series A, Peak XV, DST Global Partners, Airtree, Aura, Black Sheep — Apr 2026) · itbrief.com.au / businessnewsaustralia.com (Telstra, Aviva, Zurich ANZ, Equity Trustees, Future Super) · haast.io case studies

**⚠ Verify live before quoting in a deal:** (1) **MirrorWeb merger status — has it closed? Who's announced in which role?** (this card's central angle is time-sensitive); (2) AI Review current capability — the GPT-3.5/4 stack disclosure is a directory listing and may be stale; (3) client-count figure currently on redoak.com; (4) SOC 2 — ask directly, unverifiable publicly; (5) whether a Haast-vs-Red-Oak comparison page has appeared on either side since this run.
# BATTLECARD: Smarsh (smarsh.com)

**Run date:** 2026-08-04 · **Refresh by:** 2026-11-04 (quarterly) · **Prepared for:** Haast US sales
**Read this first:** Smarsh is NOT a head-to-head marketing-compliance competitor — it's the adjacent archiving/surveillance giant whose name gets waved into your deals as **"we already have Smarsh for compliance — why do we need you?"** This card is built to defuse that objection and keep Smarsh out of the marketing-review evaluation, not to displace their archive (don't try — you'll lose and it's not your business).
**Provenance note:** direct fetches blocked by the research environment's egress proxy — claims sourced from search-engine-indexed/cached versions of cited pages (ground rule 5), tagged **[cached]**. Competitor-authored items tagged **[competitor]**. Verify-live list in §12.

---

## TL;DR for the 2-minute pre-call read

Smarsh is the 25-year, K1-owned, ~1,700-person canonical name in communications capture/archiving/supervision — Gartner MQ Leader (DCGA, 2025), 6,500+ customers, "18 of top 20 global banks," the 17a-4 default. **None of that is marketing-compliance review.** Their only pre-publication feature is a LinkedIn profile-change gate; their AI (Intelligent Agent, Noise Reduction Agent, Discovery Agent) triages surveillance alerts on *captured* comms; they've done 6+ acquisitions over 25 years and never bought a marketing-review asset (Hearsay went to Yext); their hiring shows zero marketing-review roles; and they've *published an article arguing pre-approval of social posts isn't necessary* — they are rhetorically committed to the post-hoc model. The play is coexistence: **Smarsh = system of record, Haast = system of review** — the regulator wants both. Your leverage when they lean in anyway: contract/billing/export-fee complaints so entrenched Smarsh launched a "Data Freedom Guarantee" (Jul 2025) to fight its own reputation, the May 2025 TeleMessage breach (Senate DOJ-investigation request), rolling layoffs/offshoring, and a demo challenge they cannot meet: *"show us the screen where a draft campaign gets a claims-and-disclosures review."*

---

## 1. Company snapshot

| Item | Finding | Confidence |
|---|---|---|
| Founded / HQ | 2001, Portland OR, by Stephen Marsh (now Founder & Chairman only) | Documented [cached] |
| Ownership | K1 Investment Management since 2016 (Actiance merged in 2017); 2022 K1 ran a $3B+ GP-led continuation-vehicle process including Smarsh (completion unconfirmed). ~8–10 year hold. No sale/IPO announced 2025–26; **CFO hired Jan 2026 (Ian Goodkind) led Jamf's IPO** — soft exit-prep signal, inference | Documented [cached]; exit read inference |
| Leadership | CEO Kim Crawford Goodman (since 2022; payments background — Fiserv/Worldpay/Amex, not compliance). **Jan 2026 "AI acceleration" reorg**: Kamesh Tumsi CPO (ex-HealthEquity, GenAI mandate), Goutam Nadella CPO→CSO, CFO churn (Brolsma lasted ~10 months) | Documented [cached] |
| Scale | ~1,700 employees (flat-to-shrinking: ~1,784 peak 2024 → ~1,709 2026); 6,500+ customers (older materials say "20,000+ orgs" — SMB tails); ~$1.4B raised lifetime | Documented claims [cached] |
| M&A | Entreda (2020), Digital Reasoning (NLP/surveillance AI, 2020), Micro Focus Digital Safe ($375M, 2022), TeleMessage (closed Feb 2024), CallCabinet (voice, Feb 2025). **All comms infrastructure — never a marketing-review asset in 25 years.** (Note: Fairwords went to MyComplianceOffice, not Smarsh; Hearsay went to Yext, Aug 2024) | Documented [cached] |
| Analyst position | Leader, 2025 Gartner MQ for Digital Communications Governance & Archiving (2nd consecutive year) | Documented [cached] |
| Segments | Broker-dealers, banks, RIAs, insurers, government/public sector (FOIA). Named: Jefferies (surveillance expansion Oct 2025), ValMark | Documented [cached] |
| Pricing | Professional Archive (SMB): ~$8–35+/user/mo per aggregators. Enterprise: quote-only; **Vendr: typical ACV $75K–$300K, prices vary 30–50% for similar scope depending on negotiation** — pricing opacity documented. Auto-renewing 12-month terms with 60–90-day written non-renewal windows (their own services agreement) | Medium [cached]; contract terms primary-source |

## 2. Positioning + narrative

- **One-liner:** "Communications Intelligence Platform" — capture (100+ channels), archive (the 17a-4 canonical name), supervise (Conduct), discover. AI story since 2024: "defensible, repeatable, secure" AI for surveillance. [Documented, cached]
- **Their marketing-compliance story — and the blur it creates:** Smarsh publishes heavy SEO on the SEC Marketing Rule (FAQs 2026, 2025 Risk Alert gap analyses, finfluencer posts, FINRA 2210 regulation page). What they actually sell against those pages is the **books-and-records leg**: "capture, retain, and produce marketing communications, *approvals*, and disclosures as they were actually used." **The approvals are an input Smarsh stores — not an output Smarsh produces.** A buyer googling "SEC marketing rule compliance software" lands on Smarsh and reasonably, wrongly, concludes it's covered. [Documented, cached]
- **They are rhetorically committed against pre-publication review:** Smarsh published "Are Pre-approved Social Media Posts Necessary?" arguing regulators don't require pre-approval of dynamic content and post-hoc supervision suffices. Their entire economic engine (capture → archive → supervise) depends on the post-hoc model. [Documented, cached — gold in deals]
- **Regulatory narrative:** the off-channel enforcement wave ($390M Aug 2024, $63M Jan 2025) was their tailwind; their own blog concedes it may be "one of the last major waves" under the current administration, reframed as "Recalibration, Not Retreat." The 2026 pivot: capturing employees' *genAI tool usage* (ChatGPT Enterprise, M365 Copilot, Claude Enterprise compliance APIs) — hunting the next tailwind. [Documented, cached]
- **Who they name:** nobody (set = Global Relay, Proofpoint per comparison pages). **Zero references to Haast, Saifr, or PerformLine anywhere.** Marketing-content review has never appeared in their roadmap language, hiring, or M&A. [Documented absence]
- **Naming trap:** "CommsAI" is NOT a real Smarsh brand — the umbrella is "Communications Intelligence," agents are named (Intelligent/Noise Reduction/Discovery), and the AI org is the "Cognition" team (Digital Reasoning heritage). If a prospect says "Smarsh CommsAI," they're paraphrasing — don't concede a product that doesn't exist. [Documented absence]

## 3. Feature matrix vs. Haast (marketing-compliance lens only)

| Capability | Smarsh | Haast | Notes |
|---|---|---|---|
| Pre-publication review of marketing creative | **No product.** Only pre-pub control found: **LinkedIn Pre-Review** (gates advisers' profile changes until compliance releases) + in-stream DLP/blocking on X for "certain deployments" (Actiance heritage). No submission/approval workflow for campaigns, no claims substantiation, no disclosure-adequacy checking | **Core product** — AI review with FINRA/FTC/FCA agents pre-publication | The demo challenge: "show us where a draft campaign gets reviewed in Smarsh." No such screen exists |
| AI on marketing content | **None.** Documented AI = alert triage on captured comms: Intelligent Agent (Sep 2024→GA 2025), Noise Reduction Agent (-60% alerts, Mar 2026), Discovery Agent (e-discovery, 2026), genAI-channel capture (May 2026). Trained objective: "should a human look at this flagged message?" | AI answers: "may this asset ship, and is it still compliant while live?" | Two different questions. Make the buyer see the difference |
| Post-publication | **Capture + archive + lexicon/sampling supervision** — evidence of what was published, misconduct detection in conversations. Web Archive: site snapshots, date-compare — evidentiary, flags nothing | **Continuous compliance re-review of the live estate** — rate/reg/product changes → finds every now-non-compliant live asset | Their archive stores the drift; it never re-assesses it |
| Social media | Capture LI/X/FB/IG native format; supervision queues; SOCi partnership (publishing tool + Smarsh archive behind it — even Smarsh treats publishing workflow as someone else's product) | Monitoring + review of social marketing content | Their social product is recordkeeping-first |
| Channels | 100+ captured (email, mobile, WhatsApp, Teams, Slack, voice, social, web, genAI tools) — breadth is real, for *capture* | Marketing-content channels for *review* | Different axis entirely; don't compete on channel counts |
| Regulator coverage | SEC 17a-4 (canonical), FINRA books-and-records/3110, Marketing Rule *recordkeeping*, FCA comms, MiFID II, FOIA | FINRA/FTC/FCA *content rules* — the substantive leg | They own the records leg; you own the review leg. Both required |
| Records/archive | **The category leader. Do not compete here** | Auditable/exportable review artifacts that feed any archive (verify current integration/export posture internally before slides — no named Smarsh connector is publicly documented) | Coexistence architecture, §8 |
| Proof | Gartner MQ Leader, 6,500+ customers, Jefferies — real enterprise trust in DCGA. **Zero marketing-content-review case studies exist** | AWS case study, Telstra/Aviva/Zurich ANZ/Equity Trustees, $12M Series A (Peak XV, Apr 2026) | Their proof is in a different category — say so plainly |
| Commercial reputation | Documented friction: billing "ballooned to nearly triple" via un-agreed add-ons; auto-renew traps (60–90-day notice windows, primary source); **export-fee "data hostage" complaints so entrenched Smarsh launched a "Data Freedom Guarantee" (Jul 31, 2025 — Professional Archive tier only)**; Vendr 30–50% price variance | Table transparent pricing + paper | Their guarantee is a de facto admission; note it covers the SMB tier — probe Enterprise terms |
| Security trust | **May 2025 TeleMessage breach**: Smarsh-owned Signal clone used by US officials hacked in ~15–20 min via exposed endpoint; plaintext data incl. CBP/Coinbase; services suspended; Sen. Wyden requested DOJ investigation; Proofpoint attack-markets on it | Table Haast security pack | Use carefully — as a diligence fact, not a taunt |

## 4. Feature gaps (ranked — all in the marketing-compliance frame)

1. **No pre-publication marketing review product, and a published position against needing one.**
   (a) Evidence: no submission/approval/claims/disclosure product exists anywhere in their materials; only LinkedIn profile-change gating; their own blog argues post-review supervision suffices for dynamic content; Marketing Rule content sells recordkeeping of reviews done elsewhere.
   (b) Confidence: high (multi-source, incl. their own words).
   (c) Exploitation: the objection-killer combo — demo challenge ("show us the draft-campaign review screen") + their own article. If the CCO says "Smarsh covers marketing compliance," their vendor's own published position says marketing review isn't Smarsh's job.

2. **AI is pointed at surveillance economics, not content review — and hiring proves it.**
   (a) Evidence: every shipped AI agent triages alerts on captured comms; every AI job posting (ML engineers Bangalore, AI PM in "Cognition" team) is surveillance/archive/discovery-framed; zero postings ever referencing marketing compliance, advertising review, pre-publication, or the Marketing Rule.
   (b) Confidence: high.
   (c) Exploitation: "ask what their AI is trained to do — reduce alert noise on captured messages. Ask what it would even mean for that AI to approve an ad." Watch-item: monitor Cognition-team PM postings for "content review/marketing" language — that's the early-warning tripwire for them entering your category.

3. **25 years of M&A, never toward marketing review.**
   (a) Evidence: 6+ acquisitions all comms infrastructure; when Hearsay Systems (the adviser-marketing workflow asset) sold in 2024 it went to Yext; Smarsh's marketing-adjacent partnership (SOCi) makes them the archive *behind* someone else's publishing tool.
   (b) Confidence: high.
   (c) Exploitation: against "it's on our roadmap" — 25 years of revealed preference. Discount roadmap claims to zero without a named GA date and reference.

4. **Commercial friction corpus (billing/renewal/export).**
   (a) Evidence: multi-sourced and partially self-admitted — tripled-bill review, auto-renew terms in their own services agreement, "data hostage"/"contract hell" review language, Vendr's 30–50% negotiation variance, competitor category built on "no export fees" (Archive Intel, Presults, Jatheon), and **Smarsh's own Data Freedom Guarantee as validation**.
   (b) Confidence: high on theme; individual anecdotes unverifiable.
   (c) Exploitation: NOT to displace their archive — to counter "one vendor is simpler": "consolidating more spend into a vendor with documented renewal and export friction increases lock-in, not simplicity." Also arms procurement to renegotiate Smarsh terms — which makes you the CCO's friend.

5. **Security-trust dent: TeleMessage.**
   (a) Evidence: May 2025 breach, services suspended, CISA warning, Wyden DOJ letter; Glassdoor review ties layoffs to the fallout.
   (b) Confidence: high (multi-outlet).
   (c) Exploitation: sparingly, as diligence: "for any vendor handling regulated content, ask about their acquisition security-integration record." Never gloat — enterprise buyers punish that.

6. **Organizational strain behind the AI messaging.**
   (a) Evidence: rolling layoffs (documented round Jun 2025; "every quarter" per employee reviews), US→Bangalore offshoring resentment, support/eng understaffing themes that corroborate customer support complaints, "no clear product roadmaps" internal reviews, headcount shrinking while integrating six acquisitions, Jan 2026 exec reshuffle, CFO churn.
   (b) Confidence: medium (anonymous self-reports; consistent pattern).
   (c) Exploitation: strategy input, not talk track — expect slow support/escalation at the account, and expect their AEs to over-promise AI. Force everything to demo.

## 5. Pricing signals

- **Published:** Professional Archive semi-transparent (~$8–35+/user/mo aggregator range, ~$5 baselines, Personal Access add-on ~$5); Enterprise quote-only. [Cached, medium]
- **Benchmarks:** Vendr — **typical ACV $75K–$300K; 30–50% price variance for similar scope** (negotiation-dependent pricing = opacity ammo). 15–25% discounts on 3-year terms, volume discounts at 500+ users. A leaked 2022 pricing sheet circulates. [Cached]
- **Contract mechanics (primary source):** auto-renewing 12-month terms; written non-renewal notice 60–90 days before term end; historical terms charged "then current data extraction and exportation fees plus hardware costs" on exit — the structural basis of the data-hostage complaints. Data Freedom Guarantee (Jul 2025) waives self-service export fees **for Professional Archive** — probe what still applies on Enterprise paper.
- **How to use pricing in YOUR deal:** Haast isn't competing for the Smarsh budget line — position Haast's spend as new risk coverage the Smarsh line never provided ("you're paying for records of what published; nothing you pay today reviews it before or after"). When the buyer's Smarsh renewal is near, the export-fee/auto-renew literacy you provide builds champion trust and keeps the "consolidate into Smarsh" argument on the defensive.

## 6. Customer complaints

Unlike the AI-startup cohort, Smarsh has a real review corpus — read it precisely, because the headline is nuanced: **enterprise satisfaction is genuinely high (Gartner PI 4.6★ across ~140 reviews — their real mass); the pain concentrates in commercial terms and small-firm treatment.** Don't say "Smarsh has bad reviews" — you'll lose credibility. Say "documented contract friction and small-firm neglect."

**Flagged recurring themes (3+ independent sources):**
- **Billing/contracts/renewal (5+ sources):** tripled monthly bills via un-agreed add-ons; "contract rigidity and renewal friction are recurring pain points" (verified-review synthesis); auto-renew + notice windows (their own agreement); Vendr price variance; BBB complaints; an entire competitor category (Presults "no long-term contract") built against it.
- **Export fees / "data hostage" on exit (4+ sources):** "will hold your data hostage if you try to leave," "trapped in contract hell" (review synthesis); the "ransom payment for our own emails" small-firm story; their own historical contract language; **the Data Freedom Guarantee as de facto admission**.
- **Support responsiveness (4+ sources):** "slow support or difficult escalation paths"; "customer service can be difficult"; "apologized and offered nothing"; Gartner PI criticism of "support responsiveness" — mixed with plenty of praise; use specific instances, not blanket claims.
- **Product/UX reliability & complexity (4+ sources):** "constant error messages… searching, sorting, exporting extremely unreliable, glitchy, buggy" (25–90% of the time per one reviewer); "ProArc hangs"; steep configuration learning curve "more complex than company representatives suggest."
- **Supervision false positives (2–3 mentions — below bar, note only):** experienced but defended as industry-wide; Smarsh's own Echo Cancellation launch (Dec 2024) and "radically reduce false positives" marketing confirm the noise problem is material to their lexicon install base.
- **Community gap disclosed:** Reddit was crawler-blocked this run — adviser-forum verbatims (r/CFP, r/RIA) are worth a manual pull; the anti-Smarsh challenger ecosystem (Archive Intel, Presults, Jatheon) implies the chatter is rich.

## 7. Ex-employee signals

All from public anonymous review platforms (Glassdoor ~486 reviews, 3.5★; TheLayoff; Blind); individually unverifiable, themes recur across many posts. Nothing confidential encountered.

- **Organizational health:** "constant leadership changes, multiple re-orgs, and no clear product roadmaps"; review titles "New Leadership is destroying Smarsh," "Lay off every quarter," "Layoffs after US Govt data breach"; forced performance-score calibration to cap bonuses; voluntary turnover described as highest in company history; RTO mandate pushed exits. Teams bleeding per posts: enterprise engineering, support, long-tenured US staff.
- **Product/market truth:** support and engineering "completely understaffed… unrealistic goals"; US teams "gutted to hand off to offshore contractors" (one post alleges offshore handoffs "already caused security problems" — single anonymous claim, do not repeat externally); counter-signal: even skeptics concede "lots of potential for an AI-first use case."
- **Deal-relevant inference (marked as inference):** (1) expect slow escalation paths at your prospect's Smarsh account — quietly ask the buyer about their recent Smarsh support experience; (2) the PE-cost-pressure + offshoring pattern means their AI promises outrun staffing — force demos over decks; (3) exec churn (CPO/CFO/CSO inside 12 months) + IPO-experienced CFO reads as exit-window grooming — procurement-stability questions are fair game in any "consolidate into Smarsh" conversation.

## 8. Where they win (honest)

- **Archiving/DCGA — always, and that's fine.** If the question is "who archives our comms for 17a-4," the answer is Smarsh (or Global Relay). Haast should never contest it. The battle is only ever whether Smarsh's presence *blocks* a marketing-review purchase.
- **They win YOUR deal only when the blur wins:** a budget holder concludes "communications compliance" ⊇ "marketing compliance" and kills the line item. That's a framing loss, not a product loss — this whole card exists to prevent it.
- **Consolidation-mandate enterprises:** where IT/procurement has a hard "fewer vendors" mandate and the CCO is passive, "we'll wait for Smarsh to build it" can stall your deal into next fiscal year — even though 25 years say they won't build it. Counter with the revealed-preference history + a time-boxed risk framing (what drifts non-compliant on the live estate while you wait?).
- **The genAI-governance budget:** their ChatGPT/Copilot/Claude *capture* story is landing with AI-governance committees. If the buyer's "AI compliance" budget is really an AI-usage-archiving budget, that's Smarsh's money, not yours — qualify which problem is funded.
- **Disqualify/reframe rule:** if the deal has become "marketing review vs Smarsh renewal," you've been mis-framed — reset to system-of-record vs system-of-review or walk. If the CCO owns both budgets and understands the difference, Smarsh's presence is actually an *asset*: the archive is already solved, so the review gap is nakedly visible.

## 9. Landmines (discovery-question form — never name Smarsh)

1. Ask: **"Walk me through your last marketing campaign review — which system held the draft, the redlines, the claims substantiation, and the approval?"** → It's email/SharePoint/spreadsheets; their archive holds none of it (§4.1).
2. Ask: **"Show me where a draft ad gets a claims-and-disclosures review in your current compliance platform."** → No such screen exists in an archiving/supervision stack (§4.1).
3. Ask: **"When your supervision system flags a published page, how long was it live before the flag — and who re-reviews the whole estate when a rule changes?"** → Sampling/lexicon supervision after the fact; nobody re-reviews (§3, §4.1).
4. Ask: **"Your archiving vendor's AI — what is it actually trained to do? Alert triage on captured messages, or compliance judgment on draft content?"** → Alert-noise reduction, on their own materials (§4.2).
5. Ask: **"How many items are in your marketing pre-approval queue right now, and what's the SLA?"** → No such queue exists in their stack; surfaces the invisible manual process (§2).
6. Ask: **"Before consolidating more spend into any incumbent, has procurement reviewed the renewal-notice windows and data-export terms on the current contract?"** → Auto-renew + export-fee history; makes you procurement's ally (§5).
7. Ask: **"If a vendor tells you pre-approval isn't necessary and post-review is enough — does your examination posture agree?"** → Their published position, turned into a risk question (§2). Best used with SEC Marketing Rule Risk Alert findings in hand.

## 10. Objection-handling angles

**The core objection — "we already have Smarsh" — and its variants:**

1. *"We already pay Smarsh a lot for compliance."* → Reframe: "You pay them for *records* — proof of what was published and supervision of conversations after the fact. Regulators require two more things their platform doesn't produce: evidence a qualified review happened *before* publication, and assurance your live content is *still* compliant. That's the Haast layer. Nothing about your Smarsh deployment changes — approved content flows into their archive exactly as today."
2. *"Smarsh says their platform covers the SEC Marketing Rule."* → Reframe: "Read their pages closely — they say firms must 'capture, retain, and produce marketing communications, approvals, and disclosures.' The approval is an artifact you have to create somewhere else; they just store it. Ask them directly: where in the platform does a draft campaign get a claims-and-disclosures review? There's one honest answer."
3. *"Their AI is impressive — agents, LLMs, they even archive our ChatGPT usage."* → Reframe: "All true, and all pointed at one job: reducing alert noise on captured communications. Ask what their AI would even output for a draft ad. Capturing your genAI usage is archiving; reviewing your genAI-produced *marketing* is a different product — one their hiring, M&A history, and roadmap have never touched."
4. *"One vendor is simpler — we'd rather wait for Smarsh to build it."* → Reframe: "Twenty-five years, six acquisitions, all archiving and surveillance — when the market's adviser-marketing workflow company sold in 2024, it went to Yext, not Smarsh. And they've published that they think pre-approval isn't even necessary. Waiting is a bet against their own stated position. Meanwhile, price the wait: what's on your live estate right now that nobody has re-reviewed since the last rule change?"
5. *"Vendor sprawl / procurement fatigue."* → Reframe: "The sprawl is already here — it's the email approvals, spreadsheets, and agency threads your review process lives in today, none of it in Smarsh. Haast consolidates *that*. And on consolidation risk: their own contract terms and export-fee history are why they had to launch a 'Data Freedom Guarantee' — concentrating more spend there is lock-in, not simplicity."
6. *"Smarsh is the safe, regulator-trusted name."* → Reframe: "For archiving — agreed, keep them. Two diligence notes for the file: the TeleMessage breach (their acquired app, suspended after exposing government officials' data, with a Senate request for DOJ investigation) is worth a question about acquisition security integration; and 'safe' in your marketing-review workflow currently means manual email chains. We'd argue that's the least safe part of your stack."

**FUD Smarsh will plant about Haast — pre-armed responses:**

| Their likely line | Your response |
|---|---|
| "We're the compliance system of record — everything should live in one platform" | "Agree on records. Your own Marketing Rule pages say firms must produce *approvals* — which your platform stores but doesn't generate. Two jobs, both required. Haast generates; you archive; the examiner gets both" |
| "Our AI supervises all channels already" | "Documented function: alert triage on captured comms — 'should a human look at this flagged message?' Haast's function: 'may this asset ship, and is it still compliant while live?' Different questions. Demo both on a real draft campaign and the difference is over in five minutes" |
| "A startup point tool is risky" | "$12M Series A led by Peak XV with DST Global Partners (Apr 2026); AWS-published case study (500+ hours saved, 3x faster launches); Telstra, Aviva, Zurich ANZ, Equity Trustees in production. And risk cuts both ways: rolling layoffs, a breach with a DOJ-investigation request, and an exec bench that turned over inside twelve months — we're happy to exchange diligence packs" |
| "Pre-approval isn't required for dynamic content — post-review is sufficient" (their published stance) | "Take that position to your examiner alongside the SEC's 2025 Marketing Rule Risk Alert findings and recent 2210 actions. The firms that clear exams cleanly are the ones with review evidence *before* publication. It's also worth noting the vendor making that argument sells post-review software" |
| "We'll add marketing review to the platform" | "Ask for the GA date, the named beta customer, and which team builds it — their AI org's public postings are all surveillance roles. Then weigh 25 years of M&A that never once bought toward this category" |

## 11. MEDDPICC angles

- **Metrics:** own the numbers their category can't produce — % of marketing estate reviewed pre-publication, review-cycle time per asset, time-to-detection of live-estate drift, examiner-ready approval-artifact coverage. Never compete on channels-captured or archive volume.
- **Decision criteria to install (these keep Smarsh out of the review RFP):** (1) AI review of *draft* assets against regulator-specific rulesets; (2) claims-substantiation and disclosure-adequacy analysis (not lexicons); (3) marketing-native workflow with SLAs and versioned redlines; (4) continuous re-assessment of live content on rule/product changes; (5) weeks-to-value with marketing + compliance users; (6) review artifacts exportable to the existing archive. Smarsh checks none; even their SOCi partnership concedes publishing-side workflow is someone else's product.
- **Pain they leave unsolved:** the entire pre-publication bottleneck (which lives in email/spreadsheets today), live-estate drift, claims substantiation, and the approval-evidence gap their own Marketing Rule content says examiners demand.
- **Paper process / procurement:** their friction — auto-renew windows, export-fee history, 30–50% price variance, mid-hold PE dynamics; yours — a *new, smaller* line item that doesn't touch the archive budget, faster security review, transparent paper. Tactical: time your proposal away from "consolidation review" season, and if the buyer's Smarsh renewal is within 6 months, arm procurement with the renewal-notice/export-terms checklist — trust earned there converts.
- **Economic buyer note:** the fatal pattern is the CIO/procurement owning the decision on a "vendor count" metric. Anchor the CCO/GC on examination risk (approval evidence + live-estate assurance) early; once the review gap is framed as regulatory exposure rather than software preference, "wait for Smarsh" stops surviving contact with the risk register.

## 12. Sources

Provenance: **[cached]** = search-engine-indexed/cached content (direct fetch blocked — ground rule 5). **[competitor]** = competitor-authored. **[employee]** = anonymous review platforms. Accessed 2026-08-04.

**Smarsh first-party** (all [cached]): smarsh.com — platform/innovation ("Communications Intelligence"; genAI capture), channels (social/LinkedIn/X/Facebook/Instagram/web/Marketo), smb/web-archive, product-spotlight supervision pages (lexicon + random review), **blog/LinkedIn-pre-review** (the lone pre-pub feature), **blog "Are Pre-approved Social Media Posts Necessary?"** (their anti-pre-approval position), Marketing Rule pages (regulations/sec-marketing-rule-206-4-1; FAQs 2026; 2025 Risk Alert gaps; finfluencer), FINRA 2210 + 17a-4 regulation pages, solutions/role/marketing (archiving pitch), off-channel penalty blogs + 2025 enforcement recap ("Recalibration, Not Retreat"), NYSE Floor Talk (CEO), AI-governance capture blog (CPO), leadership page · **legal-docs/SmarshServicesAgreement-v1025.pdf** (auto-renew + notice terms — primary) · press releases: Intelligent Agent (Sep 2024), SMB AI surveillance + Noise Reduction Agent (Mar 2026), AI advances + Claude/ChatGPT/Copilot capture (May 7, 2026), AWS collaboration (Jun 25, 2026 — "77% review-workload reduction"), Gartner MQ Leader (Oct 27, 2025), Jefferies (Oct 21, 2025), **Data Freedom Guarantee (Jul 31, 2025)**, CallCabinet (Feb 2025), TeleMessage close (Feb 2024), CEO appointment (2022), Jan 2026 leadership reorg (Tumsi CPO/Goodkind CFO — businesswire 20260121767004)

**Reviews/benchmarks** (all [cached]): gartner.com Peer Insights (4.6★/~140 — their real review mass; "pricing complexity and support responsiveness" criticisms) · g2.com seller (33 reviews/4.3) + product pages (ProArc hangs; false-positives comment; complexity) · capterra p/130954 + softwareadvice profile (error-messages review; tripled-billing + email-ransom complaints) · trustradius (7.5/10, 2 reviews) · **vendr.com/marketplace/smarsh (ACV $75K–$300K; 30–50% variance)** · itqlick, selecthub, peerspot, rfp.wiki (verified-review synthesis: "data hostage," "contract hell," fee transparency, escalation paths) · bbb.org profile (detail gated)

**Anti-Smarsh challenger ecosystem** [competitor]: archiveintel.com ("never charges retrieval/export fees") · presults.com ("no long-term contract") · jatheon.com/blog/smarsh-alternatives ("no hostage fees") · orgiq.com/compare/smarsh · sedric.ai/blog/smarsh-alternatives (1-to-many pre-publication gap point) · proofpoint.com TeleMessage attack content

**TeleMessage breach** (all [cached]): techcrunch.com (May 5, 2025), securityweek.com (CISA warning), wyden.senate.gov DOJ letter PDF, nbcnews.com (services suspended), complexdiscovery.com

**Employee voice** [employee] [cached]: glassdoor E429824 (~486 reviews, 3.5★; RVW99167172 "Layoffs after US Govt data breach," RVW73870794 "Lay off every quarter," RVW83601591) · thelayoff.com/smarsh (Jun 24, 2025 round; offshoring threads) · teamblind.com India-offshore thread · indeed.com/cmp/Smarsh/reviews · reveliolabs.com (headcount 1,784→1,709)

**Corporate/M&A** (all [cached]): mergr + wikipedia (K1 2016; Actiance 2017) · buyoutsinsider.com (2022 GP-led process) · prnewswire/businesswire acquisition PRs (Entreda 2020, Digital Reasoning 2020, TeleMessage 2024, CallCabinet 2025) · sec.gov Micro Focus 6-K (Digital Safe $375M) · **yext investor releases + businesswire + wsgr (Hearsay → Yext, $125M + $95M earnout, closed Aug 1, 2024)** · mco.mycomplianceoffice.com (Fairwords → MCO, correcting a common misattribution) · vvp.vc (SOCi partnership) · lever.co/smarsh + builtin + instahyre (job postings; Bangalore ML roles; zero marketing-review roles) · pitchbook/tracxn/crunchbase profiles

**Haast baseline** (all [cached]): aws.amazon.com/solutions/case-studies/haast-case-study/ · prnewswire 302737540 + axios.com/pro (Apr 9, 2026 — $12M Series A, Peak XV, DST, Airtree; 4.5x growth, zero churn company-reported) · itbrief.com.au / businessnewsaustralia.com (Telstra, Aviva, Zurich ANZ, Equity Trustees) · haast.io (integrations, audit trail — via snippets)

**⚠ Verify live before quoting in a deal:** (1) LinkedIn Pre-Review scope (profile changes vs all post types) and X in-stream blocking availability — demo-verify; (2) whether TeleMessage services resumed or were divested; (3) Data Freedom Guarantee's current scope (Professional vs Enterprise tiers); (4) Haast's productized export path to archiving systems — confirm with product before any "feeds your archive" slide; (5) any Cognition-team postings mentioning content review/marketing (the category-entry tripwire); (6) K1 exit developments.
# COMPETITIVE INTEL SUMMARY — 2026-08-04 Run

**Competitors covered:** Blee · AdClear · Saifr · PerformLine · Red Oak · Smarsh
**Prepared for:** Haast US sales · **Refresh by:** 2026-11-04 (sooner if the Red Oak/MirrorWeb merger closes)
**Method note:** this run's research environment blocked most direct page fetches, so the evidence base is search-engine-indexed/cached content per the run's ground rules — every battlecard flags provenance per claim and carries a "verify live before quoting" list. Treat verbatim quotes as re-verify-before-use.

---

## 1. The five most important takeaways

**1. The market splits into two attack surfaces — and Haast is the only vendor in this run that spans both.**
Three AI-native startups (Blee, AdClear, and to a degree Saifr) own pre-publication review stories but have unproven or absent post-publication monitoring; three incumbents (PerformLine, Red Oak, Smarsh) own monitoring/workflow/records but are retrofitting or ignoring AI review. Haast's pre+post lifecycle coverage is the single most repeatable differentiator across all six cards. In every deal, install "full-lifecycle coverage, demoed live" as decision criterion #1 — no one in this run can check it cleanly.

**2. Nobody has independent customer proof — turn the whole category's silence into a diligence standard.**
Across all six vendors: Blee, AdClear, Saifr, and Red Oak have effectively **zero** reviews on G2/Capterra/TrustRadius; PerformLine's footprint is a ghost town (Capterra still lists a legacy product name); only Smarsh has real review mass (Gartner PI 4.6/~140 — and its documented pain is contract friction, not product hate). Saifr and Red Oak publish **no named customers at all**. The universal reframe: "for every vendor on your shortlist, ask for named references and one independent review — then weight claims accordingly." Haast wins that comparison with named enterprise logos (Telstra, Aviva, Zurich ANZ, Equity Trustees) and an AWS-published case study.

**3. Every incumbent is mid-disruption of its own — the stability argument has flipped.**
PerformLine: founder out of the CEO seat (Jan 2026), exit-experienced operator in, two CFOs in a year, employees describing product under-investment. Red Oak: merging with MirrorWeb (announced Jul 28, 2026 — merger partner's CEO takes over; third M&A event in 30 months; 12–24 months of integration ahead). Smarsh: rolling layoffs, offshoring, exec reshuffle, TeleMessage breach fallout, long PE hold with exit signals. Meanwhile Haast raised a $12M Series A led by Peak XV (Apr 2026). "Nobody gets fired for buying the incumbent" is now answerable with documented facts — ask every buyer what happens to roadmap commitments and named support during a vendor's ownership transition.

**4. The AI claims across this market are mostly unmeasured — make measurement the battlefield.**
Blee: "85–95% accuracy," no methodology. AdClear: 88% vs "90%+" in their own materials, a 77.5% case study undercutting the headline, and a "-44% cost" stat with no source. Saifr: "90%" on the site, "93–95%" in interviews. PerformLine: genAI pre-pub scanner three weeks old. Red Oak: no accuracy claim at all for its prompt-layer. Smarsh: AI trained on alert triage, not content. The single most portable play in this run: **propose written POC success criteria — precision/recall on the buyer's own corpus, definitions agreed up front — and commit Haast to it.** Every rival either refuses or exposes themselves.

**5. Geography attacks are coming from both directions — pre-empt with the "regulator-portability" frame.**
Blee attacks Haast as "the Australian tool"; AdClear frames Haast as a "horizontal enterprise platform" vs their FCA specialism; Saifr/PerformLine/Red Oak simply ignore non-US regimes (a gap, not an attack). Standard counter, every deal: Haast ships FINRA/FTC/FCA agents, operates production deployments under three regulatory regimes (ASIC, FCA, and US frameworks), and the attackers' own coverage is single-regime — Blee has zero non-US evidence, AdClear's own PR admits EU/US were "recently expanded," and the US incumbents have no FCA/ASIC reasoning at all. Multi-jurisdiction proof is Haast's least-contested asset in this run; lead with it whenever the buyer has more than one regulator.

---

## 2. Combined feature-gap comparison (all six vs. Haast)

Legend: ✅ real strength · ⚠️ partial/claimed/unproven · ❌ absent (documented) · — not their category

| Capability | Blee | AdClear | Saifr | PerformLine | Red Oak | Smarsh | Haast |
|---|---|---|---|---|---|---|---|
| Pre-publication AI review | ✅ core | ✅ core | ✅ core | ⚠️ genAI scanner shipped Jul 2026 | ⚠️ prompt-assist layer on workflow | ❌ (LinkedIn profile gate only) | ✅ core |
| Post-publication monitoring of live marketing estate | ⚠️ claimed, unsubstantiated anywhere | ⚠️ <1 yr old; web/affiliate/Discord/Telegram scope; no reference | ❌ (their "monitoring" = people screening + comms surveillance) | ✅ core (discovery/affiliate at scale) — lexicon-based | ❌ (rep surveillance ≠ estate re-review) | ❌ (archive snapshots, no re-assessment) | ✅ core |
| Regulator coverage beyond one home regime | ❌ US list incl. "UK/EU/Asia/MENA" — zero evidence | ⚠️ FCA deep; SEC/FINRA a list, no docs; 1 US customer | ❌ US only | ⚠️ US + FCA rulebook customization (1 story) | ❌ US only | — (records regs, not content rules) | ✅ FINRA/FTC/FCA agents, 3-regime production history |
| Customer-controlled rule building | ⚠️ vendor "legal engineers" build rules | ✅ compliance team edits rule logic (claimed) | ❌ Saifr's models, Saifr's tuning | ❌ vendor-curated rulebooks + services | ⚠️ configurable workflow; AI prompts vendor-configured | ❌ lexicons | ✅ self-serve + legal implementation team |
| Published AI accuracy w/ methodology | ❌ (85–95% no method) | ❌ (88/90+/77.5 inconsistent) | ❌ (90 vs 93–95 drift) | ❌ | ❌ (none claimed) | — | POC-measurable; offer written commitment |
| 17a-4 / books-and-records story | ❌ none despite "recordkeeping" pivot | ❌ none despite broker customers | ✅ claimed 17a-4-compliant storage + FINRA filing assist | ⚠️ audit records; no 17a-4 claims found | ✅ native, incl. AI outputs | ✅ the category leader | Verify Haast posture; export-to-archive framing |
| Named referenceable customers | ✅ 5–6 fintech logos (all 2025) | ✅ ~14 UK logos + 1 US | ❌ zero in 4 years | ✅ real bank logos | ❌ zero (anonymized) | ✅ enterprise archiving logos (not marketing-review) | ✅ Telstra, Aviva, Zurich ANZ, Equity Trustees |
| Independent review footprint | ❌ zero | ❌ zero | ❌ zero | ❌ ~zero (legacy-name Capterra shell) | ❌ ~zero (3 Serchen 5-stars) | ✅ Gartner PI 4.6/~140 (pain = contracts) | Build G2 presence — the shelf is empty category-wide |
| Security/trust evidence public | ❌ none (no SOC 2 evidence, no trust page) | ⚠️ ISO/SOC 2/CE+ claimed, no public evidence | ✅ SOC 2 Type 2 | ⚠️ SOC 2 via unreliable aggregator only | ⚠️ unknown | ✅ (but TeleMessage breach 2025) | Table Haast pack day one |
| Vendor stability right now | ⚠️ ~25 ppl, sole founder, quiet $2.8M | ⚠️ 8 ppl, all London, $3.4M | ✅ Fidelity-funded (but zero named proof) | ⚠️ founder out, PE exit-grooming | ⚠️ mid-merger, CEO handover | ⚠️ layoffs, breach, long PE hold | ✅ $12M Series A Peak XV Apr 2026 |
| Channels no one else covers | Figma-native embed story | Discord/Telegram monitoring; Slack/Figma-native | Multimodal review (video/audio real) | **Calls + messages** (Haast doesn't match) | FINRA AREF filing (fortress) | 100+ capture channels, genAI-usage capture | Long-form video AI review + full lifecycle |

**How to read this in a deal:** whatever the competitor, two rows are almost always Haast-favorable and demo-provable — *post-publication live-estate re-review* and *multi-regime regulator agents*. Open evaluations there.

## 3. Pricing-signal comparison (one page)

| Vendor | Public pricing | Model (best evidence) | Est. ACV band (confidence) | Procurement friction to exploit | Their price FUD vs you |
|---|---|---|---|---|---|
| **Blee** | None ("customized quote") | Sales-led annual; "long-term contracts" w/ "pledged or paid" hedge | $30–75K blended (weak — arithmetic on unverified ~$1.5M ARR) | No SOC 2/trust evidence → security review stalls; sole-founder continuity terms | "Enterprise-grade without enterprise-exclusive pricing" (no number behind it) |
| **AdClear** | None ("volume and workflow configuration"; payback <5 mo claim) | Volume-based annual; 6-week pilots | £20–60K blended; enterprise £75–150K+ (low-med) | 8-person London vendor supporting US = SLA/timezone/continuity clauses; certs claimed w/o public evidence | Will undercut on sticker in land-grab mode — don't chase; model volume growth at yr-3 |
| **Saifr** | None; "$500/mo start" is competitor-sourced, unreliable | Enterprise annual, seats + usage hybrid; Fidelity-shaped paper | $50–250K+, lighthouse higher (low-med) | Slow FMR-entity contracting; inter-affiliate data-sharing terms legal will want to negotiate; no marketplace paper | Rarely price-FUD; pedigree-FUD — counter with "what does the premium buy in *your* deployment?" |
| **PerformLine** | None; per-channel modules | Annual, per channel/module + scan volume; services bundled | $40–150K+; big banks $200K+ (med-low) | Module-stacking → force all-in quote; mid-exit-process = demand price protection; no Vendr benchmarks | Monitoring-only sticker may undercut you — force the full-lifecycle all-modules comparison |
| **Red Oak** | None; quote-only, modular add-ons | Annual firm subscription, size-tiered; long small-account tail | Small RIA $5–20K; mid $25–75K; enterprise $100K+ (low) | Mid-merger: contracting entity, assignment clauses, roadmap survival; SOC 2 unverifiable | "Unlimited workflows at no extra cost" sweetener; counter on reviewer-hours TCO, not license lines |
| **Smarsh** | Partial (SMB ~$8–35+/user/mo); Enterprise quote | Per-user + modules; auto-renew 12-mo terms, 60–90-day notice | **Vendr: $75K–300K typical; 30–50% variance for same scope** | The one with *documented* friction: tripled-bill reviews, export-fee "data hostage" history, own Data Freedom Guarantee as admission | Not competing for your line item — the fight is budget framing ("Smarsh already covers it"), not price |

**Cross-cutting price posture for Haast:** never discount into a startup land-grab or an incumbent's monitoring-only sticker. The two portable value frames: (1) **lifecycle-per-dollar** — every rival's price buys a slice (pre-pub OR monitoring OR workflow OR records); the buyer budgets the rest separately; (2) **reviewer-hours TCO** — the AWS case study numbers (500+ hours saved, 4x capacity) move a metric no workflow tool or lexicon monitor can move. Offer multi-year price protection proactively against the three PE-owned incumbents mid-transition — they'll struggle to match it.

## 4. Top 3 universal landmine questions (work against ALL six — your new default discovery set)

1. **"Once content is approved and live — on your site, your partners' sites, your social channels — what continuously re-checks that it still complies when a rate, product, or regulation changes, and how would you know the same day?"**
   *Why it works on everyone:* Blee's monitoring claim is unsubstantiated; AdClear's is <1 year old with no reference and narrow scope; Saifr has none for content; PerformLine's is lexicon detection with structural noise; Red Oak's is rep-surveillance, not estate re-review; Smarsh archives snapshots without re-assessing them. Only Haast answers it cleanly with a live demo.

2. **"What review accuracy will each vendor commit to in writing, measured on OUR content with definitions we set during the pilot — and can your own team see, edit, and version the rules or logic the AI applies?"**
   *Why it works on everyone:* every vendor in this run either publishes no accuracy figure, publishes inconsistent ones, or hides the review logic behind vendor-configured rules/prompts/models (Blee's legal engineers, Saifr's tuning loop, PerformLine's curated rulebooks, Red Oak's implementation-team prompts, Smarsh's lexicons). It converts the eval from claims to measurement — Haast's home field.

3. **"How many named, referenceable customers matching our profile — our regulators, our size, 12+ months live — will each vendor put on the phone, and can we find a single independent review of them anywhere?"**
   *Why it works on everyone:* Saifr and Red Oak have zero named customers; Blee's logos are all <15 months old with no 2026 announcements; AdClear has one US customer; PerformLine and Smarsh have logos but zero (or contract-complaint-flavored) independent review presence — and none of the six can produce a *marketing-compliance* reference under multiple regulators. It makes proof the criterion, which is the terrain Haast holds.

---

## Deliverables index (this run)

| File | Competitor | One-line angle |
|---|---|---|
| `battlecard-blee.md` | Blee (YC S22, NYC) | US-fintech pre-pub startup; geography FUD vs Haast; no docs/monitoring substance/records story |
| `battlecard-adclear.md` | AdClear (London, 2024) | FCA-native mirror image; US depth is a homepage list; 8 people, all London |
| `battlecard-saifr.md` | Saifr (Fidelity Labs) | Pedigree play; no live-content monitoring; US-only; zero named customers; Fidelity conflict question |
| `battlecard-performline.md` | PerformLine (NJ, 2007) | Monitoring incumbent mid-exit-grooming; genAI retrofit dated Jul 2026; respect calls/partner-discovery moats |
| `battlecard-redoak.md` | Red Oak (Austin, 2010) | Workflow/filing fortress mid-MirrorWeb-merger; coexist-then-displace; AI = vendor-configured prompts |
| `battlecard-smarsh.md` | Smarsh (Portland, 2001) | Not a competitor — the "we already have Smarsh" objection; system-of-record vs system-of-review |
| `summary.md` | — | This file |

**Standing watch-items for the next quarterly run:** (1) Red Oak/MirrorWeb merger close + post-merger roadmap; (2) whether AdClear or Blee land US enterprise logos or US hires; (3) PerformLine Pre-Publication Scanner maturity + any sale process; (4) Smarsh Cognition-team postings mentioning "content review/marketing" (category-entry tripwire); (5) Saifr's Superhuman agent GA + any FCA/international move; (6) first independent reviews appearing anywhere for the AI cohort — the G2 shelf is empty and whoever fills it first (ideally Haast) owns it.
# SUPPLEMENTAL INTEL — 2026-08-04 Run Extension

**Covers seven added angles:** (1) Wayback/strategy drift · (2) Security & trust posture · (3) AI credibility audit · (4) Conference & community footprint · (5) Financial health signals · (6) Displacement target list · (7) Patents & legal footprint.
Sections 2, 3, 5, 6 consolidate evidence already gathered in the six battlecards (sources live there — this file cross-references rather than re-cites). Sections 1, 4, 7 are net-new research appended below.
**Provenance reminder:** same run constraints as the battlecards — cached/indexed sources, verify verbatim quotes live before external use.

---

## 2. Security & trust posture (cross-competitor table)

The single fastest kill-criterion for financial-services buyers. InfoSec detonates these for you — your job is just to make "vendor diligence pack on day one" a scored criterion.

| Vendor | SOC 2 | ISO 27001 | Public trust center | Public docs | Data residency / sub-processors | Customer data → model training | Net posture |
|---|---|---|---|---|---|---|---|
| **Blee** | ❌ No claim found anywhere; third-party profile explicitly notes "no public security documentation despite serving regulated industries." Hiring first Security Engineer NOW ($170–200K) | ❌ | ❌ (none) | ❌ none — docs/help subdomains don't even resolve (NXDOMAIN) | Unknown | Claims "custom LLM per client" trained on client feedback — probe data-handling terms | **Weakest in the run.** InfoSec landmine: ask for the pack; there is none public |
| **AdClear** | ⚠️ SOC 2 Type II claimed on homepage | ⚠️ ISO 27001 + Cyber Essentials Plus claimed | ❌ "dedicated trust centre" claimed but trust./security. subdomains don't resolve; no auditor/scope/cert number public | ✅ Real docs site (docs.adclear.ai) | DPA on request + "full sub-processor disclosure" claimed — not publicly posted | "AI adapts to reviewer feedback" — probe training scope | Paper-strong, evidence-thin. Ask for report scope + date; young-company certs are often narrowly scoped |
| **Saifr** | ✅ SOC 2 Type 2 (SaifrReview + SaifrScreen, annual audit) | ❌ not claimed | ❌ no public portal | ❌ gated (developer docs customer-only) | **The unique issue:** privacy policy allows sharing "with other Fidelity Labs, LLC companies" — inter-affiliate data flow inside FMR | Models trained on Fidelity's historical corpus; client feedback loops documented for SaifrScreen | Solid certs; the diligence question is *governance vs a competitor-parent*, not controls |
| **PerformLine** | ⚠️ Claimed only by an unreliable aggregator (same one misattributed a rival's AI engine to them); no first-party claim found | ❌ | ❌ none found | ❌ none (help subdomain NXDOMAIN) | Unknown; Asia/Oceania staffing noted | Bedrock-based prompting (AWS blog) — ask data-retention terms with model provider | Surprising gap for a vendor claiming 6 of top-10 banks — soft probe, could be real-but-unpublished |
| **Red Oak** | ❓ Unknown — no public evidence either way | ❌ | ❌ | ❌ (no public KB; app versioning visible on login page) | Unknown; AI stack disclosed as GPT-3.5/4 on Microsoft Azure (directory listing — verify) | AI Review results stored 17a-4-compliant (their claim); "no model training" positioning | Ask directly; mid-merger security re-papering is also a fair question |
| **Smarsh** | ✅ (enterprise-grade posture assumed/marketed; Gartner-Leader tier) | ✅ (marketed) | ✅ | ⚠️ partial | Mature program | Capture-side genAI integrations (ChatGPT/Copilot/Claude compliance APIs) | Strong on paper — **but the May 2025 TeleMessage breach (acquired-app, plaintext exposure, services suspended, Wyden DOJ letter) is the counter-fact for any "acquisitions are safe" narrative** |

**Play:** table Haast's security pack in meeting one, every deal. Against Blee/PerformLine/Red Oak, "ask every vendor for SOC 2 + trust center + sub-processor list on day one" does damage without you saying a negative word. Against Saifr, it's the affiliate-sharing clause. Against Smarsh, it's acquisition-integration security history — used as diligence, never as a taunt.

## 3. AI credibility audit (cross-competitor table)

"AI-powered" claims vs what's actually under the hood, per job postings, engineering artifacts, and their own materials.

| Vendor | What the "AI" actually is (best evidence) | ML hiring signal | Accuracy claims & methodology | Human-in-the-loop design | Credibility verdict |
|---|---|---|---|---|---|
| **Blee** | "15 specialised AI agents per review," "custom LLM per client" — self-published only; "custom LLM" almost certainly fine-tuning/RAG, not custom models | AI Engineer role (SF) exists; tiny eng org (founding-team titles in yr-4 postings) | "85–95% accuracy" — no methodology, benchmark, or third-party validation anywhere | Human review after AI pre-read | **Marketing-forward.** Agent-count is a criterion they invented because only they publish one |
| **AdClear** | GenAI trained on FCA obligations + client rules; "applies your rules without inventing them; compliance edits rule logic" — credible design story; "regulatory changes in 24h" has no described pipeline | Senior AI Engineer + Founding Engineer (AI/LLM integrations) — real but tiny; no ML-research roles | 88% vs "90%+" internally inconsistent; Flagstone case at 77.5% undercuts headline; no accuracy figure committed | "Compliance-in-the-loop" explicit | **Plausible core, overstretched edges** (24h claim, 100+ bodies on 8 people) |
| **Saifr** | Proprietary NLP trained on 15–20 yrs Fidelity corpus + LLM layers; real data-science org (Fidelity Labs); eComms trained on "open-source and synthetic data" | Applied-AI research roles (Westlake TX) — genuine research hiring, the only one in the run | "90%" site vs "93–95%" CEO — drift, no methodology public | SME validation loop documented | **Most technically credible AI org in the run — but the model is theirs to tune, not yours** |
| **PerformLine** | Rules/lexicon core (+3,500 terms was the 2025 improvement) + real Bedrock prompt-engineering (AWS blog) + genAI products shipped May–Jul 2026 | **Zero AI/ML postings found** despite "AI expansion" narrative — retrofit via foundation-model APIs + offshore eng [inference] | None published for the new AI products | Human reviewers central; AI reduces back-and-forth | **GenAI-retrofit, dated July 2026.** Never say "no AI" — say "measure it" |
| **Red Oak** | GPT-3.5/4 on Azure (directory-disclosed), prompts configured by Red Oak's implementation team; deliberately conservative ("precision not prediction," "no model training") | Eng ad wants Copilot-style AI *tool use*, not model building; no ML roles ever observed | None — no accuracy claim exists at all | Strong HITL framing (their selling point) | **A prompt layer with a trademark ("Compliance-Grade AI™").** Two questions kill it: can you see/version the logic? what's the catch-rate? |
| **Smarsh** | Real ML lineage (Digital Reasoning) pointed at surveillance: alert triage, noise reduction (-60%), e-discovery; genAI-usage capture | Real ML hiring — all Bangalore, all surveillance-framed; zero marketing-review roles | Surveillance-side claims (77% review-workload cut w/ AWS) — different problem domain | Analyst-in-the-loop on alerts | **Credible AI, wrong target.** Trained to ask "should a human look at this message?", not "may this ad ship?" |

**Play:** the portable move is identical everywhere — written POC commitment to precision/recall on the buyer's corpus with agreed definitions. Nobody else in this run can sign it comfortably. Secondary tell to teach champions: "AI-powered" + no ML hires + no methodology = prompts on someone else's model.

## 5. Financial health signals (cross-competitor table)

"Will this vendor exist, unchanged, in three years?" — weaponize gently, as procurement diligence.

| Vendor | Funding recency | Headcount trend | Exec stability | Layoffs/strain | 3-year continuity read |
|---|---|---|---|---|---|
| **Blee** | ~$2.8M total (never announced; Cardumen corroborated); nothing since | 15 → ~27 over 18 mo | Sole founder; CRO exists; first AE/PMM/SE being hired now | None visible | Alive but thin; sole-founder + quiet funding = ask for continuity terms |
| **AdClear** | £2.1M seed Nov 2025 (oversubscribed) — freshest startup money in the run | 3 → 8 (Nov 2025) | 3 co-founders intact | None | Momentum real; capacity math (8 ppl vs EU+US+APAC+insurance roadmap) is the risk |
| **Saifr** | No external funding — FMR-funded indefinitely | ~30–60, opaque (Fidelity payroll) | CEO stable since launch; Giant Oak leaders retained; NA sales head unfilled | None visible | Existence risk ≈ zero; *strategy* risk = Fidelity could deprioritize; zero named customers after 4 yrs is the tell to probe |
| **PerformLine** | M33 top-up Jan 2026 (undisclosed); lightly capitalized life | ~39 → ~69–89, slow, offshoring | Founder→board; operator CEO w/ exit record; 2 CFOs in ~1 yr | Employee-reported bonus non-payouts, constant turnover | **Exit-grooming pattern.** Continuity clauses + price protection = fair asks |
| **Red Oak** | Mainsail $51M (2023) + merger financing | ~50–70 → ~116; merger ~doubles | C-suite fully replaced 2024–26; **CEO seat passing to merger partner (MirrorWeb's Bosu)** | Top-level churn, rank-and-file stable | **Mid-merger.** Which entity signs? Whose roadmap survives? Time-boxed opportunity |
| **Smarsh** | PE (K1) ~10-yr hold; continuation-vehicle economics; IPO-experienced CFO hired Jan 2026 | ~1,784 → ~1,709 (shrinking) | CPO/CFO/CSO churn inside 12 months | Rolling layoffs, offshoring, breach fallout | Exists in 3 years, yes — under whose ownership and with what support model is the honest question |

**Play:** Haast's counter-position in every one of these conversations: $12M Series A led by Peak XV with DST Global Partners (Apr 2026), founder-led, single product, growth phase. Offer the continuity/escrow/multi-year terms proactively — incumbents mid-transition struggle to match them.

## 6. Displacement target list (named accounts that provably buy this category)

Every public logo below is a company that has budget, a compliance-review pain, and a current vendor with documented weaknesses. Attack angle attached. (Anonymized case-study accounts excluded — can't target what isn't named.)

**From Blee (all announced May–Dec 2025; no 2026 announcements — probe satisfaction):**
| Account | Sub-vertical | Angle |
|---|---|---|
| Rocket Mortgage | Mortgage (enterprise) | Pre-pub-only vendor; no monitoring substance, no 17a-4 story; ~25-person vendor supporting an enterprise |
| Marqeta | Card issuing / embedded finance | Partner-ecosystem content risk = live-estate + affiliate monitoring gap |
| Public.com | Broker-dealer | FINRA books-and-records angle — their vendor has no 17a-4 substance |
| Betterment | RIA / robo-advisor | Same records angle + SEC Marketing Rule depth |
| NerdWallet | Fintech media / affiliate | Affiliate content at scale — monitoring gap is the wedge |

**From AdClear (UK-heavy; US-expansion accounts are the prize):**
| Account | Sub-vertical | Angle |
|---|---|---|
| NinjaTrader | US futures broker | Their vendor's ONLY US logo; FINRA/CFTC depth demo beats an FCA-first rule layer |
| IG Group | CFD/trading (UK&I rollout only) | Group-wide/multi-entity coverage beyond UK&I is unclaimed territory |
| Marshmallow, PensionBee, Plum, InvestEngine, Flagstone, Ocean Finance, ActivTrades, Trade Nation, Freetrade, Yonder | UK fintech/insurtech | Longer play — revisit when Haast pushes UK growth; 8-person vendor capacity math is the seed of doubt |

**From PerformLine (consumer-finance enterprise; coexistence entry — "keep them for calls/partners, add Haast for content lifecycle"):**
| Account | Sub-vertical | Angle |
|---|---|---|
| Cross River Bank, Central Payments | BaaS / sponsor banks | Content-lifecycle layer on top of their partner-monitoring; pre-pub AI gap |
| Cadence Bank, Republic Bank | Regional banks | Kraken-award customers = deep users; sell the review-effort metric their vendor can't move |
| Bread Financial, PREMIER Bankcard | Cards | UDAAP-heavy; false-positive/noise burden discovery |
| Upstart | Fintech lending | AI-forward buyer — genAI-native vs retrofit story lands hardest here |
| TD Bank, Rocket Mortgage, Benchmark Mortgage | Bank / mortgage | Summit speakers (inferred customers) — validate first |

**From Red Oak / Smarsh (indirect — no named Red Oak customers exist; Smarsh logos are archiving accounts):**
- Red Oak: no named accounts to target; instead, time outbound to the **MirrorWeb merger integration window** across their stated base (19 of top-20 US asset managers) — ABM into asset-manager compliance teams with the "hedge the integration" message.
- Smarsh: Jefferies + ValMark are archiving relationships, not marketing-review losses — use Smarsh presence as a *qualifier* (budget + compliance maturity exists; review gap is naked), not a displacement.

**Complaint-theme hooks to attach to outbound:** Blee/AdClear accounts — "how's the monitoring/records story working out?"; PerformLine accounts — alert-noise and all-in module pricing; any Smarsh shop — the pre-approval-evidence gap their own vendor says isn't necessary.

---

## 4. Conference & community footprint — H2 2026 (October-planning input)

### The calendar that matters (Aug–Dec 2026)

| Event | Date | City | Competitors present | Buyer density |
|---|---|---|---|---|
| FinovateFall | Sep 9–11 | NYC | Blee likely (Finovate demo alum; 2026 list unpublished) | Medium |
| Future Proof Festival | Sep 14–17 | Huntington Beach | None of the six confirmed (COMPLY/ComplySci attends) | High (wealth/RIA) |
| SIFMA C&L Northeast Regional | Sep 16 | NYC | Smarsh (2025 sponsor; 2026 unpublished) | High (BD/AM compliance) |
| **ITC Vegas (InsureTech Connect)** | Sep 29–Oct 1 | Las Vegas | **NONE of the six found — white space** | High (9,000+ insurance) |
| **SIFMA Social Media & Digital Marketing Seminar** | **Oct 1** | NYC | Red Oak (2026 confirmed); Smarsh historically | **VERY HIGH — the exact marketing+compliance crossover room** |
| **FINRA Advertising Regulation Conference** | **Oct 15–16** | Washington DC | Red Oak confirmed; Saifr probable (sponsor history) | **HIGHEST buyer purity of the half** |
| Money20/20 USA | Oct 18–21 | Las Vegas | PerformLine (multi-year home turf) | Medium-high |
| **NSCP National Conference** | **Oct 25–28** | Orlando | Red Oak confirmed; Smarsh (Booth 10 in 2025); Saifr likely | **VERY HIGH — densest CCO room** |
| Schwab IMPACT | Oct 27–29 | Boston | None confirmed — but conflicts with NSCP | High (RIA) |
| ComplyConnect (COMPLY/ComplySci — not PerformLine's brand) | Nov 8–11 | Nashville | Smarsh among sponsors | High (RIA/wealth CCOs) |
| A-Team RegTech Summit NY | Nov 19 (verify) | NYC | Saifr recurring sponsor pattern | High (regtech buyers) |

Already passed (don't plan around): Red Oak Accelerate (Apr, Austin), Smarsh Connect (Apr), PerformLine Client Summit (~Jun), LegalTechTalk London (Jun — Blee was official partner), FINRA Annual (May — **Haast exhibited**, relationship exists).

### Recommended October sequencing
**Oct 1 SIFMA Social/Digital (NYC — cheap, one day, perfect persona) → Oct 15–16 FINRA Ad Reg (DC — book NOW, limited exhibitor slots via FINRA's Jeffrey Arcuri) → Oct 18–21 Money20/20 walk-the-floor only (PerformLine's turf; booth cost high, buyer purity low) → Oct 25–28 NSCP Orlando (booth; get in the NSCP vendor directory like Saifr/Red Oak).** Add ITC Vegas (Sep 29–Oct 1) if insurance is a live 2026 segment — note it butts against SIFMA Oct 1, so it's an either/or without two teams. Nov 19 RegTech Summit NY is the natural coda — a speaking slot there directly contests Saifr's AI narrative in their room.

### Likely booth pitches you'll walk past
- **Saifr:** "AI from Fidelity Labs — compliant content 10x faster" (pedigree + agents narrative)
- **PerformLine:** "omni-channel marketing compliance at scale" + State of Marketing Compliance Report data (Money20/20)
- **Red Oak:** end-to-end review workflow + books-and-records, FINRA-native reliability (now with MirrorWeb "full lifecycle" language)
- **Smarsh:** comms capture/archive/supervision + "AI outputs as records" governance framing
- **Blee/AdClear:** unlikely to have US booths; Blee plays legal-ops rooms (CLOC), AdClear plays the UK circuit

### Community assets you're up against (and three open lanes)
PerformLine owns the deepest moat (COMPLY community, Kraken Awards, annual State of Marketing Compliance Report — they own the phrase "marketing compliance" in US search). Smarsh rents SIFMA's audience via co-branded forums. Saifr runs an analyst/report cadence. Red Oak runs customer-conference loyalty. Blee = YC/CLOC credibility-by-association. AdClear = UK founder circuit (note: their "Between the Guidelines" podcast could NOT be verified this run — an earlier finding, now flagged unconfirmed).
**Three community lanes nobody owns:** (a) insurance marketing compliance, (b) AI-generated-content governance for marketing (Haast's own Series A framing), (c) cross-regime FCA+FINRA+FTC comparative content. All three are open and compound with the event white space above.

### New threat surfaced during this research
**Hadrius raised $27M (CRV) and explicitly plans "AI-first review & approval of marketing materials" by end of 2026** — a direct future collision in RIA/wealth-land; expect them at RIA compliance events. Add to the quarterly watch-list alongside the six.

---

## 1. Strategy drift — current positioning vs 12–24 months ago

**Method honesty:** Wayback Machine and all archive services were hard-blocked by this environment's proxy. Drift below was reconstructed via **search-index archaeology** (old page titles/taglines surviving in directories and stale index entries) and **press-release boilerplate diffing** (2024 vs 2025–26 releases) — provenance solid, exact change-dates approximate. No pixel-level diffs were possible; historical pricing/tier names were unrecoverable for all six (nobody publishes pricing in either era — itself exploitable with transparent Haast packaging).

| Vendor | What changed (old → new) | What it reveals | Sales use |
|---|---|---|---|
| **Blee** | "Smart, Fast, and Collaborative Marketing Compliance Reviews" → "AI-First Marketing Compliance Platform" — with a **still-live Webflow staging site titled "AI-powered Communications Review and Recordkeeping"** (a third, aborted positioning). New claims that didn't exist in 2024 copy: 85–95% accuracy band, "always-on monitoring," 60% faster reviews. Comparison pages now self-describe as "built specifically for **US** regulations" | **Three positionings in ~24 months on one ~$500K–2.8M pre-seed** — including a seriously-considered, abandoned pivot into recordkeeping. The US-only framing is a concession of non-US markets | "Which of their three descriptions is on your contract?" Show the staging URL. In any non-US-exposure deal, quote their own "US-specific" framing back |
| **AdClear** | "Financial Promotions Compliance, in Seconds" → "FinProm Compliance Platform for Finance Brands" (both titles simultaneously indexed mid-migration). **Metric drift: 88% (Nov 2025 funding PR) → "over 90%" (current)** + new metrics (35→90%+, -44% cost, "4–5 hours") that didn't exist at the seed | Point-tool → platform climb; coining "FinProm" fences them into FCA-land; numbers are marketing variables, not measured constants | "They told investors 88% in November and tell you 90%+ today — which cohort, which denominator, why did it change?" Plus "in seconds" vs their own 6-week pilots |
| **Saifr** | Boilerplate rewrite: "a **RegTech** incubated in Fidelity Labs… simplify regulatory compliance" (2024) → "redefines how compliance operates… **AI agents**" (2025–26). **"RegTech" deleted; SaifrReview™/SaifrScan™ product names receding from front-line messaging.** Homepage title now "Compliance & Risk Management" — not marketing compliance | Fidelity repositioning Saifr from destination product to embeddable agent layer sold through partners (ServiceNow, Superhuman) — a strategic admission the standalone app underperformed. Marketing review now one of three diluted legs | "Their own press no longer leads with marketing review. Who at Saifr wakes up owning YOUR ad-review roadmap?" + "Are SaifrReview/SaifrScan still the products of record, or being folded into 'agents' — and what does that migration mean for your implementation?" |
| **PerformLine** | "Omni-channel compliance oversight… discover, monitor, act" → homepage "AI Marketing Compliance Software **for Growth**"; Pre-Publication Scanner shipped Jul 13 2026 — building in year 19 what the AI-natives started with. Capterra fossil: still listed as "**PerformMatch**" with iON™-era branding. (Note: "RuleLogic" could NOT be verified as ever a real PerformLine name — drop that term; their branding is "proprietary Rulebooks") | Monitoring company squeezed by AI-natives; retitled around AI, pivoted persona toward growth/marketing buyers, bolted LLMs on a rules core | "They launched pre-publication AI review in July 2026 — ask how many production customers it has." The unretired PerformMatch listing is a show-don't-tell exhibit of platform housekeeping |
| **Red Oak** | Most drift of any vendor: AdMaster Compliance™ → "Red Oak Software" (renamed flagship; **both old and new domains still live and indexed**); "the global advertising review software of choice" (2024) → "the industry's first Compliance Connectivity Platform" + "Compliance-Grade AI™" (2025–26); "financial services" quietly became "financial services **and insurance**" (TAM stretch); then the Jul 2026 MirrorWeb merger with the acquirer's CEO taking over | They abandoned the category label they OWNED. Ad review is now one module of a PE roll-up facing a four-codebase, two-AI-stack integration | "They spent a decade as 'the ad review software of choice' — why did that phrase disappear, and if ad review is module 1-of-4, who iterates it weekly? Whose AI — Red Oak's prompts or MirrorWeb's Mira — reviews your ads in 18 months?" |
| **Smarsh** | "Transform oversight into foresight" (2024) → "reactive oversight to proactive foresight… cloud-native AI-powered platform" (2026); umbrella brand oscillating (Communications Intelligence 2021 → Enterprise Platform 2022–24 → Communications Intelligence again 2025–26; homepage now SEO'd to Gartner's "DCGA" label). **Bank claim drifted: "19 of the top 20 global financial institutions" (Jul 2024) → "18 of the top 20 banks" (2026)** — logo lost or class redefined, both in dated press | Analyst-led demand gen won internally; messaging never claims marketing *review* in any era — scope-disqualify with confidence | The 19→18 drift is a gentle "check every vendor's claims" softener; umbrella churn feeds a fair procurement question: "which SKU am I buying, and will it be renamed mid-contract?" |

**Cross-vendor pattern (deck-ready):** between mid-2024 and mid-2026 all six made the same three moves — (1) inserted "AI/agents" into their title tags, (2) climbed from tool to "platform," (3) quietly revised quantified claims (88→90%+, 19-of-20→18-of-20, a new 85–95% band). None published pricing in either era. The two structurally distracted vendors right now: **Red Oak** (mid-merger) and **Saifr** (agent-pivot) — cleanest near-term displacement targets. The most direct messaging threat: **Blee**, actively running a "Blee vs Haast" SEO page.

---

## 7. Patents & legal footprint

**Method note:** Google Patents/Justia/CourtListener-RECAP via search index (direct patent-record fetches blocked); absences = "not found in these sources," not certified clearance searches.

| Vendor | Patents | Litigation | Trademarks | Regulatory | Sales use |
|---|---|---|---|---|---|
| **Smarsh** | **Only real portfolio in the set — almost entirely acquired**: Digital Reasoning NLP/surveillance family (incl. US12106078B2, granted 2024 — ML-model lifecycle over comms, the roadmap signal), Actiance archiving family, MobileGuard mobile-capture, TeleMessage legacy. Assignment records suggest the portfolio is pledged as loan collateral. **No marketing-review patents; no recent organic filings found** | *North v. Smarsh* (archive-integrity claims — dismissed); **Cohan v. Smarsh (Del. Ch.): MobileGuard founder's $10M fraud/earn-out suit alleging post-acquisition IP misappropriation — outcome not found**; NO TeleMessage class action found (say so honestly) | None found | **TeleMessage: CISA Known-Exploited-Vulnerabilities listing (May 2025) + Wyden DOJ referral (False Claims Act theory) — no public outcome as of Aug 2026** | Never claim "no IP" vs Smarsh — false. Do note the moat aims at surveillance, not your category. Cohan suit = counter-story when they lead with acquisitions. TeleMessage = the sharpest security-diligence fact in the set |
| **Saifr/FMR** | **US20210312256A1 — "Systems and Methods for Electronic Marketing Communications Review" (FMR, pub. 2021, CNN-based)** — the ONLY direct patent read on Haast's category in the whole set; found as an *application*, grant status unverified → **check USPTO Patent Center before treating as threat OR using "no granted IP" as a line**. Plus Giant Oak's GOST patent (10,885,124) via acquisition — screening, not marketing review | Zero Saifr-party dockets found | SAIFR (2021) + 2024 filing + "WORK SMARTER. STAY SAIFR." (Apr 2026) — active brand investment, no disputes | None found | If the application never granted: "four years, no granted IP on the core product." Verify first |
| **PerformLine** | **None found (high confidence)** — 18+ years, zero filings; moat = trade secrets/rulebooks, not technology | One minor bankruptcy-adversary docket (Corinthian Colleges trustee clawback, 2017 — echo of for-profit-ed heritage); nothing else | COMPLY (2023), PERFORMLINE (2024) registered; "Kraken" = informal codename since 2011, unregistered, no crypto-exchange conflict found | None found | "No patents after 18 years" is fair game — services moat, not tech moat |
| **Red Oak** | **None found (high confidence US)** — AI Review module has no patent protection | Zero federal dockets found | ADMASTER COMPLIANCE registered (2011-era); **"Compliance-Grade AI™" appears UNREGISTERED** — a ™ on a marketing label, no USPTO filing found (quick TESS check before quoting) | None found | "The trademarked AI has no patent and — as far as USPTO shows — no trademark registration either." Use lightly |
| **Blee** | Zero (high confidence) | None found | **No Blee Inc. filings found; "BLEE" is registered to an unrelated LLC** — namespace fragility, not a dispute | None found | No patents, no registered mark in their own name — vendor-viability texture, not a legal attack |
| **AdClear** | Zero (high confidence) | None found | Namespace crowded (AdClear GmbH Berlin ad-tech; SEVEN Networks ad-blocker apps); no UKIPO/EUIPO registration verifiable, no dispute found | None found | Same as Blee — zero registered IP found, EU brand-collision risk |

**Cross-portfolio takeaways:** (1) the only patent that reads on Haast's category is a possibly-ungranted FMR application — verify, then use either way; (2) four of six competitors have zero patents — the category's moats are data, rules-content, and workflow lock-in, not IP; (3) Smarsh's TeleMessage record (CISA KEV + unresolved DOJ referral, but no class action) is the strongest security-diligence fact in the set — deploy as diligence, never as drama.

---

## Run-extension index

| Section | Status | Net-new or consolidated |
|---|---|---|
| 1. Strategy drift (Wayback-style) | ✅ Complete — via search archaeology + press diffing (archives proxy-blocked) | Net-new |
| 2. Security & trust posture | ✅ Complete | Consolidated from battlecards |
| 3. AI credibility audit | ✅ Complete | Consolidated from battlecards |
| 4. Conference & community footprint (H2 2026) | ✅ Complete — incl. October sequencing recommendation | Net-new |
| 5. Financial health signals | ✅ Complete | Consolidated from battlecards |
| 6. Displacement target list | ✅ Complete — named accounts + angles | Consolidated + compiled |
| 7. Patents & legal footprint | ✅ Complete | Net-new |

**New watch-items from this extension (add to quarterly re-run):** Hadrius ($27M, AI marketing review planned by end-2026 — future collision in RIA-land) · FMR application US20210312256A1 grant status · Wyden/DOJ TeleMessage outcome · Blee's staging-site reposition shipping or dying · FINRA Ad Reg + NSCP 2026 exhibitor lists when published (booth-booking deadlines first).
