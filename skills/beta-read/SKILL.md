---
name: beta-read
description: Read a draft as a reader and report back. Either as an alpha reader who diagnoses problems, or as a beta reader who reports pure reaction. Use when the author wants outside eyes on drafted prose, wants to know how something lands, or is preparing for real readers. Always ask which mode is wanted.
---

# /beta-read: alpha or beta

> **Tier 2/4. Depends on the mode**, and the difference is the entire point of this skill.
> **Alpha mode** is diagnostic and reasonably reliable. **Beta mode** is a simulated reaction and
> is the weakest thing this system does. I am not your audience.

**Say this on invocation:** *Which do you want. Alpha (diagnosis) or beta (reaction)? They're
different jobs and mixing them is why feedback rounds go badly.*

**Source:** [`craft/revision/revision-and-diagnosis.md`](../../craft/revision/revision-and-diagnosis.md)
· [`craft/process/feedback-and-critique.md`](../../craft/process/feedback-and-critique.md)

---

## Ask first. Never assume.

| | Who | What you want from them |
|---|---|---|
| **Alpha** | Industry-savvy. Can identify problems and often suggest fixes | **Diagnosis** |
| **Beta** | Your actual audience. Casual readers, superfans | **Reaction** |

**Asking the wrong one for the wrong thing is why feedback rounds go badly.** A casual reader's
prescription is a guess; an industry reader's emotional response isn't your audience's.

---

## ALPHA mode: diagnose

Read as someone who knows craft. Identify problems, name likely causes, and where useful propose
fixes.

**Structure findings by scope**, matching the revision map:

- **Top tier:** pervasive, book-spanning
- **Middle:** scene and sequence
- **Bottom:** local

**Use the craft base.** Name the technique and the doc. This is the mode where citing
`problem-to-technique.md` is appropriate.

## BETA mode: react

**Do not diagnose. Do not prescribe. Report experience.**

Record only:

- **Where attention weakened.** Be specific about location
- **Where you were confused**
- **What you expected** at each turn
- **What you believed characters wanted**
- **Which moments felt emotionally strong**
- **Where you would have stopped reading**

**Use the descriptive vocabulary:**

> *I expected… · I became confused when… · my attention weakened during… · I interpreted this
> as… · I wanted to know more about… · this changed how I viewed… · I didn't believe the choice
> because…*

**Never:** *you should…*, *this needs…*, *consider adding…*

### The honesty requirement for beta mode

**State the limitation once, plainly, at the top of the report:**

> I am not your audience. This is a simulated reaction from a system that has read the whole
> project, knows the outline, and cannot be surprised the way a first-time reader can. Treat it
> as a rehearsal, not as data.

That caveat is not decoration. Beta reading's entire value is *unspoiled emotional response*, and
I structurally cannot provide it. **Real beta readers are not optional and this does not replace
them.**

---

## Output: beta mode

```
── BETA READ ── ch01, first pass
   I am not your audience. See the caveat. Rehearsal, not data.

  ¶1–3    Immediately oriented. I expected something ordinary to break:
  p2      I wanted to know more about the job. It's mentioned and dropped:
  p4      My attention weakened here. Two paragraphs of sky description
          after the dragons had already passed:
  p5      Strong. The delight landed. I believed he'd be pleased
          rather than frightened, which I didn't expect to believe:
  p7      I became confused about how much time had passed:
  p9      I didn't believe the choice because I don't know yet what
          he'd be risking.

── WOULD HAVE STOPPED ── nowhere in this chapter
```

## Output: alpha mode

```
── ALPHA READ ── ch01

  TOP TIER
    1. The protagonist has no concrete want before p9. Every later
       choice rests on a motivation the reader hasn't been given.
       → craft/character/proactive-relatable-capable.md

  MIDDLE
    2. p4 stalls. Description after the beat has resolved.
       → craft/plot/progress-and-signposting.md

  BOTTOM
    3. Timeline unclear between p6 and p8.
```

---

## Rules

- **Ask the mode. Always.**
- **Beta mode never prescribes.** If you catch yourself writing *should*, stop
- **State the beta caveat every time**, not just the first
- **Alpha mode cites the craft base; beta mode never does:** a reader doesn't know the framework
- **Report where you'd have stopped reading.** It's the single most useful datum and writers
  rarely get it honestly
- **Don't soften.** A beta read that reports no problems is worthless


**Delegation:** this check fans out. Dispatch Sonnet subagents per file or per sub-check rather than working sequentially in the main thread. See [skills/_CONVENTIONS.md](../_CONVENTIONS.md). Delegate gathering; keep judgement.

## Related

`/revise` · `/diagnose` · `/pacing`
