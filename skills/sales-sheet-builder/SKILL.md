---
name: sales-sheet-builder
description: Build or tune differentiated, source-backed B2B sales sheets from a URL, company, offer, pasted text, prior draft, or feedback notes. Use for sales sheets, sell sheets, one-pagers, buyer-ready explainers, sales collateral, URL-to-sales-copy briefs, or revision requests using JTBD, status quo, alternatives, downsides, and why the offer is worth a sales conversation.
---

# Sales Sheet Builder

Create buyer-first B2B sales sheets that make an offer easy to understand and meaningfully differentiated. Buyer understanding comes first; persuasion comes second.

## Required Input

At least one of:

- `source_url`
- `source_text`
- `prior_output`
- `feedback_notes`

Ask for a URL, pasted source text, a prior draft, or feedback notes only if none are provided and no usable context exists in the conversation.

Optional inputs: `company_name`, `product_name`, `target_audience`, `offer_type`, `sales_goal`, `competitor_urls`, `preferred_tone`, `output_length`, `industry`, `geography`, `buyer_persona`, `draft_text`, `revision_goal`, `must_keep`, `must_avoid`, and `proof_assets`.

Default `sales_goal`: book a meeting or start a qualified sales conversation.

## Core Rules

- Write for one clear buyer. If `target_audience` is provided, treat it as the source of truth.
- Use live source review and web research. Do not write from memory when a URL is provided.
- Prefer the company page for product facts and company proof.
- Use credible external sources only to validate pain, market motion, urgency, or solution-category logic.
- Research current alternatives before writing the final sheet unless the user explicitly says not to.
- Treat the status quo as the primary competitor until evidence proves otherwise.
- In startup or emerging categories, assume most buyers solve the job through the status quo or a different workaround, not a fancy new direct competitor, unless research proves otherwise.
- Let the offer, real competitors, and likely status quo define the downsides. Do not choose downsides from a generic list.
- Do not invent missing facts, testimonials, case studies, metrics, customers, screenshots, or results.
- Label careful inferences as inferences.
- Every number in the final sales sheet needs a source.
- Translate vendor jargon into plain buyer language.
- Keep the final sheet useful without requiring the reader to visit the original URL.
- The final sheet must answer: what is the buyer trying to increase or decrease, how do they do it today, what is broken about that approach, and how does this offer solve the same job without the same downside?
- The final sheet must have a clear big idea: `If you are doing [job] with [current approach], you inherit [core downside]. This offer lets you do [same job] through [new mechanism], reducing [downside impact] while also increasing/decreasing [additional outcome].`
- Do not limit or categorize downsides. Find the actual buyer burden created by the current approach, name it in the buyer's language, and explain why it matters.
- Treat the research brief, JTBD map, alternative map, and evidence log as internal scaffolding unless the user asks for the full workbook. The buyer-facing sales sheet should contain only the distilled argument.
- Only about 10-20% of the internal workbook should survive into the published sales sheet: the buyer situation, status quo downside, new mechanism, additional gain, proof, and sales conversation hook.
- Keep the workbook separate from the sales sheet. Never make the buyer read the research machinery to understand the offer.
- Optimize the buyer-facing sheet for low mental effort: fewer sections, shorter sentences, one dominant contrast, and no framework language.
- Treat pasted text, prior outputs, and user feedback as first-class source material.
- When tuning a prior draft, preserve what works, explicitly fix the feedback, and do not restart from scratch unless the feedback requires a new positioning spine.
- If feedback conflicts with source facts, preserve source accuracy and explain the constraint briefly in the workbook or handoff note.
- If the user says the copy is too loose, generic, long, undifferentiated, too clever, too technical, or too heavy, diagnose which layer failed: buyer, job, status quo, downside, mechanism, proof, compression, tone, or structure.

## Workflow

1. Ingest the available context.
   - Accept URLs, pasted offer text, product notes, call notes, rough positioning, prior sales sheets, critique, and revision direction.
   - Separate `facts` from `feedback`, `preferences`, and `inferences`.
   - If a prior output is provided, identify what to keep, what to cut, what to rewrite, and what positioning question must be resolved.
   - Convert feedback into concrete revision requirements, such as: sharpen the status quo, make the buyer feel seen, compress the sheet, add JTBD framing internally, change the primary buyer, remove competitor lists, or make the big idea more differentiated.
   - Do not ask for a URL when pasted text or feedback is enough to make progress. Ask only when source facts or current claims cannot be verified from the provided material.

2. Inspect the source URL when provided or needed.
   - Extract the offer, product category, target audience, buyer roles, pain points, cost of pain, promise, features, benefits, differentiators, use cases, proof, metrics, workflow examples, and conversion path.
   - Capture the common language used on the page, but do not copy vendor-heavy phrasing into the final sheet.

3. Define the product plainly.
   - Use this form: `[Product] is a [plain-language category] for [buyer or team] that helps them [solve pain] by [core mechanism], so they achieve [business outcome].`
   - Answer what it is, who uses it, who pays for it, what problem it solves, what workflow it improves or replaces, and what outcome it supports.

4. Establish category clarity.
   - Name the plain category, adjacent tools or workflows, likely budget category, current alternative, and demand-creating buyer problem.
   - Avoid inflated labels such as "revenue orchestration layer" unless the source proves buyers use them. Translate technical category language into buyer language.

5. Choose the sheet audience.
   - Identify the primary buyer, economic buyer, daily user, pain owner, buying trigger, likely objection, current alternative, and desired outcome.
   - Speak to one buyer in the final sheet unless the user explicitly asks for multiple versions.

6. Build or tune the positioning logic.
   - Use `references/positioning-framework.md`.
   - Use `references/jtbd-framework.md` to define the job executor, core job, job steps, desired outcomes, related jobs, and emotional/social jobs.
   - Identify the buyer's job-to-be-done: the number, outcome, risk, or workload they are trying to increase or decrease.
   - Find where the current approach creates friction inside the job steps.
   - Map the status quo, direct/reference competitors, economic competitors, tools, services, methods, and workarounds.
   - Rank alternatives by how likely the buyer is to use them today.
   - Treat each alternative as a way the buyer currently tries to do the job.
   - Group reference competitors by the job step or value axis they primarily serve; do not list every competitor in the buyer-facing copy.
   - Mark coopetition: tools can be complements, inputs, or budget competitors. They are direct competitors only when they become the primary way the buyer does the job.
   - Name each alternative's deficiencies relative to the offer's advantages.
   - Explain the concrete buyer impact of those deficiencies.
   - Identify the extra increase or decrease the new approach creates beyond reducing the old downside.
   - Compress the strongest deficiency-to-advantage contrast into a big idea / differentiator.
   - Write the differentiator thesis: how this offer solves the same job without the status quo downside.
   - If tuning from feedback, rewrite the positioning spine before rewriting sentences. A sentence-level edit cannot fix a weak buyer/job/status quo/downside/mechanism contrast.

7. Build or update the evidence base.
   - Use `references/research-and-evidence.md` for the extraction checklist, proof hierarchy, gap analysis, and evidence log rules.
   - Research missing proof only where it changes the buyer's understanding or confidence.
   - When using pasted text, mark whether each claim came from the pasted material, the source URL, external research, or inference.
   - Exclude low-confidence claims from the final sheet unless framed as context.

8. Translate features into buyer value.
   - For each major feature, map `Feature -> Buyer benefit -> Business outcome`.
   - Keep roughly 20% features, 40% benefits, and 40% outcomes in the final sheet.
   - Remove features that do not support a clear benefit or outcome.

9. Write or revise the sales sheet.
   - Use `references/output-template.md`.
   - Make the sheet explain three things fast: what the product is, why it matters to the buyer, and what changes if they use it.
   - Lead with the buyer's situation and the cost of the current approach before explaining the product.
   - Use the big idea to shape the headline, opening problem, and differentiation section.
   - Use a simple sales conversation hook only when it naturally follows from the sheet.
   - If the research is valuable to preserve, create it as a separate workbook artifact. Do not append it below the buyer-facing copy.
   - For revision requests, return the revised sales sheet first, then a short `What Changed` note that maps the user's feedback to the changes made.

10. Rewrite for buyer effort and differentiation.
   - Run a plain-language pass sentence by sentence.
   - Remove jargon, unsupported claims, hype, technical noise, and anything that does not clarify pain, value, proof, category, or outcome.
   - Remove generic copy that could describe a competitor.
   - If the final sheet does not make the buyer feel understood, rewrite the problem and current-alternative sections before touching the product copy.
   - The buyer should understand the offer after a 30-second scan.

11. Verify.
   - Check the quality gates in `references/output-template.md`.
   - If the output is saved as Markdown, run `python3 scripts/validate_sales_sheet.py <path>`.
   - For strict checks, use `python3 scripts/validate_sales_sheet.py --mode published <path>` for the compressed buyer-facing sheet or `python3 scripts/validate_sales_sheet.py --mode workbook <path>` for the separate internal workbook.

## Deliverable Format

Default output should be one compressed buyer-facing artifact:

1. `Buyer-Facing Sales Sheet`

When saving files, use separate artifacts:

1. `[slug]-sales-sheet.md` for the compressed buyer-facing sheet.
2. `[slug]-sales-sheet-workbook.md` for research, diagnosis, testing, tuning, or the full workbook.

When the user asks for research, diagnosis, testing, tuning, or when the data is useful to preserve, create the workbook separately with these internal sections:

1. `Sales Sheet Research Brief`
2. `Input and Feedback Notes`
3. `JTBD Map`
4. `Positioning and Alternative Map`
5. `Gap Analysis`
6. `Feature, Benefit, Outcome Map`
7. `Evidence Log`
8. `Final Sales Sheet Copy`
9. `What Changed`
10. `Missing Proof or Asset Recommendations`
11. `Optional Variants`

Close with a short note on sources used, confidence, and any proof gaps that materially affect the sheet.
