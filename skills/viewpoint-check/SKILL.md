---
name: viewpoint-check
description: Check point-of-view discipline against the declared mode's own rules — detect mid-scene head-hopping, drift between narrator modes, and viewpoints carrying no promise of their own. Use when a scene reads distant, confusing, or inconsistent in perspective, when introducing a second viewpoint character, before drafting a scene with a mode shift, or when the author asks whether a POV choice or a withholding is working.
---

# /viewpoint-check — viewpoint discipline audit

> **Tier 1/2 hybrid.** Detecting head-hopping, mode drift, and a viewpoint with no promise of its
> own is mechanical — the mode either holds or it doesn't. Whether a withholding reads as a
> legitimate technique or as a cheat, and whether a viewpoint's promise is strong enough, are
> judgement calls — marked separately.

**Say this on invocation:** *Checking viewpoint discipline — the mode violations are mechanical;
whether a withholding reads as fair, I'll mark as opinion.*

**Source:** [`craft/viewpoint/viewpoint.md`](../../craft/viewpoint/viewpoint.md)

---

## The rule being checked

Read the source file first. The short version:

**First person has three modes, and they're not interchangeable:**

| Mode | Buys | Costs |
|---|---|---|
| **Epistolary** | Built-in mystery; hiding information doesn't read as a cheat — *it just wasn't in that letter* | Rigid form; verbatim-memory strain |
| **Flashback** | "Pay attention, this matters later" doesn't feel like cheating — the narrator survived and is allowed to say so | The narrator obviously survived — tension from *will they live* is gone |
| **Cinematic/immediate** | Real-time intimacy; unreliable narration is easy — *too painful, I'll get to it* is accepted | Less license to foreshadow than flashback |

**Third limited:** one character's perceptions per scene. Buys credibility and the
perception-vs-reality gap; **costs that hiding information reads as cheating.** Sanderson's own
admission belongs here as the calibration point: concealing Kelsier's secret in *Mistborn* through
third-limited narration is, in his words, **"absolutely cheating"** — and sometimes a necessary
one. The rule is real; breaking it deliberately is still a choice with a cost, not a free pass.

**Present narrator (omniscient hybrid):** "pay attention, this matters later" **does** read as
cheating here, unlike in flashback.

**The dead viewpoint:** a POV with no promise of its own — no want, question, or stake that
belongs to it — is one readers learn to skim.

**Mixing modes deliberately:** if a late mode switch is coming, seed the pattern early. *Skyward*
plants third-limited interludes at chapter ends throughout the book so the climactic switch
doesn't jar. One earlier instance is enough to make it a convention instead of a violation.

**Multiple viewpoints, separated from the start:** each thread needs its own promise and visible
progress or it reads as a diversion — the Finn/Rose failure in *The Last Jedi*, which Sanderson
names his own parallel problem in *Oathbringer* and fixed the same way: giving the viewpoint
character a personal stake.

---

## Procedure

**1. Scope.** Current chapter by default; whole manuscript on request.

**2. Identify the declared mode per viewpoint** — not "first person," but *which* of the three, or
third limited, or omniscient. Cite where it's established. This is the check everything else
depends on.

**3. Mechanical checks:**
   - **Head-hopping** — does any single scene contain another character's interior perception
     inside a third-limited or single-viewpoint first-person passage? Cite the line.
   - **Mode drift** — within one narrator's material, does it slide between immediate/cinematic
     framing and retrospective/flashback framing (tense shifts, "I would learn later," foresight
     the immediate mode hasn't earned)? Cite each instance.
   - **Dead viewpoint** — for each viewpoint, is there an identifiable want, question, or stake
     established in its own material? If none, flag it.
   - **Tense correlation** — cinematic tends present; epistolary, flashback, and epic third
     limited tend past. A mismatch isn't automatically wrong, but it's a reader-expectation flag.

**4. Judgement checks — route to `── OPINION ──`:**
   - **Withholding.** Does the viewpoint character clearly know something the narration doesn't
     share? If the mode is third limited or present narrator, name it as reading like a cheat by
     the book's own rule, and cite the Kelsier precedent as the calibration for whether it's the
     necessary kind. If the mode is flashback or cinematic, the withholding has more license —
     say so.
   - **Survival tension.** If any viewpoint is flashback or retrospective first person, survival
     is already known. Ask where the scene's tension is actually coming from instead — and if you
     can't name it, that's the finding.
   - **The unearned late switch.** If a mode switch is planned or has occurred, was the pattern
     seeded earlier — even once? If not, flag it as unearned.
   - **Separated viewpoints.** If viewpoints are apart rather than sharing scenes, does each carry
     its own promise and visible progress, or is one riding on the other's investment?

---

## Output format

```
── VIEWPOINT ── ch01, 2 viewpoints

  MODE
    protagonist    third limited, past tense              declared ch01/01
    the dragon     no viewpoint scenes yet                —

  ✓  HEAD-HOPPING       none found
  ✗  MODE DRIFT         ch01/05 — one line of the dragon's interior perception
                         inside a protagonist-POV scene ("she registered him
                         as harmless")
  —  DEAD VIEWPOINT     n/a, single viewpoint in scope
  —  TENSE              consistent with third-limited convention

── FINDINGS ──
  1 head-hop-adjacent drift · 0 dead viewpoints in scope

── OPINION ──
  ⚠  WITHHOLDING — ch01/06: the protagonist notices something about the
     dragon's wing he doesn't share with the reader. In third limited that
     reads as a cheat by the book's own rule — Sanderson names the identical
     move in Mistborn "absolutely cheating, and sometimes a necessary cheat."
     Whether it's the necessary kind here depends on whether the eventual
     payoff earns it. That's your call, not a mechanical finding.

  •  No flashback or retrospective narration in scope, so the survival-tension
     question doesn't apply yet.

  •  No mode switch planned in this scope — nothing to check for seeding.
```

`✓` clean · `✗` violation · `⚠` opinion flag · `—` not applicable in scope

---

## Rules

- **Name the mode before anything else.** "First person" is not specific enough — it's one of
  three modes with different rules, and the rest of the check is meaningless without it.
- **Head-hopping and mode drift are cited with an exact location and quoted fragment**, never
  "it feels like." This is bookkeeping, not impression.
- **Judgement calls always go in the `── OPINION ──` block**, never mixed into the mechanical
  table — this includes every withholding call, every survival-tension question, and every
  seeded-or-not judgement.
- **The Kelsier precedent exists to calibrate, not to excuse.** Citing it says "this kind of
  cheat can be necessary," not "this instance is fine." Say which you think it is.
- **Don't fix.** Findings and opinion only — repair is `/write` in Structure Mode.
- **Report clean runs plainly.** *2 viewpoints, no drift, no dead viewpoints.*


**Delegation:** this check fans out. Dispatch Sonnet subagents per file or per sub-check rather than working sequentially in the main thread — see [skills/_CONVENTIONS.md](../_CONVENTIONS.md). Delegate gathering; keep judgement.

## Related

- `/diagnose` — if a scene feels flat or distant and the cause isn't obviously viewpoint
- `/motivation` — a dead viewpoint and an unmotivated character often share a root cause
- `/pacing` — separated viewpoints without visible progress show up in both audits

