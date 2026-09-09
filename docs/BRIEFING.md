# Briefing — everything you need to know

Plain English. Read this before the meeting. Nothing here assumes you know the
jargon.

---

## 1. The idea, in one paragraph

Every time someone wants to build on contaminated land in England, they have to
tell the council — in public, in writing, months before a digger arrives. Nobody
in the waste industry is systematically reading those records. The idea is to
read them all, work out which ones will produce waste NRS could handle, and tell
the sales team who to ring and when.

**That's it.** Not AI, not a platform. Reading public paperwork that nobody
reads, and pointing at the useful bits.

---

## 2. How we got here — it changed twice, and you should know why

**Started as:** commercial intelligence for NRS — find waste opportunities from
public data.

**Detoured into:** a compliance product ("check every load against your permit").
Looked great on paper. **I then tried to kill it and succeeded** — I pulled the
Environment Agency's own compliance data and found 90.8% of waste sites have no
recorded breaches at all. You'd have been selling insurance against a problem
nine out of ten customers can prove they don't have. Dropped it.

**Came back to:** the original idea, and actually tested it rather than
describing it.

The reason this matters: **if anyone asks whether you've been objective, the
answer is that the second idea got killed by its own evidence.** That's a good
story, not a bad one.

---

## 3. The one concept you must understand

**Condition discharge.** Everything hinges on this. If you understand nothing
else, understand this.

When a council grants planning permission, it attaches **conditions** — things
that must be sorted before work starts. On contaminated land there's almost
always a condition along the lines of *"you must submit a remediation strategy
and get it approved before you begin."*

To get going, the developer submits that strategy to the council. That
submission is called **discharging the condition**, and it is a public record.

**Why it matters commercially:** when you see a contaminated-land condition being
discharged, you know three things at once —

1. Contamination is **confirmed** (not suspected — someone paid a consultant)
2. A remediation strategy **exists** (so someone knows roughly what's coming out)
3. Works are **weeks to months away**, not years

Planning *approval* is useless as a sales signal — it can be one to three years
before anything moves. **Condition discharge is the moment it becomes real.**
Almost nobody watches it, because it's buried in 300-odd separate council
websites.

**The trap:** a **verification report** is the opposite. That means remediation
is *finished* and the waste has already gone. About 45 of the records I pulled
were this — they look identical to a keyword search and are worthless. Knowing
the difference is a real part of the value.

---

## 4. What I actually did

Four steps. You can describe this in thirty seconds if asked.

**Step 1 — got the data.** There's a free service called **PlanIt**
(planit.org.uk) that scrapes UK council planning portals and offers the results
through an API. I queried it directly.

**Step 2 — searched broadly.** Ten search terms — remediation, contaminated land,
asbestos, demolition, ground investigation, materials management plan,
verification report, and others. About **4,000 records** scanned, covering
**1 May to 9 September 2026**.

**Step 3 — filtered to your patch.** Every record has coordinates. I calculated
the distance from Meriden and kept anything within **110km**. That left **442**.

**Step 4 — scored and shortlisted.** Points for being a live condition discharge,
for contamination wording, for being a Large application, for being close.
Then a second filter for **industrial history** — former works, foundries,
gasworks, factories, platers. That gave **65**. From those, ten leads, then the
five on your cards.

I also pulled **Contracts Finder** (the government's tender site) separately —
that's where the HS2 one came from.

**Total machine time: under ten minutes.** My own time verifying and writing them
up: about two hours. That gap matters — the finding is fast, the qualifying isn't.

---

## 5. Numbers to have in your head

| | |
|---|---|
| Records scanned | ~4,000 |
| **Inside 110km of Meriden** | **442** |
| Of those, Medium or Large | **38** (8.6%) — the rest are small infill |
| Passed the industrial filter | 65 |
| Worked up as leads | 10 |
| On your cards | 5 |
| Records with a named contact | **only 39%** |
| Time window | May–Sept 2026 (4 months) |

**If asked "how many real ones a year?"** — roughly **110–130** commercially
material events in the catchment annually. Two or three a week. That's honest and
it's the right order of magnitude for a weekly sales list.

---

## 6. Words you might get asked about

| Term | What it means |
|---|---|
| **Condition discharge** | Developer submitting details to satisfy a planning condition before work starts. **The core signal.** |
| **Remediation strategy** | The document saying how contaminated land will be cleaned up. Contains the volumes — which is why I can't get tonnages without it. |
| **Verification report** | Proof remediation was done. **Too late to sell into.** |
| **Phase 1 / Phase 2** | Phase 1 is a desk study of site history. Phase 2 is actual soil sampling. |
| **EWC code** | European Waste Catalogue — the standard code for a waste type. Every load needs one. |
| **PlanIt** | The free service that scrapes council planning portals. My main data source. |
| **Contracts Finder** | The government's published tender notices. Where HS2/EKFB came from. |
| **Made ground** | Ground that's been filled or built up by people rather than nature. Usually where contamination lives. |
| **ACM** | Asbestos-containing materials. |

---

## 7. The software — there isn't any

**Be clear about this if asked. Nothing has been built.**

The repository contains **documentation and research only**. The starting point
is an off-the-shelf web app template (Next.js) that hasn't been touched. The five
cards were produced by **querying a public API and filtering the results with a
short script** — not by a system.

### What would be built, if it ever got that far

| Piece | What it does |
|---|---|
| **Collector** | Pulls PlanIt and Contracts Finder daily, stores everything |
| **Filter** | Deterministic rules — is it a live condition discharge, is it contamination, how far from a facility |
| **Interpreter** | The only place an LLM is used: read the wording, work out what waste is implied |
| **Scorer** | Ranks by size, distance, timing, fit — **ordinary arithmetic, not AI** |
| **The screen** | A weekly list: what happened, why it matters, who to call |

### One rule I'd hold to

**No LLM ever produces a number.** Tonnages, distances, values, rankings are all
plain code that can be checked. The model only reads text and writes sentences.
The moment a model starts estimating tonnages, you can't defend a single figure
in front of a customer.

### Rough build effort

A working weekly list for one operator: **6–8 weeks**. Getting tonnages out of
council document portals: **considerably longer**, and it may not be possible at
all — see below.

---

## 8. What's proven, and what isn't

### Proven
- **The data is reachable.** PlanIt and Contracts Finder both work.
- **The volume is real.** 442 in four months in your patch.
- **Some of it is genuinely hard to find.** A normal web search couldn't locate
  the Rolls-Royce remediation permission — the search engine said it "may not yet
  be widely indexed." The API found it instantly. Alpha Anodizing returned
  nothing but a Facebook page.
- **The timing thesis holds.** Six of the ten leads are live condition
  discharges.

### Not proven — and this is the whole point of tomorrow
- **Whether NRS already knows.** No idea. That's the meeting.
- **Whether anyone would pay.** Jason buying tonnage data is the only real
  evidence either way, and I only heard about it today.
- **Whether the leads convert.** Completely untested.

---

## 9. The weaknesses — know these before he finds them

**Say them first. It's far better coming from you.**

1. **No tonnages, no values.** They're inside submitted documents on council
   portals I couldn't get into — one council's site returned an error entirely.
   Every number would have been invented, so there are none.
2. **No contact 61% of the time.** The record often names nobody you could ring.
3. **90% of the 442 are small.** Single plots, barn conversions. The good ones
   are a minority.
4. **Barbour probably has most of this already.** They capture *all* planning
   applications — around 500,000 a year — and research anything over ~£100k
   through to subcontract award. **The claim isn't that the data is hidden. It's
   that nobody reads 500,000 records looking for waste.**
5. **The obscure ones tend to be the small ones.** Alpha Anodizing is invisible
   *and* only eight houses. Value and obscurity pull against each other.
6. **I filtered for hazardous.** If NRS's money is really in volume C&D, I
   pointed it at the wrong thing — fixable, the data's already collected.

---

## 10. Questions you'll probably get, and honest answers

**"Isn't this just Barbour?"**
> "Barbour has the records — they capture every planning application. What they
> don't do is read them for waste. Their research effort follows construction
> value; ours would follow contamination. Different filter on the same data."

**"How much is this one worth?"**
> "Can't tell you from public data. The volumes are in reports behind council
> portals I couldn't access. That's one of the things I found out."

**"Why didn't you just ask the team?"**
> "Because then I'd know the answer, and the whole point was to find out what we
> don't know."

**"How long did this take?"**
> "The search takes ten minutes. Checking them and writing them up took me a
> couple of hours."

**"What do you want out of this?"**
> "To know whether it's worth going further. If we already knew these five,
> that's my answer."

**"Could we sell this to other operators?"**
> "Maybe eventually. But first I need to know whether it's any use to us."

---

## 11. What happens next

1. **Tomorrow:** email your manager. Five cards, thirty minutes, no attachment.
2. **In the meeting:** ask "did you already know?" *before* showing the second
   half of each card. Ask early whether the money is in hazardous or in volume.
3. **Afterwards:** wait two weeks. If nobody rings any of these counterparties
   unprompted, treat the warm words as a no.
4. **Separately:** find out what Jason bought, from whom, and for how much.
   That's the only hard evidence of willingness to pay that exists.

**The decision rule is already written down and locked** in
`docs/validation/decision-rule.md` — so you can't move the goalposts afterwards.
Roughly: three or more genuinely new *and* actionable, plus someone naming a
credible price, and it's worth building. Otherwise it isn't.

---

## Where everything lives

| Document | What's in it |
|---|---|
| `docs/validation/manager-pack.md` | The five cards |
| `docs/validation/print/manager-pack.pdf` | Printable, one card per page |
| `docs/validation/manager-interview-sheet.md` | Your questions and capture grid |
| `docs/ten-leads-test.md` | All ten leads with full evidence |
| `docs/ten-leads-analysis.md` | What the test showed, and the decision |
| `docs/data/ten-leads-pool.csv` | **All 442 records** — the raw evidence |
| `docs/validation/decision-rule.md` | The locked thresholds |
| `progress.md` | Running log of everything, newest at the bottom |
