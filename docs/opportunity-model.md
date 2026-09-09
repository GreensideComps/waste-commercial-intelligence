# Opportunity & Data Model

High-level design. Column lists are indicative, not a migration.

## 1. The chain

```
raw_document → source_record → site / organisation
                     ↓
                  signal  ("something happened")
                     ↓
              waste_arising  ("this material will arise")
                     ↓
               opportunity  ("NRS should care, this much, this soon")
                     ↓
           recommended_action → outcome → calibration
```

Each arrow is a distinct, separately testable transformation. Every derived
object references the objects it came from. Nothing is created without a parent.

## 2. Layers

### 2.1 Ingest — immutable

**`raw_document`** — never updated, never deleted.
`id, source_id, source_url, retrieved_at, content_type, content, content_hash,
http_status, fetch_run_id`

Re-fetching the same URL writes a **new row**. Comparing consecutive
`content_hash` values for a URL is how we detect change, which is itself one of
the most valuable signals we have (a planning application's status changing, a
new document appearing on a case).

**`fetch_run`** — `id, source_id, started_at, finished_at, status, stats jsonb,
error` — so any claim can be traced to the exact run that produced it.

### 2.2 Normalise

**`source_record`** — one canonical row per real-world record.
`id, operator_id, source_id, external_ref, record_type, first_seen_at,
last_seen_at, superseded_by, payload jsonb, raw_document_id`

`record_type` ∈ `planning_application`, `planning_condition_discharge`,
`permit`, `company`, `tender_notice`, `contract_award`, `carrier_registration`.

`payload` keeps the source's own shape; typed columns are added only for fields
we actually query. Resist the urge to fully model every source up front — sources
change and most fields are never used.

### 2.3 Resolve

**`site`** — a physical location.
`id, operator_id, name, address, postcode, easting, northing, geom (PostGIS),
uprn, local_authority, historic_land_use_classes[], confidence`

**`organisation`** — a legal entity.
`id, operator_id, name, companies_house_number, status, sic_codes[],
role_tags[] (developer|contractor|demolition|remediation|consultant|carrier|
competitor), incorporated_on, insolvency_flag`

**`organisation_alias`** — `organisation_id, alias, source_id, match_method,
match_confidence, confirmed_by, confirmed_at`

> **Why aliases are load-bearing:** the EA register alone lists NRS as
> `N R S WASTE CARE LIMITED`, `N. R. S. WASTE MANAGEMENT SERVICES LIMITED`,
> `NRS Environmental Services Ltd` and `NRS BROMSGROVE AGGREGATES LIMITED` —
> four entities, three spellings, one group. If our own operator's name is this
> inconsistent, third-party names will be worse. Entity resolution is a core
> component with a **human review queue**, not a string comparison.

Resolution order: exact Companies House number → exact normalised name →
trigram similarity above threshold → **human queue**. Never auto-merge below
threshold; a wrong merge silently corrupts every downstream conclusion.

**`person`** — `id, organisation_id, name, role_title, source, confidence`.
Deliberately thin. Companies House gives statutory directors, who are usually
*not* the person who buys waste services — see `docs/data-sources.md` §5. Do not
over-promise "decision maker identified".

### 2.4 Detect

**`signal`** — a typed, evidenced observation that something commercially
relevant happened.
`id, operator_id, signal_type, site_id, source_record_id, occurred_at,
detected_at, strength, detector_version, params_version, attributes jsonb`

Initial signal taxonomy (rules-first):

| Signal type | Detector | Why it matters |
|---|---|---|
| `contamination_document_present` | Document title matches a curated pattern list (Phase 2 Geo-Environmental, Remediation Strategy/Method Statement, Asbestos Survey/R&D Survey, Materials Management Plan, Ground Investigation, Land Contamination Assessment) | **Highest-precision cheap signal.** Contamination is in play and someone has paid a consultant to say so. |
| `contaminated_land_condition` | Planning condition text matches contaminated-land wording | Contamination formally recognised by the LPA |
| `condition_discharge_submitted` | Discharge application against a contamination condition | **Sharpest timing signal available.** Works are weeks–months away, not years. |
| `demolition_indicated` | Description/class matches demolition, prior approval for demolition | Demolition arisings, possible ACM |
| `historic_land_use_overlay` | Site geometry intersects former gasworks / tannery / foundry / historic landfill / industrial land | **Predicts contamination before anyone declares it** — the clearest "we didn't know that" |
| `remediation_tender` | FTS/Contracts Finder CPV codes for demolition, site preparation, remediation | Public-sector work with a real contract value attached |
| `major_earthworks` | Application scale + type thresholds | Volume-driven C&D opportunity |
| `permit_change_nearby` | Competitor permit surrendered/revoked/suspended within catchment | Capacity leaving the market — a commercial opening |

Rules first, always. An LLM classifier is permitted only for free-text that
defeats patterns, and only downstream of a deterministic pre-filter that bounds
cost. Every signal records `detector_version` so historical signals stay
interpretable after a detector changes.

### 2.5 Interpret

**`waste_arising`** — a *hypothesis* about material.
`id, opportunity_id, material_class, contaminant_classes[], candidate_ewc_codes[],
hazardous_flag, basis (source_stated|llm_extracted|inferred_from_land_use|
operator_override), confidence`

This is one of only two LLM stages. Output is schema-constrained, and every
extracted fact carries a verbatim quote verified to exist in the source text.

`candidate_ewc_codes` is plural and explicitly candidate — EWC classification is
a regulated judgement made on analytical data we do not have. **The system
suggests; it never classifies.** Getting this wrong is a compliance problem, not
just a quality problem.

### 2.6 Opportunity

**`opportunity`** — the unit of commercial attention.
`id (uuid), operator_id, site_id, primary_signal_id, title, status
(new|reviewed|pursuing|won|lost|dismissed), first_detected_at, last_updated_at,
estimated_tonnage_low/mid/high, estimated_timing_earliest/latest, timing_basis,
capability_match_level, nearest_facility_id, distance_km_straight,
distance_km_road, estimated_revenue_low/high, estimated_contribution_low/high,
economics_are_indicative (bool), score, confidence, score_version, params_version`

Notes that matter:
- **Every quantity is a band**, never a point estimate. The schema enforces the
  honesty.
- `economics_are_indicative` drives visible UI labelling wherever a figure
  derives from an unconfirmed parameter.
- `score_version` + `params_version` make historical scores reproducible after
  the model changes.

**`opportunity_signal`** — many-to-many. Opportunities accrete evidence over
time; a site with four independent signals is worth far more attention than one
with a single weak signal, and the model must represent that.

### 2.7 Provenance — the spine

**`claim`** — every material assertion the system makes.
`id, opportunity_id, field, value_numeric, value_text, unit, method
(deterministic_formula|llm_extraction|source_stated|operator_override|
default_parameter), formula_id, params_version, model_id, prompt_version,
confidence, created_at, superseded_by`

**`claim_input`** — `claim_id, input_claim_id` — the derivation DAG. A revenue
claim points at a tonnage claim, which points at an area claim, which points at
an extraction claim, which points at evidence.

**`evidence`** — `id, claim_id, raw_document_id, source_url, quote, char_start,
char_end, page, retrieved_at, content_hash`

**Rules:**
1. No claim without at least one `evidence` row or at least one `claim_input`.
2. LLM claims must include `quote`, and the quote must be verified present in the
   referenced `raw_document.content`. **Verification failure rejects the claim.**
   This single check removes most hallucination risk at negligible cost.
3. Prose shown to users is *rendered from* claims. Never store an LLM paragraph
   as the source of truth for a number.
4. Claims are append-only; corrections write a new claim and set
   `superseded_by`. The audit trail must survive disagreement.

This is what makes "check your working" a two-click operation rather than a
research project, and it is the difference between a tool a commercial director
trusts and one they quietly stop opening.

### 2.8 NRS capability — human-owned, never inferred

**`facility`** — `id, operator_id, name, permit_number, site_address, postcode,
easting, northing, geom, site_type, permit_status, source
(ea_register|operator_entered), confirmed_by, confirmed_at`

**`facility_capability`** — `id, facility_id, waste_stream, contaminant_class,
ewc_code, accepts (yes|no|case_by_case), max_annual_tonnes, notes,
confirmed_by, confirmed_at, valid_from, valid_to`

> **Why this must be human-entered.** We verified that NRS's permits in the EA
> register appear as A25 (deposit for recovery), L05 (inert landfill), A30
> (mining waste), A20 (metal recycling) and A16 (non-hazardous physical
> treatment) — **not one hazardous site type** — while NRS publicly describes
> operating one of the UK's largest hazardous treatment centres for construction
> waste, handling hydrocarbons, heavy metals, chlorinated solvents, PAH/coal tar
> and asbestos-impacted soils. The register's Site Type is a coarse primary
> classification and carries no EWC codes or capacity at all.
>
> **Therefore: capability cannot be derived from public data.** It is entered and
> confirmed by NRS, timestamped, and versioned. Any capability row without a
> `confirmed_at` is treated as unconfirmed and visibly flagged. Resolving the
> real permit position is the single highest-priority item for the NRS discovery
> session.

**Match levels:** `direct` (a confirmed capability covers the predicted stream and
contaminant) · `partial` (stream matches, contaminant unconfirmed) · `broker`
(NRS cannot treat it but could broker it — worth knowing, ranked lower) ·
`none` · `unknown` (capability data absent — surfaced as a data gap, **never
silently scored as zero**).

### 2.9 Feedback

**`opportunity_feedback`** — `id, opportunity_id, user_id, created_at,
already_knew (bool), would_action (bool), verdict (pursue|not_now|not_for_us),
tonnage_correction, value_correction, reason_code, free_text`

`already_knew` is the product's primary KPI (`docs/product-requirements.md` §5)
and must be a one-click action on every opportunity card, not buried in a form.

**`outcome`** — `opportunity_id, stage, won (bool), actual_tonnes, actual_revenue,
actual_contribution, closed_at`. Sparse for a long time; it is the eventual
training set, so capture it from day one.

## 3. Parameters — the anti-hard-coding mechanism

**`parameter_set`** — `id, operator_id, version, created_by, created_at, notes,
is_active`
**`parameter`** — `parameter_set_id, key, value_numeric, value_json, unit,
source (operator_confirmed|industry_default|placeholder), confidence, notes`

Everything NRS-specific and currently unknown lives here: bulk densities, depth
bands by development type, contaminated fractions by land-use class, gate fees by
waste class, haulage cost per mile, vehicle payload, economic haul radius, margin
target, minimum interesting tonnage, and every scoring weight.

Three consequences, all deliberate:
1. NRS tunes the model without a deploy.
2. Every opportunity records the `params_version` that produced it, so results
   are reproducible and changes are attributable.
3. `source = 'placeholder'` propagates to `economics_are_indicative` on the
   opportunity, which propagates to a visible UI label. **We can be uncertain,
   but we are never quietly uncertain.**
