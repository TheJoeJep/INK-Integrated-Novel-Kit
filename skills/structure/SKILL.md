---
name: structure
description: Pick a structure model by the symptom it fixes, not by preference — Story Circle, three-act/midpoint, Major Dramatic Question, or try-fail. Use when a draft or outline is wrong in a way you can't name, when character growth feels unearned, when the middle feels shapeless, when a subplot feels disconnected from the main story, or when nothing seems to be progressing. Also use when the author is already drawn to a specific model and wants it checked against the actual problem first.
---

# /structure — pick the model by the symptom

> **Tier 2 — diagnostic.** These are **ranked hypotheses tied to a symptom, not a verdict.** The
> author confirms which model actually fits before anything gets restructured around it.

**Say this on invocation:** *Matching a structure model to the symptom — ranked, not prescribed.
Confirm which one's real before we build around it.*

**Source:** [`craft/structure/structure-models.md`](../../craft/structure/structure-models.md) ·
[`craft/structure/try-fail-cycles.md`](../../craft/structure/try-fail-cycles.md)

---

## The rule

A model reached for because it's familiar, or because it was the last one read about, is how you
end up building the wrong scaffolding. **Pick by symptom.** If the symptom doesn't clearly point
at one, say so — that's a real finding, not a reason to guess.

## The symptom map

| Symptom | Model | Why it fits |
|---|---|---|
| Character growth feels unearned, arbitrary, or sudden | **Story Circle** | Forces a stated moment of rest and a stated moment of return, so the *difference* between them has to be nameable |
| The middle sags — things happen, nothing seems to build | **Three-act / midpoint** | Gives act two a hinge — escalation, reframing, or making it personal — instead of letting it just continue |
| A subplot or sequence reads as a side quest | **Major Dramatic Question** | Forces the one question the book actually answers into a single line, then tests every thread against it |
| Things happen but nothing is *accomplished* — stakes feel flat | **Try-fail cycles** | Forces each attempt to be intelligent, fail for a real reason, and escalate — which is where the sense of progress actually lives |

None of these require the whole model adopted wholesale. Each is reached for to fix a *specific*
shapelessness — apply only as much of it as the symptom needs.

---

## The Lucas cautionary tale

**The reason this skill insists on symptom-matching instead of preference, told in full because
it's worth remembering exactly:**

Lucas loved Campbell's monomyth, and used it to real effect in the original trilogy. By the
prequels, in Sanderson's reading, he'd **turned it into a checklist.** The monomyth calls for
divine parentage in its hero — so *The Phantom Menace* gives Anakin a virgin birth. Sanderson was
in the room at the opening-night screening. The audience — people who had brought lightsabers —
went *oh*. Collectively. At that moment.

> Anytime a structure becomes too rigid for you as a writer, you can start using even your own
> outline to the point that it negatively impacts your story. If it doesn't match your story once
> you're in it, be willing to throw it away.

**The same warning applies to three-act and to *Save the Cat*** — reading either and concluding a
specific beat has to land on a specific page. Nobody checks page counts in prose. A framework used
this way stops being a diagnostic and becomes an obligation the story is paying off instead of the
reader.

**Frameworks must stay disposable.** The moment a model stops matching the story mid-draft, the
model loses, not the story — and this skill should say so the moment it notices, not defend the
model it just recommended.

---

## Procedure

1. **Get the symptom as an experience, not a diagnosis already in the author's language.** *"The
   middle feels shapeless"* is data. *"I need a stronger midpoint"* is already a prescription — take
   it as one hypothesis, not the answer.
2. **Match against the table.** Usually more than one row is plausible — rank them.
3. **Check evidence against the relevant model's own checks** in `structure-models.md` before
   confirming a hypothesis.
4. **Say the Lucas warning aloud** if a model is about to be adopted for anything more than the
   specific symptom that produced it.

---

## Output format

```
── SYMPTOM ──
   "his arc doesn't land — by the end he's brave, but I can't say why"

── HYPOTHESES ── ranked by symptom match, checked against the outline

  1. STORY CIRCLE — unearned growth  ●●●  most likely
     No step-one baseline is stated for what he can't yet do.
     → craft/structure/structure-models.md (Harmon's circle)
     Confirm: can you point at the moment of rest and the moment of
     return, and state the difference in one line?

  2. MAJOR DRAMATIC QUESTION — untested subplot  ●●○
     The rescue thread and the arc thread may not yet be the same question.
     → craft/structure/structure-models.md
     Note: if they test as separate questions, the arc may be arcing
     for no reason the plot cares about.

  3. TRY-FAIL — growth asserted, not forced  ●○○
     Check whether any obstacle actually compels the change under the
     obstacle rule, or whether it's simply stated as having happened.
     → craft/structure/try-fail-cycles.md

── CAUTION ──
   Don't default to Story Circle because it's the familiar one here.
   Confirm #1 against the actual outline before restructuring around it.

── NEXT ──
   Confirm which lands, or run /character-arc for the axis-level check.
```

Confidence as `●●●` / `●●○` / `●○○`, same convention as `/diagnose`.

---

## Rules

- **Never hand down a verdict.** Rank hypotheses, confirm with the author before treating one as
  settled
- **Always name which symptom the model treats.** A model recommended without a stated symptom is
  preference wearing a diagnosis's clothes
- **State the Lucas warning whenever a model is about to be adopted wholesale**, not just consulted
  for one check
- **Flag checklist creep explicitly.** If a later beat is being shaped to satisfy the model rather
  than the story, say so — that's the failure this skill exists to prevent
- **Frameworks stay disposable.** If the story stops matching mid-draft, recommend dropping the
  model, not bending the story to keep it
- **Don't fix.** Restructuring goes through `/write`; this skill diagnoses which tool to reach for
- **Don't assign a model to a symptom absent from the map without saying you're improvising**

## Related

`/diagnose` · `/outline` · `/genre-mine` · `/beat` · `/write`
