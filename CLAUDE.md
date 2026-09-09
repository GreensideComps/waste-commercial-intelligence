# CLAUDE.md — Waste Commercial Intelligence (NRS)

Orientation for Claude Code. Read this before doing anything in this repo.

## What this product is

An AI-assisted commercial intelligence system that continuously monitors external
UK data and tells NRS **where to spend commercial effort this week**.

It sits *above* market data. For each opportunity it must answer:
what happened, why it matters, what waste will arise, how much, when, where,
which companies and people are involved, whether NRS can treat it, how far it is
from an NRS facility, what it is worth, how confident we are, what the evidence
is, and what the salesperson should do next.

## What this product is NOT

- Not a chatbot.
- Not a waste database.
- Not a prettier Barbour ABI, and not a replacement for it. Barbour ABI is a
  candidate *input*.
- Not a dashboard that displays data. Every screen must carry a recommendation.

## The only metric that matters right now

> "Would an experienced NRS commercial person have already known about this?"

If yes consistently, the product has failed regardless of how good the code is.
This is measured in-product by the **"I already knew this"** button on every
opportunity. Treat that rate as the primary product KPI.

## The pipeline

```
INGEST → NORMALISE → RESOLVE ENTITIES → DETECT SIGNALS → INTERPRET WASTE
→ QUANTIFY → MATCH NRS CAPABILITY → ECONOMICS → SCORE → RECOMMEND
→ OUTCOME → LEARN
```

## Hard rules

1. **No LLM arithmetic.** Tonnages, distances, revenue, margin, scores and
   rankings are computed by deterministic, unit-tested code. LLMs may only
   (a) extract structured facts from unstructured text, and (b) write prose that
   renders already-computed structured values. If you find yourself asking a
   model to "estimate" a number, stop.
2. **Every material claim carries provenance.** A number with no
   `evidence[]` chain back to a retrieved source document is a bug. LLM
   extractions must include a verbatim quote that is programmatically verified to
   exist in the source text; if it does not, reject the extraction.
3. **Nothing about NRS is hard-coded.** Facilities, permits, capabilities, gate
   fees, haulage costs, catchment radius, margin targets and "interesting" size
   thresholds all live in versioned database rows owned by the operator, never in
   source. See `docs/opportunity-model.md`.
4. **Placeholder economics must be visibly labelled.** We do not know NRS's
   prices. Any figure derived from an unconfirmed parameter is rendered as an
   indicative band and flagged in the UI. A confident wrong £ number destroys
   credibility faster than no number.
5. **Tenant-shaped from day one, multi-tenant infra later.** Every domain table
   carries `operator_id`. We do not build tenant isolation, billing or onboarding
   yet, but we never write code that assumes a single operator.
6. **Boring technology.** Postgres full-text before vector search. Cron before
   workflow engines. Do not optimise for impressiveness.

## Where to look

| Document | Purpose |
|---|---|
| `docs/product-requirements.md` | Users, jobs to be done, scope, validation |
| `docs/architecture.md` | Technical design, decisions and trade-offs |
| `docs/data-sources.md` | Verified source register — read before adding a source |
| `docs/opportunity-model.md` | Domain model, entities, provenance, capability match |
| `docs/scoring-model.md` | Tonnage, economics, scoring and confidence maths |
| `docs/roadmap.md` | Phases and the gates between them |
| `progress.md` | Living status log — update it as work lands |

## Current state

Planning stage. The repo is still an unmodified Next.js SaaS starter
(`nextjs/saas-starter`). **No application code has been written for this product
yet, and none should be until the plan in `docs/roadmap.md` is reviewed.**

## Repo conventions

- Package manager: `pnpm`. Node 22.
- Schema source of truth is Drizzle (`lib/db/schema.ts`) + generated migrations.
  Nothing else may migrate the database.
- Server Actions use the `validatedAction*` + Zod pattern already in
  `lib/auth/middleware.ts`. Keep it.
- Tests are required for anything numeric. There is currently no test runner —
  add Vitest before the first scoring code lands.

## Before adding a data source

Do not assume an API exists. Verify and record in `docs/data-sources.md`:
availability, access method, format, update frequency and lag, licence and
re-use conditions, geographic coverage, and known limitations. Several sources we
expected to be useful are not — read that document first.
