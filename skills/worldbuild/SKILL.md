---
name: worldbuild
description: Build or audit a story's setting using the three worldbuilding components, worldbuilder's disease, and the hollow iceberg. Use when starting a new setting, when worldbuilding is consuming time that should go into the manuscript, when a world feels detailed but hollow, or when deciding how much of a setting actually needs building versus implying.
---

# /worldbuild: components, disease, and the hollow iceberg

> **Tier 3. Procedural.** The components, worldbuilder's disease, and the hollow iceberg are
> Sanderson's. Specific setting content I propose is raw material.

**Say this on invocation:** *Working the worldbuilding process in stages. The framework is
Sanderson's, any setting content I propose is raw material.*

**Source:** [`craft/worldbuilding/worldbuilding-fundamentals.md`](../../craft/worldbuilding/worldbuilding-fundamentals.md)

---

## The governing heuristic: say this before anything else

> Worldbuilding should serve the story, not hinder progress.

**The question every element must answer:** does this influence a decision a character makes, or
a challenge they face? If not, it doesn't earn its place yet, however interesting it is on its
own. Cohesion beats density. Three details that interlock convincingly outweigh two hundred that
don't touch each other.

---

## Stage 1: the components

**Ask which split fits this premise before building anything.**

| | Physical | Cultural | Magic / speculative |
|---|---|---|---|
| **Exists without people** | Geography, climate, flora and fauna, cosmology | | |
| **Shaped by inhabitants** | | Laws, government, religion, technology level, language, social norms, **varying by class** | |
| **The invented capability** | | | Hard/soft, social position, limitations and costs |

**The choice that matters:** 2025 teaches these as three pillars. 2020 taught a **two-way split**
, physical and cultural only, and when a student proposed magic as a third category, Sanderson
**explicitly folded it back into physical.** That isn't a relabelling; it's a real argument. Magic
*is* part of how the physical world works.

**Use whichever fits the premise:**

- If the speculative element reads as a **discovered property of reality**. Something that was
  always true and got found, not bolted on. The **two-way split honestly describes the world**.
  Treat it as physical setting.
- If it reads as a **supernatural overlay** distinct from how physics otherwise works, keep it as
  its own third pillar.

**Check:** a couple of solid, developed ideas in each component you're using. Not one brilliant
idea in one and nothing in the rest. That's the three-pillar convergence check, and it's a
readiness gate, not a nice-to-have.

---

## Stage 2: worldbuilder's disease

**His term.** Planning so long, at such scope, that the sheer amount of work left becomes
paralysing.

**The antidote. All three, not one:**

- Pick **key elements** for deep development instead of fleshing out everything evenly
- Keep deadlines
- Work **iteratively**. Build in response to what the story needs next, not in one exhaustive
  pass up front

**Ask directly, and answer honestly:** is more worldbuilding right now the actual next task, or is
it the comfortable one?

---

## Stage 3: the hollow iceberg

**The standard metaphor is wrong, and this is Sanderson's own correction of it.**

The usual claim: worldbuilding is an iceberg, a huge unseen mass beneath a small visible tip. His
correction:

> This is usually wrong. What we're actually doing is a **hollow iceberg.**

You do just enough work that, looking down through the water, **it appears to keep going**:
without ever building the submerged mass underneath.

**The stage-magician framing:**

> Writing books is like being a stage magician. You're slowly giving them the information they
> need so you can punch them in the face later.

The reader should finish thinking *they've clearly worked all of this out, I can trust them*.
**even though most of it was never built.** The named exception is Tolkien, who had twenty years
and a linguistics career to build the real thing; a working novelist publishing every few years
can't afford that, and shouldn't pretend to.

**Why this works:** a reader infers depth from *consistency*, not quantity. Three details that
clearly imply a fourth do more work than twenty that imply nothing.

**Check:** for the element in question, are you building the submerged mass, or building enough
surface consistency to imply it? Only the first one is ever wasted effort.

---

## Stage 4: expand what you have before adding something new

**Third Law, applied to setting generally, not just magic.** Its origin: the failed 2002 *Way of
Kings* draft. 300,000 words, ten character arcs each ~10% finished, thirty planned magic systems.
Chasing bigger killed the book.

**Three ways to expand instead of adding:**

- **Extrapolate:** what happens *when*? How has this existed-for-generations feature actually
  changed society, economy, daily life? This is the most-skipped step and the most valuable one
- **Interconnect:** tie the element to theme, or to another element already in the world
- **Streamline:** consolidate, combine, cut

**Two worked comparisons:** *Daggerfall*'s ten thousand procedurally-generated dungeons, built
from a handful of recombined assets, reviewed as *an ocean an inch deep*; *Skyrim* deliberately
walked that back to fewer, hand-built dungeons and was better received. And: three religions
forked from one shared root, like Christianity, Judaism, and Islam, beat fifty shallow,
unrelated ones, because the tension lives in how the forks read the same root differently.

**Ask:** are you adding a new element where you could instead deepen one already on the page?

---

## Output format

```
── WORLDBUILD ── <setting / element under review>

  COMPONENTS   split:               three-pillar / two-pillar (magic folded into physical)
               physical:            <ideas, or NONE YET>
               cultural:            <ideas, or NONE YET>
               magic (if separate): <ideas, or NONE YET>
               convergence check:   <pass / one pillar thin>

  DISEASE      symptom present:     <yes/no. Planning outpacing drafting>
               antidote applied:    key elements / deadlines / iterative. <which are missing>

  ICEBERG      building:            submerged mass  ✗  /  surface consistency  ✓
               consistency check:   <do the built details imply more than exists?>

  EXPAND       adding vs deepening: <which, and against what existing element>
               extrapolated:        <yes/no. Has this changed anything, given how long it's existed>

── BLOCKING ──
  <anything that stops the setting from supporting a scene right now>

── OPTIONS ── (mine, raw material)
  ...
```

---

## Rules

- **Run the stages in order.** Skipping to Stage 4 on an element with no components yet just
  produces more disconnected material
- **The governing heuristic overrides interest.** *Is this cool* is not the bar; *does this touch
  a decision or a challenge* is
- **Extrapolation is the most-skipped step.** Press on it every time a capability or institution
  has existed for more than a generation
- **Check for a project-specific constraint** in `world/` or `story/` and test proposals against
  it before offering them
- **Offer options, never one design.** Tier 4 content inside a Tier 3 process
- **Don't write the world into docs unasked:** that's `/write` in Structure Mode

## Related

`/new-place` · `/new-faction` · `/magic-system` · `/real-world` · `/write`
