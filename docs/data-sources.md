# Data Sources — Verified Register

**Verification date: 2026-09-09.** Every entry below was checked against the live
source, not assumed. Re-verify before relying on any entry older than ~6 months.

Legend for **Role**:
- **Trigger** — can originate an opportunity signal.
- **Enrichment** — adds detail to an opportunity that already exists.
- **Context** — market sizing, competitor mapping, calibration. Never a trigger.

---

## 1. EA Environmental Permitting Regulations — Waste Sites / Waste Operations Register

**Role: Enrichment + Context (NRS + competitor facility map). VERIFIED, HIGH VALUE.**

- **Access:** direct ZIP download, no key, no auth —
  `https://environment.data.gov.uk/public-register/downloads/waste-operations`
- **Format:** ZIP → `waste-operations.csv` (~875 KB compressed).
- **Verified size:** 9,607 rows; 8,778 with status `Effective`.
- **Verified columns (21):** Permit Number, Waste Management Licence No.,
  Pre-EA Permit Ref, Licence Holder Name, Trading Name, Site Name, Site Type,
  Site Address, Site Postcode, Site Grid Reference, Easting, Northing,
  Local Authority, Status, Issued/Variation/Transfer/Effective/Surrendered/
  Revoked/Suspended dates.
- **Geo quality (measured on effective permits):** Easting/Northing present on
  **100.0%** (8,775/8,778). Site Postcode missing on 7.5%. Local Authority
  missing on 7.0%.
  → **Key their geography on BNG easting/northing, never on postcode.**
- **Site Type taxonomy:** 105 distinct values, mixing bespoke `A`/`L` codes and
  Standard Rules `SR….` codes. Directly relevant subsets include
  `SR2008 No 27: Treatment of Soils and Contaminated Material` (**171 permits**),
  `A09: Hazardous Waste Transfer Station` (323), `SR2008 No 9` (95),
  `SR2012 No 15` (57), `A16a: Hazardous Waste Physical Treatment Facility` (20),
  `SR2015 No 15` (30), `A17: Physical and Chemical Treatment Facility` (117),
  `A21: Chemical Treatment Facility` (16), `A02: Other landfill taking hazardous
  waste` (22).
- **Update frequency:** quarterly (per the data.gov.uk record for
  `EPR_WasteSites_download`).
- **Licence:** ⚠️ **Environment Agency Conditional Licence — NOT Open Government
  Licence.** The bundled `PRO-waste-operations-licence-information.txt` states
  you must check the conditions and that, if they are unsuitable, "this
  information is not provided with a licence for use, and the data is provided
  for read right only." **Legal review required before this feeds a commercial
  product sold to third parties.** See §Licensing risk.
- **Limitations:** does **not** contain permitted EWC codes, permitted tonnage,
  or capacity. Site Type is a coarse primary classification only.

### 🚩 Critical finding — NRS cannot be identified reliably from this register

Searching the register for NRS returns **four separate legal entities under three
different spellings**:

| Licence holder (verbatim) | Site | Postcode | Site Type |
|---|---|---|---|
| `N R S WASTE CARE LIMITED` | Meriden Quarry | CV7 7LG | A25 Deposit for recovery |
| `N R S WASTE CARE LIMITED` | Freshwater Pond Restoration Site | CV7 7LG | A25 Deposit for recovery |
| `N. R. S. WASTE MANAGEMENT SERVICES LIMITED` | Meriden Quarry Landfill Area G | CV7 7JT | L05 Inert landfill |
| `N. R. S. WASTE MANAGEMENT SERVICES LIMITED` | Meriden Quarry Area G | CV7 7JS | A30 Mining waste |
| `NRS Environmental Services Ltd` | Cornets End Recycling Facility | CV7 7LH | A20 Metal Recycling Site |
| `NRS BROMSGROVE AGGREGATES LIMITED` | Sandy Lane Quarry | B61 0QT | A16 Non-haz physical treatment |

Two consequences, both load-bearing for the design:

1. **Entity resolution is a first-class problem, not a nice-to-have.** If NRS's
   own name is inconsistent across four entities, contractor and developer names
   in planning data will be far worse.
2. **None of these permits is a hazardous site type**, yet NRS publicly describes
   operating "one of the largest hazardous treatment centres for construction
   waste in the UK", treating hydrocarbons, heavy metals, chlorinated solvents,
   PAHs/coal tar and asbestos-impacted soils. The public register therefore
   **cannot** be used to derive NRS capability. Either the hazardous permit sits
   under an entity name we cannot match, or Site Type understates the permit.
   → **NRS capability must be human-entered and confirmed.** See
   `docs/opportunity-model.md` §Capability. This must be resolved in the NRS
   discovery session.

---

## 2. EA Waste Data Interrogator (WDI)

**Role: Context only. NOT a trigger.**

- **Access:** data.gov.uk / environment.data.gov.uk, annual dataset records.
- **Format:** three ZIPs — Excel extracts of waste *received* and waste
  *removed*, plus ODS summary tables. **MS Access is no longer published.**
- **Coverage:** ~6,000 regulated sites, England.
- **Update frequency & lag:** annual, with a **9–21 month lag**. The 2024
  dataset was first published September 2025; v2 in May 2026.
- **Licence:** ⚠️ **EA Conditional Licence, and the record states "The period of
  permitted use is one year."** This is a hard blocker for embedding WDI in a
  commercial multi-operator product without a negotiated licence.
- **Why it is not a trigger:** by the time waste appears in WDI, the job is done
  and paid for. Its value is (a) sizing the addressable market by geography and
  waste class, (b) mapping which competitors actually receive which streams —
  the basis for "which customers appear to be sending relevant waste to
  competitors" — and (c) calibrating our tonnage model against reality.

---

## 3. EA Hazardous Waste Data Interrogator (HWDI)

**Role: Context only. CANNOT be a trigger.**

- **Access:** data.gov.uk, annual dataset records (2024 published).
- **Licence:** Open Government Licence v3.0 (more permissive than WDI).
- **Coverage:** England (movements EA is required to monitor).
- ⚠️ **Blocking limitation, quoted from GOV.UK guidance:** *"Hazardous waste
  producer data is commercially confidential. We have not included individual
  site names and producers' details."* Only high-level waste classification,
  geographic areas and tonnage are included.
- **Consequence:** despite being the most obviously on-topic dataset in the whole
  landscape, **HWDI cannot generate a single named lead.** Anyone who assumed it
  would has mis-scoped the product. Use it for hazardous flow volumes by area and
  EWC class, and for competitor share estimation — nothing more.

---

## 4. Planning applications

**Role: PRIMARY TRIGGER. Also the single largest technical risk.**

### 4a. planning.data.gov.uk (official)
- ⚠️ **Not usable as the primary feed.** The `planning-application` dataset is
  explicitly marked incomplete and "not yet ready for use" — approximately
  100,627 applications from **6 data providers** as of the last collector run.
  England has ~330 LPAs. Coverage is nowhere near national.
- Still useful for *other* datasets it does serve well (brownfield land
  registers, conservation areas, boundaries) as geospatial context.

### 4b. PlanIt (`planit.org.uk`) — recommended MVP feed
- **Access:** free JSON/GeoJSON/CSV/TSV API. `/api/applics/{fmt}` for
  applications, `/api/areas/{fmt}` for authorities.
- **Coverage:** England, Scotland, Wales and NI. Authorities are flagged
  `active` / `inactive` / `stale`, where **stale = the scraper has not been able
  to reach that authority for six weeks**. Coverage is therefore uneven and
  self-reported — we must ingest and monitor the area status, not assume it.
- **Limits:** rate limited (HTTP 429); hard caps of **5,000 results and 1,000 KB
  per request**, and requests are killed at 45 seconds. Pagination and per-LPA
  partitioning are mandatory.
- **Licence:** not clearly stated on the API page beyond an acknowledgements
  reference; it is a free, donation-supported service. ⚠️ **Confirm terms and
  attribution requirements in writing before commercial use.**
- **Risk:** a free third-party service is a single point of failure for our
  primary trigger. Mitigate by (a) storing everything we fetch, so we accumulate
  our own history, (b) designing the ingest adapter interface so a paid
  provider or direct LPA scraping can be swapped in per-LPA.

### 4c. Direct LPA portals (Idox/Northgate etc.)
- Needed for the highest-value signal PlanIt does not reliably carry: **document
  lists and condition-discharge applications**.
- ⚠️ Scraping raises terms-of-use, rate-limiting and blocking risk. Do this only
  for a small, named set of priority LPAs in the catchment, politely and
  cached — and take a view on ToS per authority.

### 4d. Commercial (Barbour ABI, Glenigan, Searchland, Landmark)
- Treat as **paid inputs to evaluate at Phase 2**, not competitors. Barbour ABI
  in particular gives contractor/contact relationships and project stage that
  public planning data does not. The strategic question is whether we license it
  as an input rather than rebuild it.

---

## 5. Companies House

**Role: Enrichment. VERIFIED, reliable.**

- **Access:** free REST API, free API key, no cost tier.
- **Rate limit:** **600 requests per 5 minutes** (~2/sec), HTTP 429 on breach,
  rolling 5-minute reset. Elevated limits available free on request,
  case-by-case — **apply early**, our entity-resolution workload will need it.
- **Data:** company search and profile, officers, appointments, disqualifications,
  filing history, insolvency, charges, PSC.
- **Use:** canonical key for entity resolution (company number), corporate group
  structure, officer names as a starting point for decision-makers, and financial
  health / insolvency as a risk signal on a counterparty.
- **Limitation:** officers are statutory directors, **not** commercial
  decision-makers. It will not tell you who buys waste services. Do not
  over-promise "decision maker identified" on the strength of Companies House
  alone.

---

## 6. Public procurement — Find a Tender (FTS) and Contracts Finder

**Role: Secondary trigger. Good value, low effort.**

- **Access:** both publish **OCDS** APIs, no API key required.
  - FTS: `find-tender.service.gov.uk/apidocumentation/1.0/GET-ocdsRecordPackages`
  - Contracts Finder: `contractsfinder.service.gov.uk/apidocumentation/...`
- FTS became the central platform under the Procurement Act 2023 (enhanced
  service live 24 Feb 2025); it replaced OJEU/TED for UK high-value notices from
  1 Jan 2021.
- **Fields:** buyer, supplier, award, tender and planning notices, value, dates,
  CPV codes.
- **Why it matters:** public-sector remediation, demolition and land
  regeneration frequently appear here *before* or *alongside* planning, with a
  contract value attached — which is a far better revenue anchor than our own
  tonnage model. CPV codes for demolition/site preparation/remediation give a
  clean deterministic filter.
- **Limitation:** public sector only. Misses private developer work entirely.

---

## 7. Waste Carriers, Brokers and Dealers register

**Role: Enrichment.**

- Searchable public register with CSV export of results; a full-register
  download route exists via the same public-register download service as §1.
- **Use:** confirm a contractor is a registered carrier; identify which
  contractors operate in a geography; support entity resolution.
- **Not verified in this pass to the same depth as §1** — confirm the exact
  download URL, columns and licence before building against it.

---

## 8. Other sources to investigate (not yet verified)

| Source | Expected role | Why |
|---|---|---|
| Historic land use / former industrial sites (OS, NLUD, Landmark, historic maps) | Trigger multiplier | Best predictor of contamination *before* anyone declares it — gasworks, tanneries, foundries, historic landfill |
| EA historic landfill + permitted landfill boundaries | Trigger multiplier | Development on or adjacent to historic landfill implies gas/leachate/contaminated arisings |
| Brownfield Land Registers (planning.data.gov.uk, per-LPA) | Trigger | Statutory register of brownfield sites suitable for housing — contamination-rich by definition |
| EA water quality / pollution incident data | Context | Known hydrocarbon/heavy-metal hotspots |
| BGS borehole and geology records | Enrichment | Ground conditions inform excavation depth and volume bands |
| Ordnance Survey / ONS postcode + boundary data | Infrastructure | Geocoding, catchment definition |
| National Highways / Network Rail / utility programmes | Trigger | Large infrastructure earthworks |
| Local authority regeneration and Local Plan allocations | Trigger, long lead | Multi-year pipeline visibility |
| Companies House Streaming API | Efficiency | Push updates instead of polling |

---

## Licensing risk — summary

This is a genuine commercial constraint, not a formality:

| Source | Licence | Commercial redistribution |
|---|---|---|
| EA Waste Sites register | **EA Conditional Licence** | ⚠️ Requires review |
| EA Waste Data Interrogator | **EA Conditional Licence, 1-year permitted use** | ⚠️ Blocker as-is |
| EA Hazardous Waste Interrogator | OGL v3.0 | ✅ Permitted with attribution |
| Companies House API | Free public service, OGL-style | ✅ Permitted with attribution |
| FTS / Contracts Finder | OGL v3.0 | ✅ Permitted with attribution |
| PlanIt | Unclear — free service | ⚠️ Must confirm in writing |

**Implication for the long-term product vision:** the sources most specific to
waste are the most restrictively licensed. An internal NRS tool is
straightforward. Reselling the same intelligence to other operators is not, and
needs a licensing conversation with the EA and PlanIt before that business case
is committed to. Flag this to the commercial sponsor now, not in month six.
