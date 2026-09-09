# Stress Test — Waste Permit Conformance

**Date: 2026-09-09. Adversarial review of the recommendation in
`docs/final-recommendation.md`. The brief was to disprove it.**

**Verdict: the recommendation does not survive contact with the data. It is a
real technical solution to a real regulatory obligation that the target market
does not currently experience as a problem. Downgrade from #1 to #3.**

---

## 1. The evidence that breaks it

### 1.1 The pain is not felt — measured, not assumed

Downloaded and analysed the EA's **2024 Compliance Rating dataset** (14,139
rated sites,
[data.gov.uk](https://www.data.gov.uk/dataset/1b268e32-d399-4e1c-87a0-00a17a11fce6/compliance-ratings-waste-and-installations)):

| Band | All sites | % | Waste + landfill only | % |
|---|---|---|---|---|
| A | 9,672 | 68.4% | 6,575 | 64.3% |
| B | 3,370 | 23.8% | 2,712 | 26.5% |
| C | 671 | 4.7% | 574 | 5.6% |
| D | 213 | 1.5% | 193 | 1.9% |
| E | 157 | 1.1% | 129 | 1.3% |
| F | 56 | 0.4% | 49 | 0.5% |

**90.8% of waste and landfill sites are in Band A or B — no detected
non-compliance of any kind.** Not "no acceptance breaches": *no breaches*.

The pitch was "you are about to be exposed". Nine out of ten operators have
documentary evidence from their regulator that they are compliant. Selling
insurance against a risk the buyer's own regulator says they do not have is the
hardest sale in B2B software.

### 1.2 The 9.2% who do have problems mostly have *different* problems

The dataset gives bands, not breach categories, so this is inference rather than
measurement — but the EA's own description of what a Technically Competent
Manager must oversee lists **waste acceptance as one of roughly twelve areas**,
alongside segregation and quarantine, storage and stockpile limits, processing
activities, dust, noise and odour, fire prevention, staff competence, duty of
care paperwork, record keeping, housekeeping and maintenance.

Fires, odour, stockpile heights and record keeping are what generate the serious
CCS points. Off-permit EWC codes are a paperwork breach in a category that scores
low. **We would be selling a product addressing perhaps one twelfth of the
compliance surface of the one twelfth of operators who have a compliance
problem.**

### 1.3 Enforcement is aimed somewhere else entirely

- July 2024 – end 2025: **122 prosecutions**, 10 custodial sentences, and
  **1,205 illegal waste sites shut down**.
- 2024–25: 743 illegal sites stopped, 143 high risk.
- 2025: **7,283 waste site inspections** against ~14,139 permitted sites — and
  the OEP found the EA's remote/desk-based assessment share is understated.
- **The OEP found that issues identified at inspections were not resolved in 63%
  of cases.**

Enforcement energy goes to **criminals operating without permits**, not to
permitted operators with a wrong EWC code. And when the EA *does* find something
at a permitted site, nothing happens 63% of the time.

The economic argument in the recommendation — "avoid one Category 1 breach and
the product pays for itself" — assumed detection and consequence. Both are
weak. Expected cost of the risk = probability of detection × probability of
consequence × size of consequence. The first two terms are small.

### 1.4 The ICP was wrong

I claimed "4,347 single-site operators" as the ICP. Segmenting the same dataset
by operator shows what those entities actually are:

| Segment | Count |
|---|---|
| Distinct waste/landfill operators | 5,363 |
| Holding exactly 1 site | 4,384 |
| Holding 2–10 sites | 903 |
| Holding 11+ sites | 76 |
| **ICP operators (1–10 sites)** | **5,287** covering 7,121 sites |
| …with ≥1 site in Band C–F | 643 (**12.2%**) |
| …entirely in Band A/B | 4,644 (**87.8%**) |
| **…whose "operator" is a named individual, not a company** | **1,109 (21.0%)** |
| …handling hazardous waste | 461 |

Two things fall out, and both are fatal to the ICP as described:

**The single-site tail is scrap yards and sole traders.** 2,090 of the sites are
metals recycling. 21% of ICP operators are individuals — *Helen Stevenson*,
*Richard Hardy*, *Ajab Khan*, *Mark Smith*, *Stephen Sharp*. A one-site scrap
yard run by a named individual is close to the least likely software buyer in the
UK economy.

**The multi-site "SME" segment is not SMEs.** Sorting ICP operators by site count
returns Network Rail, National Grid Electricity Distribution, United Utilities,
Warwickshire County Council, Southern Water, British Sugar, Biffa Treatment
Services, LondonEnergy and Ubico. These hold waste permits *incidental to a
completely different main business*. They have procurement functions, existing
EHS systems and 9–18 month sales cycles. They are not a self-serve SaaS motion.

**The ICP as written — "5,304 SME waste operators" — does not exist.** It is
~4,400 micro-businesses with no software budget plus ~900 large organisations
with enterprise procurement, and very little in between.

### 1.5 The price is anchored at £26

Registering for Digital Waste Tracking carries an annual charge of **about £26
per legal entity**. That is the number the entire industry is being told
compliance costs. Arriving with £150–400/month against a £26/year anchor is a
19x–180x multiple on the regulator's own price for the same obligation.

### 1.6 We are late, not early

DWT went live in April 2026 and becomes mandatory on 1 October 2026 — **three
weeks away**. 120+ providers are already approved. Operators have already
chosen their software and had the compliance conversation. The "regulatory
tailwind" I described has largely already blown through.

### 1.7 The self-incrimination objection is worse than I allowed

I listed it as one objection among several. On reflection it is structural.

The product's core output is **a document proving the operator knowingly accepted
waste outside their permit**. In a regulated industry, creating discoverable
evidence of your own breaches is not a neutral act. A competent operator's
lawyer will advise against generating it. This is not a messaging problem to be
solved with "private by default" — it is an inherent property of what the
product produces.

---

## 2. The ten questions, answered honestly

**1. Do operators experience this problem today?** Mostly no. 90.8% are rated
Band A/B. A minority with complex hazardous or mixed-waste intake genuinely
struggle with mirror entries — but that is a *classification* problem, not a
permit-list problem.

**2. How do they check conformance today?** A weighbridge operator checks against
a laminated list or memory. For a typical site the permitted list is short and
stable, and the same twenty waste streams arrive from the same customers every
week. It is not hard, and it is not felt as a burden.

**3. Who is responsible?** The **Technically Competent Manager** (CIWM/WAMITAB
CoTC), required on site for at least 20% of operating hours. At small operators
the TCM is frequently the owner, or an outsourced "CoTC cover" contractor.

**4. How often are breaches discovered?** Rarely. About half of permitted sites
see an inspection in a year, many remote, and 63% of identified issues go
unresolved.

**5. Real consequences?** For permitted operators, usually an advice-and-guidance
letter. CCS band changes affect subsistence, but most sites never leave A/B.
Serious enforcement targets illegal operators.

**6. Time spent checking?** Far less than I estimated. My "150–500 hours/year"
assumed checking is a discrete task. It is not — it is two seconds of
recognition inside an existing weighbridge conversation. The honest figure is
close to zero marginal hours.

**7. What software already exists?** Weighbridge systems (Avery Weigh-Tronix,
Weightron), 120+ DWT providers, and for larger operators AMCS or an EHS suite.
Very small sites run on paper and a spreadsheet.

**8. Why would they refuse to buy?** "We know what we're permitted for." "We've
never had a problem." "Our DWT provider handles that." "£26 is what the
government charges." And the lawyer's answer: "why would we create that record?"

**9. Would they avoid software that reveals compliance issues?** **Yes.** See
§1.7. This is the single strongest objection and it does not have a good answer.

**10. Evidence they would pay?** They already pay — for **people, not software**:
CoTC/TCM cover services, permit consultants (£8–25k per application), duty-of-care
audits (£800–2,000/day). That is genuine willingness to pay, but it is directed
at *transferring responsibility to a qualified human*, which software cannot do.

---

## 3. Twenty real operators, scored

All names and bands taken directly from the 2024 Compliance Rating dataset.
Value = realistic monthly £ they would pay.

| # | Operator (real) | Sites | Bands | Segment | Buy 1–10 | Why they might | Why they won't | £/mo |
|---|---|---|---|---|---|---|---|---|
| 1 | Network Rail Infrastructure | 10 | AAAAAAAAAA | Haz/inert/non-haz | 3 | Multi-site, reputational exposure | Enterprise procurement; existing EHS; all Band A | 0–400 |
| 2 | National Grid Electricity Distribution (South) | 10 | A×6 B×4 | Hazardous | 3 | Hazardous complexity | Same; buys from tier-1 vendors | 0–400 |
| 3 | United Utilities Water | 9 | AAAAAAAAA | Mixed | 2 | — | Perfect record; enterprise stack | 0 |
| 4 | Warwickshire County Council | 9 | A×7 B×2 | Haz/non-haz | 3 | Public accountability | Procurement, frameworks, 12-month cycle | 0–300 |
| 5 | Citron Hygiene (UK) | 9 | A×8 B×1 | Hazardous | 4 | Clinical/haz, multi-site, real complexity | Near-clean record | 200–500 |
| 6 | Biffa Treatment Services | 10 | A×8 B×2 | Non-haz | 2 | — | Part of Biffa; builds in-house | 0 |
| 7 | LondonEnergy | 10 | A×9 B×1 | Non-haz | 2 | — | Large, own systems | 0 |
| 8 | Day Group | 10 | A×9 B×1 | Inert/non-haz | 4 | Genuine mid-size independent | Inert waste = trivial code list | 150–300 |
| 9 | Ubico | 10 | A×7 B×3 | Non-haz | 3 | LA-owned, accountability | Municipal, no discretionary spend | 0–200 |
| 10 | Enovert North | 9 | AAABBCCDD | Landfill/non-haz | **6** | **Two Band D sites — active problem** | Problem is likely landfill ops, not codes | 300–600 |
| 11 | Southern Water Services | 9 | A×5 B×2 C D | Non-haz | 4 | Band C and D present | Water utility; waste is peripheral | 0–300 |
| 12 | British Sugar | 9 | A×5 B×3 D | Haz landfill/inert | 4 | Band D | Manufacturer; waste incidental | 0–300 |
| 13 | Global Ardour Recycling | 10 | A×5 B×3 C D | Metals/non-haz | **6** | **Deteriorating; multi-site** | Metals recycler, price-driven, thin margins | 200–400 |
| 14 | Mytum & Selby Waste Recycling | 3 | C C **F** | Haz/metals | **7** | **Band F — 200% subsistence uplift, real jeopardy** | Already in enforcement; needs a consultant, not software | 300–700 |
| 15 | Willshees Waste & Recycling | 3 | A B **D** | Metals/non-haz | **6** | Band D, independent, right size | Family firm; will call their consultant | 200–400 |
| 16 | Unipart Group | 3 | A B B | Metals | 3 | — | Logistics group; waste peripheral | 0–200 |
| 17 | Bakers Waste Services | 1 | **D** | Non-haz | 5 | Band D on a single site | Single site; owner-run; low budget | 100–250 |
| 18 | Genta Environmental | 1 | A | Hazardous | 4 | Hazardous specialist | Clean record; one site | 100–250 |
| 19 | European Asbestos Services | 1 | A | Hazardous | 4 | ACM = narrow, well-understood codes | Tiny permitted list; knows it by heart | 100–200 |
| 20 | Ellgia Recycling (Lancaster Way MRF) | 1 | A | Non-haz | 4 | Mid-size independent | Clean record | 100–250 |
| 21 | Halifax Metals | 1 | A | Metals | 2 | — | Scrap yard; paper-based | 0 |
| 22 | Helen Stevenson (Macclesfield Scrap Metals) | 1 | A | Metals | **1** | — | **Sole trader. Will never buy SaaS.** | 0 |
| 23 | Richard Hardy (RNH Skiphire) | 1 | A | Non-haz | **1** | — | Sole trader, skip hire | 0 |
| 24 | Ajab Khan (Seven Day Parts) | 1 | B | Metals | **1** | — | Sole trader, vehicle dismantler | 0 |

**Mean likelihood 3.5/10. Only three of 24 score ≥6, and all three are already in
trouble — which means they need a consultant to get them out, not a monitoring
subscription to tell them they are in it.**

---

## 4. The structured questions

**A. Compliance problem or sales problem?** **A sales problem.** The compliance
obligation is real and the technical solution works. The market does not
experience it as pain, and 88% have regulator-issued evidence they are fine.

**B. Who is the buyer?** There is no consistent one, which is itself the finding.
Micro-operators: the **owner**, who is also the TCM, and who is the person the
product would incriminate. Mid-size independents: **operations director**.
Utilities/councils: **compliance manager** inside procurement. Three different
motions for one small market.

**C. Who signs?** Owner/MD below ~£50m turnover; procurement above. No
self-serve path.

**D. What budget?** **None exists.** Nearest lines are TCM/CoTC cover and
consultant retainers — both already committed, both bought as *human
responsibility transfer*.

**E. Purchase trigger?** An inspection with findings, an enforcement notice, a
permit variation, a customer audit, a new TCM, or acquisition due diligence. All
**episodic, unpredictable, and roughly annual** — which produces lumpy,
event-driven demand, the opposite of what a subscription business needs.

**F. Strongest objections?** (1) "Why create a record of our own breaches?"
(2) "We've never had a problem." (3) "£26 is the government's price."
(4) "Our DWT provider does compliance." (5) "I'd rather pay a consultant who
carries the responsibility."

**G. Evidence of spending?** Yes — on humans. CoTC cover, permit consultancy
(£8–25k), duty-of-care audits (£800–2,000/day). **No evidence of spend on
conformance software, which after this analysis reads as revealed preference
rather than an unserved need.**

**H. What would they do instead?** Nothing. Or ask their consultant at the next
visit. "Do nothing" is a strong, cheap, socially acceptable competitor.

---

## 5. What survives

Two things are still true and worth keeping:

1. **The permit dataset is real and buildable** — 68 Standard Rules documents
   cover 37% of permits, and nobody has structured it. It is an asset. It is
   just not, on this evidence, a *product*.
2. **Mirror-entry misclassification is described by the EA as one of its most
   common findings.** That points at **WM3 classification**, not permit
   conformance — a judgement problem, not a list-checking problem.

The plausible pivot is therefore *down* the stack into classification, or
*sideways* into selling the permit dataset to people who profit from it
(brokers routing waste, consultants, M&A diligence) rather than to operators
who must confess with it.
