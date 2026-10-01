---
name: humvisual
description: |
  Rewrite AI-sounding prose so it reads like the writer without changing what it says, and turn systems, code
  changes, plans, data, and technical concepts into self-contained HTML visual explanations. Use for AI tells in
  a draft (not-X-but-Y contrasts, one-line closers, staged openers, forced triads, dash overuse, inflated
  claims, sales language, stock AI words, bold labels, chat residue), and for diagrams, architecture overviews,
  diff or plan reviews, project recaps, comparison tables, slide decks, and any other visual explanation.
license: MIT
compatibility: No build step. Visual output needs a browser. Optional Node utilities cover quick mode, MCP render tools, and PPTX export.
metadata:
  version: "1.0.0"
  upstream: "humanizer 3.1.0, visual-explainer 0.11.0"
---

# HumVisual

Two jobs. Rewrite prose so it reads like the writer who meant it. Build visual explanations that carry an idea
faster than a wall of terminal text. Pick one per request, or do both in the order below.

This prompt holds the workflow and the rules that decide output. The long material sits in `./references/`:
`prose-patterns.md` for the 26 tells with watch lists and examples, `css-patterns.md`, `libraries.md`,
`themes.md`, `slide-patterns.md`, and `responsive-nav.md` for page craft. Read what the current task needs, no
more, before the first draft.

## Pick the job

| The request | Job | Where the output goes |
|---|---|---|
| "Humanize this", "does this sound like AI?", a draft, a commit message, a PR body | Prose | The chat, or the named file |
| "Diagram this", an architecture, a diff review, a plan review, a recap, a table, a deck | Visual | `~/.agent/diagrams/<name>.html`, opened in a browser |
| A page that needs words on it | Both: prose first, then the page | Page copy written by the prose rules |
| Ask for AI-readable output or a source brief | Both | `<name>.md` beside `<name>.html` |

When a request has no clear shape, ask one question: page or text? Guessing wrong costs more than asking.

## Rules both jobs share

- **Evidence.** Every fact, name, number, date, quote, citation, and code reference comes from the source, the
  user, or a command you ran. If a sentence needs a detail nobody gave you, ask for it or write the shorter
  sentence. Never fill a gap with a plausible guess.
- **Audience.** Write for the person who will read this, with the context they already have. A reply inside a
  thread, or a page for the team that owns the code, does not rebuild the background it can assume.
- **One claim per unit.** A sentence adds something. A figure states one thing in its caption. A section holds
  one idea. If a unit only signals importance, cut it.
- **Structure carries meaning.** Numbered steps only when order matters. Labels only when they classify.
  Dividers only at a real seam. An arrow that says nothing is decoration, so label it or drop it.
- **Plain words, active voice.** Name the actor. Prefer the common word. Keep the tone flat and let the content
  carry weight.
- **Check the draft against the source.** After writing, compare claim by claim. An invented detail is an error.
  A lost claim is an error unless a rule called for cutting it.

## Part 1: prose

### Why AI text sounds the way it does

A language model writes whatever is most likely to come next, so by default it makes the choice that fits the
widest range of readers and subjects. A person writes for one reader and one subject, so their choices are
uneven and specific. Every pattern below is one form of that default choice: staging that adds weight instead of
a fact, rhythm and formatting applied by rule, ordinary facts dressed as pivotal, leftovers from the chat, and
replies that re-explain what the reader already has.

Word habits change with every model release, so treat the list of words as the part that ages. The structural
habits persist, so they lead.

A tell counts in proportion to how rarely a careful writer would make it on purpose. Section A to E patterns
justify an edit on one sighting. A pattern marked *weak alone* needs company from other tells in the same
passage before you act.

### How to work

1. **Mark the tells.** Read the whole text once and mark every pattern, strongest first. Look at paragraph shape
   as well as sentences. A contrast split across two sentences, three parallel examples, or the same closer after
   every section is the same tell at a larger scale.
2. **Draft the rewrite.** Keep every supported claim. Shorten dull parts and change structure freely, but keep
   the information. An opinion or reaction is fine where the voice calls for one. A factual claim is not.
   Fiction is exempt, because invented detail is the task.
3. **Check the draft.** Read it aloud. Ask what still sounds generated, and whether the rewrite added or dropped
   a fact, name, number, date, quote, citation, ranking, or claim that two things happen at once. Shape edits
   under §6, §9, and §19 drop claims most often. Search again for the tells that survive a rewrite: §1
   contrasts, §2 closers, §6 triads, §8 dashes, and §19 bold labels.
4. **Write the final version.** State each point naturally instead of patching flagged phrases one at a time. If
   a sentence stays awkward, rewrite the paragraph around its point. Vary sentence length, because real writing
   alternates short and long.

### Voice

If the user supplies a writing sample, read it first and match its sentence length, word choice, punctuation,
openings, and transitions. The sample overrides the patterns below, including the dash rule in §8. If the
sample uses dashes, keep them at about the same rate.

Without a sample, take the voice from the kind of text. Blog posts, essays, opinions, and personal writing keep
the writer's opinions, uncertainty, mixed feelings, humor, and asides, and you may add a reaction where the
writer would. Reference, technical, legal, and factual text stays neutral and plain.

Removing tells is half the job. The result must still sound like a person.

### What to return

- **Pasted text (default).** The draft, a short list of patterns still present, then the final rewrite.
- **File mode.** When the user names a file, run the whole process but write only the final text to the file.
  Change prose only. Keep code blocks, inline code, commands, paths, YAML metadata, data, and link targets
  unchanged. Then give a short summary.
- **Embedded mode.** When another task uses this skill for a pull request, commit message, or document, return
  only the final text.

### Pattern index

Full entries with watch lists, reasons, and before and after examples: `./references/prose-patterns.md`. Read
the entry for a pattern before you act on it.

#### A. Staging instead of stating

| # | Pattern | Watch for | Fix |
|---|---|---|---|
| 1 | Not X but Y | "It's not just X, it's Y"; "This does not mean X. It means Y." | State the point directly |
| 2 | One-line closers and dramatic fragments | "That is the real win."; "Let that sink in."; "No prior. No nostalgia." | Cut a closer that repeats or explains the example; merge fragments into a claim |
| 3 | Sayings that sound deep | "At its core"; "what really matters"; "X is the language of Y" | Replace the saying with the specific claim |
| 4 | Staged run-up before the point | "Let's dive in"; "Here's what you need to know"; "Honestly?" | Remove the run-up and make the point |
| 5 | Arguing with no one | "This isn't mainly about"; "I'm not saying"; "A tempting approach would be" | Remove the objection nobody raised; keep any real claim it holds |

#### B. Rhythm by rule

| # | Pattern | Watch for | Fix |
|---|---|---|---|
| 6 | Forced triads | "innovation, inspiration, and insights"; three examples plus a lesson | Use the count the meaning needs |
| 7 | Repeated sentence openings | "She noted... She noted... She filed..." | Merge, change the subject, or start with the action |
| 8 | Dashes as the universal connector (*weak alone*) | "institutions, and the people, yet this continues" | Use a period, comma, colon, or parentheses; match a sample that uses dashes |
| 9 | Stacked qualifiers (*weak alone*) | "could potentially possibly be argued" | Keep only the qualifiers the source supports |
| 10 | Hyphenated pairs everywhere (*weak alone*) | "the report is high-quality" | Keep the hyphen before the noun, or where the dictionary has one |
| 11 | Passive voice and missing subjects (*weak alone*) | "No configuration file needed" | Name the actor when it helps |

#### C. Inflation and borrowed authority

| # | Pattern | Watch for | Fix |
|---|---|---|---|
| 12 | Overused AI words | delve, testament, landscape, showcasing, pivotal, robust | Use plain words |
| 13 | Inflated significance | "marking a pivotal moment"; "Despite these challenges... continues to thrive"; "The future looks bright" | Keep the fact, drop the significance, end on the last concrete fact |
| 14 | Vague connection or association | "associated with the leadership of"; "in connection with" | State the relationship the source gives |
| 15 | Shallow -ing riders | "symbolizing", "reflecting", "showcasing", "ensuring" | Keep only what the source supports |
| 16 | Sales language | "nestled within the breathtaking region"; "must-visit" | State what the thing is |
| 17 | Borrowed authority | "Experts believe"; a list of outlets standing in for a person | Name a real source and what it said, or cut the claim and the list |
| 18 | Avoiding is, are, and has | "serves as"; "features"; "boasts"; "refers to" | Use is, are, and has |

#### D. Formatting by rule

| # | Pattern | Watch for | Fix |
|---|---|---|---|
| 19 | Bold as decoration | "**OKRs**"; a bold label and colon on every list item | Remove the bold, and turn a labeled list into prose when the labels carry nothing |
| 20 | Decorative headings | Title case on every heading; emoji or arrow markers; a rule between sections; "The decision, on one screen" | Sentence case, no decoration, and a heading that names what the section holds |
| 21 | Curly quotation marks (*weak alone*) | said “the project” | Use straight quotes where the writer or format does |

#### E. Leftovers from the chat and the draft

| # | Pattern | Watch for | Fix |
|---|---|---|---|
| 22 | Chatbot residue | "Great question!"; "I hope this helps"; "Let me know if..." | Remove the wrapper, keep the content |
| 23 | Knowledge-limit disclaimers and guesses | "as of my last update"; "it is believed that"; "likely grew up in" | State what the source shows, or remove the sentence |
| 24 | A heading repeated in the first sentence | "## Performance" followed by "Speed matters." | Let the heading do the work |
| 25 | Writing about the document instead of its subject | "was added to replace"; "compiled from"; "the table below compares" | Describe the subject, and state a convention only when the reader cannot infer it |

#### F. Writing for the wrong reader

| # | Pattern | Watch for | Fix |
|---|---|---|---|
| 26 | Re-explaining what the reader knows | A reply that walks the diagnosis and proves the plan before the decision | Lead with the decision, and leave the proof for the ticket that follows |

### When not to act

Each pattern is a default choice, and a person can make any one of them on purpose. Leave a watched phrase alone
inside a quotation, a title, a proper name, or a passage that discusses the phrase rather than uses it.
Salutations and sign-offs predate chatbots. Text written before November 30, 2022 is not AI-written. People who
judge by feel do little better than chance, and human writing keeps absorbing AI habits, so several tells
together are the safeguard.

Keep the details that carry the writer's voice unless they hurt the meaning: a specific and unusual detail, mixed
feelings and unresolved tension, a dated reference, a first-person choice the writer can explain, a genuine
aside or self-correction.

The patterns come from Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

## Part 2: visual explanations

### Trigger and delivery rules

- Prefer an HTML page over terminal ASCII when the output is inherently visual.
- If a table would have 4 or more rows or 3 or more columns, render it as HTML and give only a short chat summary.
- Write files to `~/.agent/diagrams/` or the explicit output path, with descriptive filenames.
- Generate a Markdown companion only when the user asks for AI-readable output or a source brief. Keep HTML as
  the final visual output; Markdown is a companion, never the source for HTML. Write `<name>.md` beside
  `<name>.html` when possible, and ask before replacing an existing companion.
- Open generated pages in the browser when running normally. In Pi package installs, use `visual_explainer` with
  `prepare` for planning and context, and `render` only after the complete HTML document exists. MCP hosts use
  `visual-explainer-mcp`, which defaults render tools to `open: false`. Use `viewer: "glimpse"` only when the
  user wants a native Glimpse window and `glimpseui` is installed; `viewer: "auto"` may fall back to the browser.
- The final page must be a complete self-contained HTML document, including embedded CSS, a self-contained
  favicon, and any needed JS. In Pi, `visual_explainer.render` also adds a missing `html lang`, missing viewport
  metadata, and display-math escaping for raw `<` and `>` inside `$$...$$`.

### Quick mode

Quick mode is opt-in. Use it only when `--quick` appears on `/generate-web-diagram`, `/diff-review`,
`/plan-review`, or `/project-recap`. Default and all other prompt behavior stays full HTML generation.

For quick mode, read `./quick/README.md` and `./quick/schema.json`. Gather and verify the same source facts as
full mode, but emit the compact JSON spec. In Pi, call `visual_explainer` with `action: "render_quick"`,
`filename`, `spec`, and optional `open` or `viewer`. In other harnesses, save the JSON and run the local
`./quick/render.mjs` script. The renderer validates the spec and creates the complete HTML document.

Quick mode does not fit custom visual composition, slides, Mermaid-rich topology, or content the schema cannot
express. If it is not a fit, validation fails, or rendering errors, fall back to full HTML. Do not use quick mode
for slides, fact-check, visual plans, PPTX, themes, or updates.

### Design judgment

Before writing any HTML:

- Calibrate treatment. Diff reviews, memos, audits, and recaps get polished-utilitarian: real hierarchy,
  considered spacing, no flashy hero. Showcases and narrative decks get editorial. A well-composed page is never
  wrong, and an over-designed one sometimes is.
- Precedence: the user's words, then the project's existing design system (theme and token files, component
  styles), then this skill's choices. Check repo tokens before picking a palette for diff or plan reviews.
- Plan first: 4 to 6 named hex values, type roles, and a one-sentence layout concept. Audit once by asking
  "would I produce this plan for any similar page?" and revise the generic parts. Generic: slate `#0f172a`,
  indigo, Inter, a hero plus three cards. Revised for a CLI recap: near-black green, phosphor text, amber accent,
  JetBrains Mono, with the layout following the release timeline.
- Structure must encode something true. The rule holds here as it does in prose.

### Reference routing

Read only the references the current output needs:

| Need | Read |
|---|---|
| Text-heavy architecture or cards | `./templates/architecture.html` |
| Mermaid flowcharts, sequence, ER, state, class, C4, data flow | `./templates/mermaid-flowchart.html`, and the Mermaid sections in `./references/libraries.md` |
| Data tables, comparisons, audits | `./templates/data-table.html` |
| Slide decks | `./templates/slide-deck.html`, `./references/slide-patterns.md` |
| CSS layout, type scale, overflow, depth, collapsibles, SVG connectors, generated images | `./references/css-patterns.md` |
| Pages with 4 or more major sections | `./references/responsive-nav.md` |
| Switchable themes or fonts, or a named palette such as Dracula, Nord, or Gruvbox | `./references/themes.md` |
| Prose-heavy pages | "Prose Page Elements" in `./references/css-patterns.md`, and the typography sections in `./references/libraries.md` |
| A prose tell, before rewriting | `./references/prose-patterns.md` |

### Choose the representation

| Content | Default representation |
|---|---|
| Flowchart, pipeline, state machine, decision tree | Mermaid |
| Sequence, ER or schema, class, C4, topology-focused architecture | Mermaid |
| Text-heavy architecture, module internals, implementation plans | CSS grid cards, optionally with a Mermaid overview |
| 15 or more element architecture | Hybrid: a small Mermaid overview plus CSS detail cards |
| Comparison, audit, or status matrix | Semantic HTML `<table>` |
| Timeline or roadmap | CSS timeline |
| Dashboard or metrics | CSS grid plus charts and KPIs |
| Slide deck | `100dvh` slides using the slide template patterns |

### Mermaid invariants

What to draw, before how:

- Depict the mechanism, not its name. The path a request takes through a cache says more than a box labeled
  "cache".
- Label every arrow: `writes`, `invalidates`, `polls every 30s`. An unlabeled arrow only says "related somehow".
- To compare options, draw the difference: the edge each adds or removes. Match complexity to what the decision
  turns on.
- One figure, one claim, and the caption states it.

How to render:

- Use `theme: 'base'` with custom `themeVariables` matching the page palette.
- For complex diagrams use ELK layout when available.
- Never use bare `<pre class="mermaid">`.
- Use the canonical `diagram-shell` pattern from `./templates/mermaid-flowchart.html`: `.diagram-shell` >
  `.mermaid-wrap` > `.zoom-controls` + `.mermaid-viewport` > `.mermaid-canvas`.
- Every Mermaid diagram needs zoom in, out, reset, and expand controls, Ctrl or Cmd plus scroll zoom, drag
  panning, and click to expand.
- Prefer `flowchart TD` for complex diagrams. Use `LR` only for simple 3 or 4 node linear flows.
- Use `<br/>` in quoted flowchart labels. Do not use escaped `\n` labels.
- Never define a page-level `.node`, because Mermaid uses it internally. Use namespaced page classes such as
  `.ve-card`.
- For 15 or more elements, do not cram everything into one Mermaid diagram. Use the hybrid overview plus cards
  pattern.

### Layout and style invariants

- Use semantic HTML where it helps accessibility and copy and paste: `<table>`, headings, lists, `<details>`,
  captions.
- Use CSS custom properties for the palette: `--bg`, `--surface`, `--border`, `--text`, `--text-dim`, and 3 to
  5 accents.
- Pages meant to persist ship both color schemes: tokens on `:root`, and the `prefers-color-scheme` media query
  redefines tokens only, with components styled through tokens. Pick the second theme's values, never invert.
  Single-theme is fine when deliberate: one-shot pages, quick mode, and the `themes.md` picker.
- Commit to one palette, with its light and dark variants, and one font pair. Add a runtime picker only when the
  user asks to switch themes or fonts, or names a prebuilt palette; see `./references/themes.md`.
- Anchor the aesthetic direction to the content's domain: CLI and infrastructure get terminal or IDE
  inspiration, metrics and audits get data-dense treatment, plans and architecture get blueprint treatment,
  recaps get editorial treatment, prose gets paper and ink. Warm cream with a serif and terracotta on everything
  is itself a cliché.
- Avoid generic defaults when choosing freely, and let a project's existing design system override this list: no
  body font that is only Inter, Roboto, Arial, Helvetica, or system-ui; no violet or fuchsia Tailwind-default
  accents as the main palette (`#8b5cf6`, `#7c3aed`, `#a78bfa`, `#d946ef`); no cyan, magenta, and purple neon
  dashboard; no gradient-mesh blobs; no purple-to-blue gradient hero, emoji section markers,
  centered-everything layouts, uniform large border-radius, or default accent bars on rounded cards.
- Set type deliberately: running text near 65ch, a committed type scale, `text-wrap: balance` on headings, and
  letter-spacing on uppercase labels.
- For non-slide, scrollable pages, use a rem-based type scale with one root knob: set `html { font-size: 16px }`
  or a value in the 16 to 18px range, and express ordinary page text in `rem` so a single line rescales the
  page. Minimum effective sizes at the chosen root: body and reading text at least 14px, secondary text and
  labels at least 11px, code and mono at least 12px. Never hard-code reading text below 14px in px, because dense
  all-px scales render as unreadable dashboards. Mermaid SVG labels stay in px, because Mermaid sizes them
  through configuration. Slide decks are a deliberate exception: preserve their viewport-responsive
  `clamp(...px, ...vw, ...px)` typography and `autoFit()` runtime fitting from `slide-patterns.md` and
  `slide-deck.html`. Reference snippets and templates demonstrate structure, so re-scale ordinary page px values
  when copying them.
- Bias neutrals toward the accent hue, because pure mid-grey reads as unconsidered. Space siblings with flex or
  grid `gap`, not collapsing margins. Use `tabular-nums` where digits align in columns, and watch specificity so
  classes do not silently cancel each other's spacing.
- Microcopy is design material. Name things by what readers recognize, not by internal structure. Controls say
  exactly what happens. Specific beats clever.
- Dashboards are scanned, not read: summary before detail, state encoded in form through pills, chips, and
  severity stripes, semantic color kept separate from the accent hue, and interactive things that look
  interactive.
- Good font pair families: DM Sans with Fira Code; Instrument Serif with JetBrains Mono; IBM Plex Sans with IBM
  Plex Mono; Bricolage Grotesque with JetBrains Mono; Plus Jakarta Sans with Azeret Mono.
- Load every font weight the CSS uses, including mono labels. Do not rely on faux bold for 500, 600, or 700
  weights.
- Good accent directions: terracotta with sage, teal with slate, rose with cranberry, amber with emerald, deep
  blue with gold.
- Prevent overflow: `min-width: 0` on grid and flex children, `overflow-wrap: break-word` for long text, and
  scroll containers for wide tables and code.
- Do not set `display: flex` directly on `<li>` when list markers matter.
- Use depth sparingly: hero and elevated for primary sections only, flat or recessed for reference material.
- Use entrance and hover animation only when it clarifies hierarchy. Respect `prefers-reduced-motion`. No
  continuous glow, pulse, or breathing effects on static content.

### Slide deck mode

Use slides only when explicitly requested or when a command asks for slides. Slides are a different medium, not a
paginated article. If the user asks for PPTX or passes `--pptx` to `/generate-slides`, generate the HTML deck
first, then use the best-effort static exporter in `./pptx/export.mjs` or the `visual-explainer-pptx` binary when
package or checkout dependencies are available. If they are not, deliver the HTML deck and explain the missing
export dependency path. State that HTML remains the source of truth, and that PPTX does not preserve animations,
reader navigation, responsive layout, custom fonts, live Mermaid, Chart.js, SVG, canvas rendering, or JavaScript
behavior.

Slides rules:

- Each slide gets one `100dvh` viewport budget with no page-level scrolling. The template's `overflow: hidden`
  can clip excess content silently, so enable `prefers-reduced-motion: reduce` at target and short landscape
  heights, then fix every vertical-overflow or `autoFit()` warning before delivery.
- Use larger type, fewer objects per slide, varied compositions, and visible navigation.
- Include the slide nav chrome from `slide-deck.html`: prev and next controls, slide count with reading percent,
  keyboard navigation, an expandable reader rail, outline and help overlays, `#slide-N` deep links, and resume
  state.
- Before writing HTML, inventory the source and map every source item to slides.
- Do not drop content to fit a fixed slide count. Add slides instead.
- Use the 10 slide types from `slide-patterns.md`: title, section divider, content, split, diagram, dashboard,
  table, code, quote, and full bleed.

### Optional generated images

If `surf` is available, generated images may be embedded as base64 for hero banners, conceptual illustrations, or
educational visuals. Skip images for data-heavy, structural, or Mermaid and CSS suitable content. Pages must stand
on CSS, typography, and diagrams without images.

### Final checklist

Before delivery, verify:

- the document is complete HTML and written to the requested path;
- no console errors when it opens, and no horizontal overflow at normal desktop width;
- fonts load with fallbacks, and the page has a self-contained favicon;
- tables preserve rows and columns and wrap long text;
- interactive elements have visible keyboard focus states;
- diagrams sit in `<figure>` with a claim-stating `figcaption`, plus `role="img"` and a matching `aria-label` on
  the shell wrapper rather than the Mermaid SVG, because a re-render replaces it;
- both color schemes hold up, or a single theme was deliberate;
- Mermaid diagrams use `diagram-shell` with zoom, pan, and expand;
- a runtime picker, if present, swaps palette and font variables and re-renders every diagram;
- slides fit one viewport, include the reader rail plus outline and help navigation, preserve source coverage, and
  pass the template's overflow and `autoFit()` delivery check under reduced motion. If PPTX was requested, the
  static `.pptx` came after the HTML deck and its fidelity limits were stated;
- a non-slide page uses rem with one root knob and meets the minimum effective sizes: body at least 14px, labels
  at least 11px, mono at least 12px. Mermaid SVG labels may stay config-driven px, and slide decks keep their
  `clamp()` typography and `autoFit()` fitting;
- visual hierarchy makes the main idea obvious in the first viewport;
- the styling would still be recognizable next to a generic dark violet template;
- page copy passes the prose rules above: no §1 to §5 tells, no decorative bold, sentence-case headings, and a
  caption that states a claim;
- if a Markdown companion was requested, it is a concise source brief that matches the delivered HTML without
  becoming its source of truth.

## Part 3: when the page and the draft are the same job

A page is prose with layout, so the two halves of this skill agree more than they differ. When the request is
both, run the prose pass on the words first, then build the page around the result.

- Write page copy to the same bar as a document: headings in sentence case that name what the section holds,
  captions that state one claim, labels that use the reader's words, and no chat wrapper.
- Treat microcopy as part of the edit. A button that says "Submit" when it writes a file is a tell in a
  different costume.
- The JSON spec in quick mode carries prose too. Card titles, callouts, and table headers are read by people.
- A Markdown companion is a source brief, not a transcript of the page. It states the claim, the evidence, and
  the open questions.
- Keep the same evidence bar in both halves. A diagram with a wrong arrow label fails the visual checklist, and a
  caption with an invented number fails the prose one.

## Credits and license

Merged from two MIT skills:

- Humanizer 3.1.0 by blader, built on Wikipedia's
  ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- visual-explainer 0.11.0 by Nico Bailon, which borrows ideas from
  [Anthropic's frontend-design skill](https://github.com/anthropics/skills) and
  [interface-design](https://github.com/Dammyjay93/interface-design).

MIT. See `LICENSE`.
