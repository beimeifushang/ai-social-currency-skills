---
name: prompt-to-product
description: Turn prompts, AI workflows, internal automations, creator hacks, or one-off agent instructions into productized MVP briefs, user personas, feature boundaries, pricing experiments, prototype specs, launch content, and first-customer plans. Use when the user asks to convert a prompt into a SaaS/product, find monetizable AI workflow ideas, create a one-person startup plan, generate MVP specs, or package an AI automation as a sellable product.
---

# Prompt To Product

## Overview

Transform a useful prompt or workflow into a product concept with a buyer, wedge, interface, MVP boundary, demo, and launch path. Optimize for a one-person studio that can ship evidence before building a company.

## Workflow

1. Decode the prompt.
   - Identify the recurring job, input material, decision criteria, output artifact, and user pain.
   - Distinguish "nice answer" from "workflow people would pay to repeat."
   - Extract any domain-specific data, judgment, or distribution advantage.

2. Productize the workflow.
   - Choose the product shape: micro-SaaS, internal agent, Chrome extension, template pack, API, report generator, marketplace tool, or service-with-software.
   - Read `references/productization-patterns.md` when choosing shape, pricing, or go-to-market.
   - Define the smallest product that proves willingness to use or pay.

3. Build the MVP brief.
   - Name the ICP, urgent trigger, first use case, must-have features, anti-features, and success metric.
   - Design the interface around the workflow object, not the prompt textbox.
   - Include trust, data, and human approval boundaries.

4. Package for shipping.
   - Produce a one-page product brief, prototype spec, demo script, pricing test, and first 10 customer acquisition plan.
   - Include a "kill test": the fastest way to learn if nobody cares.

## Output Shape

- Product name.
- ICP and urgent trigger.
- Job-to-be-done.
- Product shape.
- MVP scope.
- Anti-features.
- Interface sketch.
- Pricing experiment.
- First 10 customer plan.
- 60-second demo script.
- Kill test.

## Bundled Tools

Use `scripts/product_brief.py` for a structured first pass:

```bash
python3 scripts/product_brief.py --prompt "Summarize messy brand emails into creator deal terms and negotiation risks" --audience "MCN operators"
```

Read `references/productization-patterns.md` when shaping the MVP or go-to-market.

Use `assets/mvp-onepager.css` for quick one-page prototype pages.

## Quality Bar

- Name the buyer, not just the user.
- Keep the MVP narrow enough to build.
- Make the workflow repeatable.
- Add a distribution wedge.
- Include a fast falsification test.
