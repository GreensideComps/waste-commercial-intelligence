# Risks and Unknowns

## 1. Technical risks

| # | Risk | Severity | Mitigation |
|---|---|---|---|
| T1 | **Planning data coverage.** PlanIt is a free third-party service with rate limits (5,000 results / 1,000 KB / 45 s per request) and self-declared `stale` authorities. planning.data.gov.uk is explicitly incomplete (~6 providers). Our primary trigger depends on a single volunteer-supported feed. | **Critical** | Store everything fetched so we build our own history; monitor per-LPA staleness as a first-class metric; keep the ingest adapter interface swappable per-LPA; evaluate a paid provider at Phase 2 |
| T2 | **The best signal lives in documents, not fields.** Condition discharges and document lists are often only on LPA portals, behind Idox/Northgate UIs with terms-of-use and blocking risk. | **High** | Target a small named set of priority LPAs; polite, cached, low-rate access; take a per-authority ToS view; treat document *titles* as the Phase 0 signal so PDFs are not on the critical path |
| T3 | **Entity resolution.** Verified: NRS itself appears under four entities and three spellings in one register. Third parties will be worse. Wrong merges silently corrupt every downstream conclusion. | **High** | Companies House number as canonical key; never auto-merge below threshold; human review queue; store aliases with match method and confidence |
| T4 | **Tonnage credibility.** Every default in the estimation model is an industry-shaped guess. One badly wrong number in front of a commercial director costs more trust than ten good ones earn. | **High** | Bands not points; tier the estimate by evidence quality; mark wide bands `low_precision` and rank them on non-financial terms; calibrate against WDI and NRS history |
| T5 | **LLM hallucination.** Fabricated contaminants or volumes are worse than no output. | **High** | LLM confined to extraction and prose; mandatory verbatim-quote verification against source text, rejecting on failure; no LLM arithmetic; assert prose contains no unknown numbers |
| T6 | **Licensing.** EA Waste Sites and the Waste Data Interrogator are under the **EA Conditional Licence**, and WDI's permitted use is stated as **one year**. PlanIt's terms are unclear. | **High** — blocks the multi-operator vision, not the internal tool | Legal review before any third-party sale; prefer OGL sources (HWDI, Companies House, FTS) in anything productised; open the EA/PlanIt licensing conversation early |
| T7 | **Hazardous Waste Interrogator withholds producer identities** ("commercially confidential"). The most on-topic dataset cannot produce a single named lead. | Medium — scoping, already handled | Use for market sizing and competitor flow only; never plan a feature that needs producer names from it |
| T8 | Postcode missing on 7.5% of effective permits | Low | Key geography on BNG easting/northing (100% populated) |
| T9 | Straight-line distance under-states haulage by 20–30% | Low | Label it; add routing at Phase 2 |
| T10 | Next.js pinned to a **canary** release (`15.6.0-canary.59`) | Low | Move to a stable release before production |

## 2. Commercial and product risks

| # | Risk | Severity | Mitigation |
|---|---|---|---|
| C1 | **"We already knew that."** The core failure mode. If the system mostly surfaces what an experienced person already tracks, there is no product. | **Critical** | Test it in Phase 0 before building; make the metric a one-click button in the UI; if the rate is bad, change the detection thesis rather than the interface |
| C2 | **Timing mismatch.** Planning approval precedes waste arising by 1–3 years. A salesperson cannot act on something two years out, so an approvals feed is commercially useless however complete it is. | **Critical** | Prioritise near-term triggers — condition discharge, demolition notices, tender awards — over approvals; make lead time explicit on every card |
| C3 | **The waste decision may not be the developer's.** Routing is frequently chosen by the principal contractor, demolition subcontractor or remediation specialist, who may be invisible in planning data and unappointed at the time we detect the signal. | **High** | Model role explicitly; where the contractor is unknown, say so and recommend calling *before* appointment — early contact is the advantage, not a gap |
| C4 | **NRS capability may not be what we assume.** Verified: their public permits show no hazardous site types, while their marketing describes major hazardous treatment. | **High** | Capability is human-entered and confirmed; resolve in the discovery session before any capability matching is built |
| C5 | **Adoption.** Sales teams abandon systems that generate noise, and they do it silently. | **High** | Ten opportunities a week, not five hundred; precision over recall; the weekly scorecard makes disuse visible |
| C6 | **This may be a service, not a product.** The value may sit in analyst judgement that does not automate cleanly. | Medium | Phase 0 is deliberately a human-assisted research exercise — it tells us honestly how much judgement is required before we commit to automating it |
| C7 | **Single-customer design.** Building precisely for NRS can produce something no other operator can use. | Medium | Tenant-shaped schema from migration one; every NRS-specific value is a parameter row, not code |
| C8 | **Competitive response.** Barbour ABI or a similar incumbent adds waste interpretation. | Medium | The defensibility is the NRS-specific capability/economics layer and the outcome feedback loop, not the public data — which anyone can obtain |

## 3. What we do not know about NRS (do not hard-code any of it)

Every item below is a `parameter_set` row or an operator-owned table, seeded with
a clearly-labelled placeholder and flagged unconfirmed in the UI until NRS
confirms it. **This list is the agenda for the discovery session.**

### Blocking — the MVP cannot be honestly scored without these
1. **The real facility estate**, and which legal entity holds which permit. Four
   NRS-named entities appear in the EA register under three spellings; we cannot
   tell from outside which are in scope.
2. **Actual hazardous capability and permitted EWC codes** — the public register
   shows none, the marketing implies substantial capability. Which is right?
3. **Economic haul radius**, and whether it varies by waste class or facility.
4. **Minimum interesting opportunity size** — is a 500 t job worth a call, or is
   the floor 5,000 t?

### Important — needed before £ figures can be shown at all
5. Gate fees by waste class and facility.
6. Treatment cost per tonne.
7. Haulage economics: fleet, payload, cost per mile or per load, tipping.
8. Target margin / contribution thresholds.
9. Current spare capacity and any constrained streams.

### Needed to avoid embarrassing the sales team
10. **Existing customers and live opportunities** — surfacing an account NRS
    already owns as a "new opportunity" is the fastest way to lose credibility.
11. What NRS already receives from Barbour ABI or any other subscription, so we
    are not sold as a duplicate of something they already pay for.
12. Current sales process and CRM.
13. Geographic priorities — where they *want* to grow, not just where they are.
14. Which waste streams they most want to fill, and which they would rather
    decline.
15. Whether brokered work (treated elsewhere) counts as an opportunity at all.
