---
name: diagnose
description: Work out why something in the story isn't working, starting from the symptom. Use when the author says a scene is flat, boring, confusing, unsatisfying, slow, or that a character doesn't work. Or when a beta reader reports a problem and the cause is unclear. The general entry point for any "why isn't this working?" question.
---

# /diagnose: symptom to cause

> **Tier 2. Diagnostic.** I map symptoms to likely causes using documented base rates. These are
> **ranked hypotheses, not verdicts.** The author confirms which one is real.

**Say this on invocation:** *Diagnosing from the symptom. I'll give ranked hypotheses with base
rates, not a verdict.*

---

## The front door

This is the general entry point. Other skills are narrower instruments; this one decides which to
reach for.

**Primary reference:**
[`craft/reference/problem-to-technique.md`](../../craft/reference/problem-to-technique.md)

---

## Procedure

### 1. Get the symptom as a reader experience

**Not as a writer's theory.** Push for this if needed:

- âŒ *"The pacing is off in act two"*. That's a diagnosis wearing a symptom's clothes
- ✅ *"I got bored around chapter nine and started skimming"*. That's data

**The three tiers of what a reader gives you**, and they have very different authority:

| | Authority | Treat as |
|---|---|---|
| **Reaction:** *I got bored here* | High | Evidence |
| **Diagnosis:** *because nothing happens* | Medium | Hypothesis |
| **Prescription:** *add a fight scene* | Low | One option of many |

**Take the location seriously. Diagnose the cause yourself.**

### 2. Ask the three questions first

Before consulting anything, on any problem:

1. **What did this promise, and did it pay?**
2. **What does this character want, and does it show?**
3. **What progressed here, and can the reader see it?**

Most problems are one of these three. Most of the rest are downstream of them.

### 3. Work the index

Find the symptom in `problem-to-technique.md`. Causes are **ordered by base rate**. Work down,
don't jump to the interesting one.

**Documented base rates worth stating aloud:**

- **~60% of character problems are motivation problems.** Not dialogue, not prose. Check first
- **Invisible progress is the most common cause of mid-book abandonment.** Things *are* happening;
  the reader can't see them
- **A boring sequence is usually a promise/progress misalignment:** an interesting promise was
  made, then the writer got interested in something else

### 4. Check the evidence

For each hypothesis, look at the actual text or docs. **Don't theorize from the symptom alone.**

### 5. Report ranked hypotheses

---

## Output format

```
── SYMPTOM ──
   "I got bored around chapter nine and started skimming"

── HYPOTHESES ── ranked by base rate, checked against the text

  1. INVISIBLE PROGRESS  â, â, â.   most likely
     ch08–ch10 advance the investigation, but nothing signposts it.
     Last visible marker is ch07.
     → craft/plot/progress-and-signposting.md
     Confirm: can you point at the line where a reader sees advancement?

  2. PROMISE MISALIGNMENT  â, â, â. ‹
     ch09 opens a thread the book hasn't promised. Reads as a side quest.
     → craft/plot/promise-progress-payoff.md
     Note: the fix is usually to change the PROMISE, not the sequence.

  3. UNIFORM PACING  â, â, ‹â. ‹
     ch06–ch10 are within 200 words of each other with similar beat density.
     → craft/plot/progress-and-signposting.md

── NEXT ──
   Run /pacing for a full signposting audit, or tell me which of these lands.
```

Confidence as `â, â, â, ` / `â, â, â, ‹` / `â, â, ‹â. ‹`.

---

## Rules

- **Rank by base rate, then adjust for evidence.** Say when you're departing from the base rate
  and why.
- **Never give one cause.** If you only have one, you're asserting, not diagnosing.
- **Always name the craft doc.** The author must be able to check your reasoning.
- **Give a confirmation test per hypothesis:** something the author can check in a minute.
- **Don't fix.** Repair goes through `/write`. Point at the narrower skill if one fits.
- **Reader prescriptions are the weakest input.** Say so when one is driving the question.

## Hands off to

`/pacing` · `/motivation` · `/threads` · `/promises` · `/viewpoint-check` · `/gorillas` ·
`/continuity`

**Delegation:** this check fans out. Dispatch Sonnet subagents per file or per sub-check rather than working sequentially in the main thread. See [skills/_CONVENTIONS.md](../_CONVENTIONS.md). Delegate gathering; keep judgement.
