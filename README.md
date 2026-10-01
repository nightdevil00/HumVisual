# HumVisual

One agent skill with two jobs. It rewrites AI-sounding prose so it reads like the writer who meant it, and it
turns systems, code changes, plans, data, and technical concepts into self-contained HTML pages that explain
something in the time it takes to read it.

Merged from two MIT skills, so a single prompt covers the words and the page:

- **Humanizer 3.1.0** by Siqi Chen, built on Wikipedia's
  ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). 26 patterns, numbered by
  strength and frequency.
- **visual-explainer 0.11.0** by Nico Bailon. Diagrams, diff and plan reviews, recaps, tables, and slide decks as
  self-contained HTML, with Mermaid, Chart.js, and a theme picker.

## See both halves at work

`examples/humvisual-paper.html` is a paper about this merge, written in the merged style. Its prose follows the
26 patterns, its layout follows the visual invariants, and it shows both side by side: the same content as raw
chat text against the same content as a page. Open it in a browser.

Prose, before and after:

> I'm thrilled to announce that shared drafts are finally here! 🚀 For months, our own team was drowning in files
> named final_v7.docx, and we knew there had to be a better way. Now two people can edit the same doc at once,
> with every change appearing live for both of them. It's not just a feature; it's a whole new way to collaborate.
> Comments stay anchored to the exact sentence they reference, even as the text around them evolves. And the best
> part? It's available today on every plan, completely free. Let that sink in.

After:

> Shared drafts are out today. For months our own team passed around files named final_v7.docx, so we built a way
> for two people to edit the same doc at once, with each person's changes showing up live for the other. Comments
> stay pinned to the sentence they're about, even when the text around them changes. It's free on every plan.

The rewrite keeps every fact and adds none. What it drops is the staging, the closer, the emoji, and the sales
voice.

## Install

No build step. The skill is Markdown, and the only hard requirement for the visual half is a browser.

| Harness | Install |
|---|---|
| Claude Code | `/plugin marketplace add <owner>/humvisual` then `/plugin install humvisual@humvisual` |
| Agents with the Skills CLI | `npx skills add <path-to-this-folder> --global --agent '*'` |
| Agents with a skills folder | Copy this folder into the agent's skills directory and read `SKILL.md` |
| MCP hosts | `node mcp/server.mjs` after `npm install --no-package-lock`, or the `visual-explainer-mcp` binary from a package install |
| PPTX export | `node pptx/export.mjs deck.html deck.pptx` after installing dependencies, or the `visual-explainer-pptx` binary |

The two Node utilities keep their upstream names so existing host configurations keep working. Drop off the
`--global` flag to install for the current project only.

## Usage

Ask in plain language:

```text
Humanize this: [paste text]
Humanize the prose in docs/launch-post.md
Draw a diagram of our authentication flow
Review the diff on this branch as a page
Turn this plan into slides
```

Or use the bundled commands:

| Command | What it does |
|---|---|
| `/humanize` | Rewrite text in your voice without changing its facts |
| `/generate-web-diagram` | Generate an HTML diagram for any topic |
| `/generate-visual-plan` | Generate a visual implementation plan for a feature |
| `/generate-slides` | Generate a slide deck, with optional `--pptx` |
| `/diff-review` | Visual diff review with architecture comparison and risk review |
| `/plan-review` | Compare a plan against the codebase with a risk matrix |
| `/project-recap` | Mental model snapshot for context switching |
| `/fact-check` | Verify a generated document against real code and git history |

Add `--quick` to `/generate-web-diagram`, `/diff-review`, `/plan-review`, or `/project-recap` to emit a compact
JSON spec instead of hand-written HTML. The bundled renderer turns the spec into a complete page.

Visual output goes to `~/.agent/diagrams/<name>.html` and opens in a browser. Ask for AI-readable output and the
agent also writes `<name>.md` beside it as a source brief.

### Match your voice

Give the skill two or three paragraphs of your own writing and it will match your rhythm, word choice,
punctuation, and deliberate quirks, dashes included.

```text
/humanize

Here's a sample of my writing: [paste your own paragraphs]

Now rewrite this: [paste the text to fix]
```

## The 26 patterns

Numbered by strength and frequency. Patterns A to E justify an edit on one sighting. Patterns marked *weak alone*
count only when several tells share a passage, because a careful writer may use one of them on purpose. Full
entries with watch lists and before and after examples live in `references/prose-patterns.md`.

### A. Staging instead of stating

| # | Pattern | Watch for | Fix |
|---|---|---|---|
| 1 | **Not X but Y** | "It's not just X, it's Y"; "This does not mean X. It means Y." | State the point directly |
| 2 | **One-line closers and dramatic fragments** | "That is the real win."; "Let that sink in."; "No prior. No nostalgia." | Cut a closer that repeats; merge fragments into a claim |
| 3 | **Sayings that sound deep** | "At its core"; "what really matters"; "X is the language of Y" | Replace the saying with the specific claim |
| 4 | **Staged run-up before the point** | "Let's dive in"; "Here's what you need to know"; "Honestly?" | Remove the run-up and make the point |
| 5 | **Arguing with no one** | "This isn't mainly about"; "A tempting approach would be" | Remove the objection nobody raised |

### B. Rhythm by rule

| # | Pattern | Watch for | Fix |
|---|---|---|---|
| 6 | **Forced triads** | "innovation, inspiration, and insights" | Use the count the meaning needs |
| 7 | **Repeated sentence openings** | "She noted... She noted... She filed..." | Merge, change the subject, or start with the action |
| 8 | **Dashes as the universal connector** (*weak alone*) | "institutions, and the people, yet this continues" | Use a period, comma, colon, or parentheses |
| 9 | **Stacked qualifiers** (*weak alone*) | "could potentially possibly be argued" | Keep only the qualifiers the source supports |
| 10 | **Hyphenated pairs everywhere** (*weak alone*) | "the report is high-quality" | Keep the hyphen before the noun, or where the dictionary has one |
| 11 | **Passive voice and missing subjects** (*weak alone*) | "No configuration file needed" | Name the actor when it helps |

### C. Inflation and borrowed authority

| # | Pattern | Watch for | Fix |
|---|---|---|---|
| 12 | **Overused AI words** | delve, testament, landscape, showcasing, pivotal | Use plain words |
| 13 | **Inflated significance** | "marking a pivotal moment"; "The future looks bright" | Keep the fact, drop the significance |
| 14 | **Vague connection or association** | "associated with the leadership of" | State the relationship the source gives |
| 15 | **Shallow -ing riders** | "symbolizing", "reflecting", "showcasing" | Keep only what the source supports |
| 16 | **Sales language** | "nestled within the breathtaking region" | State what the thing is |
| 17 | **Borrowed authority** | "Experts believe"; a list of outlets standing in for a person | Name a real source, or cut the claim |
| 18 | **Avoiding is, are, and has** | "serves as"; "features"; "boasts" | Use is, are, and has |

### D. Formatting by rule

| # | Pattern | Watch for | Fix |
|---|---|---|---|
| 19 | **Bold as decoration** | "**OKRs**"; a bold label on every list item | Remove the bold; turn a labeled list into prose |
| 20 | **Decorative headings** | Title case, emoji markers, a rule between sections | Sentence case, no decoration, a heading that names its section |
| 21 | **Curly quotation marks** (*weak alone*) | said “the project” | Use straight quotes where the format does |

### E. Leftovers from the chat and the draft

| # | Pattern | Watch for | Fix |
|---|---|---|---|
| 22 | **Chatbot residue** | "Great question!"; "I hope this helps"; "Let me know if" | Remove the wrapper, keep the content |
| 23 | **Knowledge-limit disclaimers and guesses** | "as of my last update"; "it is believed that" | State what the source shows, or remove the sentence |
| 24 | **A heading repeated in the first sentence** | "## Performance" then "Speed matters." | Let the heading do the work |
| 25 | **Writing about the document instead of its subject** | "compiled from"; "the table below compares" | Describe the subject, not the document |

### F. Writing for the wrong reader

| # | Pattern | Watch for | Fix |
|---|---|---|---|
| 26 | **Re-explaining what the reader knows** | A reply that walks the diagnosis before the decision | Lead with the decision |

## What is in the folder

```text
HumVisual/
├── SKILL.md                     the merged prompt: routing, shared rules, prose workflow, visual invariants
├── references/
│   ├── prose-patterns.md        the 26 tells with watch lists and examples
│   ├── css-patterns.md          tokens, type scale, layouts, Mermaid containers, prose page elements
│   ├── libraries.md             Mermaid, Chart.js, anime.js, Google Fonts
│   ├── themes.md                11 palettes, font pairs, runtime picker
│   ├── slide-patterns.md        slide engine, nav chrome, 10 slide types, presets
│   └── responsive-nav.md        sticky table of contents for multi-section pages
├── templates/                   architecture, mermaid-flowchart, data-table, slide-deck
├── commands/                    humanize + the seven visual commands
├── quick/                       compact JSON schema and the local renderer
├── pptx/                        best-effort static slide deck export
├── mcp/                         local stdio MCP server with render tools
├── examples/                    humvisual-paper.html
├── agents/openai.yaml           display name and default prompt
├── scripts/validate-package.py  package checks, no dependencies
├── extension.ts                 Pi native tool
└── .claude-plugin/, .cursor-plugin/, package.json
```

## Design rules the visual half holds to

The full list is in `SKILL.md`. The ones that change output most:

- One page claim per figure, stated in the caption, with every arrow labeled.
- Semantic HTML, both color schemes through tokens, and a rem type scale with one root knob.
- A palette anchored to the content's domain, never the default dark violet template.
- Dashboards read at a glance: summary first, state encoded in form, tables that wrap.
- Page copy passes the prose patterns in the same folder.

## Credits

- Humanizer by Siqi Chen, from Wikipedia's
  ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) maintained by WikiProject
  AI Cleanup.
- visual-explainer by Nico Bailon, which borrows ideas from
  [Anthropic's frontend-design skill](https://github.com/anthropics/skills) and
  [interface-design](https://github.com/Dammyjay93/interface-design).

## License

MIT. Both upstream copyrights are kept in `LICENSE`.
