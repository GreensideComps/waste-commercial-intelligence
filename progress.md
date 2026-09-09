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
