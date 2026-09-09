# User Experience

Designed for a commercial director and a salesperson. Not for a generic SaaS
user. Deliberately written *after* the intelligence design, because the UI is a
rendering of the model — if the model is weak, no interface saves it.

## Principle

**This is a briefing, not a dashboard.** The mental model is an inbox where every
item already has a verdict attached — not a BI tool the user has to interrogate.
If a screen shows data without a recommendation, it is the wrong screen.

Corollary: **no KPI tiles, no chart wall, no chat box.** A commercial director
does not need us to count things they already know. They need us to point.

## Screen 1 — This Week (the product)

A ranked list of opportunities, highest score first, defaulting to the current
week. Everything else in the app is secondary to this list.

Each card answers six questions without a click:

```
┌──────────────────────────────────────────────────────────────┐
│ Former gasworks site, Bloxwich — residential redevelopment   │
│ ● Score 82   ● Confidence Medium   ● NEW THIS WEEK           │
├──────────────────────────────────────────────────────────────┤
│ WHAT      Remediation strategy submitted to discharge a       │
│           contaminated-land condition (14 Aug 2026)           │
│ WASTE     Hydrocarbon + heavy-metal contaminated soil,        │
│           coal tar suspected (former gasworks)                │
│ HOW MUCH  8,000 – 15,000 t   ·  indicative £240k – £520k ⓘ   │
│ WHEN      Works likely to start within 2 – 4 months           │
│ WHY US    Direct match · Meriden (soil treatment) · 23 km     │
│ WHO       Redrow Homes (developer) · [Contractor unknown]     │
├──────────────────────────────────────────────────────────────┤
│ NEXT  Call the developer's project manager before the         │
│       remediation contractor is appointed.                    │
├──────────────────────────────────────────────────────────────┤
│ [ Pursue ]  [ Not now ]  [ Not for us ]  [ I already knew ]   │
└──────────────────────────────────────────────────────────────┘
```

Details that carry real weight:

- **"I already knew this" is a first-class button.** It is the product's own
  report card (`docs/product-requirements.md` §5), it must cost one click, and
  its rate is reported to the team weekly. A product that hides its own failure
  metric cannot improve.
- **"Contractor unknown" is displayed, not hidden.** Honest gaps build more trust
  than smooth omissions, and they tell the salesperson exactly what to find out.
- **ⓘ next to any £ figure** expands to "indicative — based on unconfirmed
  assumptions about gate fees and haulage" whenever
  `economics_are_indicative` is set.
- **Every number is a link** into the evidence trail.

## Screen 2 — Opportunity detail (the evidence)

The full brief, rendered from claims, not written by a model. Three panes:

1. **The narrative** — what happened, why it matters, what will arise, timing,
   the recommended action and the reasoning behind it.
2. **The working** — every claim with its method (formula / extraction /
   operator override / default parameter), its inputs, and the assumptions used.
   Any user can change an assumption and see the score recompute live; an
   analyst can persist the override, which is recorded as a new claim with
   attribution.
3. **The sources** — each piece of evidence with the **verbatim quote**, the
   source URL, and when it was retrieved. **Two clicks maximum from any number to
   the sentence it came from.** This is the single most important trust feature
   in the product.

## Screen 3 — Map

Catchment view: NRS facilities, capability radii, opportunities plotted and
sized by tonnage, coloured by capability match. Optional overlays for historic
land use and competitor permitted sites.

A commercial director thinks geographically about haulage. The map exists to
answer "what's near Meriden that we should be on?" — not to look impressive.

## Screen 4 — Feedback and calibration

Weekly scorecard: opportunities surfaced, already-known rate, pursued, converted,
estimate accuracy on closed jobs. This is where the product proves — or fails to
prove — its own value, and it should be visible to the sponsor without asking.

## Deliberately absent from the MVP

| Not building | Why |
|---|---|
| Chat interface | The value is a ranked list with reasoning, not conversation. A chat box invites questions the data cannot answer. |
| Configurable dashboard widgets | Displaces the opinionated ranking that is the whole point |
| Email digest | Only after the in-app list has proven useful. A weekly email of bad leads trains people to ignore us. |
| CRM integration | Until we know NRS's CRM and that the leads are worth pushing |
| Search over all planning data | That is Barbour ABI's job, and doing it badly invites the comparison we want to avoid |
| Self-serve onboarding, billing | One operator until it works |
