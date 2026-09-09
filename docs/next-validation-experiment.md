# Next Validation Experiment — The NRS Awareness Test

**Cost: ~£0. Duration: 1 week. Build: none. Conversations: up to 5.**
**Decision it produces: BUILD or KILL.**

---

## What we are testing

One hypothesis: **that publicly available information can surface commercially
useful waste opportunities NRS does not already know about.**

Nothing else. Not the UI, not pricing, not the roadmap. If this fails, none of
the rest matters.

## Rules that keep it honest

1. **Show the leads before asking anything.** Never ask "would it be useful if…".
2. **Ask "did you already know" before revealing the score you gave it.**
   Otherwise you anchor them.
3. **Lead 7 (Mell Square) is the control.** It is a 1,600-home Muse/GRAHAM
   scheme 9 km away with national trade coverage. **If anyone says they did not
   know about it, the participant is not close enough to the commercial pipeline
   and their answers on the other nine are unreliable.** Discard that interview.
4. **Randomise the order.** Do not lead with the best one.
5. **Write down what they say, not what you hoped.** A disappointed founder with
   accurate notes is worth more than an encouraged one without.
6. **Do not sell.** The moment you defend a lead, the data is contaminated.

## Who to speak to

Up to five people, ideally spanning: commercial director / sales lead, an
estimator or technical manager, and one operations person. **At least three must
be involved in winning work**, or the awareness answers mean nothing.

## Materials

One side of A4 per lead — project, location, what is happening, source, date,
what waste is expected and why, distance from Meriden. **No tonnage. No £
values.** Both would be fabricated (`docs/ten-leads-analysis.md` §D), and one
invented number destroys the credibility of the whole exercise.

---

## The script

### Opening (do not skip)

> "I've been testing whether public data — planning applications, tender
> notices, environmental records — can find waste opportunities that a good
> commercial team wouldn't already have. I've got ten. I need you to tell me
> honestly which ones you already knew about. **The useful answer for me is 'we
> knew that' — that tells me the idea doesn't work, which is what I need to find
> out.** Please don't be polite about it."

### Per lead (~4 minutes each)

Hand over the sheet. Let them read. Then:

**Q1 — AWARENESS (ask first, always)**
> "Before today, did you know about this?"
>
> 1 Knew it well, already engaged · 2 Knew of it · 3 Vaguely aware ·
> 4 Did not know · 5 Did not know, and surprised it exists

**Q2 — follow-up on any 1–3**
> "How did you hear about it, and when?"
> *(Capture the channel: Barbour, trade press, existing customer, contractor
> relationship, word of mouth. This tells you what you are actually competing
> with.)*

**Q3 — ACTION**
> "Would you do anything about this? Yes, no, or not yet — and why?"

**Q4 — VALUE**
> "If this converted, roughly what order of magnitude is it to NRS?
> Under £10k / £10–50k / £50–250k / £250k+ / can't tell from this."
>
> *If they say "can't tell" — ask what is missing. That answer defines the
> product.*

**Q5 — WHO**
> "Who would you actually call, and would we be talking to the right person at
> the right time?"

**Q6 — EFFORT**
> "If I hadn't given you this, how would you have found it — and how long would
> it have taken?"

### After all ten

**Q7 — the one that matters**
> "Of these ten, how many were genuinely new to you?"

**Q8 — DISCOVERY TODAY**
> "How do opportunities normally reach you now? Roughly what proportion comes
> from existing customers, contractor relationships, tenders, subscriptions,
> word of mouth?"

**Q9 — INCUMBENT**
> "Do you subscribe to Barbour ABI, Glenigan or anything similar? What does it
> do well, and where does it let you down?"

**Q10 — CADENCE**
> "If leads like these arrived reliably, how often would you want them? Daily,
> weekly, monthly? How many per week could the team actually work?"

**Q11 — TRUST**
> "What would you need to see to trust this enough to act without checking it
> yourself?"

**Q12 — WILLINGNESS TO PAY (last, and asked plainly)**
> "If this delivered five to ten leads a week at roughly the quality of the best
> three here, what would that be worth per month to NRS? And who would sign it
> off?"
>
> *Do not name a price first. If they ask, say "that's what I'm trying to work
> out."*

**Q13 — CATCHMENT (needed regardless of outcome)**
> "How far will you economically haul contaminated soil? Does Derby work?
> Mansfield? Does it change by waste type?"
>
> *This is a blocking unknown in `docs/risks.md` §3 and must be answered
> whatever the verdict.*

**Q14 — the disconfirming question**
> "What would make this useless to you?"

---

## Scoring

| Metric | Threshold to proceed |
|---|---|
| **Leads scoring 4–5 on Q1 (did not know)** | **≥4 of 10** |
| Leads they would act on (Q3 = yes) | ≥3 of 10 |
| Control (Mell Square) correctly identified as known | **Must be 1–2, or discard the interview** |
| At least one lead rated £50k+ | ≥1 |
| A number given at Q12 | Any number, even a low one |

## Decision rule — write this down before you start

| Outcome | Decision |
|---|---|
| ≥4 unknown **and** ≥3 actionable **and** a price named | **BUILD** the Phase 1 MVP in `docs/roadmap.md` |
| ≥4 unknown but nothing actionable | Interpretation layer is wrong, detection is right — **iterate on qualification, do not build UI** |
| 2–3 unknown | **Narrow to the obscure-industrial niche only** (the Alpha Anodizing pattern) and re-test |
| ≤1 unknown, or control failed | **KILL** |

**Agree this table with yourself before the first meeting.** Deciding the bar
afterwards is how founders talk themselves into building things.

---

## What to do in parallel (same week, no extra cost)

**The tonnage feasibility spike — 1 day.** Pick three LPAs from the leads (Derby,
East Staffordshire, Solihull). Try to retrieve the *document list* for one
application at each and download one contamination report. This answers whether
tonnage is ever obtainable. ⚠️ Derby's portal returned **HTTP 503** on the single
direct attempt during this test, so treat it as genuinely uncertain.

If document retrieval fails at all three, the product cannot estimate tonnage or
value from public data — and the honest product is a **ranked alerting service**,
not the "£300k–£500k opportunity" described in `docs/product-requirements.md`.
That is a materially smaller business, and better to know in week one.
