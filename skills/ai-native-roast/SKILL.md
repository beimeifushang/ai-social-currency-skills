---
name: ai-native-roast
description: Critique AI products, startups, demos, landing pages, feature lists, pitch decks, or app ideas to judge whether they are truly AI-native or just old software with a chatbot. Use when the user asks to roast an AI product, score AI-native quality, find weak product thinking, expose wrapper vibes, sharpen a controversial critique, create teardown content, or identify what would make an AI product more native and defensible.
---

# AI Native Roast

## Overview

Deliver a sharp but fair teardown of AI products. The goal is not cruelty; the goal is taste, precision, and a publishable critique that explains what is fake, what is real, and what would make the product dangerous.

## Workflow

1. Gather the artifact.
   - Use the product description, feature list, landing page, screenshots, demo transcript, repo, or user notes.
   - If critiquing a real current product, browse and cite primary sources or visible product materials before making factual claims.
   - Separate observed facts from inference and taste.

2. Score the product.
   - Use six dimensions: workflow ownership, model leverage, interface transformation, data flywheel, trust boundary, and distribution wedge.
   - Read `references/roast-rubric.md` when scoring or explaining a dimension.
   - Do not punish a product for being narrow. Punish it for pretending the AI changes more than it does.

3. Write the roast.
   - Start with the cleanest judgment.
   - Name the "wrapper smell" if present.
   - Name the strongest real insight if present.
   - Give one brutal line and one constructive rebuild.

4. Package for content.
   - Produce a scorecard, 60-second teardown script, visual proof plan, and comment-bait question that invites serious debate.
   - Include a legal/reputation guardrail: do not allege fraud, fake metrics, or bad intent without evidence.

## Output Shape

- Verdict: AI-native, AI-assisted, AI-wrapped, or AI theater.
- Scorecard: six dimensions, 1-5 each.
- What is actually new.
- What is old software in costume.
- Best spicy line.
- Constructive rebuild: the one move that would make it more native.
- 60-second creator script.
- Claims to avoid.

## Bundled Tools

Use `scripts/roast_score.py` for a deterministic scorecard:

```bash
python3 scripts/roast_score.py --product "CRM with chatbot that writes follow-up emails" --features "chat, email drafts, contact search"
```

Read `references/roast-rubric.md` when writing the critique or adjusting scores.

## Quality Bar

- Be specific enough that the product team would recognize the critique.
- Keep the heat in the wording, not in unsupported accusations.
- Reward real workflow change.
- Penalize AI as decoration.
- End with a better product move, not just a dunk.
