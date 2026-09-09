# Ten Leads Test — Candidate Pool and Filtering

**Run date: 2026-09-09. Catchment: 110 km radius of Meriden (52.4361, −1.6469),
NRS's principal permitted site cluster. Window: applications with a start date
between 2026-05-01 and 2026-09-09.**

Raw pool exported to **`docs/data/ten-leads-pool.csv`** (442 rows) — the audit
trail for everything below.

---

## 1. Method

**Source: the PlanIt API** (`https://www.planit.org.uk/api/applics/json`),
verified working from this environment. Ten search terms were run, each paged,
and every result geocoded and filtered to the catchment by great-circle distance
from Meriden.

| Search term | Records scanned | — |
|---|---|---|
| remediation | 750 | |
| contaminated land | 628 | |
| demolition | 750 | |
| materials management plan | 609 | |
| land contamination | 628 | |
| verification report | 447 | |
| asbestos | 119 | |
| ground investigation | 107 | |
| hydrocarbon | 2 | thin — term rarely used in application titles |
| gasworks | 1 | thin |
| **Total scanned** | **~4,041** | |
| **In catchment** | **442** | |

**FACT:** the national result count for "remediation" alone was **46,262**. The
volume of signal available is not the constraint.

### Pool composition (measured)

| Attribute | Count | % |
|---|---|---|
| Application type = Conditions (discharge) | 296 | 67.0% |
| State = Undecided (live, not yet determined) | 294 | 66.5% |
| Size = Small | 399 | 90.3% |
| Size = Medium | 24 | 5.4% |
| **Size = Large** | **14** | **3.2%** |
| Within 60 km of Meriden | 197 | 44.6% |
| With a named agent (not blank / "See source") | 173 | 39.1% |

**The single most important number here is 90.3% Small.** The signal is
abundant; commercially material signal is scarce. See §4.

---

## 2. Scoring applied to the pool

Deterministic, no LLM:

```
+4  application type is a condition discharge
+4  description matches remediation / contaminated land / verification /
    ground gas / asbestos / geo-environmental / ground investigation
+2  description mentions demolition
+2  state is Undecided (live)
+3  size Large   (+1 Medium)
+2  within 60 km (+1 within 90 km)
```

Then a second filter for **industrial land-use heritage** — address or
description matching works / foundry / gasworks / factory / industrial / depot /
filling station / forge / tannery / mill / engineering / plating / anodising /
chemical / scrap / colliery / quarry / landfill / pottery / smelting — **combined
with** a contamination term.

**65 of 442 (14.7%) passed both.** That subset supplied nine of the final ten
leads; the tenth (Lead 1) came from the Contracts Finder tender harvest. This
filter is the operational definition of the product.

---

## 3. Elimination — why 432 candidates were discarded

| Reason discarded | Approx. count | Rule |
|---|---|---|
| **Too small to be commercially material** | ~300 | Single-plot residential infill, barn conversions, individual dwellings. A contaminated land condition on a 4-house infill plausibly yields tens to low hundreds of tonnes. Below any credible commercial threshold. |
| **Verification/validation report only** | ~45 | ⚠️ **A verification report means remediation is complete or nearly complete. The waste has already moved.** This is a systematic false positive and had to be explicitly excluded — an important design finding. |
| **Contamination term incidental** | ~40 | "Drainage verification report", "storm verification report", materials/landscaping conditions caught by keyword but unrelated to soil. |
| **No identifiable counterparty** | ~25 | Applicant and agent both blank or "See source"; no route to a buyer. |
| **Already determined and stale** | ~15 | Permitted months ago with no live phase. |
| **Outside plausible economic haul** | ~7 | 90–110 km with no offsetting scale. |

---

## 4. What the filtering revealed — three findings that matter more than the leads

**FINDING 1 — The signal is abundant, the value is not.**
442 catchment candidates in four months, but only **38 are Medium or Large**
(8.6%). Extrapolating, a full year across the catchment might yield ~110–130
commercially material events. That is roughly **two to three per week** — which
is the right order of magnitude for a weekly sales briefing, but it is not a
large number, and it caps how much a subscription can be worth.

**FINDING 2 — Verification reports are a trap.**
"Verification report" was one of the highest-volume matching terms, and it is
almost always **too late**: it evidences remediation that has already happened.
Any naive keyword system would surface these as leads and be wrong. Correct
handling requires distinguishing *prospective* conditions (remediation strategy,
site investigation, remedial scheme, ground gas) from *retrospective* ones
(verification, validation). **This is a real, non-obvious product requirement.**

**FINDING 3 — Tonnage is not derivable from this source.**
⚠️ **No record in the 442-row pool contains site area, excavation depth,
contaminated volume, or tonnage.** The PlanIt record carries a description, an
address, coordinates, dates and sometimes an agent — nothing dimensional.

Tonnage exists only inside the **submitted documents** (remediation strategy,
Phase 2 geo-environmental assessment), which are on LPA portals behind
per-application document lists that PlanIt does not carry.

This directly contradicts the worked example in `docs/product-requirements.md`
("8,000–15,000 tonnes … £300k–£500k"). **That output is not achievable from the
planning API alone.** It requires document retrieval and parsing — Phase 2 in
`docs/roadmap.md`, not the MVP. This is the most significant estimate-related
finding of the test and is carried into `docs/ten-leads-analysis.md`.

---

## 5. Sources that were tested and did not work

| Source | Result |
|---|---|
| **Contracts Finder OCDS API** | ⚠️ **Partially successful.** Reachable and correctly structured, but **HTTP 429 rate limiting** repeatedly throttled paginated harvesting even at 12-second intervals. A backed-off run eventually scanned **648 notices over 7 pages and returned 8 catchment-relevant hits** — including the single best lead in the test (Lead 1, EKFB/HS2). Production use needs proper backoff, caching and probably overnight batch collection. |
| **EA consultation portal** (`consult.environment-agency.gov.uk/psc/`) | ❌ 404 at the index. Individual application documents are reachable when a direct URL is known, but there is no discoverable listing endpoint. A permit-variation feed remains an attractive but **unverified** hypothesis. |
| **Direct LPA portals** | ⚠️ Mixed. Derby's portal returned **HTTP 503** on direct fetch. Others (statmap, agileapplications, Salesforce-hosted) each use different software. Confirms T2 in `docs/risks.md`: document-level access is per-LPA engineering, not a single integration. |
| **General web search for obscure applications** | ❌ **Could not locate Derby application 26/00060/FUL** (the Rolls-Royce Sinfin A remediation permission), returning "may be a very recent 2026 application that might not yet be widely indexed online". PlanIt surfaced it in seconds. **This is the single clearest demonstration of the discovery advantage in the whole test.** |
