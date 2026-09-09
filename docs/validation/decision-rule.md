# Decision Rule — Critique, Revision, and Lock

**Read this before the first interview. Sign and date it. Do not reopen it
afterwards.**

---

## Part 1 — Critique of the proposed rule

The framework in the brief was:

> **BUILD:** ≥4 unknown AND ≥3 actionable AND ≥1 credible WTP signal
> **VALIDATE FURTHER:** 2–3 unknown, or needs narrowing
> **KILL:** ≤1 unknown, or control fails, or consistently would-not-act

It has **five defects**. Four are fixable; one is structural and you should
simply accept it.

### Defect 1 — "≥4 unknown" has no defined unit of analysis 🔴 **critical**

Five packs × five opportunities = **25 observations across 10 leads and 5
people**. Each non-control lead is seen by only **two or three** participants.

So "4 unknown opportunities" is undefined. Unknown to one person? To everyone
who saw it? If Lead 2 is unknown to participant A but known to participant C,
does it count?

**This matters commercially, not just statistically.** If any commercial person
at NRS already knew, then *NRS knew*, and the product added nothing to the
company. The knowledge does not have to be evenly distributed to exist.

**Fix:** the unit is the **lead**, and a lead counts as unknown only if **every
participant who saw it** scored it unknown. Unanimity among 2–3 viewers.

### Defect 2 — "unknown" and "actionable" are counted independently 🔴 **critical**

As written you could score 4 unknown leads (all commercially useless) plus 3
actionable leads (all of which NRS is *already pursuing*) and trigger BUILD.
**That is a false-positive path straight through the middle of the test.**

An actionable lead they already knew about is worth nothing — they are already
acting on it. Value only exists where **new** meets **actionable**.

**Fix:** actionable is measured **only on the subset that qualified as unknown**.
One combined metric, not two independent ones.

### Defect 3 — "≥1 credible WTP signal" is far too weak 🟠

One person out of five naming a number is noise, and these people know you
(see `bias-controls.md` §Ben effect). Worse, the rule does not say *how much*.
"We'd pay £50 a month" satisfies the rule as written and simultaneously proves
the business cannot exist.

**Fix:** require (a) **two or more** participants to independently name a
number, and (b) at least one number at or above a **viability floor**.

**Deriving the floor, explicitly:** £1m ARR needs roughly 50–80 customers at
£1–2k/month. At £250/month it needs ~330 waste operators with a commercial
function, which likely exceeds the entire UK population of such firms. So
**£500/month is the floor below which the business does not work**, and a
number below it is a negative result, not a soft positive.

### Defect 4 — control failure is under-specified 🟠

Mell Square is a 1,600-home Muse/GRAHAM scheme 9 km from Meriden with national
trade coverage. If a participant does not know it, **that participant** is not
close enough to the commercial pipeline for their other answers to be reliable —
their interview is discarded.

But discarding leaves you with n=4 or fewer, and the lead-coverage matrix
collapses.

**Fix:** one control failure → discard that interview and **recruit a
replacement**. Two or more control failures → **abort the test**; you have
recruited the wrong people, and the result is uninterpretable rather than
negative.

### Defect 5 — n=5 cannot measure a rate 🔵 **structural — accept it**

With ~2 observations per lead, this test **cannot distinguish a 30% unknown rate
from a 50% one.** Confidence intervals at this sample size are wider than the
gap between BUILD and KILL.

**Do not fix this by adding participants** — you do not have 20 waste commercial
directors available, and pretending otherwise delays the decision by months.

**Instead, be honest about what the test is:** a **screening test**. It reliably
detects the extremes — "obviously dead" and "obviously alive" — and is genuinely
inconclusive in the middle. The revised rule below therefore makes the middle
outcome resolve to a **specific narrower action**, not to an indefinite
"validate further" loop. A test whose ambiguous outcome is "do the same thing
again" is a test you will keep re-running until it tells you what you want.

### The missing category — and it may be the real finding 🟢

The brief's own instinct is right: **"knew the project but not the waste
opportunity" (category C) is the most important cell in the whole test.**

If NRS knew Rolls-Royce Sinfin A was developing but did not know a *remediation
consent* had been granted with contaminated arisings imminent, then:

- the product's value is **interpretation, not discovery**;
- Barbour ABI becomes a **supplier, not a competitor** (buy the project feed,
  add the waste layer);
- the ICP widens, because interpretation is valuable even to firms that already
  subscribe to project intelligence;
- and the cheapest possible MVP changes shape entirely.

A result of "mostly C" is a **pivot signal, not a failure**. The revised rule
gives it its own branch.

---

## Part 2 — The revised rule (LOCKED)

### The primary metric

**NNAL — Net New Actionable Leads.**

A lead counts toward NNAL only if **all four** hold:

1. **Unanimously new** — every participant who saw it scored **A** or **C**
   (see `data-collection.md` §Unknown), and none scored **B** or **D**;
2. **Actionable** — at least one participant satisfied the **full four-part
   actionability test** (why / who / what / when — `data-collection.md`);
3. **Not already being pursued** by NRS in any form;
4. **Within NRS's stated haul radius**, as confirmed at Q13.

NNAL is measured out of the **9 non-control leads**.

### Thresholds

| NNAL (of 9) | Plus conditions | Decision |
|---|---|---|
| **≥3** | ≥2 participants name a price **and** ≥1 price ≥£500/month **and** ≤1 control failure | 🟢 **BUILD** — Phase 1 MVP in `docs/roadmap.md` |
| **≥3** | but no price ≥£500/month | 🟠 **CHANGE THE PRODUCT** — the information is new and useful but not worth subscription money. Test a different delivery model (brokerage, commission, or paid research retainer) before writing code. |
| **1–2** | and those leads cluster in one recognisable type | 🟠 **NARROW THE ICP** — re-run against that niche only (see `post-interview-analysis.md` §Signal type) |
| **1–2** | with no pattern | 🔴 **KILL** |
| **0** | — | 🔴 **KILL** |
| any | **≥2 control failures** | ⚫ **ABORT** — wrong participants, result void, re-recruit |
| any | majority of new leads scored **C** (knew project, missed waste) | 🟠 **CHANGE THE PRODUCT** → interpretation layer over a bought feed |

### Why ≥3 of 9 and not ≥4 of 10

Because unanimity is now required, and each lead has only 2–3 viewers, the bar
is materially harder than the original "≥4 unknown". Requiring 3 unanimously-new
*and* fully-actionable *and* not-being-pursued leads out of 9 is, on the evidence
from `docs/ten-leads-analysis.md`, a genuinely uncertain outcome — which is what
a real test should be. My own prior is that NRS already knows 3–5 of the 10, so
this rule can plausibly fail. **If a threshold cannot plausibly fail, it is not a
test.**

### The tie-breaker that outranks everything

**Revealed preference beats every stated answer in this document.**

If, within 14 days of the interviews, **any participant has actually contacted a
counterparty on one of these leads** — without being prompted a second time —
that outweighs any number they said out loud. Log it (`data-collection.md`
§Follow-up). Conversely, if all five said "very interesting" and **nobody
contacted anybody**, treat the stated enthusiasm as worthless regardless of what
the numbers say.

---

## Part 3 — Lock

> I have read the critique above. I accept the revised thresholds. I will not
> alter them after interviews begin. If the result is KILL, I will kill it.
>
> Signed: ______________________  Date: ____________
