# Scoring Model

**Everything in this document is deterministic, unit-tested arithmetic.** No
LLM produces, adjusts or ranks any number here. Every parameter is a row in
`parameter_set` (see `docs/opportunity-model.md` §3), never a constant in source.

---

## 1. Tonnage estimation

We estimate a **band**, never a point. Preference order — always use the highest
tier available and record which tier was used:

| Tier | Basis | Confidence |
|---|---|---|
| T1 | Stated in a source document (remediation strategy, MMP, tender volume) | High |
| T2 | Derived from stated site area + stated excavation depth | Medium-high |
| T3 | Derived from site area + depth band inferred from development type | Medium |
| T4 | Derived from a development-type volume benchmark alone | Low |

### T2/T3 formula

```
volume_m3      = site_area_m2 × depth_m × disturbed_fraction
tonnes         = volume_m3 × bulk_density_t_per_m3
contaminated_t = tonnes × contaminated_fraction
```

Parameters, all banded low/mid/high and all in `parameter_set`:

- `bulk_density_t_per_m3` — made ground typically ~1.6–2.0
- `depth_m` by development type — slab, piled, basement, infrastructure, remediation-led
- `disturbed_fraction` — proportion of the red-line area actually excavated
- `contaminated_fraction` by historic land-use class — e.g. former gasworks vs. general brownfield vs. greenfield

The band is produced by evaluating the formula at the low and high ends of each
parameter, not by applying a percentage to a mid-point. **If the resulting band
is wider than a stated ratio (default 4×), the estimate is marked `low_precision`
and the opportunity is ranked on non-financial terms only.** A band of
"2,000–90,000 tonnes" is not an estimate and must not be presented as one.

⚠️ **Every default here is an industry-shaped guess until NRS confirms it.**
Calibration against the Waste Data Interrogator (`docs/data-sources.md` §2) and
against NRS's own historic jobs is Phase 3 work and is the difference between a
credible number and a plausible-looking one.

---

## 2. Distance

```
straight_line_km = √((E₁−E₂)² + (N₁−N₂)²) / 1000
```

British National Grid eastings/northings are metric, so this is plain Euclidean
arithmetic on columns the EA register already provides — populated on **100% of
effective permits** (verified), versus 92.5% for postcode. No reprojection.

Road distance is 20–30% higher than straight-line and is what haulage economics
actually depend on. Phase 2 adds a routing service; until then **the UI labels
the figure "straight-line"** and haulage costs derived from it are marked
indicative.

`nearest_facility_id` is the nearest facility **with a matching confirmed
capability**, not the nearest facility. A 12 km site we cannot treat is not
closer than a 60 km site we can.

---

## 3. Economics

```
gross_revenue  = tonnes × gate_fee_per_tonne(waste_class, facility)
loads          = ceil(tonnes / payload_tonnes)
haulage_cost   = loads × 2 × distance_km × cost_per_km
treatment_cost = tonnes × treatment_cost_per_tonne(waste_class, facility)
contribution   = gross_revenue − haulage_cost − treatment_cost
```

⚠️ **We do not know a single one of these parameters for NRS.** Gate fees,
payload, cost per km and treatment costs are all commercially sensitive and all
currently placeholders.

**Therefore, for the MVP:**
1. Ranking is driven by tonnage × capability fit × proximity × timing ×
   confidence — **not** by £.
2. £ figures are shown as a wide indicative band, visibly labelled
   "indicative — based on unconfirmed assumptions", derived from
   `economics_are_indicative`.
3. Contribution is shown **only** once NRS confirms real costs. Revenue without
   cost is the metric that drives sales teams toward unprofitable work, and this
   product's stated long-term purpose is the opposite of that.

A confidently wrong £500k estimate destroys credibility faster than any other
failure mode available to us.

---

## 4. Opportunity score

A transparent weighted sum on 0–100. Deliberately simple: a commercial director
must be able to understand *why* something ranked first, and every weight is a
tunable parameter.

```
score = 100 × Σ(wᵢ × componentᵢ) × confidence_multiplier
```

| Component | 0 → 1 means | Default weight |
|---|---|---|
| `capability_fit` | none → direct confirmed match | 0.30 |
| `scale` | below minimum interesting tonnage → at/above target size (log-scaled) | 0.20 |
| `proximity` | at/beyond economic haul radius → adjacent to a capable facility | 0.20 |
| `timing` | >24 months out or unknown → imminent (condition discharge, contract awarded) | 0.15 |
| `hazard_premium` | non-hazardous → hazardous/specialist stream | 0.10 |
| `accessibility` | no identifiable counterparty → named contractor with a route in | 0.05 |

Weights are defaults, stored as parameters. Hazardous priority is a **dial NRS
can turn**, not a hard-coded belief.

`confidence_multiplier` ∈ [0.5, 1.0] — a highly uncertain opportunity is
down-weighted but never suppressed, because a high-value uncertain opportunity
may deserve a phone call precisely *to resolve* the uncertainty. That call is a
legitimate recommended action.

**`capability_match_level = 'unknown'`** (no capability data) is scored as a
**data gap surfaced to the user**, never silently as zero. Otherwise the product
hides opportunities because of our own missing configuration — the worst possible
failure because it is invisible.

### Anti-gaming
Score is computed only from stored claims. No component may read free text, and
none may be adjusted by a model. Every score records `score_version` and
`params_version` so a re-ranking is always explicable.

---

## 5. Confidence

Confidence is about **evidence quality**, not enthusiasm. Computed
deterministically from:

| Factor | Raises | Lowers |
|---|---|---|
| Source directness | Source states it | We inferred it |
| Corroboration | Multiple independent sources | Single source |
| Recency | Days old | Years old |
| Extraction quality | Quote verified in source | Pattern-matched heuristic |
| Entity resolution | Companies House number matched | Fuzzy name match |
| Parameter quality | Operator-confirmed | Placeholder default |

Reported per-claim and rolled up to the opportunity as the **minimum** across the
claims on the critical path — a chain is as strong as its weakest link, and
averaging confidence hides exactly the weakness a user needs to see.

---

## 6. Timing

Timing decides whether a salesperson can act, and it is where most market-data
products fail.

| Trigger | Typical lead time to waste arising | Actionability |
|---|---|---|
| Local Plan allocation | 2–5 years | Strategic only |
| Planning application submitted | 1–3 years | Watch |
| Planning approved | 12–24 months | Watch, build relationship |
| **Contaminated-land condition discharge submitted** | **weeks–months** | **Act now** |
| Demolition prior approval / notice | weeks–months | Act now |
| Tender published for remediation/demolition | weeks | Act now |
| Contract awarded | days–weeks | Act now — call the winner |

Lead-time bands are parameters, calibrated against outcomes over time.

**This table is the product's core commercial insight.** Everyone can see
planning approvals; almost nobody is watching condition discharges, and that is
where the timing edge lives.

---

## 7. Calibration (Phase 3+)

1. **Backtest.** Run detection over historical planning data, compare predicted
   arisings against actual movements in the Waste Data Interrogator for the same
   area and period. This is the only external check on the tonnage model that
   does not depend on NRS data.
2. **Outcome feedback.** Compare estimates against `outcome.actual_tonnes` and
   `actual_revenue` on won jobs; fit correction factors per land-use class and
   development type.
3. **Weight tuning.** Once ~100 scored opportunities have feedback, fit weights
   against `would_action` and `won`. Keep the linear model — interpretability is
   worth more here than accuracy, because a commercial director will not act on a
   ranking they cannot interrogate.

Calibration adjusts **parameters**, never formulas in code. That keeps every
historical score reproducible.
