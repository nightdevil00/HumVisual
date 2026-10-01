# Changelog

## 1.0.0

Merged Humanizer 3.1.0 and visual-explainer 0.11.0 into one skill package, with one prompt and one folder.

### Added

- Merged `SKILL.md`. It opens with a routing table that sends each request to the prose job or the visual job, then holds the rules both jobs share, the prose workflow with a 26-pattern index, the visual invariants, the slide deck and quick mode rules, and a part on requests that need both halves.
- Added `references/prose-patterns.md`, holding the 26 tells with their watch lists, reasons, and before and after examples. Pattern numbers 1 to 26 are unchanged from Humanizer 3.1.0, so every `§` reference still resolves.
- Added `commands/humanize.md`, the prose entry point in the shape of the visual commands.
- Added `examples/humvisual-paper.html`, a paper written in the merged style that shows the text half and the visual half on the same content.
- Added `scripts/validate-package.py`, which checks version sync across every manifest, one root `SKILL.md`, pattern numbering in the reference, pattern names in the README index, `§` reference targets in `SKILL.md` and the commands, the 5,500 word budget on `SKILL.md`, no em dash in `SKILL.md`, the files the prompt routes to, command frontmatter, `package.json` binaries, and both upstream copyrights.
- Added `AGENTS.md`, `package.json`, and a merged `.claude-plugin/` and `.cursor-plugin/` manifest set. All manifest descriptions use the first sentence of the `SKILL.md` description.

### Changed

- Moved the skill to the folder root. The visual half used to live at `plugins/visual-explainer/`, so the skill, references, templates, and commands are now siblings, and every `./references/...` and `./templates/...` path in the prompt and the commands resolves from the root.
- Renamed the harness-neutral project config to `humvisual.config.md` and the Claude local override to `.claude/humvisual.local.md`.
- Pointed the command templates and template file headers at HumVisual.
- Kept the upstream names for the optional Node utilities: `visual_explainer`, `visual-explainer-mcp`, `visual-explainer-pptx`, the MCP resource URIs, and the quick schema `$id`. Existing host configurations keep working.

### Unchanged

- All 26 prose patterns, their numbering, their watch lists, and their examples.
- The visual invariants, the 11 palettes, the five font pairs, the four templates, the quick schema, and the slide deck engine.

### Upstream history

The releases below are the histories of the two merged skills. Their pattern numbers are the numbers each release
used.

### Humanizer 3.1.0

- Added pattern #26 and section F for replies that re-explain context the reader already has (#269). It acts on replies, not standalone writing. 26 patterns total.
- Extended the core rule so "something the reader did not already have" counts the surrounding conversation, not only earlier text.
- Widened #25 to text that describes its own sourcing, assembly, or layout (#290), and added headings written for effect to #20.
- Extended #2 to "That distinction matters." (#277) and to a sentence that explains what an example already showed (#295).
- Narrowed #10 so words the dictionary always hyphenates keep their hyphen. Gave each watched word one pattern, and stated the evidence rule and the no-invention rule once each.
- Fixed the Voice section's dash reference (#273) and the marketplace schema URL (#288).
- Added a Cursor plugin manifest (#278).

### visual-explainer 0.11.0

- MCP users can choose where local HTML renders are saved with `VISUAL_EXPLAINER_OUTPUT_DIR`, and the default stays `~/.agent/diagrams/`.
- Added rem-based type-scale guidance for non-slide pages, with copyable role selectors and readable minimums. Based on PR #95 by @ZanziPanzi.
- Added a reduced-motion slide budget check that marks vertical overflow and `autoFit()` fallbacks instead of silently clipping content. Reported by @bertheto in #92.
- Guarded the responsive table-of-contents history update for `file://` pages so local scrolling works without console errors. Based on PR #94 by @ZanziPanzi.
- Fixed the stale nested Claude plugin version that made Claude Code report the wrong latest version after 0.10.0, and added a version check across package, marketplace, plugin, and skill metadata. Reported by @proxet-p35 in #93.
- Earlier releases added the design-judgment section, project design-system precedence, content-anchored aesthetic directions, diagram rhetoric guidance, and the dual color scheme baseline.
