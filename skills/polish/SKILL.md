---
name: polish
description: Run the 5.0 polish pass — cut roughly 10% of length, eliminate passive voice, upgrade weak verbs to strong ones, then copyedit and proofread. Refuses to run if structure isn't locked and explains why, unless the author overrules. Use only after the revision map's top and middle tiers are resolved and any beta-driven changes are in, when a chapter is ready for a final line pass, or when the author explicitly asks to polish prose.
---

# /polish — the 5.0 pass

> **Tier 3 — procedural, and this one has a gate.** It refuses to run on structurally unresolved
> material and explains the cost before the author overrules it. Once running, it follows the
> documented order — cut, then passive voice, then weak verbs, then copyedit — and doesn't
> reorder it.

**Say this on invocation:** *Checking whether structure is locked here before I touch prose.
Polishing a chapter with a structural problem is wasted work — and worse, it makes the chapter
harder to cut later, because now it's pretty.*

**Source:** [`craft/revision/revision-and-diagnosis.md`](../../craft/revision/revision-and-diagnosis.md)

---

## The gate

**Ask before doing anything else:** has the material this skill is about to touch already been
through 2.0 self-revision, and — if the project used them — has alpha feedback been incorporated
(3.0) and beta-driven changes made (4.0)?

If the answer is no, or unclear, **refuse and explain the cost**, in these terms:

> Polishing prose fixes how a sentence reads. It does nothing for whether the scene, character
> arc, or promise underneath it is sound — and if that turns out to be broken, this pass has to
> be redone from scratch, on top of whatever structural rewrite follows. Worse: prose that reads
> well is *harder to cut*, because it no longer signals "rough draft, safe to remove." Polishing
> early makes bad structure stickier, not better.

Then point at what should happen instead: `/revision-map` if there's no map yet, `/revise` to
confirm which stage applies, or `/beta-read` if reaction hasn't been gathered.

**The author can overrule this.** If they do, proceed — but say once, plainly, that the gate was
overruled, and don't repeat the warning on every subsequent invocation for the same material.

---

## The pass, in order

Once the gate clears (or is overruled), work in this sequence. Don't interleave steps — cutting
after upgrading verbs means re-checking cuts you already made.

### 1. Cut ~10% of length

Look for what's cheap to lose without losing anything the reader needs:

- Redundant beats — the same information or emotion landed twice
- Throat-clearing — scene openings that delay the first thing that actually matters
- Description that outlasts its purpose — detail that continues after it's done its job
- Dialogue tags and beats that repeat what the dialogue already conveyed

Report the percentage actually cut against the target; don't force exactly 10% at the cost of
cutting something load-bearing, and don't stop short of it if more is genuinely dead weight.

### 2. Eliminate passive voice

Flag constructions where the actor is missing or demoted (*the dragon was seen* → *he saw the
dragon*), and convert unless the passive is a deliberate choice — e.g. the actor is unknown, or
the sentence is specifically about the thing being acted on rather than who acted.

### 3. Upgrade weak verbs to strong ones

Flag verb-plus-modifier constructions doing a stronger single verb's job (*walked quickly* →
*strode*; *was very angry* → *seethed*), and constructions leaning on *was/were* plus an adjective
where a verb would carry more.

### 4. Copyedit and proofread — last

Grammar, spelling, punctuation, formatting consistency. This step exists to catch what the first
three steps introduce as much as what was already there — a cut or a verb swap can leave a
dangling clause behind.

---

## Output format

```
── POLISH ── ch06/03-the-attic.md · gate: clear (2.0 and beta done)

  CUT — target ~10%, achieved 8%
    ¶4    redundant with ¶2's beat, cut
    ¶11   description outlasts the scene's need, trimmed to two lines

  PASSIVE VOICE — 6 flagged, 5 converted
    "the ladder was pulled down by him" → "he pulled the ladder down"
    "it was decided that" — kept; the actor is deliberately withheld here

  WEAK VERBS — 9 upgraded
    "moved quickly across" → "crossed"
    "was very quiet" → "went still"

  COPYEDIT — 3 items
    missing comma, ¶7 · doubled word, ¶14 · "it's" → "its", ¶19

── RESULT ── 1,340 → 1,232 words
```

---

## Rules

- **Refuse first.** Check the gate before reading for anything else. Don't polish and mention the
  structural risk afterward — the order matters, because seeing polished prose changes how the
  author weighs the warning.
- **The author can overrule the gate.** One clear statement that it was overruled, then proceed —
  don't relitigate it mid-pass.
- **Follow the documented order: cut, passive, weak verbs, copyedit.** Don't copyedit first because
  it's easier, and don't skip the cut because nothing obviously stands out — look again.
- **Preserve voice.** Check against `canon/voice-and-style.md` before changing a sentence; a
  strong verb that doesn't sound like the narrator isn't an improvement.
- **Never invent a proper noun or a fact while tightening a sentence.** A cut can remove
  information; it cannot add any that isn't already established.
- **This skill marks changes; it doesn't silently rewrite.** Show the before/after so the author
  can veto individual calls — that's what the output format's line-by-line pairs are for.
- **Don't run this on undrafted material.** There's no prose to polish; that's `/scene` or
  `/write`.

## Related

`/revise` · `/revision-map` · `/beta-read` · `/write`
