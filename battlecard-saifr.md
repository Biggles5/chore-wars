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
