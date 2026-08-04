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

*Sections 1 (strategy drift) and 7 (patents & legal) appended below from dedicated research agents.*
