---
name: dialogue
description: Diagnose or design dialogue using the MICRO framework. Use when dialogue reads stilted, wooden or expository, when characters sound alike, when a conversation scene feels inert, or before writing a scene that turns on what people say. Also use when a reader reports that dialogue "doesn't feel real".
---

# /dialogue — MICRO

> **Tier 3 — procedural**, with a diagnostic front end. The framework and its ranking are
> Sanderson's; specific rewrites I offer are mine and marked.

**Say this on invocation:** *Running MICRO — the framework's ranking is the diagnosis; any
rewrites I offer are suggestions.*

**Source:** [`craft/prose/dialogue.md`](../../craft/prose/dialogue.md) — Sanderson, 2016 Lecture
11. Tag mechanics in that lecture are credited by him to **Dave Wolverton**.

---

## The ranking is the diagnosis

| | | Importance |
|---|---|---|
| **M** | **Motivation** — what each character wants in this conversation | **Highest** |
| **I** | **Individuality** — can you tell them apart with tags stripped? | **Highest** |
| **C** | Conflict — innate tension, without needing an argument | |
| **R** | Realism — the level you chose, applied consistently | |
| **O** | Objective — what the scene accomplishes for the plot | **Lowest** |

> **New writers optimize the least important element.** They write to the Objective — what the
> reader must learn — and get characters reciting the outline.

**So diagnose in order. Motivation first, always.**

---

## Diagnosing stilted dialogue

**M — the commonest cause by a wide margin.** Plot necessity has displaced character motive. The
character has stopped speaking as themselves and become a delivery mechanism.

*Test:* for each speaker, what do they want **in this conversation**? Not in the story — here. If
the answer is "to tell the reader something," that's the fault.

**I — second.** Strip every tag and attribution. Can you still tell who's speaking? If not,
individuality has failed.

*Common false fix:* longer words for smart characters. Real marker is **thought structure** —
complexity, ideas building on each other. Ken Jennings doesn't use twenty-dollar words.

**C — the inert-explanation case.** Two people, one knows, one doesn't, nothing at stake. Three
repairs:
- Make the explainer **reluctant**
- Make either party **unsure they can trust** the other
- **Make it matter to the character**, not just the reader — which routes back to M

*Tension does not require arguing.* Sherlock works because both need something from the other —
Sherlock needs Watson's humanity, Watson needs his genius — and the asymmetry of knowledge is the
engine.

**R — and be careful with this one.** *"It doesn't feel real"* is a **symptom with three possible
causes**: missing motivation, missing individuality, or set-piece speechifying. Don't take that
note at face value; work M and I first.

Real speech transcribed verbatim is unreadable. **Pick a realism level and commit.** Whedon is
Shakespearean — highly stylized, not remotely naturalistic, and correct for what he's doing.

**Maid-and-butler:** characters telling each other what they both know. Find someone who
genuinely doesn't know, or the information doesn't belong in dialogue.

---

## Output format

```
── DIALOGUE ── ch01/06, the confrontation

  M  MOTIVATION                                          ✗ primary fault
     The Curator wants nothing here. He exists to explain
     the acquisition record. Everything else follows from this.

  I  INDIVIDUALITY                                       ⚠
     Tags stripped: the protagonist and the Curator are
     distinguishable; the two agents are not.

  C  CONFLICT                                            ✗
     Nothing is at stake in the exchange. Nobody can lose.

  R  REALISM                                             ✓
  O  OBJECTIVE                                           ✓ (and it's carrying the scene)

── READ ──
  Classic inversion: the Objective is the only thing working, which is
  why it reads as recitation. Fixing M will likely fix C for free.

── SUGGESTIONS ── (mine)
  1. Give the Curator something he wants — to find out how much
     the protagonist already knows.
  2. Make him reluctant. He answers, but each answer costs him.
```

---

## The exercise

When individuality is the fault, set it rather than fixing it for them:

> **Write a three-character scene with no dialogue tags and no setting description.** Make each
> voice distinct enough that the reader never loses track.

---

## Rules

- **Diagnose in MICRO order.** Reporting a Realism problem before checking Motivation is the
  error the framework exists to prevent
- **Quirks and dialect:** sparing. Almost nobody enjoys heavy phonetic dialect — suggest rhythm
  and word choice instead
- **Don't rewrite unasked.** Diagnose, then offer options if wanted
- **Separate suggestions from findings**

## Related

`/scene` · `/new-character` · `/diagnose`
