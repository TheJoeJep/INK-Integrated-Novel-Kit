# INK — Integrated Novel Kit

A writing system for novelists working with an AI collaborator. It holds a craft knowledge base,
40 skills, a documentation architecture, and a local reading dashboard.

**It is built to help you write. It is not built to write for you.** That distinction shapes
every design decision below.

> Craft knowledge derived from **Brandon Sanderson's** publicly published writing lectures, with
> guest material from **Mary Robinette Kowal** and **Brandon Mull**, and techniques Sanderson
> credits to **Dave Wolverton**. See [CREDITS.md](CREDITS.md).
>
> **Go watch the lectures.** They're free, they're better, and they're his.

---

## What you get

| | |
|---|---|
| **`craft/`** | 34 documents distilled from 39 lectures — plot, structure, character, viewpoint, prose, dialogue, worldbuilding, revision, short fiction, publishing |
| **`skills/`** | 40 skills, from `/brainstorm` to `/synopsis` |
| **`templates/`** | Document scaffolds for characters, places, factions, plot beats, subplots, chapters, scenes |
| **`dashboard/`** | A local reading view with a context sidebar that follows your scroll |

---

## The idea it's built on

**Every skill declares how much you should trust it.**

A system that sounds equally confident about verifying a fact and inventing a character will
mislead you on the second. So skills carry a tier, and say it out loud when they run:

| Tier | Does | Trust |
|---|---|---|
| **1 · Mechanical** | Verifies against a documented rule | **High.** There's a right answer |
| **2 · Diagnostic** | Symptom → cause, using documented base rates | **Good.** Ranked hypotheses, not verdicts |
| **3 · Procedural** | Runs a documented process | **Good for the process.** Won't let you skip stages |
| **4 · Generative** | Produces raw material | **Lowest — and it says so** |

`/threads` reports flatly because unclosed threads are a fact. `/beta-read` states plainly that
it is not your audience and cannot replace real readers.

That gradient came from being caught: three frameworks were built into the craft base from a
summary and turned out **not to exist in the lectures at all.** Everything is now sourced to a
transcript, and anything that isn't Sanderson's is labelled `[not from the lectures]`.

---

## Getting started

```bash
git clone <this repo> my-novel
cd my-novel
```

Open it in Claude Code and say **`/new-story`** — or **`/import`** if you already have a
manuscript.

Then the loop is `/write`. Everything else exists for when something goes wrong.

### The reading dashboard

```bash
python dashboard/serve.py "path/to/your/novel"
```

Serves at `localhost:8778`, rebuilds within seconds of any file changing. `--lan` makes it
readable from your phone on the same network.

---

## How it's organised

```
story/     the shape of the book — premise, rules, outline, open questions
canon/     the constraints — continuity ledger, names, voice
world/ factions/ characters/ places/    the documentation
plot/      one small doc per beat, plus subplots/
manuscript/    the prose. One folder per chapter, one file per scene
sessions/  resume pointer and logs
craft/     the knowledge base
```

**`story/` versus `canon/` is the important split.** `story/` is what the book is *trying* to be
— change it freely. `canon/` is what the text has already committed to; changing it means
retconning prose that exists.

---

## Design principles

**Documentation is maintained, not reconstructed.** Every fact a scene establishes goes into a
document in the same exchange that wrote it. Nothing lives only in the prose.

**Craft is looked up, not guessed.** Skills consult the craft base and name the technique they're
using, so you learn the vocabulary by watching it work.

**The markdown is the database.** The dashboard derives everything from your files and writes
nothing back — so it can't drift, and no skill had to learn a second format.

**Findings and repairs are separate.** Checks report; `/write` and `/revise` fix. A check that
silently edits is a check you can't trust.

**The author decides.** Skills offer options, write what's chosen, and say once when they think
a choice is costly. They don't relitigate.

---

## What it doesn't do

- **It doesn't replace beta readers.** `/beta-read` says so every time it runs
- **It doesn't cover the masquerade problem** — why a hidden magical world stays hidden. Checked
  across all 39 lectures; it isn't there, and the docs say so rather than improvising
- **It doesn't do live voice conversation.** Turn-by-turn only. See [`voice/`](voice/README.md)

---

## Licence and attribution

The architecture, skills, templates and craft rewrites are offered freely — see [LICENSE](LICENSE).
The underlying teaching is Sanderson's, Kowal's, Mull's and Wolverton's, and is not ours to
license.

If this is useful, go
[watch the lectures](https://www.youtube.com/playlist?list=PLSH_xM-KC3ZvzkfVo_Dls0B5GiE2oMcLY)
and buy their books.
