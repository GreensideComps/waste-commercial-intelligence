# The Ten Leads Test — Results

**Run 2026-09-09. Catchment: 110 km of Meriden. Public sources only.**
Method, pool and filtering: `docs/ten-leads-candidates.md`.
Collective analysis and decision: `docs/ten-leads-analysis.md`.

## Evidence labelling

- **FACT** — retrieved from a primary or named source, quoted or citable.
- **INFERENCE** — reasoned from a fact, stated as reasoning.
- **ESTIMATE** — a number I have derived; assumptions stated.
- **HYPOTHESIS** — untested belief, including every "NRS awareness" score.

⚠️ **On tonnage:** no record in the 442-candidate pool contains site area,
depth, volume or tonnage. **I have not estimated tonnage for any lead.** Where
the brief asks for it, the honest answer is "not derivable from the sources
used" — see `docs/ten-leads-candidates.md` §4, Finding 3. Any tonnage figure I
produced here would be fabricated, which the brief forbids.

⚠️ **On NRS awareness:** I have no access to NRS's knowledge. Every awareness
score is a **HYPOTHESIS to be tested by the experiment in
`docs/next-validation-experiment.md`**. That is the entire point of this test.

---

## LEAD 1 — EKFB JV / HS2 C23: Waste Management Services ⭐ STRONGEST

**1. Opportunity**
- **FACT** Buyer: Eiffage Kier Ferrovial BAM (EKFB) JV, HS2 Main Works Civils, Lots C2 & C3.
- **FACT** Title: "EKFB JV — Waste Management Services". Published **2026-08-26**.
- **FACT** Value stated: **£1,000,000**.
- **FACT** Description: *"Eiffage Kier Ferrovial BAM (EKFB) JV is seeking expressions of interest from interested parties for Waste Management Services to support the delivery of the C23 project, which forms part of the HS2 Main Works Civils Contracts."*
- **FACT** C23 covers an **80 km section between the Chiltern Tunnel and Long Itchington Wood**; delivery areas include North Chilterns to Aylesbury (NC2A) and Calvert to Greatworth (C2G).
- **INFERENCE** Long Itchington Wood is in Warwickshire, ~25 km from Meriden. The northern end of C23 sits inside NRS's catchment.
- Status: **live expression-of-interest**, two weeks old at time of research.

**2. Waste opportunity**
- **INFERENCE** Major rail civils: excavated arisings, contaminated ground from historic land uses along route, demolition arisings, general C&D, hazardous fractions from tunnelling/utilities.
- **FACT (separate notice, same buyer)** "EKFB JV — Daywork Hire of 8 Wheel Tipper Wagons", £1,000,000, published 2026-07-22 — *"the supply of 8 wheel tipper wagons to support the delivery of our C23 HS2 project"*. **INFERENCE** muckaway haulage demand is live and explicit.
- **Tonnage: NOT ESTIMATED.** The notice states contract value, not volumes.
- Classification: **INFERENCE** predominantly non-hazardous/inert with hazardous fractions.

**3. Commercial chain**
- **FACT** Client: HS2 Ltd. Principal contractor: **EKFB JV** (Eiffage, Kier, Ferrovial Construction, BAM Nuttall).
- **FACT** Route in: register on **CompeteFor**, or Constructionline using code **HS2EK**.
- **INFERENCE** EKFB's procurement function controls this contract directly — unusually, the buyer is named and is *asking*.

**4. Evidence**
- Contracts Finder OCDS API, notices retrieved 2026-09-09: `https://www.contractsfinder.service.gov.uk/`
- [EKFB supply chain / CompeteFor](https://www.competefor.com/ekfb/) · [Constructionline EKFB partnership](https://www.constructionline.co.uk/buyers/partnership/ekfb/)
- Chain: *public tender notice → named principal contractor → explicit waste management requirement → stated £1m value → named registration route.*

**5. Why NRS might care** — Tipper haulage, muckaway, inert/C&D handling, and hazardous fractions all map to NRS's stated capabilities. Long Itchington Wood end is within economic haul of Meriden.

**6. Discovery difficulty: 4/10** — public and indexed, but requires monitoring Contracts Finder daily; HS2 notices are watched by large contractors, less so by regional waste SMEs.

**7. Likely existing awareness: 4/10 (HYPOTHESIS)** — HS2 is famous; this *specific two-week-old notice* may not have been seen. Being aware of HS2 ≠ knowing an EOI is open now.

**8. Commercial action** — *"Register NRS on CompeteFor and on Constructionline under code HS2EK this week, then contact EKFB procurement referencing the Waste Management Services EOI published 26 August 2026 for the C23 project, and separately the 8-wheel tipper daywork notice of 22 July 2026."*

**9. Scores** — Evidence 10 · Waste certainty 9 · Commercial value 8 · Timing 9 · NRS fit 8 · Discovery 4 · NRS-doesn't-know 4 · **Overall 7.4**

---

## LEAD 2 — Rolls-Royce Sinfin A Site, Victory Road, Derby

**1.** **FACT** Derby CC refs **26/00898/DISC** — *"Discharge of condition nos 3 (Construction Environmental Management Plan) and 4 (Remediation Strategy) of previously approved permission 26/00060/FUL — Remediation w[orks]"*; and **26/00920/DISC** — condition 4 (Contaminated Land) of **25/01884/FUL** (new manufacturing services building). **FACT** Agent on both: **AECOM**. Status **Undecided**. 52.3 km. **FACT** A related **25/01586/EIA** exists for the Sinfin A site.

**2.** **INFERENCE** Aero-engine manufacturing since the 1900s implies hydrocarbons, chlorinated solvents, heavy metals, cutting oils, possible asbestos in demolition. **FACT** The parent permission is *for remediation itself* — the strongest possible confirmation that contaminated material will be excavated. **Tonnage: NOT ESTIMATED.** Classification: **INFERENCE** hazardous fraction likely.

**3.** Client **Rolls-Royce plc**; consultant **AECOM (FACT — named as agent)**. **INFERENCE** AECOM will specify the remediation strategy and materially influence disposal routing; the earthworks/remediation contractor appears not yet named publicly.

**4.** PlanIt records retrieved 2026-09-09; LPA: `https://eplanning.derby.gov.uk/online-applications/` (⚠️ returned HTTP 503 on direct fetch — record verified via PlanIt, **not** the LPA portal). Chain: *dedicated remediation consent → remediation strategy under discharge → named consultant → contractor not yet appointed.*

**5.** Hazardous/hydrocarbon/heavy-metal soils, soil washing, specialist treatment — NRS's stated core.

**6. Discovery difficulty: 9/10** — **FACT: a general web search could not locate application 26/00060/FUL**, returning "may be a very recent 2026 application that might not yet be widely indexed online". PlanIt returned it immediately.

**7. Likely existing awareness: 7/10 (HYPOTHESIS)** — Rolls-Royce Derby is a household name and majors will court it, but *this specific remediation consent* is obscure and recent.

**8. Commercial action** — *"Contact AECOM's Derby geo-environmental team as consultant on Derby applications 26/00898/DISC and 26/00920/DISC (Sinfin A, Victory Road), submitted 2026, to register NRS as a treatment outlet before the remediation contractor is appointed."*

**9.** Evidence 8 · Waste certainty 9 · Value 7 · Timing 8 · Fit 9 · Discovery 9 · Doesn't-know 7 · **Overall 8.1**

---

## LEAD 3 — Rolls-Royce Sinfin D Site, Wilmore Road, Derby

**1.** **FACT** Ref **26/01101/DISC**: *"Discharge of conditions 3 (Ground Gas), 4 (Remediation Scheme), 5 (Construction Environmental Management Plan), 6 (Verification Report) and 7 (Remediation)"*. Status Undecided. Agent recorded as "Frank Shaw". 51.7 km. **FACT** Site has prior applications 23/01759/FUL, 24/00386/FUL (modular office extension), 24/01017/DISC.

**2.** **INFERENCE** Ground gas conditions indicate made ground or historic fill. Combined remediation + verification conditions indicate a live remediation programme. **Tonnage: NOT ESTIMATED.**

**3.** Rolls-Royce plc. **INFERENCE** contractor unnamed in public record.

**4.** PlanIt record retrieved 2026-09-09. Chain: *ground gas + remediation conditions → active remediation → operational industrial site.*

**5.** Ground gas and made ground → excavation and offsite treatment; hydrocarbon-impacted soils.

**6. Discovery: 8/10.** **7. Awareness: 6/10 (HYPOTHESIS).**

**8. Action** — *"Contact the Rolls-Royce Derby facilities/estates team referencing discharge application 26/01101/DISC to establish who is delivering the remediation scheme and when arisings begin."*

**9.** Evidence 8 · Waste 8 · Value 6 · Timing 8 · Fit 9 · Discovery 8 · Doesn't-know 6 · **Overall 7.6**

---

## LEAD 4 — Friar Gate Goods Yard, Derby

**1.** **FACT** Ref **26/00755/DISC**, size **Large**, Undecided: *"Discharge of condition 11 (Contaminated Land) of previously approved permission 23/01102/FUL — Restoration and Change of Use of the Bonded Warehouse"*. **FACT** Developer **Wavensmere Homes**; **£75m**; 11.5 acres; 276 homes + 110,000 sq ft commercial. **FACT** *"Following historic tipping to raise site levels in the 1880's, the site was formerly used as a railway bonded warehouse with a rail yard, sidings and locomotive sheds"* — Great Northern Railway goods depot handling **coal**, livestock, timber, metals. **FACT** Groundworks commenced November 2024; completion anticipated end 2028. 55.1 km.

**2.** **INFERENCE** Historic tipping + railway coal handling → coal tar, PAH, hydrocarbons, heavy metals, ash; asbestos likely in 1870s listed-building refurbishment. **Tonnage: NOT ESTIMATED** (11.5 acres is site area, not excavation volume). **INFERENCE** hazardous fraction probable.

**3.** Developer **Wavensmere Homes (FACT)**; architect Glancy Nicholls (FACT). **INFERENCE** groundworks contractor already appointed given works began Nov 2024 — **this is a strike against the lead**.

**4.** [Wavensmere](https://www.wavensmere.co.uk/news/wavensmere-homes-starts-work-at-75m-friar-gate-goods-yard-in-derby-city-centre/) · [Derbyshire Times](https://www.derbyshiretimes.co.uk/lifestyle/homes-and-gardens/wavensmere-homes-starts-work-at-ps75m-friar-gate-goods-yard-in-derby-city-centre-4824047) · [Derby CC contaminated land doc 23/01102/FUL](https://docs.derby.gov.uk/padocumentserver/DownloadDocument.aspx?docid=201447032)

**5.** Coal tar / PAH / gasworks-type material is explicitly within NRS's stated treatment range.

**6. Discovery: 2/10** — £75m scheme with extensive press. **7. Awareness: 2/10 (HYPOTHESIS)** — almost certainly known.

**8. Action** — *"Contact Wavensmere Homes' project team about the Bonded Warehouse phase (condition 11 discharge, ref 26/00755/DISC, live September 2026) — later phases may still be uncontracted even though enabling works began in November 2024."*

**9.** Evidence 9 · Waste 8 · Value 8 · Timing 5 · Fit 9 · Discovery 2 · Doesn't-know 2 · **Overall 6.1**

---

## LEAD 5 — Land north of Occupation Lane, Woodville, Swadlincote

**1.** **FACT** Ref **DMOT/2026/0939** (South Derbyshire), size **Large**, Undecided: *"Approval of details reserved by condition 8 (contamination), 9 (ground investigation), 14 (site levels), 18 (trees and hedgerows) and 26 (odour assessment)"*. 37.4 km.

**2.** **FACT** The Woodville Regeneration Area is ~35 hectares; *"once the industrial heart of the Swadlincote urban area and home to numerous ceramics factories"*; phase one link road was built across a **former open cast site**, and during that work *"unsuitable material, tyres and other controlled waste had to be removed"*. **INFERENCE** Former opencast + ceramics + an **odour assessment condition** together strongly suggest made ground and possibly landfill gas. **Tonnage: NOT ESTIMATED**, though "site levels" + Large scale imply substantial earthworks. Classification **INFERENCE** mixed inert/non-hazardous with hazardous possible.

**3.** ⚠️ **Applicant and agent not identified in the public record retrieved** — a real weakness. **INFERENCE** buyer would be the housebuilder's groundworks contractor.

**4.** PlanIt record 2026-09-09 · [Destination South Derbyshire — Woodville Regeneration Area](https://www.destinationsouthderbyshire.co.uk/invest/woodville-regeneration-area/) · [South Derbyshire case study on managing environmental impact](https://www.southderbyshire.gov.uk/assets/attach/2543/case-study-2-managing-the-environmental-impact-of-development.pdf)

**5.** Large-volume made ground, site levelling, possible gas-impacted material.

**6. Discovery: 7/10.** **7. Awareness: 5/10 (HYPOTHESIS)** — Woodville regeneration is locally known; this specific live discharge less so.

**8. Action** — *"Obtain the applicant name for South Derbyshire ref DMOT/2026/0939 from the planning portal, then contact them regarding the condition 8/9 contamination and ground investigation details currently under determination."* ⚠️ Note this action begins with a research step because the counterparty is not in the public feed.

**9.** Evidence 7 · Waste 7 · Value 7 · Timing 8 · Fit 8 · Discovery 7 · Doesn't-know 5 · **Overall 7.0**

---

## LEAD 6 — Alpha Anodizing & Polishing Ltd, Bond End, Yoxall

**1.** **FACT** Ref **P/2026/00884** (East Staffordshire), Undecided: *"Discharge of Condition number 9d (remediation works) and 9e (verification report) of planning permission allowed on appeal APP/B3410/W/23/3332984 relating to demolit[ion]"*. **FACT** Site: Alpha Anodizing and Polishing Ltd, Bond End Works, Yoxall DE13 8NL. **FACT** Company number **06979528** (Companies House). 37.5 km.

**2.** **INFERENCE — the core of this lead.** Anodising and metal polishing uses sulphuric/chromic acid baths, caustic etch, and generates heavy-metal-bearing sludges. A remediation condition on a former anodising works implies **heavy metals (chromium, nickel, aluminium), acids and possible cyanide-bearing residues** in soils. **INFERENCE** demolition of an industrial works of this age → likely ACM. **Tonnage: NOT ESTIMATED** — small site, so volume is probably modest but the *hazard classification* is likely high-value per tonne.

**3.** **FACT** Site occupier/owner Alpha Anodizing & Polishing Ltd. **INFERENCE** the permission was won on appeal, suggesting a developer purchaser for housing. ⚠️ Developer not identified in the public record.

**4.** PlanIt record 2026-09-09 · [Companies House 06979528](https://find-and-update.company-information.service.gov.uk/company/06979528/officers) · appeal ref APP/B3410/W/23/3332984 (Planning Inspectorate). Chain: *industrial occupier → demolition consent won on appeal → remediation works condition live → heavy-metal soils inferred from process type.*

**5.** **This is the archetype of NRS's stated specialism**: heavy-metal contaminated soil requiring specialist treatment, not landfill. High £/tonne.

**6. Discovery: 10/10** — **FACT** targeted web searching returned only company directory listings and *could not surface the appeal or the remediation condition*. This is invisible without systematic planning monitoring.

**7. Likely existing awareness: 9/10 (HYPOTHESIS)** — a small anodising works in a Staffordshire village generates no press. Strongest candidate for "NRS did not know".

**8. Action** — *"Contact Alpha Anodizing & Polishing Ltd (Companies House 06979528) and the agent on East Staffordshire ref P/2026/00884 to offer heavy-metal contaminated soil treatment ahead of the condition 9d remediation works, which are currently under determination."*

**9.** Evidence 7 · Waste 8 · Value 5 · Timing 8 · Fit 9 · Discovery 10 · Doesn't-know 9 · **Overall 8.0**

---

## LEAD 7 — Mell Square / Holbeche Place, Solihull [deliberate control]

**1.** **FACT** Ref **PL/2026/01052/DIS**: *"Discharge condition No. 7 (Land Contamination (Full — Phase 1)"*, agent **Turley**. 9.1 km. **FACT** Developer **Muse** (Morgan Sindall-owned), appointed preferred bidder Oct 2023; approved 6 Feb 2026; up to **1,600 homes**; renamed **Holbeche Place**. **FACT** **GRAHAM** appointed to deliver phase one — 346 build-to-rent homes across four buildings. **FACT** *"Demolition and enabling works are expected to start in summer 2026."*

**2.** **INFERENCE** Town-centre demolition of 1960s retail → substantial C&D arisings, likely ACM in buildings of that era, made ground beneath. **Tonnage: NOT ESTIMATED.**

**3.** **FACT** Developer Muse; phase 1 contractor **GRAHAM**; planning agent Turley; landowner Solihull MBC. **INFERENCE** GRAHAM controls the phase 1 waste contract.

**4.** [Construction Enquirer — GRAHAM appointment](https://www.constructionenquirer.com/2026/04/28/graham-to-deliver-first-phase-of-solihull-town-centre-revamp/) · [Construction Enquirer — Muse go-ahead](https://www.constructionenquirer.com/2026/02/10/muse-go-ahead-for-1600-home-solihull-town-centre-reset/) · [Solihull MBC Mell Square masterplan](https://www.solihull.gov.uk/about-council/mell-square-masterplan)

**5.** Demolition arisings and ACM, 9 km from Meriden — excellent haul economics.

**6. Discovery: 1/10.** **7. Awareness: 1/10 (HYPOTHESIS)** — **included precisely to calibrate the test.** If NRS says they did not know about this, the whole exercise is unreliable.

**8. Action** — *"Contact GRAHAM's Midlands pre-construction team regarding demolition and enabling works at Holbeche Place (Mell Square), starting summer 2026."*

**9.** Evidence 10 · Waste 8 · Value 9 · Timing 8 · Fit 8 · Discovery 1 · Doesn't-know 1 · **Overall 6.4**

---

## LEAD 8 — Jaguar Land Rover, Lode Lane, Solihull

**1.** **FACT** Ref **PL/2026/01382/DIS**, Undecided: *"Discharge of condition 4 (Contaminated Land parts 1 and 2) planning approval PL/2025/01396/PPFL dated 09.04.2026 for Demolition of 1 No. single storey [building]"*. **8.8 km — the closest lead.**

**2.** **INFERENCE** Automotive manufacturing since the 1940s → hydrocarbons, solvents, metals; demolition of a mid-century industrial building → probable ACM. **Tonnage: NOT ESTIMATED** — the description says a *single* single-storey building, so volume is likely modest.

**3.** **FACT** Occupier Jaguar Land Rover. ⚠️ Contractor not named.

**4.** PlanIt record 2026-09-09; Solihull MBC portal.

**5.** Closest lead to Meriden; JLR is a strategically valuable account beyond this single job.

**6. Discovery: 6/10** — JLR is obvious as a *company*; this specific small demolition consent is not. **7. Awareness: 4/10 (HYPOTHESIS)** — NRS likely already knows JLR; may not know this job.

**8. Action** — *"Contact JLR Lode Lane facilities/estates referencing discharge PL/2026/01382/DIS to be considered for the demolition arisings and contaminated land works under approval PL/2025/01396/PPFL (dated 09.04.2026)."*

**9.** Evidence 8 · Waste 7 · Value 4 · Timing 7 · Fit 8 · Discovery 6 · Doesn't-know 4 · **Overall 6.3**

---

## LEAD 9 — Former Hermitage Mill, Hermitage Lane, Mansfield

**1.** **FACT** Ref **2026/0327/CON**, size Medium, Undecided: *"DISCHARGE OF CONDITIONS 4 (ENVIRONMENTAL MANAGEMENT PLAN), 5 (CONSTRUCTION AND ENVIRONMENTAL MANAGEMENT PLAN), 7 (REMEDIATION STRATEGY), 9 (GROUNDWATER RESOURCES)"*. Agent **Jackson Design Associates**. 82.7 km.

**2.** **INFERENCE** A former mill with a **groundwater resources** condition alongside a remediation strategy indicates a controlled-waters risk — usually solvent or hydrocarbon impact. **Tonnage: NOT ESTIMATED.**

**3.** **FACT** Agent Jackson Design Associates. ⚠️ Developer and contractor not identified.

**4.** PlanIt record 2026-09-09; Mansfield DC portal.

**5.** Groundwater-risk sites usually require treatment rather than landfill.

**6. Discovery: 8/10.** **7. Awareness: 7/10 (HYPOTHESIS).** ⚠️ **82.7 km may be beyond economic haul — unknown until NRS confirms its radius** (see `docs/risks.md` §3).

**8. Action** — *"Contact Jackson Design Associates as agent on Mansfield ref 2026/0327/CON to establish the remediation strategy timetable for Hermitage Mill — subject to confirming Mansfield is inside NRS's haul radius."*

**9.** Evidence 7 · Waste 7 · Value 5 · Timing 7 · Fit 7 · Discovery 8 · Doesn't-know 7 · **Overall 6.9**

---

## LEAD 10 — Site 26 Egghill, Berry Hill Industrial Estate, Droitwich Spa

**1.** **FACT** Ref **W/26/01517/CCO** (Wychavon), Undecided: *"Discharge of conditions 3 (Site access), 4 (Contaminated land), 5 (CEMP: Biodiversity), 6 (Drainage design), 7 (Onsite drainage), 8 (Infiltration testing), 9 (Surface water manage[ment])"*. 38.9 km.

**2.** **INFERENCE** New development on an established industrial estate; a contaminated land condition plus infiltration testing implies ground contamination assessment before construction. **Tonnage: NOT ESTIMATED.** ⚠️ **Waste certainty is the weakest of the ten** — a contaminated land condition can be discharged with no excavation at all.

**3.** ⚠️ Applicant and agent not identified in the retrieved record.

**4.** PlanIt record 2026-09-09; Wychavon portal `https://plan.wychavon.gov.uk/Planning/Display/W/26/01517/CCO`.

**5.** Industrial estate development within comfortable haul of both Meriden and Bromsgrove.

**6. Discovery: 8/10.** **7. Awareness: 7/10 (HYPOTHESIS).**

**8. Action** — *"Retrieve the applicant for Wychavon ref W/26/01517/CCO from the portal and contact them regarding condition 4 (contaminated land) currently under determination, to establish whether excavation and offsite disposal is required."* ⚠️ Weakest action of the ten — begins with a qualification step.

**9.** Evidence 6 · Waste 4 · Value 4 · Timing 7 · Fit 6 · Discovery 8 · Doesn't-know 7 · **Overall 5.7**

---

## Summary table

| # | Lead | Dist | Disc. | Awareness | Overall |
|---|---|---|---|---|---|
| 2 | Rolls-Royce Sinfin A, Derby | 52 km | 9 | 7 | **8.1** |
| 6 | Alpha Anodizing, Yoxall | 38 km | **10** | **9** | **8.0** |
| 3 | Rolls-Royce Sinfin D, Derby | 52 km | 8 | 6 | 7.6 |
| 1 | EKFB / HS2 C23 tender | ~25 km+ | 4 | 4 | 7.4 |
| 5 | Occupation Lane, Woodville | 37 km | 7 | 5 | 7.0 |
| 9 | Hermitage Mill, Mansfield | 83 km | 8 | 7 | 6.9 |
| 7 | Mell Square, Solihull *(control)* | 9 km | 1 | 1 | 6.4 |
| 8 | JLR Lode Lane, Solihull | 9 km | 6 | 4 | 6.3 |
| 4 | Friar Gate Goods Yard, Derby | 55 km | 2 | 2 | 6.1 |
| 10 | Egghill, Droitwich | 39 km | 8 | 7 | 5.7 |

**Mean overall 6.95. Mean discovery difficulty 6.4. Mean "NRS doesn't know" 5.2.**
