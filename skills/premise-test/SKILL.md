---
name: premise-test
description: Run the six consequential questions against a premise to find out whether it's a novel or a setting. Use when a premise is in hand and needs pressure-testing, before outlining, when a story idea feels thin without being able to say why, or when the author asks whether a concept can actually carry a book.
---

# /premise-test — the six consequential questions

> **Tier 2 — diagnostic.** The six questions, and the transplant read on question five, are the
> test. My score on how well the premise clears each one is a **ranked hypothesis, not a
> verdict** — the author is the one who knows whether a dilemma is genuinely unique to this
> premise.

**Say this on invocation:** *Running the six consequential questions — I'll rank how well this
clears each one and flag the weak ones, not hand down a verdict.*

**Source:** [`craft/process/idea-generation.md`](../../craft/process/idea-generation.md)

---

## The six questions

| # | Question |
|---|---|
| 1 | What does the premise **allow** the protagonist to do? |
| 2 | What does it **prevent** them from doing? |
| 3 | **Who benefits** from this situation? |
| 4 | **Who is harmed**? |
| 5 | What **difficult choice is unique** to this premise? |
| 6 | What **promise** does the premise make to the reader? |

---

## Question 5 is the test

> If the premise doesn't generate a dilemma that couldn't happen in another story, you have a
> setting rather than a novel.

A setting is a place plus a threat. A novel is a place plus a dilemma **that place's specific
mechanics produce and no other backdrop would.** The question isn't whether the choice is hard —
it's whether the choice is *this premise's*, or whether it would survive being dropped into an
unrelated story unchanged.

**Question 6 hands off directly to** [`craft/plot/promises.md`](../../craft/plot/promises.md) —
the premise is already promising something to the reader, and it's worth knowing what before the
opening pages get written. See `/promises` for the full manuscript-level audit once prose exists.

---

## Procedure

**1. Get the premise as one sentence.** Not a pitch, not a world description. If it can't be
stated in one sentence, that's a finding on its own — say so before scoring anything.

**2. Work questions 1–4 concretely.** Push for specifics over theme. *"It challenges his beliefs"*
is not an answer to what it prevents; *"he can't go to the authorities because his own reputation
is the noise that would bury a real report"* is.

**3. Isolate the dilemma for question 5.** State it as a forced choice, not a general theme. Then
run the transplant check: could a character in an unrelated story face this same choice, moved to
a different setting, and lose nothing that makes it work? If yes, flag it — this is the single most
common way an idea-generation pass fails.

**4. Name the promise (question 6).** Cross-check it isn't already contradicted by the answers to
1–4 — a premise that prevents X while promising X is a live conflict, not a formality.

**5. Rank each question**, not just question 5, using the evidence gathered — not a restatement of
the premise's own pitch.

---

## Output format

```
── PREMISE ──
   "A Boston conspiracy theorist who has researched dragons his whole life
   as a hobby watches real ones fly over the city, then finds a wounded one
   in his backyard that same night."

── SIX QUESTIONS ──

  1. ALLOWS       ●●●  he has exact, decades-deep expertise no institution
                        will credit
  2. PREVENTS     ●●●  can't go to authorities — his own reputation is the
                        noise that would bury a real report
  3. BENEFITS     ●●○  the dragon, obviously — no one else named yet
  4. HARMS        ●●○  him, socially — who's harmed if he succeeds is still
                        open
  5. UNIQUE       ●●●  see transplant check below
  6. PROMISE      ●●○  "the guy everyone dismissed was right" — doesn't yet
                        say what that costs him

── TRANSPLANT CHECK (Q5) ──
   Could "someone finds a wounded animal and hides it" happen in another
   story? Yes — trivially. Could HIS specific choice — trusting decades of
   dismissed research over his own instinct for self-preservation, with no
   one left who'd believe him even if he told them — happen to a different
   character in a different setting and still make sense? No.
   ✓ Reads as a novel, not a setting.

── FINDINGS ──
   Clears the test on Q5, the load-bearing one. Weakest links are Q3 and
   Q4 — benefit and harm are currently one-directional. Worth naming who
   pays if he's right before treating the premise as locked.
```

---

## Rules

- **Rank every question with the evidence behind it** — never a flat pass/fail, and never a
  restatement of the pitch dressed up as an answer
- **Always isolate question 5 as its own step**, with an explicit transplant check. It's the one
  that decides novel vs. setting, and the one authors skip because it's the least comfortable
- **State the base rate plainly:** a setting mistaken for a premise is the most common way this
  test fails
- **Don't rewrite the premise.** Point at where it's thin; repair happens in `/new-story` or
  `/write`
- **If the premise won't compress to one sentence**, say so before scoring anything else

## Related

`/new-story` · `/brainstorm` · `/scale` · `/write`
