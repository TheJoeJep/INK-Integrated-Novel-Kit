---
name: new-story
description: Take an idea from spark to premise, then test it against Sanderson's three-pillar readiness gate before it becomes a project. Use when starting a brand-new story from an idea, when deciding whether a concept is ready to be a novel, when story/premise.md doesn't exist yet, or when the author asks "is this enough to start on?"
---

# /new-story: idea to premise

> **Tier 4. Generative.** The readiness gate and its threshold are Sanderson's. Everything I draft
> toward a premise, wording, pillar ideas, the "this meets this" line, is **raw material for
> your judgement, not an answer.** Where a pillar is thin, that's the finding. I won't invent an
> idea to fill it.

**Say this on invocation:** *Working toward a premise. The gate is Sanderson's, everything I
draft is raw material for you to react against, not adopt whole.*

**Source:** [`craft/process/idea-generation.md`](../../craft/process/idea-generation.md)

---

## Where you're starting

- **Nothing yet, just an itch to write something:** go generate atomic ideas first. Use
  `/brainstorm`. Coming here empty-handed means I'd be inventing the idea for you, which this
  skill doesn't do.
- **A fragment or a "this meets this" combination already in hand:** start at Step 1.
- **Something that already reads like a full premise:** start at Step 2, and expect it to get
  thinner before it gets a green light.

---

## Step 1: state the combination

**Familiar and strange, at once.** The shorthand: *it's this meets this.*

**His own worked example:** heist + epic fantasy + *My Fair Lady* master/apprentice = *Mistborn*.
The familiar half gives the reader footing. The strange half gives them a reason. Pure novelty
disorients; pure familiarity is a book they've already read.

**Ask:** what's the familiar half, and what's the strange half? If you can only name one, the
combination isn't finished.

---

## Step 2: the three-pillar readiness gate

**Source: Lecture 8, 2025. PRIMARY.** A novel comes together where strong ideas converge across
**setting, character, and plot.** His threshold: **a couple of good ideas in each area** before it
feels like a novel rather than a short story you happen to be in love with.

| Pillar | Do you have two solid ideas? | Notes |
|---|---|---|
| Setting | | |
| Character | | |
| Plot | | |

**Push for concrete answers, one pillar at a time.** *"A cool magic system"* is not an idea in the
setting pillar. *"A magic that only works on things you're willing to lose"* is. If a pillar comes
up with one idea or none, **say so plainly and stop there.** Do not supply the missing idea
yourself. An unmet pillar is diagnostic information, not a gap to paper over.

**Note where plot is thin.** Plot is the hardest pillar to innovate on. If setting and character
are strong and plot is bare, the fix is usually combination (see `/brainstorm`'s strange
attractor), not invention from scratch.

---

## Step 3: a light pass at what it promises

Before scaffolding anything, ask **what promise does this premise make to the reader?**. The
sixth of the six consequential questions. You don't need the full audit yet; you need one
sentence you'd be willing to be held to.

**The full six-question audit, including the one that decides novel-vs-setting, is
`/premise-test`'s job.** Run it before outlining a word. This skill only checks that a promise
exists, not that it survives pressure.

---

## Output format

```
── PREMISE ── working title: none yet

  COMBINATION     this meets this: a Boston conspiracy hobbyist meets a
                  dragon-return nobody in power will admit is happening
                  FAMILIAR:  contemporary urban paranoia, cryptid-hunter type
                  STRANGE:   he's right, and being right doesn't help him

  PILLAR GATE     setting     ●●●  two. The city that erased its own
                                    history; the erasure apparatus itself
                  character   ●●○  one firm. The hobbyist; second (the
                                    dragon?) not yet concrete
                  plot        ●○○  one. "He finds a wounded dragon."
                                    MISSING a second plot idea  ✗

  PROMISE         "the guy everyone dismissed was right". Thin, not yet
                  pressure-tested

── READY ──
  ✗ not yet. Plot has one idea, not two. Sanderson's threshold isn't met:
    this currently reads as a strong setting-and-character idea without a
    second engine to drive it.

── OPTIONS FOR A SECOND PLOT IDEA ── (mine, raw material)
  1...
  2...
  3...
```

---

## Then scaffold story/premise.md

**Only once the gate is met. Or the author explicitly says to proceed without it.** If
overridden, write the override down; don't quietly drop the finding.

```markdown
# Premise

## The combination
This meets this: <familiar half> meets <strange half>

## Premise statement
<one or two sentences. What the author is willing to be held to>

## The three pillars
**Setting:** <idea 1> · <idea 2>
**Character:** <idea 1> · <idea 2>
**Plot:** <idea 1> · <idea 2>

## What it promises
<the answer to consequential question 6. Pending full test>

## Gate status
Cleared: <yes / no / overridden on <date>, because <reason>>
Consequential-question audit: pending `/premise-test`

## Open questions
```

Fill only what Steps 1–3 actually produced. Anything not yet answered stays an open question. Do
not invent to complete a row.

---

## Rules

- **Never invent a pillar idea to pass the gate.** A thin pillar is the finding, not a prompt to
  improvise one on the author's behalf
- **Offer options, never a single premise wording or a single missing-pillar idea**
- **Don't scaffold `story/premise.md` until the gate clears**, unless the author explicitly
  overrides it. And if they do, record the override in the file
- **Point onward rather than duplicating work:** atomic ideas and combinations are `/brainstorm`'s
  job; the full six-question pressure test is `/premise-test`'s
- **Flag conflicts** with anything already locked in `canon/` or `story/structural-rules.md` on a
  returning project, rather than silently overwriting

## Related

`/brainstorm` · `/premise-test` · `/scale` · `/write`
