# Sales Sheet Builder

Sales Sheet Builder is a Codex and Claude Code plugin for turning a company,
product, service, offer, or URL into a compressed, differentiated B2B sales
sheet.

It is built for sales, founder-led GTM, product marketing, and agency operators
who need a buyer-ready explanation that is sharper than generic website copy.

The plugin does the heavy thinking in a separate workbook, then compresses the
answer into a sales sheet that takes as little mental effort as possible to
understand.

## Best for

- turning a homepage into a one-page sales sheet
- sharpening an offer before outbound or sales calls
- explaining a new or hard-to-categorize product in plain language
- positioning against the real status quo, not just named competitors
- preserving useful research without making buyers read the research process
- creating a sales asset that can be tested, tuned, and reused

## What the plugin does

The plugin adds the `sales-sheet-builder` skill.

It reviews the source material, researches current alternatives, and produces a
clear sales argument around four practical questions:

1. What is the buyer trying to increase, decrease, avoid, or improve?
2. How do they try to get that job done today?
3. What downside does the current approach create?
4. How does this offer solve the same job without that downside?

The skill uses Jobs to Be Done, status quo analysis, competitor bucket mapping,
and source-backed evidence, but it does not expose that framework language to
the buyer-facing sheet by default.

## What you get back

By default, the plugin returns two separate artifacts when the research is worth
keeping:

- a compressed buyer-facing sales sheet
- a separate internal workbook

The buyer-facing sheet focuses on:

- the buyer's current situation
- the real status quo or workaround
- the cost of the current approach
- the new mechanism
- the additional gain or reduction the new approach creates
- proof and proof gaps
- a simple sales conversation hook

The workbook preserves:

- source extraction notes
- JTBD map
- status quo and alternatives
- competitor buckets
- coopetition roles
- feature, benefit, outcome mapping
- evidence log
- proof gaps and asset recommendations

The buyer sees the conclusion. The operator keeps the research.

## How it thinks

Most weak sales sheets explain the product too early.

This plugin starts with the job the buyer already has. It identifies the way the
buyer gets that job done today, then finds where that current approach creates
friction.

That current approach might be a named vendor, but it is often something more
ordinary:

- spreadsheets
- manual research
- an agency
- a rep's personal workflow
- another hire
- a broader tool already in the stack
- doing nothing differently

The skill treats competitors as ways the buyer gets the job done. A tool can be
a competitor, a complement, an input, or a budget alternative depending on how
the buyer uses it.

The final sales sheet should make the buyer think:

> This understands what I am trying to do, why the current way is frustrating,
> and why this approach might work better.

## Codex requirements

This plugin ships a skill. It does not bundle its own MCP server, app connector,
or external API service.

It works inside Codex by using the tools already available in the current run.

### Required

- Codex plugin support with skill loading enabled
- web research access when a URL or current competitor research is required
- `python3` for the bundled output validator

### Recommended

- Browser or Chrome tooling when the source page requires rendered inspection
- access to credible public sources for market proof, buyer behavior, and
  competitor claims

### What happens without them

- without web research, the skill can still structure the sales sheet from
  provided material, but it should not claim current competitor or market proof
- without Browser or Chrome tooling, the skill should not claim it inspected
  rendered-only page states
- without strong company proof, the skill will keep the sales sheet more modest
  and move missing proof into the workbook

## Repository Layout

- `.codex-plugin/plugin.json`: Codex plugin manifest
- `.claude-plugin/plugin.json`: Claude Code plugin manifest
- `skills/sales-sheet-builder/SKILL.md`: main skill instructions
- `skills/sales-sheet-builder/references/jtbd-framework.md`: Jobs to Be Done
  analysis rules
- `skills/sales-sheet-builder/references/positioning-framework.md`: status quo,
  alternatives, and differentiation rules
- `skills/sales-sheet-builder/references/research-and-evidence.md`: source
  extraction, proof, and evidence rules
- `skills/sales-sheet-builder/references/output-template.md`: separate sales
  sheet and workbook formats
- `skills/sales-sheet-builder/scripts/validate_sales_sheet.py`: validator for
  published sheets and workbooks

## Typical inputs

The plugin works best when the request includes:

- a source URL
- the product, service, or offer name
- the target buyer, if known
- the sales goal, such as booking a meeting or starting a qualified sales
  conversation
- any known competitors or current alternatives
- desired output length or tone

If the user provides only a URL, the skill should infer the rest from the source
page and label uncertain assumptions.

## Example Prompts

- Build a sales sheet from `https://example.com`.
- Create a compressed buyer-facing sales sheet and a separate workbook for this offer.
- Use JTBD and status quo analysis to make this sales sheet more differentiated.
- Turn this homepage into a one-page sales sheet for SDR leaders.
- Rewrite this sales sheet so it fights the status quo, not a random competitor
  list.
- Build a workbook that preserves the research, then give me the simplest
  buyer-facing version.

## Validation

Validate the plugin manifest from the repository root:

```bash
python3 /Users/williamflanagan/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

Validate the skill metadata:

```bash
python3 - <<'PY'
from pathlib import Path

skill = Path("skills/sales-sheet-builder/SKILL.md")
text = skill.read_text(encoding="utf-8")
assert text.startswith("---\n")
end = text.index("\n---\n", 4)
frontmatter = dict(line.split(":", 1) for line in text[4:end].splitlines())
assert frontmatter["name"].strip() == "sales-sheet-builder"
assert len(frontmatter["description"].strip()) <= 500
print("skill metadata passed")
PY
```

Validate a generated sales sheet or workbook:

```bash
python3 skills/sales-sheet-builder/scripts/validate_sales_sheet.py --mode published path/to/sales-sheet.md
python3 skills/sales-sheet-builder/scripts/validate_sales_sheet.py --mode workbook path/to/sales-sheet-workbook.md
```

## Install source

Marketplace entries can reference this repository:

```text
https://github.com/audienti/sales-sheet-builder.git
```

## Publisher

Published by Audienti.

Maintainer: William Flanagan, `wflanagan@audienti.com`
