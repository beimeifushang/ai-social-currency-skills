---
name: trend-compounder
description: Transform AI papers, launch notes, GitHub repos, product news, raw research notes, or messy link dumps into source-backed creator theses, WeChat Channels video angles, hooks, scripts, and publishable tech POVs. Use when the user asks for AI trend analysis, social currency, hot takes, video ideas, short-form scripts, content maps, contrarian angles, narrative arbitrage, or a creator brief from multiple AI/tech signals.
---

# Trend Compounder

## Overview

Turn scattered AI signals into a compact creator thesis with evidence, tension, and a video-ready narrative. Optimize for "accurate enough to defend, sharp enough to spread."

## Workflow

1. Collect the signals.
   - Use the user's links, notes, transcripts, papers, repos, release notes, or product pages.
   - If the user asks for latest/current/today or the claim is time-sensitive, browse and cite current primary or high-quality sources before forming the angle.
   - Separate facts from interpretation. Never invent benchmark numbers, release dates, funding amounts, or company claims.

2. Build a signal ledger.
   - Source: link/title/entity/date when available.
   - Factual claim: what the source actually supports.
   - Delta: what changed versus the likely audience's prior belief.
   - Maturity: rumor, demo, preview, shipped, adopted, regulated, or deprecated.
   - Creator risk: overclaiming, hype, privacy, safety, China-specific availability, or missing evidence.

3. Compound the angle.
   - Find the tension: faster vs cheaper, open vs closed, agentic vs reliable, demo vs production, scale vs trust, labor saving vs skill loss.
   - Name the wedge in one sentence: "This matters because X just became Y for Z."
   - Produce three intensity levels: safe, sharp, and spicy. The spicy version may be provocative, but must remain defensible.

4. Package for short-form video.
   - Hook: 1 line that makes a technical viewer stop.
   - Thesis: 1 defensible sentence.
   - Proof: 2-4 source-backed claims.
   - Visual plan: what appears on screen, not just narration.
   - Script spine: 0-5s hook, 5-20s evidence, 20-45s implication, 45-60s sharp takeaway.
   - Caption and comment prompt: invite disagreement without engagement bait or misinformation.

## Output Shape

Default deliverable:

- Title: a memorable thesis name.
- One-line POV: the clearest claim.
- Why now: the trigger signal.
- Signal ledger: concise table of sources and supported claims.
- Three creator angles: safe, sharp, spicy.
- 60-second script: natural spoken language.
- Visual proof plan: screens, diagrams, demos, or overlays to capture.
- "Do not say" guardrails: claims that would outrun the evidence.

## Bundled Tools

Use `scripts/signal_brief.py` when the user provides a raw notes file or wants a deterministic first pass:

```bash
python3 scripts/signal_brief.py --topic "AI agents replacing dashboards" --notes notes.md
```

Read `references/angle-grammar.md` when the content needs more original framing, a stronger title, or a cleaner short-form structure.

## Quality Bar

- Prefer one strong, weirdly specific point over ten generic observations.
- Keep claims traceable to sources.
- Make the user sound like a thoughtful operator, not a hype account.
- Avoid absolute predictions unless the evidence is unusually strong.
- Give the user at least one visual they can actually put on screen.
