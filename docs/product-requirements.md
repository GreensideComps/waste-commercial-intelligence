# Product Requirements

## 1. The question the product answers

> **"Where should NRS spend its commercial effort this week?"**

Everything else is subordinate to that sentence. A feature that does not help
answer it does not belong in the MVP.

## 2. Users

### Primary — Commercial Director (the buyer and the sceptic)
Wants to know the pipeline is being worked in the right places, and wants to
catch opportunities the team missed. Will judge the product in about ninety
seconds by reading three opportunities and deciding whether we told them anything
they did not know. **Design for this person first.**

### Secondary — Business Development / Sales
Wants a short, ranked, specific list with a name to call and a reason to call
them. Will abandon the product permanently if it produces volume without
precision. Ten good leads beat five hundred mediocre ones.

### Tertiary — Analyst / Estimator
Wants to interrogate an estimate, disagree with it, and correct it. Needs the
evidence trail and the ability to override an assumption.

**Explicit non-user:** the generic SaaS self-serve signup. There is no funnel, no
trial, no pricing page in the MVP. This is an internal tool for one operator
until it has proven itself.

## 3. Jobs to be done

| # | Job | Success looks like |
|---|---|---|
| J1 | Tell me about waste-generating events I don't already know about | "I hadn't seen that" rate above 50% |
| J2 | Tell me what waste it will produce and roughly how much | Tonnage band a competent estimator would accept |
| J3 | Tell me whether we can actually treat it | Cites a specific NRS facility and capability |
| J4 | Tell me whether it's worth the diesel | Distance + indicative contribution, not just revenue |
| J5 | Tell me who to call and why now | Named organisation, role, and a timing rationale |
| J6 | Let me check your working | Every number traceable to a source quote in ≤2 clicks |
| J7 | Let me tell you when you're wrong | Feedback captured and visibly changes future ranking |

## 4. Scope

### In scope for MVP
- External public data only.
- England first (all verified EA datasets are England-scoped).
- A defined catchment around NRS's confirmed facilities.
- Hazardous and specialist waste **prioritised**: contaminated soil, hydrocarbon
  contamination, heavy metals, asbestos-containing material, coal tar / PAH,
  hazardous demolition, remediation, industrial redevelopment.
- Non-hazardous C&D, demolition, construction, infrastructure, excavation and
  site clearance **supported but ranked lower by default** — the ranking weights
  are configuration, so this is a dial NRS can turn, not a hard-coded belief.
- Output: a ranked weekly opportunity brief with evidence and a recommended
  action.

### Explicitly out of scope for MVP
- RoadTrak or any NRS internal data. The architecture must accept it later
  without a rewrite (see `docs/architecture.md` §Internal data readiness), but no
  MVP behaviour may depend on it.
- Billing, subscriptions, self-serve onboarding, multi-operator UI.
- A chat interface.
- Automated outbound contact of any kind.
- Mobile app.
- Rebuilding a projects/companies database. We consume; we do not curate a
  market database.

## 4a. ⚠️ Reality check from the Ten Leads Test (2026-09-09)

The worked example in this document ("8,000–15,000 tonnes … £300k–£500k") was
**not achievable** in the actual test. No record in a 442-candidate pool
contained site area, depth, volume or tonnage. Those figures live only inside
submitted planning documents, which require per-LPA document retrieval that has
not yet been proven to work.

Until that spike succeeds, treat the deliverable as **a ranked, evidenced
alert with a named next action** — not a quantified financial opportunity.
See `docs/ten-leads-analysis.md`.

## 5. The MVP objective and its gate

> **Find 10 genuinely commercially interesting hazardous/specialist waste
> opportunities within NRS's relevant catchment, using external data only, each
> with evidence for why it was identified.**

This is a research deliverable, not a software deliverable. It can be a document.
The gate before any significant application build is a review session where an
experienced NRS commercial person scores each of the ten:

| Score | Question A — "Did you already know?" | Question B — "Would you act on this?" |
|---|---|---|
| 1 | Knew it well, already engaged | No, irrelevant |
| 2 | Knew of it | Probably not |
| 3 | Vaguely aware | Maybe |
| 4 | Did not know | Yes, would follow up |
| 5 | Did not know and surprised it exists | Yes, would prioritise this week |

**Pass condition (proposed, to be agreed with NRS before the test, not after):**
≥5 of 10 score A≥4, **and** ≥5 of 10 score B≥4, **and** at least 2 opportunities
score ≥4 on both. Agreeing the bar in advance is what makes this a real test
rather than a demo.

**If it fails**, the correct response is to change the detection thesis — not to
build a nicer UI over the same weak signals.

## 6. Differentiation thesis (what makes this not-Barbour)

Barbour ABI answers *"what projects and companies exist?"*. Our bet is that the
commercially useful signal is not the existence of a project — an experienced
salesperson already knows the big ones — but three things Barbour does not
surface:

1. **Contamination evidence buried in planning submissions.** The presence of a
   "Phase 2 Geo-Environmental Assessment", "Remediation Strategy", "Asbestos
   Survey" or "Materials Management Plan" in an application's document list is a
   cheap, deterministic, high-precision indicator that hazardous arisings are in
   play. The document *titles* alone are signal; parsing the PDFs is a second
   pass for tonnage detail.

2. **Condition discharge as a timing signal.** Planning approval can precede
   waste arising by one to three years, which is useless to a salesperson. A
   *discharge of a contaminated-land condition* means contamination is confirmed,
   a remediation strategy exists, and works are weeks-to-months away. This is the
   sharpest timing signal available in public data and it is buried in LPA
   portals where nobody looks.

3. **Historic land use overlaid on current applications.** A development on a
   former gasworks, tannery, foundry or historic landfill will generate
   contaminated arisings whether or not anyone has said so yet. Predicting
   contamination before it is declared is the clearest possible answer to "we
   didn't know that".

If these three theses are wrong, the product is a worse Barbour ABI. They should
be tested in Phase 0, cheaply, before anything is built around them.

## 7. Product principles

1. **Ranked and opinionated, never a table.** Every view leads with a
   recommendation.
2. **Show the working.** Confidence is earned by traceability, not by design.
3. **Say "I don't know".** An explicit unknown is more valuable than a confident
   guess, and far cheaper to recover from.
4. **Precision over recall.** Ten right beats five hundred plausible.
5. **The feedback loop is a feature, not instrumentation.** "I already knew this"
   is the product's own report card.

## 8. Non-functional requirements

- **Latency:** none that matters. This is a weekly-cadence product; a pipeline
  run may take hours.
- **Freshness:** planning signals should surface within 7 days of appearing at
  the LPA. Anything slower loses the timing advantage.
- **Auditability:** every AI-derived claim reproducible from stored raw source +
  prompt + model version. Raw source documents are immutable once stored.
- **Cost:** LLM spend must be bounded by a deterministic pre-filter. We do not
  send every planning application to a model.
- **Correctness over uptime.** A wrong tonnage is worse than a late report.
