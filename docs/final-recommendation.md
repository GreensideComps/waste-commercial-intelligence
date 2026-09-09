# Final Recommendation

> ## ⚠️ SUPERSEDED — 2026-09-09
> This recommendation **did not survive adversarial review**. Analysis of the EA
> 2024 Compliance Rating dataset found 90.8% of waste sites in Band A/B (no
> detected non-compliance), an ICP that is 21% sole traders and otherwise large
> utilities/councils, enforcement aimed at illegal rather than permitted
> operators, and a £26/year regulatory price anchor. See
> **`docs/stress-test-permit-conformance.md`**. Permit conformance is downgraded
> from #1 to #3. Retained for the reasoning and the market data, which remain
> valid.

---

# ⭐ PermitGuard — waste permit conformance & duty-of-care assurance

**The one-line pitch:** *"Every load you accept, checked against your permit —
before the regulator checks it for you."*

---

## Part 1 — The top 3, deep

### #1 Waste permit conformance & duty-of-care assurance ⭐ RECOMMENDED

| | |
|---|---|
| **Current human process** | A weighbridge operator or transfer station supervisor checks incoming loads against a printed or remembered list of permitted waste codes. Periodically, a consultant runs a sampled duty-of-care audit. Producers "check the carrier is registered" — a manual two-minute lookup — and usually do **not** check that the destination site is permitted for that specific waste. |
| **Labour cost** | Weighbridge checking: ~2–5 min/load × 20–100 loads/day ≈ **0.5–2 FTE-days per site per week**, mostly invisible because it is buried in another role. Duty-of-care consultancy audits: **£800–£2,000/day**, typically 2–10 days a year for a mid-size producer. Permit compliance reviews: similar. |
| **Hours involved** | 150–500 h/yr per permitted site in embedded checking; 20–80 consultant hours/yr for a producer's supply-chain assurance |
| **Why the task exists** | Accepting waste not listed on the permit is a permit breach (GOV.UK CCS guidance). Duty of care under s.34 EPA 1990 is a **criminal offence** — unlimited fine, up to 2 years' imprisonment. The permit is the licence to operate. |
| **Why software hasn't solved it** | The permitted-waste-code list is not published in structured form anywhere. The public register (verified: 9,607 rows, 21 columns) has permit numbers, holders, site types and coordinates — **no EWC codes, no capacity**. Those sit inside bespoke permit PDFs and Standard Rules documents. Until LLM extraction, building that dataset was an unjustifiable data-entry project. |
| **What AI changes** | Extraction collapses from a multi-year data-entry project to weeks. **Critically: 68 Standard Rules documents cover 3,258 permits — 37% of the national market.** The *checking* itself is then deterministic set membership, which is where it belongs. |
| **Customer ROI** | Avoiding one Category 1 breach (60 CCS points) can move a site from Band A to Band E: **+50% on subsistence**, up to **+200% at Band F**. Plus avoided enforcement, avoided load rejection, and 100–300 hours a year of checking. Against £2–5k/yr, ROI is one avoided breach. |
| **Pricing** | Sites: **£150–£400/month** by site count. Producers/brokers: **£500–£2,000/month** by supplier volume. Data API: **£10–25k/yr**. |
| **Gross margin** | **85–92%.** Extraction is one-off per permit; serving is a database lookup. |
| **Target customer** | The **4,347 single-site permit holders** (measured), then the 813 holding 2–5. Buyer: owner-operator, compliance manager, or technically competent manager (WAMITAB). |
| **Market size** | 8,778 effective permits, 5,304 holders. Expands April 2027 to carriers/brokers/dealers and exempt sites — a far larger population. Serviceable revenue **£15–35m/yr**; £1m ARR ≈ **330 customers ≈ 6% of holders**. |
| **Competitive landscape** | Category **A**. See `docs/competitive-landscape.md` §1. |
| **Major incumbents** | None in conformance. 120+ Defra-approved DWT providers in *capture*; Intelex/VelocityEHS/Ecesis in enterprise EHS; EcoComply nearest in permit-obligation extraction. |
| **Incumbent weaknesses** | Capture vendors have no permit dataset and are consumed by the October deadline. EHS suites are priced and shaped for enterprises. Consultancies sample; they cannot check every load. |
| **Existing alternatives** | A laminated list at the weighbridge; consultant audits; EWC lookup tools; spreadsheets. |
| **Data required** | EA public register (verified downloadable); 68 Standard Rules documents (published); bespoke permit PDFs (public register); EWC catalogue (published); customer movement data (CSV/API). |
| **Data availability** | **Excellent.** Every input verified accessible in this research. ⚠️ Register is under the **EA Conditional Licence** — legal review needed before resale. |
| **Technical difficulty** | **Medium.** Document extraction + deterministic rules + CSV ingest. Squarely in Claude Code's range. |
| **Regulatory risk** | **Medium.** We assist compliance; we never certify it. Product must be positioned as decision support with the duty holder responsible — explicit in terms and UI. |
| **Sales difficulty** | **Medium.** Small operators, small budgets, low digital maturity. Offset by a hard deadline and criminal liability. |
| **Acquisition difficulty** | **Low–medium**, unusually. The founder has direct waste-industry access via NRS; the register gives **name, site, address and postcode for all 5,304 holders** — a complete, legally obtained prospect list. |
| **Moat** | The structured permit dataset (accumulating, expensive to replicate); switching cost once it is the audit trail of record; a corpus of real movements that improves classification; regulator-shaped workflow. |
| **Expansion** | Producers → brokers/carriers (April 2027) → Scotland/Wales/NI → WM3 classification module → permit variation advisory ("you keep rejecting X; vary your permit") → market intelligence from aggregate flows. |

---

### #2 Phase 1 contaminated land desk study automation

| | |
|---|---|
| **Current process** | A geo-environmental consultant buys a Landmark Envirocheck or Groundsure data pack, reviews historic maps, BGS geology, EA/Coal Authority records, does a walkover, and writes a 30–60 page Preliminary Risk Assessment. |
| **Labour / hours** | **1–2 consultant days**, £400–£700/day equivalent; report sells at £700–£2,500 |
| **Why it exists** | Planning conditions routinely require a Phase 1 PRA before development on brownfield land |
| **Why unsolved** | The data incumbents (Landmark, Groundsure) sell *inputs* and have no incentive to automate the deliverable that consultancies bill for. Local authorities explicitly state a search report alone does not satisfy the requirement. |
| **What AI changes** | The report is synthesis-of-documents-into-prose — the single best-fitting LLM task available. A consultant could go from 2 days to 3 hours. |
| **ROI / pricing** | Consultancy throughput up 3–4×. Price **£150–300/report** or £500–1,500/mo. |
| **Margin** | 80–88%, less the data-pack cost if we resell it |
| **Customer / market** | 500–1,000 UK geo-environmental consultancies. £1m ARR ≈ 150–200 firms. |
| **Competition** | **Category B.** No direct product; EcoScribe proves the pattern in ecology. |
| **Data** | ⚠️ **Dependency on Landmark/Groundsure** for historic maps — a data incumbent in our supply chain. |
| **Risks** | Consultancies may resist tools that reduce billable days; professional liability sits close to the output; the data dependency is a pricing lever someone else controls. |

**Why not first:** the input-data dependency on two incumbents is a structural
weakness, and the buyer is a professional services firm — exactly where the AI
startup wave is heading next.

---

### #3 WM3 waste classification assistant

| | |
|---|---|
| **Current process** | Consultant takes lab analysis, applies WM3 guidance, assesses HP1–HP15 hazard properties against concentration thresholds, assigns an EWC code, writes an assessment |
| **Labour / hours** | 2–8 hours per assessment at **£600–£1,200/day** consultant rates, plus lab costs |
| **Why it exists** | An EWC code cannot lawfully be assigned without a documented WM3 assessment; mis-classifying hazardous waste as non-hazardous is a serious offence |
| **Why unsolved** | Small, deeply technical market; consultancies have no incentive; software vendors lack the domain knowledge |
| **What AI changes** | Extraction of lab results from PDF certificates (LLM) + threshold assessment (**deterministic** — this is arithmetic against published criteria, and must never be an LLM judgement) |
| **Pricing / margin** | £50–150/assessment or £300–800/mo; 85–90% |
| **Market** | Waste producers, consultancies, labs, permitted sites. Small — likely £3–8m serviceable. |
| **Competition** | **Category A** — genuinely nothing found. Only consultancies and EWC lookup tools. |
| **Risk** | ⚠️ **Highest regulatory exposure of the three.** A wrong hazardous/non-hazardous call has legal consequences. Requires expert sign-off in the loop. |

**Why not first:** market too small to be the company, and the liability profile
demands a domain expert on the team from day one. **It is an excellent second
module for #1** — same buyer, same data, strong attach.

---

## Part 2 — Why #1 beats the alternatives

1. **A regulatory deadline is doing the selling.** DWT is mandatory for receiving
   sites from **1 October 2026** and extends to carriers, brokers and dealers in
   April 2027. Every prospect is already thinking about waste data compliance.
2. **The buyer is not where the AI startups are.** Single-site waste operators
   are unglamorous, small-budget and hard to reach — which is precisely why 22
   targeted searches found no competitor.
3. **The data barrier is real but one-sided.** Nobody has structured permitted
   waste codes. Building it is expensive-but-finite for us, and the same
   expensive-but-finite cost for anyone following — with our head start
   compounding as customer movement data accumulates.
4. **The founder has an unfair advantage.** Direct waste-industry access through
   NRS, plus a legally obtained list of all 5,304 licence holders with addresses.
   The hardest part of a compliance SaaS — the first ten customers — is the part
   already solved.
5. **It hits four of the five value tests.** Prevents expensive mistakes, reduces
   regulatory risk, saves labour, and increases capacity. If it disappeared, an
   operator would notice at the next inspection.

## Part 3 — Why this market is not already dominated

- **The data didn't exist in usable form.** The public register has no EWC codes;
  they are inside PDFs. Pre-LLM, structuring them was uneconomic.
- **There was no forcing function until now.** Off-permit acceptance was
  invisible unless an inspector found it. From October, it is a data record.
- **The 120 approved providers are running at a deadline**, building submission,
  not assurance — and Defra's own provider page confirms approval covers only
  recording and transmitting mandated fields.
- **The market looks too small to enterprise vendors and too boring to startups.**
  5,304 operators is a poor fit for Intelex and an unfashionable one for a
  venture-backed AI team. It is a very good fit for a solo founder using Claude
  Code targeting £1–10m ARR.

---

## Part 4 — The MVP

### What it does

1. **Ingest the permit.** Site enters its permit number → we look it up in the
   register (verified download) → if Standard Rules, we already hold the
   permitted waste codes from the 68 published SR documents; if bespoke, we
   extract from the permit PDF with human verification.
2. **Ingest movements.** CSV export from the weighbridge or DWT software. No
   integration required for v1 — deliberately, so we never compete with the
   capture vendor a site already uses.
3. **Check.** Deterministic set membership: every accepted EWC code against the
   permitted list, with quantity and site-type rules.
4. **Report.** A Permit Conformance Report: conforming movements, off-permit
   movements with the exact code and date, ambiguous cases needing review, and
   an estimated CCS points exposure — each linked to the permit clause it
   breaches.
5. **Watch.** Weekly re-check; alert on new off-permit acceptances; flag permit
   variations that change the permitted list.

### The wedge that gets the first conversation

**A free Permit Conformance Check.** Upload 90 days of movement data, get a
report showing exactly which loads were off-permit. For most sites this is the
first time anyone has ever checked. It costs us nothing, demonstrates value in
one screen, and is very hard to ignore weeks before a regulator gains the same
visibility.

### Architecture (reuses the design already in this repo)

The pipeline pattern in `docs/architecture.md` transfers almost unchanged:
immutable ingest → deterministic normalisation → **LLM extraction with
verbatim-quote verification** → deterministic checking → evidence-linked output.

The rules from `CLAUDE.md` apply verbatim, and matter more here:
- **No LLM arithmetic.** Conformance is set membership. CCS points are a lookup
  table. If a model is deciding whether a code is permitted, the product is
  broken.
- **Every finding cites the permit clause it came from**, with the quote.
- **Extraction is verified against source text**, and a claimed permitted code
  that cannot be quoted from the permit is rejected, not downgraded.

### What Claude Code can build (~85%)

Register ingest and refresh; SR document extraction pipeline; bespoke permit PDF
extraction; the permitted-code data model and review queue; CSV movement ingest
and normalisation; the deterministic conformance engine; CCS points calculation;
evidence-linked report generation; the Next.js app, auth and billing; the
free-check funnel; alerting; tests.

### What only you can do (~15%, and it is the part that decides the outcome)

- **Validate with three real operators** that off-permit acceptance is a
  recognised worry — before building. If they shrug, this is wrong.
- **Verify extraction accuracy** on ~50 permits against the source documents.
  Nothing else matters if the dataset is wrong.
- **The EA Conditional Licence review** — necessary before selling.
- **Domain judgement** on edge cases (mirror entries, mixed loads, mobile plant).
- **All sales.** Compliance software to owner-operators is sold by a person.
- **Recruit a WAMITAB-qualified adviser** for credibility and edge-case review.

---

## Part 5 — The commercial test

**1. Who pays?** The permit holder — an owner-operator or compliance manager at a
single-site waste transfer station, treatment facility or recycler. Later, the
waste producer's compliance function.

**2. Why?** Their permit is their licence to operate, and from October their
acceptance data goes to the regulator automatically. Fear of losing the permit
outranks any efficiency argument in this industry.

**3. How much?** £150–400/mo for sites; £500–2,000/mo for producers. A single
Band C→E move costs more than five years of subscription.

**4. What now?** A laminated list at the weighbridge, an annual consultant audit,
and hope.

**5. Why hasn't it been solved?** The permit data was never structured, there was
no forcing function, the capture vendors are busy, and the market is too small
for enterprise EHS and too boring for venture-backed AI.

**6. First version in 2–4 weeks?** Yes. 68 SR documents extracted, register
ingested, CSV upload, deterministic checker, evidence-linked PDF report. That
alone covers 37% of permitted sites with no bespoke extraction at all.

**7. First 10 customers?** (a) NRS and their network — warm intros in a sector
that runs on relationships. (b) The free Permit Conformance Check, offered
directly to a hand-picked list built from the register, which gives name, site
and postcode for all 5,304 holders. (c) The trade bodies and the WAMITAB/ESA
adviser community. (d) Consultants, as a channel — it makes their audits faster
and their findings better evidenced.

**8. What makes them refuse?** "We already know what we're permitted for."
"Nobody has ever checked." "Our DWT provider handles compliance." "I don't want
a written record of breaches I'd then have to act on" — **the most serious
objection, and it is real.** Answer: private-by-default, remediate-then-report,
and framing as risk reduction rather than self-incrimination. Also: price
sensitivity, and low digital maturity at the smallest sites.

**9. Biggest competitive threat?** A DWT capture provider adding conformance —
but they lack the permit dataset. Second: EcoComply moving from obligations to
transactions.

**10. If a major copies it?** AMCS or a large EHS vendor could. They would build
it for enterprise waste groups, where the money looks better and the 4,347
single-site operators do not. The long tail is defensible by focus and price,
and by then the dataset and the accumulated audit history are ours.

**11. Moat after 2 years?** The structured permit dataset across ~8,800 permits
including bespoke ones; a movement corpus that makes classification suggestions
progressively better; switching cost once we are the audit trail of record;
regulator-recognised report formats; and a second product (WM3) attached to the
same buyer.

**12. £1–10m ARR?** £1m is realistic — 330 sites at £250/mo, about 6% of holders.
£3–5m is credible with producer accounts and the April 2027 carrier/broker
expansion. £10m needs geographic expansion or an adjacent regulated vertical
using the same pattern. **The honest ceiling is a very good £3–5m business, not
a unicorn** — which matches the stated objective.

---

## Part 6 — 12-month roadmap

| Phase | Weeks | Deliverable | Gate |
|---|---|---|---|
| **0 — Validate** | 1–2 | 5 operator conversations. Does off-permit acceptance worry them? Would they pay? **No code.** | 3 of 5 say yes → proceed |
| **1 — Dataset** | 3–6 | Register ingest; 68 SR documents extracted and **manually verified**; permitted-code data model | ≥95% extraction accuracy on a sample |
| **2 — Checker** | 7–10 | CSV ingest, deterministic conformance engine, CCS exposure, evidence-linked report | Report is right on 3 real datasets |
| **3 — Free check** | 11–14 | Landing page + self-serve free check; run 20 manually if needed | 20 reports delivered; ≥5 want to continue |
| **4 — Product** | 15–22 | Auth, monitoring, alerting, billing, dashboard | **10 paying customers** |
| **5 — Bespoke** | 23–34 | Bespoke permit extraction at scale → all 8,778 permits | 80% national coverage |
| **6 — Producers** | 35–44 | Supplier assurance: is my disposal chain permitted for what I send? | 3 producer accounts |
| **7 — Expand** | 45–52 | WM3 module; carrier/broker readiness for April 2027; Scotland/Wales | **£250k ARR run rate** |

**Kill criteria — decided now, not later.** If Phase 0 says operators do not
worry about this, stop. If extraction accuracy cannot reach 95%, stop — a
conformance product that is wrong is worse than nothing. If fewer than 5 of 20
free checks convert to interest, the wedge is wrong; change it before Phase 4.
