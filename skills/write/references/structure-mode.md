# Structure Mode

Story-level work. No prose gets written here.

On entry, ask which:

```
  1. DECISION — settle something: an open question, a name, an outline change, a world rule
  2. AUDIT    — I read the project and report what's broken or missing
```

---

## Decision

Same loop as Chapter Mode, aimed at documents instead of prose.

### Step 1 — Frame it

State the question in one sentence, and state what it blocks. If it's from
`story/open-questions.md`, read that entry first — it may already have options on the table
and a history of prior thinking.

### Step 2 — Offer

Two to four options. For each: the option in one line, then what it costs and what it buys.
Lead with your recommendation and say why.

```
OPEN QUESTION #2 — Manifesting: hard rules, limits, costs
Blocks: every action scene, and the whole Act 3 race

A) Perception-only — dragons see how reality is assembled; changing it is
   slow, deliberate, and physically expensive.
   Buys: keeps them fearsome without making them invincible. Costs: weak in
   fast action beats — you'll need other tension in fights.

B) ...

Recommend A — the erasure premise needs manifesting to be *unimpressive*
in the short term, or the Custodians would never have needed a 10,000-year
information campaign.

> 
```

That last move — checking a proposed rule against the rest of the premise — is the job. Don't
offer options you haven't tested against what's already locked.

### Step 3 — Write the decision into the docs

Not a summary of the decision. The decision, in the documents where it belongs, in the right
template sections. A world rule goes in `world/`. A name goes in `canon/names-and-terms.md`
with its register (who says it, who doesn't) and status `LOCKED`. A structural change goes in
`story/outline.md` and every affected `plot/` doc.

Then update `story/open-questions.md`: mark it resolved, date it, and record *why* — the
reasoning is worth more later than the answer.

### Step 4 — Check the blast radius

Before reporting, check whether this decision contradicts anything in
`canon/continuity-ledger.md` or invalidates a `plot/` doc. Name what it touches. This is the
main way structural revision breaks a manuscript, and it is cheap to catch here.

### Step 5 — Report

`── DECIDED ──` block naming every document changed. Then stop.

---

## Audit

Read the project and report what's wrong. Findings only — fixes come after, one at a time,
through the decision loop.

### What to check

| Check | Looking for |
|---|---|
| **Contradictions** | Two documents asserting incompatible facts |
| **Undocumented prose** | Facts established in `manuscript/` with no home in a doc |
| **Stale docs** | Docs asserting things the manuscript has since changed |
| **Blocking questions** | Open questions now gating work in progress |
| **Orphaned plot points** | `plot/` docs with no chapter assigned |
| **Unplanted reveals** | Reveal-ladder rungs with nothing planted in Act 1 to reinterpret |
| **Dead plants** | Plants with no payoff, payoffs with no plant |
| **Unnamed placeholders** | `PLACEHOLDER` terms in `canon/names-and-terms.md` blocking dialogue |
| **Structural drift** | Prose violating `story/structural-rules.md` — exposition dumps especially |
| **Empty Visual blocks** | Characters or places appearing in prose with no maintained description |

### Reporting an audit

Ranked by severity. For each: what's wrong, where, and what it costs to leave alone.

```
AUDIT — 6 findings

BLOCKING
1. Manifesting has no limits defined. ch01 beat 4 needs the dragon to fail at
   something and there's no rule saying what it can't do.
   → world/manifesting.md

INCONSISTENT
2. protagonist.md says he has no car; ch01/01 has him driving home.
   → conflict with continuity-ledger entry 2026-08-04

...

Work them in order? Or pick one.
```

Do not fix anything during the audit. Report, then take his pick and run the decision loop
on it.
