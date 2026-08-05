# Chapter Mode

Drafting prose, one beat at a time.

## Starting a chapter session

1. Read `manuscript/_status.md` to find the active chapter.
2. Read that chapter's `_chapter.md` — goal, entering/exiting state, beat sheet.
3. If the chapter has no `_chapter.md`, build one first from `.claude/templates/chapter.md`
   and the governing `plot/` docs. Show it to the author and get it approved before drafting a word.
4. Read the pre-writing checklist docs (`CLAUDE.md` §3).
5. Read the last ~300 words of existing prose in the chapter.

## The exchange

### Step 1 — Choose your offer type

Two kinds of offer. Pick per beat, and say in one line which you're using.

**DIRECTIONS** — when the story is at a genuine fork and the choice changes what happens.

```
NEXT BEAT — the dragon has been in the shed two days

A) He tries to talk to it for the first time
B) The neighbor knocks
C) It gets worse overnight — the wing wound is infected
D) He goes to work and spends the whole shift not being there

> 
```

Two to four options. One line each. Concrete and specific — "he lies to the neighbor," not
"a complication arises." They should be genuinely different stories, not the same beat at
three temperatures.

**PROSE VARIANTS** — when the path is settled and only the execution is in question.

```
NEXT BEAT — he touches it for the first time. Three ways in:

A) [~150 words — slow, tactile, almost nothing happens]
B) [~150 words — it flinches first and he freezes]
C) [~150 words — he narrates around it, retrospective, delaying the moment]

> 
```

Write the variants out in full. A variant described is not a variant.

**Which to use:** directions when the *plot* could go more than one way. Variants when the plot
is fixed and the question is tone, pacing, or angle. When in doubt, directions — cheaper to be
wrong before the prose exists.

### Step 2 — Take their answer

They'll reply with a letter, or with something else entirely. Something else is normal and
expected. Take it and write that. Do not re-offer, do not ask them to reconsider.

If what they pick conflicts with the continuity ledger, say so *before* writing — name the
entry, state the conflict in one sentence, ask whether to retcon it or work around it.

### Step 3 — Write

100–300 words, appended to the current scene file. Real prose:

- First person, retrospective past. He's telling this from somewhere afterward.
- No exposition dumps. If it needs history, the scene has to demand the history.
- Concrete over abstract. What he sees, what it smells like, what his hands are doing.
- No proper nouns not in `canon/names-and-terms.md`.
- End the chunk somewhere with forward pressure — a chunk that resolves itself gives the next
  exchange nowhere to go.

If starting a new scene, create the file from `.claude/templates/scene.md`, fill the header
comment, and add it to the `_chapter.md` beat sheet.

### Step 4 — Log

Append to `sessions/log/YYYY-MM-DD.md`. One line per fact established:

```
- [ch01/02-the-crash] the-dragon.md → Visual: left wing torn at the third joint
- [ch01/02-the-crash] canon/continuity-ledger.md → dragon cannot fly, duration TBD
```

Write through to the real document *now* if the fact is canon-changing (new proper noun,
world rule, revealed plot fact, new character or place, ledger-worthy). Otherwise it waits
for scene end.

### Step 5 — Report

The receipt block. Then stop and wait.

## Scene end

When the scene is done — the author says so, or the beat's exiting state is reached:

1. Run the full promotion path (`doc-protocol.md`)
2. Update the beat's status in `_chapter.md`
3. Update word count in `manuscript/_status.md`
4. Update `sessions/_current.md`
5. Give a 3–4 line scene summary: what happened, what changed for the protagonist, what it
   planted, what's next

Then ask whether to continue to the next scene or stop.

## Revising existing prose

If the author wants to change something already written, treat it as its own exchange: offer 2–3
approaches to the revision, make the change, and check whether it invalidates any continuity
ledger entry. If it does, update the ledger with a strikethrough and a pointer — never delete
the old entry.
