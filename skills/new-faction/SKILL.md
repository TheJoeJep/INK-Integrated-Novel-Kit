---
name: new-faction
description: Build a new faction through a structured interview and write its dossier. Use when adding a faction to the story, when an existing faction feels invincible, toothless, or interchangeable, or when the author asks for help working out a group's agenda and structure. Also use when a faction needs its limits defined before it can create real tension.
---

# /new-faction: structured faction build

> **Tier 4. Generative.** This produces **raw material for your judgement, not answers.** The
> limits-over-capabilities principle is Sanderson's Second Law applied to institutions rather than
> magic; the specific suggestions are mine and should be treated as starting points to react
> against. Where I offer options, pick one or reject all of them.

**Say this on invocation:** *Building a faction. The limits-first framing is Sanderson's Second
Law applied to a group instead of a power, the specific suggestions are mine and are raw material.
React against them rather than accepting them.*

**Sources:** [`templates/faction.md`](../../templates/faction.md) ·
[`craft/worldbuilding/sandersons-laws-of-magic.md`](../../craft/worldbuilding/sandersons-laws-of-magic.md)
(Second Law. Applies beyond magic to any invented capability, including institutions)

---

## Before starting

**Limits are the point, not the afterthought.** The Second Law states it about characters first,
magic second: *flaws or limitations are more interesting than powers.* A faction is a character at
institutional scale, and the same law holds. Full telekinesis makes for a worse story than
allomancy's push/pull-through-centre-of-mass, because the constraint is where the plot lives. A
faction that can simply do whatever the plot needs can't be beaten and can't create tension. Build
the limits with the same care as the capabilities, in the same sitting, not as a follow-up pass.

---

## The interview

Ask in order. **One question at a time.** Push past the vibe of the faction to what it can
concretely do and not do.

### 1. What they are

One or two lines. What kind of thing is this. A government, a cult, a guild, a family, a mob?
What would someone see if they walked into a room full of them?

### 2. Agenda: stated as an objective

**Not a vibe, an objective they could succeed or fail at.** *"They want power"* is not an agenda.
*"They want the council seat vacated by the last election recount"* is, because you can picture
what winning looks like, what losing looks like, and what they'd do differently if they were
losing.

- What do they want, concretely?
- What does **success** look like, specifically enough to stage a scene around it?
- What does **failure** look like. And is failure actually possible, or has the premise quietly
  made them unbeatable?

### 3. Structure and membership

- How are they organized. Hierarchy, cells, consensus, inheritance?
- Who joins, and how? Is membership chosen, inherited, coerced, earned?

### 4. Capabilities

What can they actually do? Resources, reach, information, force. Named specifically enough that
a scene could test one of them.

### 5. Limits: the section that matters most

**What can they not do?** This is not the leftover section after capabilities. It's the one that
makes the faction usable. Push on it as hard as the capabilities question, maybe harder:

- What resource do they not have?
- What territory, information, or authority is outside their reach?
- What would it cost them to overextend, and would they pay it?
- If the protagonist needed to beat them, what's the actual seam? *(If there isn't one yet, that's
  a blocking finding, not a detail to fill in later.)*

### 6. Visual

Iconography, dress, markings, tells. How a member is recognized, if they can be recognized at
all. Some factions are deliberately unmarked; say so rather than leaving it blank by omission.

### 7. Key members

Who represents this faction on the page? Link to (or flag as needed) dossiers in `characters/`.

### 8. History

Only as much as the plot needs to explain how they got their current capabilities and limits:
not a full institutional history. See `/worldbuild` if this threatens to expand past that.

### 9. What the protagonist knows about them, and when

Build toward the template's table: what's learned, and in which scene. This can stay open if the
plot hasn't reached those beats yet.

---

## Then write the dossier

From `.claude/templates/faction.md`, into `factions/`. Fill what the interview produced; leave the
rest as open questions rather than inventing.

**Maintain the `## Visual` block** even if sparse. It feeds image generation later.

---

## Rules

- **Limits before the dossier is called finished.** A faction with capabilities but no limits is
  half-built, regardless of how much else is filled in
- **Agenda must be an objective, not an aspiration.** If it can't fail, it isn't one
- **One question at a time.** A wall of questions gets shallow answers
- **Offer options, never one suggestion.** Raw material, clearly labelled
- **Don't fill gaps by inventing.** An unanswered question is an open question in the doc
- **Never invent a proper noun** not already in `canon/names-and-terms.md`. If the faction needs
  a name that isn't there, stop and ask
- **Say when a choice conflicts** with `canon/continuity-ledger.md` or `story/structural-rules.md`
. Including hard setting rules the faction's capabilities might quietly violate
- **Don't write the dossier into `factions/` unasked**

## Related

`/new-place` · `/new-character` · `/magic-system` · `/worldbuild` · `/write`
