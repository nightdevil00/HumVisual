# Guide for agents

This file explains how to change HumVisual without breaking its package or prompt.

## What this repo contains

HumVisual is an agent skill written in Markdown and HTML. `SKILL.md` is the prompt agents read. The repo has no
build step.

Keep the skill portable. Do not write instructions that limit it to one or two agent tools.

## Key files

- `SKILL.md` is the source of truth and the only skill file. It holds the routing between the two jobs, the rules
  both share, the prose workflow with a 26-pattern index, the visual invariants, and the delivery checklist.
- `references/prose-patterns.md` holds the 26 tells with watch lists, reasons, and examples. It is the only place
  a pattern is defined.
- `references/css-patterns.md`, `references/libraries.md`, `references/themes.md`, `references/slide-patterns.md`,
  and `references/responsive-nav.md` hold the visual material. `templates/` holds four reference pages.
- `commands/` holds the prose and visual entry points. `quick/` holds the compact spec and its local renderer.
  `pptx/` and `mcp/` are optional Node utilities that keep their upstream names.
- `README.md` explains installation, use, and the patterns. `CHANGELOG.md` holds the release notes, newest first,
  followed by the two upstream histories.
- `.claude-plugin/plugin.json` describes the Claude plugin and points its skill loader at the root `SKILL.md`.
  `.claude-plugin/marketplace.json` lets users add the folder as a marketplace. `.cursor-plugin/plugin.json`
  describes the Cursor plugin. Omit a `skills` path there so Cursor loads the root `SKILL.md`.
- `agents/openai.yaml` holds the display name, short description, and default prompt for OpenAI-compatible agents.
- `scripts/validate-package.py` checks the package files and the values they share.

## Rules for changes

Keep `SKILL.md`, `README.md`, and `references/prose-patterns.md` in sync.

- **Patterns:** Patterns are numbered from 1 without gaps, strongest and most frequent first. A new tell earns a
  pattern only when no existing pattern already implies it, so prefer folding it into an existing pattern. If you
  add, remove, or renumber a pattern, update the index table in `SKILL.md`, the table in `README.md`, and every
  `§` reference. The validator derives the count from the reference headings and checks that the README names
  match them.
- **Prose and visual halves:** A request that needs both runs the prose pass first, then the page. Keep that order
  in the prompt, because page copy written before the prose pass tends to carry the tells the prose rules remove.
- **Version:** Keep the same version in `SKILL.md` under `metadata.version`, the first `CHANGELOG.md` heading,
  `.claude-plugin/plugin.json`, the marketplace entry, `.cursor-plugin/plugin.json`, and `package.json`. Do not
  add a top-level `version` field to the skill.
- **Compatibility:** Keep install and use instructions neutral across agents. Names such as Claude Code, Cursor,
  OpenCode, Codex, and Pi are examples, not limits. Keep the optional utility names, the MCP resource URIs, and the
  quick schema `$id` as they are, so existing host configurations keep working.
- **Description:** Every manifest uses the first sentence of the `SKILL.md` description.
- **Length:** Every word of `SKILL.md` is read on each use. The validator caps it at 5,500 words; a change that
  adds words should earn them. New detail belongs in a reference file the prompt routes to.
- **Self-consistency:** `SKILL.md` follows its own prose rules, so it carries no em dash and the validator fails
  the build when one appears. Keep page-level rules in the checklist too.
- **History:** Add a short `CHANGELOG.md` note for any behavior change or non-obvious fix.
- **Checks:** Before publishing, run `python3 scripts/validate-package.py` and `claude plugin validate .`.

## Writing style

Use Plain Language in code comments, prompts, documentation, descriptions, validation messages, and progress
reports.

- Lead with the main point.
- Use common words and active voice.
- Keep sentences and paragraphs short.
- Use one term for the same item.
- Use `must` for requirements.
- Use headings, lists, and tables when they help the reader.
- Remove repeated or unnecessary words.
- Limit acronyms and explain technical terms.
- Avoid double negatives.
- Keep exact identifiers, commands, paths, schema fields, quotations, watched phrases, and behavior-bearing
  examples.
- Keep the full technical meaning.

## Editing the skill

- Keep the YAML metadata valid.
- Treat the prompt below the metadata as the product.
- Prefer a short, clear instruction over another exception or repeated explanation.
