# Progress Log

Living status. Update as work lands. Newest first.

---

## 2026-09-09 — Planning stage complete, awaiting review

**Status: 📋 PLANNING — no application code written. Build has not started and
should not start until this plan is reviewed and Gate 1 is scheduled.**

### Done
- Inspected the repo: unmodified `nextjs/saas-starter` clone. Next.js
  15.6.0-canary.59, React 19.1, Drizzle → Postgres, Stripe, JWT auth. No tests,
  no CI, no `.env`, no `node_modules`. Retain/modify/remove decided in
  `docs/architecture.md` §1.
- **Verified data sources against live endpoints** rather than assuming. Findings
  recorded in `docs/data-sources.md`. Four materially changed the design:
  1. **EA waste operations register is directly downloadable and high quality** —
     9,607 rows, 8,778 effective, BNG easting/northing on **100%** of effective
     permits (postcode missing on 7.5%). 105 site types including 171
     `SR2008 No 27: Treatment of Soils and Contaminated Material` permits — the
     contaminated-soil competitor set.
  2. **The Hazardous Waste Interrogator withholds producer identities**
     ("commercially confidential… we have not included individual site names and
     producers' details"). The most on-topic dataset available **cannot generate
     a single named lead.** Context only.
  3. **planning.data.gov.uk is not usable as the primary planning feed** —
     explicitly incomplete, ~6 data providers. PlanIt is the practical MVP
     source, with rate limits and self-declared stale authorities.
  4. **Licensing is a real constraint on the multi-operator ambition.** EA Waste
     Sites and the Waste Data Interrogator are under the **EA Conditional
     Licence**, and WDI states a **one-year permitted use**. Fine for an internal
     NRS tool; a blocker for resale without a negotiated licence.
- **🚩 NRS cannot be identified reliably from public data.** The register lists
  four NRS entities under three spellings (`N R S WASTE CARE LIMITED`,
  `N. R. S. WASTE MANAGEMENT SERVICES LIMITED`, `NRS Environmental Services Ltd`,
  `NRS BROMSGROVE AGGREGATES LIMITED`), and **none of their permits is a
  hazardous site type**, despite NRS publicly describing major hazardous
  treatment capability. Two consequences now designed in: entity resolution is a
  core component, and **NRS capability must be human-entered and confirmed**.
- Wrote the documentation set: `CLAUDE.md`, `docs/product-requirements.md`,
  `docs/architecture.md`, `docs/data-sources.md`, `docs/opportunity-model.md`,
  `docs/scoring-model.md`, `docs/ux-design.md`, `docs/risks.md`,
  `docs/roadmap.md`, this file.

### Open decisions needing a human
1. **NRS discovery session** — the four blocking unknowns in `docs/risks.md` §3.
   Phase 0 cannot be honestly scored without them.
2. **Gate 1 pass condition** must be agreed with NRS *before* the test runs.
3. **Legal review of the EA Conditional Licence** if the multi-operator product
   is a real ambition rather than a distant one.
4. **PlanIt terms of use** — confirm in writing before commercial reliance.
5. Priority LPA list for the document/condition-discharge spike.

### Not done, deliberately
No schema, no migrations, no ingestion code, no UI. Phase 0 in
`docs/roadmap.md` starts after review.

---

## 2026-09-09 (later) — Venture opportunity research complete, awaiting review

**Status: 📋 RESEARCH — no application code. Recommendation requires approval
before any build.**

Separate workstream from the NRS intelligence platform: research to identify a
B2B AI/software business buildable with Claude Code, avoiding markets with
entrenched incumbents.

### Done
- 35 candidate opportunities generated across UK sectors; all scored on 10
  dimensions (`docs/opportunity-scorecard.md`).
- Aggressive competitor research on the top 10 — killed 14 candidates on
  evidence, including several that looked attractive
  (`docs/competitive-landscape.md`).
- **Recommendation: waste permit conformance & duty-of-care assurance**
  ("PermitGuard") — `docs/final-recommendation.md`.

### Key evidence
- **Defra Digital Waste Tracking is mandatory for permitted waste receiving
  sites from 1 October 2026**, extending to carriers/brokers/dealers April 2027.
- **120+ Defra-approved DWT providers already exist** → do not build capture.
  Defra's provider page confirms approval covers recording and transmitting
  mandated fields only, with **no permit checking or validation**.
- Off-permit acceptance is a permit breach; CCS bands drive subsistence charges
  from −5% (Band A) to **+200% (Band F)**. Duty-of-care breach under s.34 EPA
  1990 is criminal — unlimited fine, up to 2 years.
- Measured from the register: **8,778 effective permits, 5,304 licence holders,
  4,347 holding a single site** (the ICP). **37.1% are Standard Rules permits
  covered by just 68 published documents** — so 37% national coverage is 68
  extractions, not 3,258.
- 22 targeted searches found **no product** validating movements against
  permitted waste codes. Nearest: EcoComply (permit obligations, not
  transactions).

### Open decisions needing a human
1. **Phase 0 validation** — 5 operator conversations before any code. If
   off-permit acceptance is not a live worry, stop.
2. Approve or reject the recommendation, and whether it runs alongside or
   instead of the NRS platform.
3. EA Conditional Licence review before any resale of register-derived data.

### Not done, deliberately
No code. Phase 0 of the roadmap in `docs/final-recommendation.md` is five
conversations, not a build.

---

## 2026-09-09 (later still) — Permit conformance stress-tested and downgraded

**Status: 📋 RESEARCH. The prior recommendation is superseded.**

Adversarial review of the permit conformance opportunity, with instructions to
disprove it. It did not survive. Full analysis in
`docs/stress-test-permit-conformance.md`; `docs/final-recommendation.md` now
carries a superseded banner.

### What killed it
- **90.8% of waste and landfill sites are in EA compliance Band A or B** — no
  detected non-compliance. Measured from the 2024 Compliance Rating dataset
  (14,139 sites), not estimated. The product prevents a problem nine in ten
  buyers have regulator-issued evidence they do not have.
- **The ICP does not exist as described.** Of 5,287 operators with 1–10 sites,
  **21% are named individuals** (sole traders), and the multi-site end is
  Network Rail, National Grid, United Utilities, councils and water companies —
  enterprise procurement, not SME SaaS. Very little in between.
- **Enforcement targets illegal operators**: 1,205 illegal sites shut down vs.
  122 prosecutions overall, ~7,283 inspections across ~14,139 sites, and the OEP
  found **63% of issues identified at inspection go unresolved**.
- **Price anchor of ~£26/year** for DWT registration against a proposed
  £150–400/month.
- **Self-incrimination is structural, not a messaging problem** — the core
  output is a discoverable record of the operator's own breaches.
- We are **late**: DWT went live April 2026, mandatory 1 October 2026, 120+
  approved providers already chosen.

### What survives
- The permit dataset is still real and buildable (68 SR documents cover 37% of
  permits) — an asset, but not a product sold to operators.
- The EA describes **mirror-entry misclassification** as one of its most common
  findings, which points at WM3 classification rather than permit conformance.

### Revised ranking for a £50k bet
1. Waste Commercial Intelligence · 2. WM3 Assistant · 3. Permit Conformance

### Open decisions needing a human
1. Accept or reject the downgrade.
2. If proceeding with commercial intelligence, run the Ten Leads Test in
   `docs/roadmap.md` — it remains the cheapest decisive test available.

---

## 2026-09-09 (Ten Leads Test) — VALIDATE FURTHER

**Status: 📋 RESEARCH. No application code. Decision: VALIDATE FURTHER.**

Ran the Ten Leads Test against live public data. Full results in
`docs/ten-leads-test.md`, method in `docs/ten-leads-candidates.md`, analysis and
decision in `docs/ten-leads-analysis.md`, next experiment in
`docs/next-validation-experiment.md`. Raw pool: `docs/data/ten-leads-pool.csv`.

### What worked
- **PlanIt API verified working.** ~4,041 records scanned across 10 search
  terms; **442 candidates inside 110 km of Meriden** for May–Sept 2026; run
  time under 10 minutes.
- **Contracts Finder OCDS partially worked** (heavy 429 rate limiting) and
  produced the single best lead: **EKFB JV "Waste Management Services", £1m,
  published 26 Aug 2026**, for HS2 C23 — whose northern end at Long Itchington
  Wood is ~25 km from Meriden.
- **Discovery advantage demonstrated, not asserted:** a general web search could
  **not** locate Derby application 26/00060/FUL (Rolls-Royce Sinfin A
  remediation consent); PlanIt returned it instantly. Alpha Anodizing (heavy
  metals, live remediation condition, 38 km) was invisible to targeted search.
- **Timing thesis confirmed:** 6 of 10 leads are at condition-discharge stage —
  contamination confirmed, strategy exists, works not started.

### What broke
- ⚠️ **Tonnage is not derivable.** **No record in 442 contains site area, depth,
  volume or tonnage.** The PRD's "8,000–15,000 t / £300k–£500k" example is not
  achievable from these sources. PRD annotated accordingly.
- ⚠️ **The buyer is missing 61% of the time** — only 173 of 442 records carry a
  named agent.
- ⚠️ **90.3% of the pool is "Small"** — mostly residential infill. Only 38
  Medium/Large, implying ~110–130 commercially material events per year in the
  catchment.
- ⚠️ **Obscurity and value are negatively correlated.** The leads NRS is least
  likely to know are mostly the smallest. Rolls-Royce Sinfin A is the only lead
  that is both obscure and substantial.
- ⚠️ **Verification/validation reports are a systematic false positive** — the
  waste has already moved. ~45 pool candidates had to be excluded.
- ⚠️ **Barbour ABI would produce ~5 of the 10, and would do the valuable ones
  better** (contacts, contract stage).

### Decision: VALIDATE FURTHER
Not BUILD — the flagship output (tonnage/value) is unproven, the buyer is often
absent, and the awareness hypothesis is untested. Not KILL — the discovery
advantage is real and demonstrated.

### Open decisions needing a human
1. **Run the NRS awareness experiment** in `docs/next-validation-experiment.md`
   — 5 conversations, one week, no code. Agree the decision table *before*
   starting.
2. **Run the tonnage feasibility spike** (1 day, 3 LPAs) in parallel. Derby's
   portal returned HTTP 503 during this test, so document access is genuinely
   uncertain.
3. Confirm NRS's economic haul radius — does Derby work? Mansfield?

---

## 2026-09-09 (validation kit) — Ready to run. Next action: RUN ANOTHER TEST

**Status: 📋 VALIDATION KIT COMPLETE. No application code. Awaiting five
customer interviews.**

Built the full five-customer validation experiment in `docs/validation/`.
Start at `docs/validation/README.md`.

### Materially changed the decision rule before locking it
Reviewed the proposed thresholds and found **five defects**, two critical
(`docs/validation/decision-rule.md`):
1. **No unit of analysis** — 5 packs × 5 cards means each lead is seen by only
   2–3 people; "≥4 unknown" was undefined. Now requires **unanimity** among
   viewers of a lead.
2. **Unknown and actionable were counted independently** — creating a
   false-positive path where 4 useless-but-new leads plus 3 already-being-pursued
   leads would trigger BUILD. Actionability is now measured **only on the
   unknown subset**.
3. **"≥1 WTP signal" was too weak and had no floor.** Now requires 2+
   independent prices and one **≥£500/month**, derived from the £1m ARR maths.
4. Control failure was under-specified — now 1 failure = discard and replace,
   2+ = abort.
5. **n=5 cannot measure a rate** — accepted as structural. The test is a
   screening test; the ambiguous middle now resolves to a *specific* action
   rather than an open-ended "validate further" loop.

Also added the missing branch the brief correctly suspected: **category C
("knew the project, not the waste opportunity")**. If most new leads are C, the
product's value is **interpretation, not discovery**, Barbour becomes a supplier
rather than a competitor, and the route is CHANGE THE PRODUCT — not KILL.

### Locked primary metric
**NNAL (Net New Actionable Leads)** out of 9 non-control leads: unanimously new,
4/4 actionable, not already pursued, within haul radius.
**BUILD at ≥3 plus a ≥£500/month price. KILL at 0, or ≤2 with no pattern.**
Tie-breaker that outranks all stated answers: **did anyone contact a counterparty
within 14 days?**

### Open decisions needing a human
1. **Sign the lock** in `docs/validation/decision-rule.md` before recruiting.
2. Recruit five participants, **at least three involved in winning work**.
3. Run the interviews; wait the full 14 days before computing anything.

---

## 2026-09-09 (manager pack) — Ready for a 30-minute conversation

**Status: 📋 No application code. Manager validation pack prepared.**

Built a cut-down, manager-facing version of the validation experiment:
`docs/validation/manager-pack.md` (5 evidence cards) and
`docs/validation/manager-interview-sheet.md` (one page, questions + capture grid
+ private interpretation notes).

### All records re-verified live before printing
Re-queried the PlanIt API on 9 September 2026. **All eight target applications
still Undecided.** Re-verification also produced new detail not in the original
test:
- **26/00898/DISC** (RR Sinfin A) — received 13 Jul 2026, agent **AECOM**;
  parent permission 26/00060/FUL is *"Remediation works, and realignment and
  installation of ground services to facilitate the future development"*.
- **P/2026/00884** (Alpha Anodizing) — received 14 Aug 2026, decision
  **PENDING**; full scheme is *"demolition of commercial works to facilitate the
  erection of 8 No. dwellinghouses"*.
- **PL/2026/01382/DIS** (JLR Lode Lane) — agent is **WSP** (not previously
  captured); parent approval PL/2025/01396/PPFL dated 9 Apr 2026.
- **PL/2026/01052/DIS** (Mell Square) — agent Turley; **consultation closes
  22 Sep 2026**.
- **DMOT/2026/0939** (Woodville, Large) — **consultation closes 23 Sep 2026**.

### Pack contents
Cards: RR Sinfin A · Alpha Anodizing · Mell Square (control) · JLR Lode Lane ·
HS2/EKFB tender. No tonnages, no revenue figures; the single £1m figure is
quoted directly from the published EKFB notice. FACT and INTERPRETATION are
separated on every card. Live source links on every card so the manager can
verify in the room.

### Open decisions needing a human
1. Run the conversation. Ask awareness **before** revealing interpretation.
2. Wait 14 days before judging — the revealed-preference test.
3. Two consultation deadlines fall on 22–23 Sep 2026 if anything is to be acted
   on quickly.

---

## 2026-09-10 — First manager conversation run (n=1, provisional)

**Status: 🔶 ONE interview complete. Not a decision point — the locked rule
requires multiple participants and the 14-day revealed-preference window.
Recorded here so it isn't lost, not as a verdict.**

### Result (from manager pack, 5 cards)

| Card | Known beforehand? |
|---|---|
| 1. Rolls-Royce Sinfin A | **New** |
| 2. Alpha Anodizing | **New** |
| 3. Mell Square (control) | Known — **control passed**, participant's other answers can be trusted |
| 4. JLR Lode Lane | **New** |
| 5. HS2 / EKFB | Known — expected; flagged in advance as the weakest lead on discovery |

**3 of 4 non-control leads new.** Ahead of the pre-interview prior (guessed
NRS probably already knew 3–5 of the original ten).

### Unprompted finding — independent evidence for the core thesis
NRS **does** subscribe to Barbour ABI or similar, but the participant described
it unprompted as *"not a custom thing, more of a general marketplace."* This is
the exact differentiation claim the whole idea rests on — Barbour captures, it
doesn't interpret — confirmed by an actual user without being led there.

### Still missing before this is decision-grade
- **Actionability (4-part test) on the 3 new leads** — why/who/what/when not yet
  captured for Cards 1, 2, 4.
- **Any willingness-to-pay signal**, even informal — not yet captured.
- **This is n=1.** Locked rule (`docs/validation/decision-rule.md`) requires
  unanimity across multiple viewers per lead and ≥2 independent prices with one
  ≥£500/mo — a single strong conversation cannot satisfy it alone, by design.
  Guard against exactly this moment — the risk of over-weighting one good
  result right after hearing it.

### 🎯 Revealed preference — same day, not day 14
A contact was actually rung, same day as the meeting — before the 14-day
window even properly opened. This is the strongest category of evidence the
whole test was designed to surface (stated intent vs. actual action). **Which
contact — Alpha Anodizing, or AECOM (RR Sinfin A) / WSP (JLR) — to be
confirmed and logged precisely.**

### Second participant — Jason (commercial director), same day
Jason — the commercial director with prior revealed spend on waste
tonnage-by-county data (see earlier entry) — has seen leads and expressed
interest, described it as having value, and said he would pay regularly for a
service like this.

⚠️ **No figure named yet.** Per the locked WTP grading, "would pay" without a
number is **🔴 None**, not a positive signal — the same standard applied
throughout this test, including to the manager's "value" comment earlier
today. Next step: ask Jason directly what the tonnage-by-county data cost him,
and whether this would be worth similarly or more — anchored to a real prior
purchase rather than a hypothetical. Also get: who signs it off, and desired
frequency.

### 14-day follow-up window
**Started 2026-09-10. Review no earlier than ~2026-09-24.** Whether anyone
actually contacts a counterparty on Rolls-Royce/Sinfin A, Alpha Anodizing or
JLR outranks anything said in the room.

### Actionability (captured after follow-up questions)
- On the 3 new leads, the participant did not initially give a specific
  who/what/when — first response was a general statement that "missed
  contracts can bring a lot of value" (engagement with the category, does
  **not** pass the 4-part actionability test as defined).
- On direct follow-up, he committed to **follow up on any lead where NRS can
  find or already has a contact.** That is a real, operationally realistic
  commitment — stronger than the first answer, though still a rule rather than
  a named individual per lead.
- Applying that rule to the cards as printed: **Rolls-Royce Sinfin A** (agent
  AECOM) and **JLR Lode Lane** (agent WSP) both clear it directly. **Alpha
  Anodizing has no named contact in the public record and would fall through
  his own filter as it stands** — despite being the strongest discovery-quality
  lead of the three. Action for Ben: chase a contact for Alpha Anodizing this
  week (ring the occupier directly, or pull the applicant name from the East
  Staffordshire portal) so the best lead doesn't get dropped on a technicality.

### Willingness to pay
Did not come up as a figure. Conversation was framed around value/category,
not price. Per the locked WTP grading in `data-collection.md`, this is
**🔴 None** — a real, discussed conversation, but not evidence of willingness
to pay. Not a bad sign; just not data yet.

### Next
1. Capture the actionability and WTP detail from this conversation while fresh.
2. Second participant — Jason (commercial director, prior revealed spend on
   waste tonnage data) is the strongest remaining candidate per
   `docs/validation/interview-packs.md` recruitment criteria.
