---
name: subplot
description: Plan, document, or audit a subplot as a thread in its own right. Its archetype, promise, progress, payoff, and how it connects to the main story. Use when adding a secondary storyline, when a subplot feels shapeless or disconnected, when readers skim a thread, when deciding whether a subplot earns its place, or when the author asks what subplots the book is running.
---

# /subplot: subplots as first-class threads

> **Tier 2/3 hybrid.** Auditing existing subplots is diagnostic. Documented rules, ranked
> findings. Designing a new one is procedural, and any *content* I propose is raw material to
> react against.

**Say this on invocation:** *Working subplots. The audit is against documented rules; any thread
content I propose is a suggestion.*

**Source:** [`craft/plot/plot-archetypes.md`](../../craft/plot/plot-archetypes.md) ·
[`craft/plot/promise-progress-payoff.md`](../../craft/plot/promise-progress-payoff.md) ·
[`craft/structure/structure-models.md`](../../craft/structure/structure-models.md) ·
[`craft/short-fiction/short-fiction.md`](../../craft/short-fiction/short-fiction.md) (MICE)

---

## Why subplots need their own documents

**A subplot is a whole story in miniature.** Its own promise, its own kind of progress, its own
payoff, its own archetype. The craft base asks these questions directly. *What archetype is each
subplot running?*, *does every subplot touch the Major Dramatic Question?*. And with nowhere to
record the answers, they get decided by accident.

**The failure this prevents:** a subplot with no archetype has no shape, and a thread with no
shape is the one readers skim. Its progress is invisible because there's nothing to measure it
against.

Subplots live in `plot/subplots/`, one document each, from `.claude/templates/subplot.md`.

---

## AUDIT: what is this book actually running?

**1. Inventory.** Read `plot/`, `story/outline.md`, `plot/subplots/`, and the manuscript if it
exists. List every thread that isn't the main line.

**Include undocumented ones.** A subplot running in the prose with no document is the most common
finding and the most useful.

**2. Per subplot, check six things:**

| Check | Failure looks like |
|---|---|
| **Archetype** | None identifiable → no shape → readers skim |
| **Promise** | Never made, or made and forgotten |
| **Progress** | Nothing visibly advancing |
| **Payoff** | Opens, never resolves |
| **Touches the MDQ** | Reads as a side quest however good it is |
| **Thread closure** | A MICE type opened without its matching close |

**3. Check the count against the length.** The shorter the work, the fewer threads it carries.
More than the length supports produces a book that feels busy and unresolved.

**4. Report.**

---

## Output format

```
── SUBPLOTS ── 5 running, 3 documented

  ✓  The dragon's trust          relationship      doc ✓
     promise ch01/04 · progress visible · pays Act 3 · touches MDQ ✓

  ⚠  The Rider order's decay     NO ARCHETYPE      doc ✓
     Runs beat 7 → Act 2A with no identifiable shape.
     Candidates: mystery (what do they actually know?) or
     betrayal (they aren't what they claimed).

  ✗  The neighbour. NO DOC
     Appears ch01/04, ch01/05. Opens an Inquiry thread
     (does she know?) that never closes.

  ✗  The heretic scientist       mystery           doc ✓
     Does not touch the Major Dramatic Question.
     Currently reads as a side quest.

── FINDINGS ──
  1 undocumented · 1 without archetype · 1 disconnected from the MDQ

── OPINION ──
  The neighbour thread is cheap to convert. It could carry the leak in
  beat 5, which is still undecided. That closes it and pays a main-line
  beat at once.
```

---

## DESIGN: building a new subplot

Interview, one question at a time:

1. **What is this thread about**, separate from the main plot?
2. **What archetype?** Not "relationship". *Which kind*. Deepening, souring into betrayal,
   master/apprentice?
3. **What does it promise, and where?**
4. **What kind of progress:** information, relationship, or internal? **How is it signposted?**
5. **What pays it off?**
6. **Which MICE thread** does it open, what closes it, and **does it nest inside another?**
7. **How does it touch the Major Dramatic Question?**
8. **What breaks if you cut it?** If nothing, say so. That's the useful answer

Then write the doc from the template into `plot/subplots/`.

---

## Rules

- **An undocumented subplot running in the prose is a finding.** Report it first
- **"What breaks if it's cut" is the question that matters.** Ask it of every subplot and report
  honestly when the answer is *nothing*
- **Don't invent an archetype to fill a gap.** Offer candidates; let the author choose
- **Cross-check with `/threads`.** They overlap deliberately. `/threads` finds unclosed threads
  mechanically; this asks whether a thread should exist at all
- **A subplot disconnected from the MDQ isn't automatically wrong:** but say so plainly, since
  it's the commonest reason a well-written thread gets skimmed
- **Don't fix.** Findings and designs only; repair goes through `/write`


**Delegation:** this check fans out. Dispatch Sonnet subagents per file or per sub-check rather than working sequentially in the main thread. See [skills/_CONVENTIONS.md](../_CONVENTIONS.md). Delegate gathering; keep judgement.

## Related

`/threads` · `/promises` · `/plants` · `/pacing` · `/structure`
