# Sales Sheet Builder

Sales Sheet Builder is an Audienti plugin for creating compressed, differentiated B2B sales sheets from a company, product, service, offer, or URL.

The skill uses JTBD, status quo analysis, competitor/alternative mapping, and source-backed evidence to build two separate artifacts:

- A short buyer-facing sales sheet that is easy to understand quickly.
- A separate internal workbook that preserves research, evidence, JTBD mapping, and positioning logic when the data is useful.

## What It Does

- Reviews a source URL and current market alternatives.
- Identifies the buyer's job, likely status quo, and current approach downsides.
- Separates direct competitors, economic competitors, complements, inputs, and budget alternatives.
- Compresses the strongest argument into a low-effort sales sheet.
- Keeps the research workbook separate from the buyer-facing copy.

## Repository Layout

- `.codex-plugin/plugin.json` contains the Codex plugin manifest.
- `.claude-plugin/plugin.json` contains the Claude Code plugin manifest.
- `skills/sales-sheet-builder/` contains the reusable skill.
- `skills/sales-sheet-builder/references/` contains JTBD, positioning, research, and output guidance.
- `skills/sales-sheet-builder/scripts/validate_sales_sheet.py` validates published sheets and workbooks.

## Example Prompts

- Build a sales sheet from `https://example.com`.
- Create a compressed buyer-facing sales sheet and a separate workbook for this offer.
- Use JTBD and status quo analysis to make this sales sheet more differentiated.
- Turn this homepage into a one-page sales sheet for SDR leaders.

## Validation

Validate the plugin manifest:

```bash
python3 /Users/williamflanagan/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

Validate an output:

```bash
python3 skills/sales-sheet-builder/scripts/validate_sales_sheet.py --mode published path/to/sales-sheet.md
python3 skills/sales-sheet-builder/scripts/validate_sales_sheet.py --mode workbook path/to/sales-sheet-workbook.md
```
