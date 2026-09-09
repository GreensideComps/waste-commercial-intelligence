# Roadmap

Phases are separated by **gates**. A gate is a decision point with a stated pass
condition, agreed *before* the work starts. If a gate fails, the response is to
change the thesis — not to proceed with a nicer interface over the same weak
signal.

---

## Phase 0 — The Ten Leads Test (Weeks 1–4) ⭐ THE ONLY PHASE THAT MATTERS YET

**Deliverable: a document, not an application.** Ten evidenced opportunities.

There is no UI, no auth, no deploy. Scripts, Postgres, and a written brief. The
purpose is to find out whether the differentiation thesis in
`docs/product-requirements.md` §6 is true, at the lowest possible cost, before
anything is built on top of it.

### Week 1 — Ground truth and foundations
- **NRS discovery session.** Work `docs/risks.md` §3 top to bottom. The four
  blocking unknowns must be answered. Without them the test cannot be scored
  honestly.
- Strip the starter: remove Stripe, pricing and marketing surfaces.
- Postgres + PostGIS locally; Vitest; CI (typecheck, lint, test).
- Ingest the EA waste operations register (verified: direct ZIP, 9,607 rows,
  BNG coordinates on 100% of effective permits). Build the facility and
  competitor map. Confirm NRS's estate against what NRS actually says.
- Define the catchment from confirmed facilities and a confirmed haul radius.

### Week 2 — Data acquisition
- PlanIt adapter: per-LPA partitioned, paginated, rate-limit aware, storing raw
  responses immutably. Monitor and record per-LPA staleness.
- Companies House adapter (apply for an elevated rate limit on day one — it is
  free but takes time).
- FTS / Contracts Finder OCDS adapter filtered to demolition, site preparation
  and remediation CPV codes.
- Entity resolution v1 with a human review queue.
- **Spike, timeboxed to 2 days:** can we retrieve *document lists* and
  *condition discharge* applications for 3–5 priority LPAs? This is the highest
  value / highest uncertainty question in the whole plan. Answer it early.

### Week 3 — Detection and estimation
- Rule-based detectors for the signal taxonomy in `docs/opportunity-model.md`
  §2.4, starting with `contamination_document_present`,
  `condition_discharge_submitted` and `historic_land_use_overlay`.
- Historic land use overlay (source to be selected in week 2).
- LLM interpretation with schema-constrained output and verbatim-quote
  verification.
- Deterministic tonnage bands, distance, capability match, scoring.
- Claim + evidence graph populated for every number.

### Week 4 — The test
- Generate the top ~30, manually review down to the strongest 10.
- Produce the brief: full evidence, sources, quotes, assumptions, and an explicit
  statement of what we do not know for each.
- **Sit with an experienced NRS commercial person and score them** against the
  rubric in `docs/product-requirements.md` §5.

### 🚦 GATE 1
**Pass:** ≥5 of 10 score "did not know" ≥4, ≥5 score "would act" ≥4, and ≥2 score
≥4 on both — with the bar agreed before the review, not after.

- **Pass** → Phase 1.
- **Partial** (they'd act, but already knew) → the interpretation layer works and
  the detection thesis does not. Change sources and triggers; re-run in two
  weeks. Do not build UI.
- **Fail** → stop and reconsider the premise. This is a legitimate and cheap
  outcome, and finding it in week 4 is the entire point of running Phase 0 first.

---

## Phase 1 — Make it usable (Weeks 5–8)

Only after Gate 1 passes.

- Auth, roles, operator profile (repurposing the starter's `teams`).
- **Screen 1 (This Week)** and **Screen 2 (Opportunity detail with evidence)**.
- Feedback capture — including the "I already knew this" button.
- Scheduled weekly pipeline run.
- Assumption overrides for analysts, recorded as attributed claims.
- Deploy for a handful of real NRS users.

### 🚦 GATE 2
Are NRS users opening it weekly and acting on it, unprompted? Measured, not
asked. If it is not used, more features will not fix it.

---

## Phase 2 — Sharpen (Weeks 9–14)

- Targeted LPA portal ingestion for priority authorities: document lists and
  condition discharges at scale.
- Python document-extraction service — PDF parsing of remediation strategies and
  geo-environmental reports for stated volumes (T1 tonnage evidence).
- Road distance via a routing service.
- Map screen; competitor overlay.
- Barbour ABI evaluation **as an input** — is the contractor/contact data worth
  the licence fee?
- Expanded signal taxonomy; alerting on the sharpest triggers.

## Phase 3 — Calibrate (Weeks 15–20)

- Backtest tonnage predictions against the Waste Data Interrogator.
- Fit correction factors from real outcomes.
- Tune scoring weights against `would_action` and `won` once ~100 scored
  opportunities carry feedback. Keep the model linear and interpretable.
- Competitor flow analysis from WDI/HWDI — the "who is our waste going to?"
  question.

## Phase 4 — Internal data (when RoadTrak is available)

Nothing here changes the architecture; it changes the *source* of rows that
already exist. Real capacity, real gate fees, real haulage costs and historic
volumes replace placeholders, and `economics_are_indicative` starts coming back
false. This is the test of whether the parameter design in
`docs/opportunity-model.md` §3 was done properly.

Unlocks: spare-capacity matching, customer leakage analysis, contribution-first
ranking.

## Phase 5 — Productise (only if Phases 1–3 succeeded)

- Resolve the licensing constraints in `docs/data-sources.md` — this is the
  gating item, not the engineering.
- Multi-operator onboarding; capability and parameter configuration as a
  self-serve flow.
- Reinstate billing.

---

## Sequencing rules

1. **No UI before Gate 1.** The intelligence either works or it does not, and a
   dashboard will not tell you which.
2. **No £ figures presented as fact** until NRS confirms the economics.
3. **No new data source** without a verified entry in `docs/data-sources.md`.
4. **No LLM-generated number, ever.**
5. **Precision over coverage** at every decision point.
