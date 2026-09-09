# Opportunity Research — UK B2B AI/Software

**Date: 2026-09-09.** Research conducted via live web search and direct analysis
of public datasets. Sources cited inline; full competitor detail in
`docs/competitive-landscape.md`; scoring in `docs/opportunity-scorecard.md`;
the recommendation in `docs/final-recommendation.md`.

---

## 1. Method

1. Generate a broad candidate list across UK sectors, biased toward "boring"
   industries where software is weak and specialist human labour is expensive.
2. Score every candidate on ten dimensions.
3. Take the top ten and research competitors **aggressively** — direct, adjacent,
   incumbent, startup, open-source, and the consultancies doing the work by hand.
4. Kill anything with a strong incumbent or a crowded AI-startup field.
5. Deep-dive the survivors.

**The controlling filter:** *"If this company disappeared tomorrow, would a
business owner immediately notice the lost economic value?"*

---

## 2. The Barbour ABI lesson — what kind of moat to avoid

Barbour ABI's defensibility is **not** its software. It is:

- A project database accumulated over decades that cannot be back-filled.
- A human research team phoning contractors to verify and enrich records.
- A relationship graph (who builds for whom, who specifies what) that is not
  derivable from public data.
- Contact data with consented, maintained decision-maker details.
- An installed base whose workflows and renewals are already committed.

A newcomer must reproduce all five *before* selling anything, and four of them
are labour, not code. AI collapses the cost of *interpreting* data; it does not
collapse the cost of *accumulating proprietary data over twenty years*. That is
the asymmetry that makes head-on competition unwinnable.

**The transferable rule:** avoid markets whose incumbent moat is accumulated
proprietary data. Prefer markets where

- the underlying data is **public but unusable** (locked in PDFs, scattered
  across registers, unstructured),
- the incumbent is a **consultancy day-rate**, not a software company, and
- a **regulatory change** has just reset everyone's position.

The winner in §6 satisfies all three.

---

## 3. Where AI startups have already clustered (avoid)

An observable pattern from this research: AI startups cluster where the buyer is
a **high-margin professional services firm** — law, insurance broking,
accountancy, ecology. Those buyers have budget, high hourly rates and obvious
document workloads, so everyone targets them.

Verified crowding:
- **Insurance policy comparison** — CopyCat, Cluda, Layer3Labs already shipping.
- **Biodiversity Net Gain** — BioGain, Joe's Blooms, AiDash BNGAI, EcoScribe,
  One Click LCA. One vendor's own comparison page says the market is "filling up
  fast". BNG scope was *reduced* from 6 Aug 2026 (developments ≤0.2 ha exempt),
  so the market is crowding while shrinking.
- **Subcontractor compliance documents** — ContractorVault, SubComply, Onetrace,
  Boxcore, ExpiryFlow, Subcompliant, SiteSamurai. A commodity expiry-tracker
  market with no differentiation left.
- **Manufacturing RFQ/quoting** — Paperless Parts (well-funded, US), Tempus
  Tools, DigiFabster, Fulcrum, ShopVox, Quintadena, KipwareQTE.
- **Digital waste transfer notes** — see §5. **120+ approved providers.**

Conversely, AI startups have *not* reached buyers who are asset-heavy operational
SMEs with small software budgets and unglamorous compliance obligations. That is
where the whitespace is — and it is whitespace precisely because it is harder to
sell into, which is a real cost, not a free lunch.

---

## 4. The 35 candidate opportunities

Scored in `docs/opportunity-scorecard.md`. ❌ = killed on competitive research;
⭐ = advanced to deep dive.

### Waste and environmental services
| # | Opportunity | Verdict |
|---|---|---|
| 1 | **Waste permit conformance & duty-of-care assurance** — structured database of what every UK waste site is *permitted* to accept; validate movements against it | ⭐ **#1** |
| 2 | **WM3 hazardous waste classification assistant** — automate EWC coding and HP1–HP15 hazard assessment | ⭐ **#3** |
| 3 | Digital Waste Tracking capture app (WTN/consignment notes) | ❌ 120+ approved providers |
| 4 | Environmental permit obligation management for SME permitted sites | Top 10 |
| 5 | Environmental permit application/variation drafting assistant | Top 10 |
| 6 | Waste commercial intelligence (the existing NRS project) | Top 10 |
| 7 | Waste broker routing & margin optimisation | Mid |
| 8 | Packaging EPR data compliance | ❌ crowded, big-4 adjacent |

### Environmental consultancy deliverables
| # | Opportunity | Verdict |
|---|---|---|
| 9 | **Phase 1 contaminated land desk study automation** | ⭐ **#2** |
| 10 | Remediation validation / verification report drafting | Top 10 |
| 11 | Biodiversity Net Gain assessment | ❌ crowded + shrinking scope |

### Construction
| # | Opportunity | Verdict |
|---|---|---|
| 12 | Planning condition discharge & pre-commencement obligation tracking | Top 10 |
| 13 | Subcontractor compliance document tracking | ❌ commodity |
| 14 | O&M manual / handover documentation compilation | Mid — Zutec, Operance, Bimsense |
| 15 | CDM / RAMS generation | ❌ many micro-vendors |
| 16 | NEC/JCT contract notice & early-warning management | Mid |
| 17 | Construction variation & claim analysis | Mid |
| 18 | Building Safety Act golden thread | ❌ Brocade, ThreadSovereign, Operance, Zutec |

### Property and facilities
| # | Opportunity | Verdict |
|---|---|---|
| 19 | Commercial service charge reconciliation | ❌ MRI Qube, Re-Leased, Brocade |
| 20 | Lease abstraction | ❌ enterprise incumbents |
| 21 | Dilapidations schedule drafting | Mid — thin market |
| 22 | FM statutory compliance evidence | ❌ served |

### Insurance
| # | Opportunity | Verdict |
|---|---|---|
| 23 | MGA delegated authority / bordereaux processing | ❌ DistriBind, IDS, Regure, Vipr, Inari |
| 24 | Broker policy wording comparison | ❌ CopyCat, Cluda |
| 25 | Claims triage | ❌ heavily contested |

### Transport and logistics
| # | Opportunity | Verdict |
|---|---|---|
| 26 | O-licence / PMI / defect compliance | ❌ FleetCheck, Zerity, Microlise, Mandata |
| 27 | Haulage rate benchmarking | Mid — data acquisition problem |
| 28 | Tachograph infringement analysis | ❌ solved |

### Manufacturing and engineering
| # | Opportunity | Verdict |
|---|---|---|
| 29 | Fabrication RFQ → quote automation | ❌ Paperless Parts et al. |
| 30 | Material test certificate (EN 10204 3.1) traceability | Top 10 |
| 31 | UKCA/CE technical file & Declaration of Conformity management | Top 10 |

### Back office and professional services
| # | Opportunity | Verdict |
|---|---|---|
| 32 | Energy/utility invoice validation | ❌ EIC, Inspired, Zenergi, TEAM, MRI, VuePoint |
| 33 | Agency worker compliance files (RTW/DBS) | ❌ ComplyCube, Sense HR |
| 34 | Business rates appeal identification | Mid — agents own the relationship |
| 35 | R&D tax credit preparation | ❌ crowded and reputationally damaged |

---

## 5. The regulatory event that reframes everything

**Defra's Digital Waste Tracking (DWT) service becomes mandatory for all
permitted and licensed waste *receiving* sites on 1 October 2026** — within weeks
of this research — expanding to carriers, brokers, dealers and exempt sites in
April 2027. Submission is via API, CSV upload or a web portal, and software
providers must pass 14 production approval tests (PAT).
[Defra developer guide](https://defra.github.io/waste-tracking-service/) ·
[Choose a software provider](https://www.gov.uk/government/publications/report-receipt-of-waste-choose-a-software-provider/report-receipt-of-waste-choose-a-software-provider)

Two conclusions, pulling in opposite directions:

**Do not build capture.** Defra's own page lists **120+ approved providers** that
have already integrated with the receipt-of-waste API and passed PAT. Entering
that market weeks before the mandate, against 120 incumbents, with an
undifferentiated note-capture app, would be commercial suicide.

**But the mandate creates the opportunity above it.** Until now, what a site
actually accepted was visible only in its own paperwork. From October 2026, every
movement is a structured record submitted to the regulator. As one industry guide
puts it: *"DWT submissions must match your permit waste acceptance schedule. If
you are accepting waste streams not listed on your permit (even informally), DWT
will surface this immediately."*
([Wastebolt](https://wastebolt.app/waste-blog/digital-waste-tracking-waste-receivers-2026))

Thousands of operators are about to have years of informal practice made
machine-readable to their regulator — and the 120 approved providers sell
*submission*, not *assurance*. Defra's provider page contains **no mention of
permit checking, validation or compliance verification**; approval tests only
require that software can record and transmit the mandated fields.

**That gap is the opportunity.**

### Why the exposure is expensive

Accepting waste not listed on the permit is a permit breach
([GOV.UK](https://www.gov.uk/government/publications/assessing-and-scoring-environmental-permit-and-licence-compliance/assessing-and-scoring-environmental-permit-compliance)).
Breaches accumulate points under the Compliance Classification Scheme —
Category 1 = 60 points, Category 2 = 31, Category 3 = 4 — and the annual total
sets a compliance band that directly multiplies the subsistence charge:

| Band | Points | Subsistence effect |
|---|---|---|
| A | 0 | −5% |
| B | 0.1–10 | none |
| C | 10.1–30 | **+10%** |
| D | 30.1–60 | **+25%** |
| E | 60.1–149.9 | **+50%** |
| F | 150+ | **+200%** |

Two Category 1 breaches move a site from Band A to Band E. Separately, waste
duty-of-care breach under s.34 Environmental Protection Act 1990 is a **criminal
offence carrying an unlimited fine and up to two years' imprisonment**
([GOV.UK code of practice](https://www.gov.uk/government/publications/waste-duty-of-care-code-of-practice/waste-duty-of-care-code-of-practice)).

This is a market where the product prevents an expensive mistake *and* reduces
regulatory risk — two of the five value tests, with a third (saved labour) on
top.

---

## 6. Market structure — measured, not estimated

Analysed directly from the Environment Agency's downloadable waste operations
register (ZIP → CSV, no API key,
`https://environment.data.gov.uk/public-register/downloads/waste-operations`):

| Measure | Value |
|---|---|
| Total permits in register | 9,607 |
| **Effective permits** | **8,778** |
| Standard Rules permits (`SR….`) | 3,258 (37.1%) |
| Bespoke permits (`A…`/`L…`) | 5,520 (62.9%) |
| **Distinct SR rule sets to model** | **68** |
| Distinct bespoke site types | 35 |
| **Distinct licence holders** | **5,304** |
| Holders with exactly 1 site | **4,347** — the SME long tail, and the ICP |
| Holders with 2–5 sites | 813 |
| Holders with 6+ sites | 144 |
| Easting/northing populated | **100.0%** of effective permits |

Two findings that materially shape the MVP:

1. **68 Standard Rules documents cover 3,258 permits (37% of the market).** Each
   SR rule set is a published PDF with a defined permitted-waste-code table. So
   37% of national coverage is *68 document extractions*, not 3,258. That is a
   two-week job, not a two-year one.
2. **4,347 single-site operators** are the target. The majors — Suez (100 sites),
   EMR (75), Biffa (73), Veolia (72), Tarmac (65) — have enterprise systems and
   compliance departments. They are not the ICP, and their absence from the ICP
   is a feature: it means no enterprise vendor is defending this ground.

---

## 7. Sources

- [EA waste operations public register download](https://environment.data.gov.uk/public-register/downloads/waste-operations) — analysed directly
- [Defra Digital Waste Tracking developer guide](https://defra.github.io/waste-tracking-service/)
- [Report receipt of waste: choose a software provider](https://www.gov.uk/government/publications/report-receipt-of-waste-choose-a-software-provider/report-receipt-of-waste-choose-a-software-provider)
- [Assessing and scoring environmental permit compliance (CCS)](https://www.gov.uk/government/publications/assessing-and-scoring-environmental-permit-and-licence-compliance/assessing-and-scoring-environmental-permit-compliance)
- [Waste duty of care: code of practice](https://www.gov.uk/government/publications/waste-duty-of-care-code-of-practice/waste-duty-of-care-code-of-practice)
- [Digital waste tracking for waste receivers](https://wastebolt.app/waste-blog/digital-waste-tracking-waste-receivers-2026)
- [Standard rules: environmental permitting](https://www.gov.uk/government/collections/standard-rules-environmental-permitting)
- [WM3 waste classification guidance](https://www.gov.uk/government/collections/classify-different-types-of-waste)
- [SOCOTEC WM3 overview](https://www.socotec.co.uk/media/hot-topics/wm3)
- [EcoScribe BNG competitor comparison](https://ecoscribe.co.uk/alternatives/)
- [Paperless Parts](https://www.paperlessparts.com/job-shop-software/) · [DistriBind](https://distribind.io/) · [Cluda](https://www.cluda.ai/) · [CopyCat](https://www.runcopycat.com/commercial-renewal-comparison-software)
