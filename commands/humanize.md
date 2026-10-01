---
name: humanize
description: Rewrite AI-sounding prose so it reads like the writer without changing what it says
---

Load the HumVisual skill and rewrite the text named by `$@`. If no argument is given, use the text the user
pasted.

## Read first

Read `./references/prose-patterns.md` before the first draft. Use the pattern index in `SKILL.md` to find the
tells, then read the full entry for each pattern you plan to act on.

## Mark, then rewrite

1. Mark every tell in the passage, strongest first, at sentence and paragraph scale.
2. Keep every supported claim. Add no fact, name, number, date, quote, or citation that the source or the user
   did not give you. If a sentence needs a detail nobody supplied, ask or write the shorter sentence.
3. Draft the rewrite without patching phrases one at a time. Vary sentence length.
4. Check the draft against the source claim by claim, then search again for §1 contrasts, §2 closers, §6 triads,
   §8 dashes, and §19 bold labels.

## Voice

If `$@` includes a writing sample, match its sentence length, word choice, punctuation, openings, transitions,
and dash rate. Without a sample, take the voice from the kind of text: personal writing keeps opinions and
asides, reference and technical writing stays neutral.

## Return

- Pasted text: the draft, the patterns still present, then the final rewrite.
- A named file: write only the final text, keep code, commands, paths, YAML, data, and link targets unchanged,
  then summarize.
- Another task such as a commit message or pull request: return only the final text.
