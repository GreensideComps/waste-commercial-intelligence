# Data Collection — Definitions and Live Capture Sheet

---

## 1. What counts as "UNKNOWN" — the four categories

Record **one letter per card**, before any discussion.

| | Category | Counts as unknown? |
|---|---|---|
| **A** | **Never heard of it** — no awareness of the site, the scheme or the company's activity | ✅ **YES** |
| **B** | **Vaguely aware of the project** — had heard something, no detail, no action | ❌ **NO** |
| **C** | **Knew the project, but not the waste opportunity** — aware the scheme existed, did not know contaminated material was arising, or that it was arising *now* | ✅ **YES — and this is the most important cell in the test** |
| **D** | **Already actively pursuing it** — contacted someone, quoted, or in the pipeline | ❌ **NO** |

### Why C counts, and why it may be the whole answer

The product's proposition has two separable halves: **finding the event**, and
**understanding what it means for waste**. Category C isolates the second.

If NRS knew Rolls-Royce Sinfin A was developing, but did not know a **remediation
consent had been granted with AECOM writing the strategy and arisings weeks
away** — then we did not tell them about a project. We told them about a
*commercial event inside a project they already knew about*. That is a
materially different and, arguably, more defensible product:

- the value is **interpretation, not discovery**;
- **Barbour ABI becomes a supplier rather than a competitor** — buy the project
  feed, add the waste layer on top;
- it works for firms that *already* subscribe to project intelligence, which
  widens the market rather than narrowing it.

⚠️ **If most new leads come back as C rather than A, do not read it as a weak
result.** It is a different result, and `decision-rule.md` routes it to CHANGE
THE PRODUCT, not to KILL.

### Why B does not count

"I think I'd heard something" is unverifiable and inflated by hindsight bias.
**If they cannot say how and roughly when they heard (Q2), downgrade B to A** and
note the uncertainty in comments. Apply this consistently, including when it
helps the idea.

---

## 2. What counts as "ACTIONABLE"

A lead is actionable **only if the participant supplies all four, unprompted**:

| | Test | Fails if… |
|---|---|---|
| 1 | **Why** — a specific commercial reason to pursue | "we'd have a look" |
| 2 | **Who** — a named person, company or role to contact | "the developer" with no idea which |
| 3 | **What** — what NRS would actually sell (treatment, haulage, disposal, brokerage) | "waste services" |
| 4 | **When** — roughly when they would act | "at some point" |

**Four out of four, or it is not actionable.** If you had to prompt any of them,
it fails. **"That's interesting" scores zero** — write the word INTERESTING in
comments so you can count them at the end.

---

## 3. The willingness-to-pay test

Never rely on "would you pay for this?" — it is the least reliable question in
customer discovery. The script asks seven questions in a fixed order, moving from
**actual current spend** (verifiable) to **hypothetical future spend** (weak).

| Q | What it establishes | Weight |
|---|---|---|
| 3.4 | Current subscription spend | **High** — real money already leaving the business |
| 3.5 | Current labour cost of this research | **High** — the true incumbent cost |
| 3.6 | Consultant spend | **High** |
| 3.7 | Outcome that would justify the cost | Medium — their own ROI logic |
| 3.8 | **Their price, named first** | **High** — never anchor |
| 3.9 | Preferred model (subscription / per lead / commission) | Medium |
| 3.10 | **Budget holder + what gets displaced** | **Highest of the stated measures** |
| 3.13 | **Revealed preference — do they act within 14 days?** | 🎯 **Outranks everything above** |

### Grading a WTP signal

| Grade | Definition |
|---|---|
| 🟢 **Strong** | Names a number ≥£500/month, names a budget holder, and names something it would displace |
| 🟡 **Weak** | Names a number, but no budget holder or nothing displaced |
| 🔴 **None** | "We'd pay something" with no figure — **record as none, not as positive** |
| ⚫ **Negative** | Names a number below £500/month — this is a **negative** result, not a soft yes (see `decision-rule.md` §Defect 3) |

---

## 4. Live capture sheet

One row per card. A blank CSV is at `docs/validation/capture-sheet.csv` — print
five copies, one per participant.

| Field | Enter |
|---|---|
| Participant | P1–P5 |
| Pack | A–E |
| Card | 1–10 |
| Order shown | 1st–5th |
| **Already knew?** | **A / B / C / D** |
| How did they know? | verbatim channel + rough date |
| Downgraded B→A? | Y/N |
| Would pursue? | Y / N / Not yet |
| **Actionable 4/4?** | Why ✓ Who ✓ What ✓ When ✓ → **Y/N** |
| Who would they contact | name / company / role |
| Estimated value | <£10k / £10–50k / £50–250k / £250k+ / can't tell |
| If "can't tell" — what's missing | verbatim |
| Expected to find via own sources? | Y/N + when |
| What would stop them | verbatim |
| Would pay? | Y / N / conditional |
| **"INTERESTING" said with nothing behind it** | Y/N |
| Comments | best verbatim quote |

### Per-participant sheet (once, at the end)

| Field | Enter |
|---|---|
| Role | |
| Involved in winning work? | Y/N *(if N, flag interview)* |
| **Control (Card 7) scored** | **A/B/C/D — must be C or D, else discard** |
| Card 10 enthusiasm? | Y/N *(politeness detector — if Y, discount)* |
| Current sources used | |
| Subscriptions + annual cost | £ |
| Hours/week on opportunity research (all staff) | |
| Who does the research | |
| Lead time normally achieved | |
| **Haul radius stated** | miles / km, and whether it varies |
| Minimum interesting job size | |
| Price named (Q3.8) | £ /month |
| Model preferred | subscription / per lead / commission |
| Budget holder | |
| What would be displaced | |
| **WTP grade** | 🟢 / 🟡 / 🔴 / ⚫ |
| Asked for the document (Q3.13)? | Y/N |
| **14-day follow-up: did they contact anyone?** | **Y/N — fill in later** |
| Interviewer gut score (1–10) | |
| Did I lead them anywhere? | |
