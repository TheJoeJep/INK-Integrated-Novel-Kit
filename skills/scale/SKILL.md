---
name: scale
description: Calibrate a book's length against its scope, using the ~120,000-word threshold where readers expect escalated stakes or breadth. Use when a draft or outline feels too big or too small for its content, when deciding a target length for a new project, when a manuscript is running long, or when chapter lengths feel arbitrary rather than chosen.
---

# /scale — length and scope calibration

> **Tier 2 — diagnostic.** The thresholds and reference figures are Sanderson's benchmarks.
> Whether *this* book's scope actually matches its length is a **ranked hypothesis, not a
> certification** — the author confirms it against what the story is actually about.

**Say this on invocation:** *Checking length against scope — the numbers are Sanderson's
benchmarks, the read on whether this book fits them is a ranked hypothesis, not a verdict.*

**Source:** [`craft/structure/scale-and-length.md`](../../craft/structure/scale-and-length.md)

---

## The governing rule

> If you're going over around 120,000 words, the reader is going to expect an escalation in
> scope.

Length is itself a promise — readers see the size and calibrate what they expect the book to be
*about*. **This cuts both ways:** a long book with small stakes disappoints; a world-ending premise
crammed into 70,000 words feels rushed.

## Two ways to earn length

Scope isn't only *bigger threat*:

| Path | How it works |
|---|---|
| **Escalating stakes** | The *Harry Potter* path — stops being *can I get good enough grades to stay a wizard*, becomes *can I save the world*, and the books lengthen in step |
| **Breadth of time or life** | A family across generations, or one person's whole lifetime. Historical fiction earns length this way with no world-saving at all |

## Reference figures

| Work | Length | Note |
|---|---|---|
| Thrillers, most romance | 80–100k | Small scale, sustained |
| *Dune* | ~170–180k | |
| *Lord of the Rings* | ~480k total, ~150k/book | "That's the epic scope" |
| *A Christmas Carol* | Novella | One life, hit very quickly |

---

## The reading-session insight

**80–100k is a one-sitting book.** A fast reader finishes it in five to eight hours — that's why
thrillers live there:

> You can grab someone by the teeth and yank them through this story to the end so they're
> gasping.

**An epic is read across days or months.** Readers *will* put it down. So the book has to be
plotted around the fact that **break points exist**, with those points designed rather than left
to wherever the reader happens to stop.

### Chapter length is a pacing control

| You want | Chapter length |
|---|---|
| The reader able to stop comfortably | Long — a complete unit of story |
| The reader unable to stop | Short — see [`craft/plot/progress-and-signposting.md`](../../craft/plot/progress-and-signposting.md) |

*The Stormlight Archive* runs deliberately long chapters so that ending one feels like a complete
piece of story — **except at climactic moments**, where it cuts to short chapters. *"Short chapters
actually pull people through faster than long chapters do."*

---

## When a book runs long

**Note the direction of the fix.** When a book runs over its intended size, the answer is often to
**expand the scope** so the length is earned — not to cut back to the original size. This is the
counterintuitive half of this skill and the one worth checking first, before recommending cuts.

---

## Procedure

**1. Get the number.** Current or target word count, plus the stated stakes and time-breadth.

**2. Check the 120k threshold.** Has scope actually escalated — in stakes or in breadth of time —
to match, or is a small-scale story ballooning past its natural size?

**3. Check the one-sitting band (80–100k).** If aiming there, is it paced for a single sitting —
fast throughline, few designed stopping points?

**4. Audit chapter length variation.** Varying with intended pace, or uniform by habit? Where are
the climaxes, and are chapters shortening approaching them?

**5. If long and dragging: test expand-scope before cut.** Ask what stakes or time-breadth this
length could be earning that it currently isn't, before reaching for a cut recommendation.

---

## Output format

```
── SCALE ── current draft: ~142,000 words

  THRESHOLD     over 120k                               ✓ crossed
  SCOPE CHECK   stakes: personal (find the dragon)       ⚠  hasn't escalated
                breadth: single week, single city         ⚠  hasn't escalated
  BAND          neither one-sitting (80–100k) nor          —
                clearly epic-scoped

── READING FIT ──
  ●●●  most likely: long book, small stakes — the commonest drag pattern.
       Nothing in the outline currently justifies 142k against an
       80–100k, one-sitting version of the same plot.
  ●●○  alternative: scope HAS escalated (world-level stakes by act 3) and
       it just isn't visible yet in the first third — confirm against the
       outline before treating this as a cut.

── CHAPTER LENGTH ──
  ch01–ch14 average 3,100 words, std-dev 180 — effectively uniform.
  No shortening detected approaching the act break. Pacing control unused.

── FINDINGS ──
  Two live options, not one verdict:
  1. CUT toward ~90k and commit to a one-sitting, personal-stakes book
  2. EXPAND scope — escalate stakes or widen time-breadth — so 142k is
     earned. Sanderson's guidance: this is usually the right direction
     when a book runs long, not (1).
```

---

## Rules

- **State the word count and the stakes/breadth read before scoring anything**
- **Default to the expand-scope hypothesis before the cut hypothesis** when a book is running
  long — that's the documented correction, not a stylistic preference
- **Chapter-length uniformity is a finding on its own**, the same way `/pacing` treats it
- **Don't set a target length.** Report what the current length promises and whether the content
  matches it
- **Don't rewrite chapters or the outline.** Point to `/outline` or `/write` for repair

## Related

`/pacing` · `/outline` · `/premise-test` · `/write`
