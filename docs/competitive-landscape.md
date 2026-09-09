# Competitive Landscape

Market classification used throughout:

- **A — Truly underserved.** No product does this; the work is done by people.
- **B — Competitive but fragmented.** Many small players, no leader.
- **C — Strong incumbents.** A defended category. Avoid.
- **D — Looks attractive, hidden competition.** Funded startups already shipping.
- **E — Avoid.** Structurally bad regardless of competition.

---

## 1. Waste permit conformance & duty-of-care assurance — **Category A**

The recommended opportunity. Researched hardest, precisely because a "category A"
claim is the easiest thing to get wrong.

### Alternatives found

| # | Alternative | What it actually does | Gap |
|---|---|---|---|
| 1 | **120+ Defra-approved DWT providers** (Bartec, InfoTech, Wastebolt, Skiplog, Wye Valley, AMCS…) | Record and transmit mandated waste movement data via the receipt-of-waste API. Approval = passing 14 production approval tests. | Defra's provider page contains **no mention of permit checking, validation or compliance verification**. They submit; they do not tell you whether the submission is *lawful*. |
| 2 | **WTN/consignment apps** — DigitalWTN, WTNcloud, Quick Consign, WasteNote (Waste Matrix), Wastebolt, Mandata | Digitise the note; some validate that an EWC code is well-formed | Well-formed ≠ permitted. None holds a structured model of what each site's permit allows. |
| 3 | **EWC lookup tools** — WasteSupport, Quick Consign EWC Finder, Wastebolt EWC list | Free searchable EWC code lists | Reference lookups. No permit, no site, no validation, no audit trail. |
| 4 | **EHS suites** — Intelex, VelocityEHS, Enablon, Ecesis, EHS Data, Remindax | Permit *registers*: store the permit, track expiry and obligations | US/enterprise-shaped, priced far above a single-site operator, and they track the permit as a **document with dates**, not as a machine-readable list of permitted waste codes checked per movement |
| 5 | **EcoComply** | UK AI startup; extracts obligations from permits and tracks deadlines with evidence linking | **The closest competitor.** Obligation-and-deadline shaped, not transaction-validation shaped. Worth monitoring closely — the extraction capability is adjacent to ours. |
| 6 | **SOCOTEC MiPortal**, Alkali, The Compliance People, Waste Experts | Consultancy: manual duty-of-care audits and permit compliance reviews | Day-rate, periodic, sampled. Cannot check every load. **This is the real competitor: the status quo is a human.** |
| 7 | **Weighbridge systems** — Avery Weigh-Tronix, Weightron, Cortex | Capture weights, integrate with DWT | Weight and ticket capture. Permit conformance is out of scope. |
| 8 | **The actual incumbent: a laminated list** | Weighbridge operator checks incoming loads against a printed permit schedule | Manual, error-prone, unaudited, no evidence trail, and it fails silently |
| 9 | Open source | None found | — |

### Why nobody has built it

1. **The permit data doesn't exist in structured form.** The public register
   (verified: 9,607 rows) gives permit numbers, holders and site types — but
   **no permitted EWC codes and no capacity**. Those live inside permit PDFs and
   Standard Rules documents. Someone has to do the extraction work; until LLMs,
   that was a data-entry project nobody could justify.
2. **Until October 2026 there was no forcing function.** Off-permit acceptance
   was invisible unless an inspector found it. DWT changes that in weeks.
3. **The 120 approved providers are racing to a submission deadline**, not
   building an assurance layer. Their roadmaps are full until October.
4. **EHS vendors sell to enterprises.** The 4,347 single-site operators are too
   small for Intelex and too unglamorous for AI startups.

### Honest competitive risks

- **A DWT provider adds validation as a feature.** The most likely threat. Any of
  the 120 could bolt on "check against permit" — *if* they had the permit data.
  They do not, and the extraction is the hard part. Our defence is to own the
  dataset, and to be usable alongside whichever capture system a site already
  runs rather than competing with it.
- **EcoComply moves from obligations to transactions.** Plausible; they already
  have permit extraction. Speed and waste-sector specificity are the answer.
- **Defra publishes structured permit conditions.** Would destroy the data moat
  overnight. No indication of it, and government data programmes move slowly —
  but it is the tail risk to watch, and it argues for building the workflow and
  evidence layer, not just the dataset.

---

## 2. Phase 1 contaminated land desk study — **Category B**

| # | Alternative | What it does | Gap |
|---|---|---|---|
| 1 | **Landmark Envirocheck** | Sells the historic map + environmental data pack consultants buy | Sells *inputs*. Explicitly not a Phase 1 assessment — local authorities state a search report alone does not satisfy the requirement. |
| 2 | **Groundsure** | As above, with some interpretive products | Same: data, not the assessed deliverable |
| 3 | **Geo-environmental consultancies** — GeoCon, Chevin, Ground & Water, G&J, Abbeydale, Arbtech | The actual competitor: a consultant writes the report over 1–2 days | Labour. This is the cost we would remove. |
| 4 | **EcoScribe** (ecology reports) | AI report writing for ecologists, "keeps the ecologist in control" | Adjacent discipline — proves the pattern works and that someone will eventually do it for geo-environmental |
| 5 | **BGS / EA / Coal Authority open data** | Free underlying datasets | Raw; requires the interpretation layer |
| 6 | Word templates | What most small consultancies actually use | The true baseline |

**Assessment: B.** No direct product, but the input data sits with two
incumbents who could move up-stack, and the market is roughly 500–1,000 UK
consultancies — enough for a good business, not an obvious £10m one.

---

## 3. WM3 waste classification — **Category A, small**

| # | Alternative | What it does | Gap |
|---|---|---|---|
| 1 | **SOCOTEC, ECL, Alkali, The Testing Lab** | Consultant-led WM3 assessments with lab analysis | Day-rate specialist work |
| 2 | **UKAS labs** | Chemical analysis | Produce the input data; do not make the classification judgement |
| 3 | **WasteSupport, Quick Consign, Wastebolt** | EWC code search tools | Lookup only; no HP1–HP15 assessment |
| 4 | **GOV.UK WM3 technical guidance** | The 200-page rulebook | Free, and unusable at speed by non-specialists |
| 5 | **Spreadsheets** | What consultancies actually use for threshold calculations | The real baseline |
| 6 | Open source | Nothing credible found | — |

**Assessment: A**, and genuinely surprising — the hazard-property assessment is
substantially deterministic (concentration thresholds against HP criteria), which
is exactly the sort of rule-based calculation software should have automated
years ago. Constraint is market size and the regulatory weight of getting a
hazardous/non-hazardous call wrong. **Best deployed as a module of #1, not as a
standalone company.**

---

## 4. Categories C and D — the killed ideas, with evidence

| Opportunity | Cat | Competitors found |
|---|---|---|
| **DWT capture** | C | 120+ Defra-approved providers |
| **Subcontractor compliance** | B→E | ContractorVault, SubComply, Onetrace, Boxcore, ExpiryFlow, Subcompliant, SiteSamurai — commodity, no pricing power |
| **Biodiversity Net Gain** | D | BioGain, Joe's Blooms, AiDash BNGAI, EcoScribe, One Click LCA — *and* statutory scope cut to exclude ≤0.2 ha from 6 Aug 2026 |
| **Insurance policy comparison** | D | CopyCat, Cluda, Layer3Labs |
| **MGA bordereaux** | D | DistriBind, Insurance Data Solutions, Regure, Inari, InsurSystems, Vipr |
| **Fabrication quoting** | C | Paperless Parts, Tempus Tools, DigiFabster, Fulcrum, ShopVox, Quintadena, KipwareQTE |
| **Service charge** | C | MRI Qube, Re-Leased, Brocade, Landlord Vision |
| **Energy invoice validation** | C | EIC, Inspired, Zenergi, TEAM, MRI Energy, SOCOTEC, VuePoint — mostly bundled free with brokerage, so price is effectively zero |
| **O-licence compliance** | C | FleetCheck, Zerity, ETM, FleetRabbit, Microlise, Mandata |
| **BSA golden thread** | C/D | Brocade, ThreadSovereign, Operance, Zutec, Sitemate |
| **RTW/DBS compliance** | C | ComplyCube, Sense HR, and every ATS |

---

## 5. Pattern

The two Category A findings share a shape:

1. The buyer is an **operational SME**, not a professional services firm — so the
   AI startup wave has not arrived.
2. The required data is **public but locked in PDFs** — so it looks like a
   data-entry problem, which is exactly what has become cheap.
3. The incumbent is a **consultant's day rate**, not a software licence — so
   there is no vendor defending the territory, and the price to beat is high.
4. A **regulatory change** has just reset the field.

That combination is rarer than it sounds, and it is worth more than a larger
market with a defended incumbent.
