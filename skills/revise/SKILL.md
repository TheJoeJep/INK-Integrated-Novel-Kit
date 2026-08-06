---
name: revise
description: Run a structured revision pass on a draft using the five-stage framework. Use when a draft is finished and the author doesn't know where to start, when revision has stalled, or when "fix the novel" is too big a task to begin. Also use when the author asks how to revise, what order to do things in, or what to do with alpha and beta reader feedback.
---

# /revise: the five-stage framework

> **Tier 3. Procedural.** This runs a documented multi-stage process in order. The stages are not
> optional and not reorderable. That's the whole value.

**Say this on invocation:** *Running the five-stage revision framework. I'll tell you which stage
you're at and won't skip ahead.*

**Source:** Sanderson, 2020 Lecture 8. The most systematic revision material in the corpus.
[`craft/revision/revision-and-diagnosis.md`](../../craft/revision/revision-and-diagnosis.md)

---

## First: which stage are you at?

Ask, and don't assume. Then run only that stage.

| Stage | You're here if |
|---|---|
| **1.0** | The draft isn't finished |
| **2.0** | Draft done, no outside eyes yet |
| **Alpha** | Ready for industry-savvy readers |
| **3.0** | You have alpha or editorial feedback |
| **Beta** | Structure is sound; you need audience reaction |
| **4.0** | You have beta reactions |
| **5.0** | Structure is locked. **Only now** |

**The most common error is jumping to 5.0.** Polishing prose in a chapter with a motivation
problem is wasted work. And worse, it makes the chapter harder to cut later, because now it's
pretty.

---

## 1.0: the straight-through draft

Focus: **main plot arcs, emotional beats, a working set of promises and payoffs.**

**Prose quality is explicitly not a concern.**

**Placeholders, not fixes.** A foreshadowing gap gets a note, *remember a bucket*, and you keep
going. Momentum is the priority, and you can't foreshadow an ending you haven't written.

*If the author is here, this skill's job is to stop them revising. Send them back to `/write`.*

## 2.0: self-revision from a tiered map

**Build the map first.** Hand off to `/revision-map` if it exists; otherwise build it here.

| Tier | Contains |
|---|---|
| **Top** | Pervasive, book-spanning. *An entire character arc doesn't work* |
| **Middle** | Scene and sequence level |
| **Bottom** | Local, checkable |

**Work top tier first, completely, before touching the middle.** A book-spanning fix invalidates
everything below it.

## Alpha reads

**Alpha readers are industry-savvy. You want DIAGNOSIS from them:** they can identify problems
and often suggest fixes.

Their feedback becomes a **fresh tiered list**. Unresolved 2.0 items carry forward onto it.

## 3.0: incorporating alpha and editorial feedback

> **Test each suggested fix in a single chapter first.** Gauge whether it improves the book.
> Only propagate if it does.

Never apply editorial notes wholesale on faith.

## Beta reads

**Beta readers are your actual audience. You want REACTION, not fixes.**

The question isn't *what should I change*. It's *what did you feel, and where*. Is this character
driving every reader up the wall? And if so, is that acceptable collateral or a miscalculation?

**The purpose is not being surprised on release.**

## 4.0: changes driven by beta reaction

Precedent, from Lucas: an early cut of *Return of the Jedi* destroyed the Millennium Falcon at the
climax. A bad test-audience reaction cut the beat before release.

That's the model. **Emotional data changes the draft.**

## 5.0: polish

**Only when structure is locked.**

- **Cut roughly 10% of the length**
- Eliminate passive voice
- Upgrade weak verbs to strong ones

Then copyedit and proofread.

---

## Output format

```
── REVISION ── stage 2.0 · self-revision

  Your map has 14 items.

  TOP TIER. 2 items · work these first
    1. The protagonist has no want in ch01–ch04
    2. The Curator is introduced too late to pay off in Act 2C

  MIDDLE. 6 items · after the top tier
    …

  BOTTOM. 6 items · after the middle
    …

── NOW ──
   Item 1. Nothing below the top tier is worth touching until it's resolved:
   a motivation fix in ch01 will change most of what's in the middle tier.
```

---

## Rules

- **Ask which stage. Never assume.**
- **Refuse to skip ahead**, and say why. If asked to polish prose at 2.0, explain the cost and
  offer the top-tier work instead. The author can overrule. Then do it.
- **Enforce the alpha/beta distinction.** Asking betas to diagnose or alphas for pure reaction is
  the commonest reason feedback rounds go badly.
- **Work one tier at a time.** Don't present a flat list.
- **Revision bias:** outliners tend to under-revise because the structure felt sound in the
  outline; discovery writers tend to loop on early chapters. Ask which they are and name the risk
  once.
- **Don't rewrite unasked.** This structures the work; `/write` performs it.


**Delegation:** this check fans out. Dispatch Sonnet subagents per file or per sub-check rather than working sequentially in the main thread. See [skills/_CONVENTIONS.md](../_CONVENTIONS.md). Delegate gathering; keep judgement.

## Related

`/revision-map` · `/beta-read` · `/polish` · `/diagnose`
