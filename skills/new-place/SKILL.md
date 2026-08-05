---
name: new-place
description: Build a new place through a structured interview and write its dossier. Use when adding any significant location, when an existing setting reads as generic or interchangeable, or when the author asks for help developing where a scene happens. Also use when a place's Visual block needs filling in for image generation.
---

# /new-place — structured place build

> **Tier 4 — generative.** This produces **raw material for your judgement, not answers.** The
> sensory and characterization principles are Sanderson's; the specific suggestions are mine and
> should be treated as starting points to react against. Where I offer options, pick one or reject
> all of them.

**Say this on invocation:** *Building a place — the sensory framework draws on Sanderson's craft
base, the specific suggestions are mine and are raw material. React against them rather than
accepting them.*

**Sources:** [`templates/place.md`](../../templates/place.md) ·
[`craft/worldbuilding/worldbuilding-fundamentals.md`](../../craft/worldbuilding/worldbuilding-fundamentals.md)

---

## Before starting

**A place needs a reason it has to be *this* place**, not generic scenery a scene happens to be
staged in front of. If the interview can't answer *why here and not somewhere else*, that's worth
surfacing before going further — cohesion beats density, and an orphan location is worldbuilding
that touches nothing.

---

## The interview

Ask in order. **One question at a time.** Push for the concrete detail over the generic one — *an
office* is nothing; *a rent-controlled walk-up with a police scanner running in the kitchen* is a
place.

### 1. Role in the story

- What happens here?
- Why does it have to happen *here*, specifically — what does this location make possible or
  impossible that another one wouldn't?

### 2. Visual — for image generation

Concrete enough to render:

- **Scale** — how big, how many rooms/floors/blocks
- **Architecture / structure**
- **Condition** — new, worn, decaying, maintained
- **Light** — natural and artificial; what time of day it's usually seen
- **Weather / climate**
- **Distinguishing features** — the one or two things that make this place recognizable, not
  interchangeable with any other

### 3. Sensory — beyond the visual

**The instruction from the craft base is explicit: describe how it feels, not how it works.**
The shimmer of spice, the metallic taste of burning metal — sensation before system.

- What does it **sound** like?
- What does it **smell** like?
- What's the **temperature**, the quality of the **air**?

**Then the sharper question: what does a character *notice* here, and what do they walk past
without a glance?** That choice is not inventory — it's characterization. A character who clocks
the exits notices differently than one who clocks the dust on the windowsill. Filtering the
sensory list through *whose* attention it is belongs in the prose; the dossier should record
enough raw sensory material that the filtering has something to choose from.

### 4. Geography and layout

- How is it arranged?
- What's adjacent to it?
- How do you get in, and how do you get out? *(If a scene will need an escape, a chase, or a
  hiding place, this is where that gets decided or ruled out.)*

### 5. History

What happened here before the story needed it? Only as much as earns its place — a hollow
iceberg, not an excavated one. See `/worldbuild` if this threatens to become its own project.

### 6. Who controls it

Who has authority here, formal or otherwise? Does that connect to a faction already in
`factions/`? If the answer is nobody, say so — an ungoverned place is itself a fact.

---

## Then write the dossier

From `.claude/templates/place.md`, into `places/`. Fill what the interview produced; leave the
rest as open questions rather than inventing.

**Maintain the `## Visual` block** even if sparse — it's what makes image generation possible
later, and it stays live: every time prose establishes something new about how this place looks,
that fact lands here, not just in the manuscript.

---

## Rules

- **One question at a time.** A wall of questions gets shallow answers
- **Push past the visual.** Sound, smell, temperature, air — a place that's only described is a
  set, not a setting
- **What a character notices is characterization**, not a checklist to exhaust. Name this when it
  applies
- **Offer options, never one suggestion.** Raw material, clearly labelled
- **Don't fill gaps by inventing.** An unanswered question is an open question in the doc
- **Never invent a proper noun** not already in `canon/names-and-terms.md` — if the place needs a
  name that isn't there, stop and ask
- **Say when a choice conflicts** with `canon/continuity-ledger.md` or `story/structural-rules.md`
- **Don't write the dossier into `places/` unasked** if this is being run as a side inquiry rather
  than the actual build — confirm first

## Related

`/new-faction` · `/worldbuild` · `/real-world` · `/write`
