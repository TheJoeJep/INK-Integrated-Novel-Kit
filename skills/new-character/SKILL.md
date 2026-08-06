---
name: new-character
description: Build a new character through a structured interview and write their dossier. Use when adding any significant character, when an existing character feels flat or generic, or when the author asks for help developing someone. Also use when a character needs an arc designed or their position in the cast worked out.
---

# /new-character: structured character build

> **Tier 4. Generative.** This produces **raw material for your judgement, not answers.** The
> questions are Sanderson's; the suggestions are mine and should be treated as starting points to
> react against. Where I offer options, pick one or reject all of them.

**Say this on invocation:** *Building a character. The framework is Sanderson's, the specific
suggestions are mine and are raw material. React against them rather than accepting them.*

**Sources:** [`craft/character/motivation-personality-values.md`](../../craft/character/motivation-personality-values.md)
· [`craft/character/proactive-relatable-capable.md`](../../craft/character/proactive-relatable-capable.md)
· [`craft/character/arcs-and-iconic-characters.md`](../../craft/character/arcs-and-iconic-characters.md)

---

## Before starting

**Say this once, because it changes expectations usefully:** characters usually take more than one
attempt. Three Vins. Two Kaladins. Dalinar worked first time. *Too stubborn to be anybody else*.
A character not working in draft one is normal.

**And:** every character starts as a stereotype crossed with an archetype. Nuance arrives as the
story goes. Don't try to make them three-dimensional at first appearance.

---

## The interview

Ask in order. **One question at a time.** Don't move on until there's a concrete answer. Abstract
answers ("stability," "meaning") are where flat characters come from.

### 1. Motivation: the foundation

- **What do they want?** Concretely, today
- **What don't they want anyone to know about them?**
- **What failure will they never repeat?**
- What in their history informs their current decisions?

*Questions two and three do the most work. A character with a concealed thing and an unrepeatable
failure has motivation, internal conflict, and a flaw in one stroke.*

### 2. Personality: how they pursue it

**Generate three expressions of the same want, and push for the non-obvious one.**

Worked example: a character who loves their family expresses it as (a) shared meals, (b) working
extra hours to provide, (c) fierce protectiveness and teaching self-defence. Same want, three
different people.

### 3. Values

What principles shape both the want and its expression?

**For an antagonist, decide deliberately:** comprehensible values (Magneto. His goal isn't
relatable, his fear is), or elemental force of nature (Sauron, whose interiority would add
nothing). **Commit either way.** A half-explained villain is worse than either.

*If elemental. Is there a Gollum somewhere to anchor it?*

### 4. Position on the three axes

Score them **in the situation the story puts them in**, not as global traits.

| Axis | Where do they sit? |
|---|---|
| **Proactive** | Do they make the story happen? |
| **Relatable** | Do we understand them? (**Not the same as likable**) |
| **Capable** | What are they good at? |

**Target shape:** very high on one, moderate on another, **growing on the third.**

**Then:** which is lowest? *That's the arc.*

**Check:** is your antagonist out-proacting your protagonist? If so, accept it and lean on the
other axes, let the plot force proactivity, or seed it small early.

### 5. Flaw, restriction, or limitation: decide which

| | | Story job |
|---|---|---|
| **Flaw** | Should be overcome | Drives the arc |
| **Restriction** | Self-imposed; **you don't want it overcome** | Reveals values |
| **Limitation** | Inflicted, worked around not removed | Generates plot |

*He renames these across lectures; the concepts are stable. Restriction is the underused one.*

**Has the flaw's cost been shown before you try to pay it off?** And is it double-edged. Hubris
is also self-confidence?

### 6. Arc or iconic

**Decide deliberately.** An iconic character, no arc, consistent book to book, is **just as
valid**, and a cast where everyone transforms flattens the book.

If arc: which axis moves, and **why** would they choose differently by the end? *Fail three times
then succeed* is not an answer.

### 7. Voice

- What would they do on a rainy day with nothing planned?
- **How do they treat service workers?**
- What's in their refrigerator?

Then: any quirk **must express a deeper trait.** David is bad at metaphors because he leaps before
thinking. A quirk attached to nothing reads as forced.

---

## Then write the dossier

From `.claude/templates/character.md`, into `characters/`. Fill what the interview produced; leave
the rest as open questions rather than inventing.

**Include the `## Visual` block** even if sparse. It's what makes image generation possible later.

---

## Rules

- **One question at a time.** A wall of questions gets shallow answers
- **Push back on abstractions.** *What would they actually reach for today?*
- **Offer options, never one suggestion.** Three, clearly labelled as raw material
- **Don't fill gaps by inventing.** An unanswered question is an open question in the doc
- **Say when a choice conflicts** with `canon/` or `story/structural-rules.md`
- **Name the technique** as you use it. One clause, not a lecture

## Related

`/character-arc` · `/motivation` · `/dialogue` · `/write`
