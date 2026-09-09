# Ten Leads Test — Collective Analysis and Decision

Leads: `docs/ten-leads-test.md`. Pool and method: `docs/ten-leads-candidates.md`.
Raw evidence: `docs/data/ten-leads-pool.csv` (442 rows).

---

## A. Discovery advantage — how many are genuinely hard to find?

| Band | Leads | Count |
|---|---|---|
| **Genuinely hard (8–10)** | Alpha Anodizing (10), Rolls-Royce Sinfin A (9), Sinfin D (8), Hermitage Mill (8), Egghill (8) | **5** |
| Moderate (5–7) | Occupation Lane (7), JLR (6) | 2 |
| Easy (1–4) | EKFB/HS2 (4), Friar Gate (2), Mell Square (1) | 3 |

**5 of 10 are genuinely difficult to discover manually.**

Two hard demonstrations rather than assertions:

1. **FACT** A general web search **could not locate Derby application 26/00060/FUL** (the Rolls-Royce Sinfin A remediation permission), returning that it "may be a very recent 2026 application that might not yet be widely indexed online". The PlanIt API returned it in under a second.
2. **FACT** Targeted searching on Alpha Anodizing returned only company directory listings and Facebook — **not** the appeal, the demolition consent, or the live remediation condition.

**The discovery advantage is real and demonstrable.** That is the strongest positive result of this test.

## B. Commercial advantage — how many are actionable?

**7 of 10** carry an action a salesperson could take on Monday.

Three are materially weakened:
- **Occupation Lane** and **Egghill** — applicant/agent absent from the public feed, so the action starts with a research step.
- **Egghill** — waste certainty only 4/10; a contaminated land condition can be discharged with no excavation.

⚠️ **Named counterparty was available on only 173 of 442 pool records (39.1%).** For roughly 6 in 10 detections, **the system finds the event but not the buyer.** This is a structural limitation of the source, not a bug.

## C. Timing advantage

| Signal | Lead time to arisings | Leads |
|---|---|---|
| Remediation strategy / site investigation under determination | **Weeks–months** | 2, 3, 5, 6, 9, 10 |
| Live tender for waste services | **Now** | 1 |
| Demolition consent granted, works pending | 1–6 months | 7, 8 |
| Enabling works already begun | ⚠️ **Too late for the main package** | 4 |

**6 of 10 are at the sharp end** — a condition discharge is under determination, meaning contamination is confirmed, a strategy exists, and works have not started. This **confirms the timing thesis** in `docs/product-requirements.md` §6.

**It also confirmed a trap:** *verification/validation* reports mean the work is done. ~45 pool candidates were this false positive. Any naive keyword build would surface them as leads and be wrong.

## D. Information advantage over existing products

What the pipeline adds beyond a project database:

1. **Contamination-specific filtering** — Barbour/Glenigan index projects; they do not systematically rank by *waste consequence*.
2. **Prospective vs retrospective condition classification** — the verification-report trap. Genuinely non-obvious.
3. **Industrial land-use inference** — reading "Alpha Anodizing" as *heavy metals, acids, possible cyanide* is domain interpretation, not data retrieval.
4. **Proximity to NRS's actual permitted sites**, using verified BNG coordinates.
5. **Sub-threshold coverage** — small industrial sites beneath the reporting floor of construction intelligence products.

What it **does not** add:
- ⚠️ **No tonnage.** Not derivable from these sources (`docs/ten-leads-candidates.md` §4).
- ⚠️ **No contractor graph.** Barbour's core asset.
- ⚠️ **No decision-maker contacts.**

## E. NRS awareness hypothesis (HYPOTHESIS — untested)

My best guess, to be tested, not asserted:

| Probably known | Possibly known | Probably not known |
|---|---|---|
| Mell Square (1) · Friar Gate (2) | JLR (4) · EKFB/HS2 (4) · Occupation Lane (5) · Sinfin D (6) | **Alpha Anodizing (9)** · Sinfin A (7) · Hermitage Mill (7) · Egghill (7) |

**Estimate: NRS already knows 3–5 of the 10.** Reasoning: the two lowest scores are large, heavily publicised local schemes any commercial team would track; JLR and Rolls-Royce are obvious *accounts* even if the specific consents are not; the obscure industrial sites generate no press and appear in no trade publication.

**The uncomfortable correlation:** the four leads NRS is least likely to know (Alpha Anodizing, Egghill, Hermitage Mill, Sinfin A) are also, with one exception, the **smallest**. Obscurity and commercial value are negatively correlated, because value attracts publicity. **Sinfin A is the one lead that is both obscure and substantial — and one lead is not a business.**

⚠️ If NRS knows 8 of 10, this idea is finished. If they know 3, it is a business. I cannot resolve this without them, which is the entire justification for the next experiment.

## F. The Barbour test

| Lead | Would Barbour ABI produce it? |
|---|---|
| Mell Square, Friar Gate | ✅ **Certainly** — flagship schemes with named contractors; Barbour would do it *better* than us (contacts, contract stages) |
| EKFB/HS2 | ✅ Likely — major infrastructure programme |
| JLR, Sinfin D | ⚠️ Possibly — as projects, not as waste events |
| Occupation Lane, Hermitage Mill | ⚠️ Perhaps as housing schemes, without the contamination framing |
| **Alpha Anodizing, Egghill, Sinfin A** | ❌ **Unlikely** — sub-threshold, no contract value, no press |

**Barbour would produce roughly 5 of 10, and would produce the valuable ones better than us.**

To differentiate we must add, in order:
1. **Waste interpretation** — what arises, what class, what treatment. Barbour does not attempt this.
2. **Sub-threshold coverage** — small industrial sites Barbour ignores.
3. **Condition-discharge timing** — Barbour tracks project stage, not condition-level triggers.
4. **NRS-specific capability and proximity matching.**

⚠️ **Honest reading: on 5 of 10 leads we are worse than an existing product.** Differentiation rests on the *other* five plus the interpretation layer — which is thinner ground than the original recommendation implied.

## G. Manual effort

| Lead | Manual discovery time |
|---|---|
| Mell Square, Friar Gate | 5 min (trade press) |
| EKFB/HS2 | 15 min (if already monitoring Contracts Finder) |
| JLR, Sinfin D, Sinfin A | 1–2 h each (portal-by-portal search) |
| Occupation Lane, Hermitage Mill, Egghill | 2–3 h each |
| **Alpha Anodizing** | **4 h+, and only if you already knew to look at Yoxall** |

**Total to find all ten manually: ~15–20 hours**, and realistically nobody would, because the search has no natural starting point — you cannot search for a site whose name you do not know.

**Machine time for this run: under 10 minutes** (~4,041 records scanned, 442 filtered). **ESTIMATE: 50–100× speed advantage**, and more importantly a *coverage* advantage — a human would never check 330 LPAs.

⚠️ Offsetting: **I spent ~2 hours of research verifying and enriching ten leads.** The harvest is fast; the qualification is not. A production system must automate qualification too, or the product is a lead-generation tool with a human analyst attached — which is a service business.

## H. Where AI is dramatically better

| Task | Verdict |
|---|---|
| Scanning thousands of applications across every LPA | ✅ Overwhelming — no human does this |
| Classifying prospective vs retrospective conditions | ✅ Strong, and non-obvious |
| Inferring contaminants from industrial land use ("anodising → heavy metals") | ✅ **The highest-value AI step in the pipeline** |
| Distance and geographic filtering | ➖ Deterministic arithmetic, not AI |
| Drafting the brief | ✅ Good |
| **Estimating tonnage** | ❌ **Not possible from this data — and must never be faked** |
| **Identifying the contractor** | ❌ Absent from the source in 61% of cases |
| Judging whether NRS already knows | ❌ Requires NRS |

---

# THE DECISION: **VALIDATE FURTHER**

Not BUILD. Not KILL.

### Why not BUILD

Three findings block it:

1. **The core product promise is not deliverable from the sources tested.** `docs/product-requirements.md` promises "8,000–15,000 tonnes … £300k–£500k". **No record in 442 contains any dimensional data.** Tonnage requires document retrieval and parsing from per-LPA portals — Phase 2 work, and Derby's portal returned HTTP 503 on the one direct fetch attempted. Until that is proven, the flagship output is unproven.
2. **The buyer is missing 61% of the time.** A lead without a counterparty is a research task, not a lead.
3. **The awareness hypothesis is completely untested**, and it is the only thing that matters. Building before asking NRS would be building on an assumption.

### Why not KILL

The discovery advantage is **real and demonstrated, not asserted**:
- Web search could not find the Rolls-Royce Sinfin A remediation consent; PlanIt found it instantly.
- Alpha Anodizing — a heavy-metal contaminated site with a live remediation condition, 38 km from Meriden — is invisible to anyone not systematically monitoring planning data.
- 442 catchment candidates in four months from a ten-minute run, with a repeatable deterministic filter.
- The timing thesis held: 6 of 10 are at condition-discharge stage, weeks-to-months from arisings.

That is a real information asymmetry. It is not yet a proven commercial one.

### What must be true for this to become BUILD

| Test | Threshold |
|---|---|
| **NRS did not know** ≥4 of the 10 | Below that, no information advantage |
| NRS would act on ≥3 | Below that, no commercial advantage |
| NRS confirms haul radius covers Derby/Mansfield | Otherwise the catchment collapses |
| Document retrieval proves feasible on ≥3 LPAs | Otherwise no tonnage, ever |

The first two are answered by five conversations and no code. Run those first.
