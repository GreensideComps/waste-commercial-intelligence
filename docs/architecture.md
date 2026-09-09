# Architecture

## 1. What we inherited

The repo is an unmodified clone of `nextjs/saas-starter`: Next.js 15.6 canary,
React 19, TypeScript 5.8, Tailwind 4, shadcn/ui, Drizzle ORM → Postgres, Stripe,
JWT-cookie auth. ~40 source files. No tests, no CI, no CLAUDE.md, and
`node_modules`/`.env` were never created in this container.

### Retain

| Part | Why |
|---|---|
| Next.js + TypeScript + Tailwind + shadcn/ui | Right weight for an internal analytical tool. React Server Components suit read-heavy, data-dense pages. |
| Drizzle + Postgres + `drizzle-kit` migrations | Postgres is the correct single store here: relational integrity for the evidence graph, JSONB for raw payloads, PostGIS for geography, full-text for search. Drizzle keeps schema in TypeScript with real migrations. |
| `lib/auth/session.ts` (jose JWT + bcrypt) | Adequate for a small internal user base. Not worth replacing with an IdP yet. |
| `middleware.ts` route protection | Works; extend the matcher, don't rewrite. |
| `validatedAction` / `validatedActionWithUser` / `withTeam` in `lib/auth/middleware.ts` | Genuinely good pattern — Zod validation at the Server Action boundary. Reuse it for every mutation. |
| `activity_logs` | Repurpose as the audit trail. An intelligence product needs to record who saw and who overrode what. |
| `teams` | Repurpose as the tenant anchor (`operators`). This is the cheapest path to multi-operator later. |

### Modify

| Part | Change | Reason |
|---|---|---|
| `teams` → `operators` | Rename; drop the Stripe columns for now; add operator profile fields | NRS is operator #1, not "a team" |
| `users.role` | `owner`/`member` → `admin`, `commercial_director`, `sales`, `analyst`, `readonly` | Roles drive what each person sees and may override |
| `activity_logs` → `audit_log` | Generalise: subject type + id, actor (user *or* pipeline run), before/after | Must cover pipeline and AI decisions, not just user actions |
| Primary keys | Keep `serial` for app tables; use **UUID** for domain entities (opportunities, signals, claims, evidence) | These appear in URLs, exports and cross-system references; sequential integers leak volume and collide across environments |
| Session cookie `secure: true` | Make environment-conditional | Breaks local `http://localhost` development as written |
| `middleware.ts` matcher | Protect everything except auth routes | There is no public marketing surface in this product |

### Remove

| Part | Reason |
|---|---|
| `lib/payments/*`, `app/api/stripe/*`, `app/(dashboard)/pricing/*` | No billing in an internal tool. Recoverable from the upstream starter if the product is ever sold. |
| `app/(dashboard)/terminal.tsx`, marketing `app/(dashboard)/page.tsx` | Starter marketing content |
| Stripe dependency and env vars | Dead weight |

### Add

- **Vitest** — non-negotiable before any scoring code lands. We are shipping
  numbers; untested numbers are a liability.
- **PostGIS** extension — catchments, distance, historic-land-use overlays.
- **A `pipeline/` workspace** with no Next.js imports (see §3).
- **CI** — typecheck, lint, test, migration check.

---

## 2. System shape

```
┌─ SOURCES ─────────────────────────────────────────────────────────┐
│ PlanIt API │ EA registers │ Companies House │ FTS/Contracts Finder │
│ LPA portals (targeted) │ historic land use / geospatial            │
└───────────────────────────────┬───────────────────────────────────┘
                                │  adapters (one per source)
                                ▼
┌─ INGEST ──────────────────────────────────────────────────────────┐
│ raw_documents: immutable, content-hashed, retrieved_at, source_url │
│ Nothing is ever mutated in place. Re-fetch = new row.              │
└───────────────────────────────┬───────────────────────────────────┘
                                ▼
┌─ NORMALISE → RESOLVE ─────────────────────────────────────────────┐
│ source_records (canonical fields) → sites, organisations, people   │
│ Entity resolution keyed on Companies House number where possible   │
└───────────────────────────────┬───────────────────────────────────┘
                                ▼
┌─ DETECT (rules first, LLM only where rules can't reach) ──────────┐
│ signals: typed, scored, each linked to the evidence that raised it │
└───────────────────────────────┬───────────────────────────────────┘
                                ▼
┌─ INTERPRET (LLM, constrained, quote-verified) ────────────────────┐
│ waste_arisings: material, contaminant, candidate EWC codes         │
└───────────────────────────────┬───────────────────────────────────┘
                                ▼
┌─ QUANTIFY → MATCH → ECONOMICS → SCORE  (100% deterministic) ──────┐
│ tonnage bands │ capability match │ £ bands │ score + confidence    │
└───────────────────────────────┬───────────────────────────────────┘
                                ▼
┌─ RECOMMEND (LLM writes prose over already-computed values) ───────┐
│ opportunities + recommended_actions                                │
└───────────────────────────────┬───────────────────────────────────┘
                                ▼
┌─ PRESENT (Next.js) → OUTCOME (human) → LEARN (calibration) ───────┐
└───────────────────────────────────────────────────────────────────┘
```

---

## 3. Decisions and trade-offs

Recorded because these are the choices that are expensive to reverse.

### D1 — Where does the pipeline run?

| Option | For | Against |
|---|---|---|
| Next.js API routes + Vercel cron | One codebase, one deploy | Serverless timeouts kill long ingests; Node is weak for document extraction; couples analysis to the web app |
| Separate Python service | Best-in-class PDF/geo/calibration libraries | Two languages, two toolchains, for a very small team |
| **Standalone TypeScript `pipeline/` workspace, same repo, same DB** ✅ | One language, shared schema types via Drizzle, runs as a plain long-lived process, trivially portable | Node PDF extraction is materially worse than Python's |

**Recommendation:** start TypeScript-only. Phase 0 does not need PDF parsing —
document *titles* are the signal, and titles come from the API/portal listing.
Introduce a **narrow Python service for document extraction only** at Phase 2, if
and when PDF parsing is on the critical path. Its interface is a queue and a
table, nothing else.

The rule that keeps this cheap: **the pipeline never imports from `app/`, and the
web app never invokes the pipeline synchronously.** Postgres is the contract.

### D2 — Orchestration

**Recommendation: plain scripts on cron for Phase 0–1; `pg-boss` (Postgres-backed
queue) when retries, concurrency and per-source backoff become real.** Rejected:
Temporal and Airflow (operational weight far beyond this problem), Inngest
(another vendor for something Postgres already does).

### D3 — Search

**Recommendation: Postgres full-text + `pg_trgm` for fuzzy name matching. No
vector database in the MVP.** Our matching problems are lexical (company names,
document titles, waste descriptors), not semantic. Add `pgvector` only if a
concrete retrieval problem defeats full-text — and say what that problem is
first.

### D4 — Multi-tenancy

**Recommendation: tenant-shaped schema, single-tenant operations.** Every domain
table carries `operator_id` from the first migration. We do **not** build tenant
isolation, per-tenant auth, or onboarding. Adding the column now is nearly free;
retrofitting it across an evidence graph later is a rewrite. This is the concrete
answer to "expandable to other operators".

### D5 — Where AI is allowed

Two places, and nowhere else:

| Stage | Mechanism | Guard |
|---|---|---|
| **Interpretation** — unstructured text → structured facts | LLM with a strict output schema | Every extracted fact must carry a **verbatim quote** that is programmatically confirmed to exist in the source text. Fails verification ⇒ claim rejected, not downgraded. |
| **Explanation** — structured values → readable prose | LLM given only already-computed values | Rendered prose must contain no number absent from the input payload. Assert this in tests. |

Everywhere else — tonnage, distance, revenue, margin, score, ranking, dedup,
matching — is deterministic TypeScript with unit tests. Restated because it is
the easiest rule in this document to erode: **if you are asking a model to
produce a number, you have made a mistake.**

Cost control: LLM calls only on records that pass a deterministic pre-filter.
Model choice by stage — a smaller fast model for high-volume extraction, a larger
one for hard cases and for the weekly brief. Every call records model id, prompt
version and parameters against the claim it produced.

### D6 — Geography

**Recommendation: compute distance directly in British National Grid
easting/northing.** BNG is a metric projected CRS, so straight-line distance is
plain Euclidean arithmetic on the columns the EA register already provides — and
those columns are populated on **100% of effective permits** (measured), whereas
postcode is missing on 7.5%. No reprojection is needed for distance.

Store both straight-line and (later) road distance; label which is shown. Road
distance via a routing service is a Phase 2 refinement — haulage economics depend
on road miles, and straight-line will systematically under-estimate by roughly
20–30%. Use PostGIS for polygon work (catchments, historic land use overlay), and
reproject to WGS84 only for map display.

### D7 — Internal data readiness (RoadTrak, later)

Not in the MVP, and no MVP behaviour may depend on it. Readiness is achieved by
three design choices rather than by building anything now:

1. **Facilities, capabilities, capacity, pricing and haulage costs are already
   database rows**, sourced today from human entry with a `source` and
   `confirmed_at` field. A RoadTrak feed later changes the *source* of those
   rows, not the schema and not the consumers.
2. **The scoring engine reads parameters, never constants**, so richer inputs
   (actual spare capacity, real gate fees, historic win rates) refine existing
   terms instead of requiring new ones.
3. **Outcomes are recorded from day one** even while volumes are tiny, so there
   is a training and calibration set on the day internal data arrives.

The questions in the long-term vision — filling spare capacity, customers leaking
to competitors, highest-contribution rather than highest-revenue — are all
answerable by populating the *same* parameter and outcome tables with better
data. That is the test of whether this design is genuinely extensible.

---

## 4. Environment and operations

- Local: Postgres via Docker (available in this environment), `pnpm dev`.
- Secrets: `POSTGRES_URL`, `AUTH_SECRET`, `BASE_URL`, plus
  `COMPANIES_HOUSE_API_KEY`, `ANTHROPIC_API_KEY`. Stripe vars removed.
- Raw source documents stored in Postgres initially (they are small); move to
  object storage when PDFs arrive.
- **Backups matter more than uptime.** The accumulated raw corpus is the asset —
  it is what lets us re-run improved detection over history and prove the
  product's value retrospectively. Losing the app is a redeploy; losing the
  corpus loses the history we cannot re-fetch.
