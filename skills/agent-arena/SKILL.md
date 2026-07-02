---
name: agent-arena
description: Run structured multi-agent debates that pressure-test AI and technology theses, creator scripts, product narratives, investment-style arguments, and controversial hot takes. Use when the user asks for agent directions, persona debate, critique, red-team review, stronger POVs, script sharpening, content angle selection, skeptical review, or a defensible but provocative take.
---

# Agent Arena

## Overview

Use multiple specialized personas to turn a soft tech opinion into a defensible, memorable position. The goal is not consensus; the goal is a sharper thesis with visible tradeoffs.

## Workflow

1. Frame the thesis.
   - Convert the user's idea into one claim that can be attacked.
   - Identify the audience: builders, founders, investors, creators, operators, or general tech viewers.
   - If facts are time-sensitive, browse and cite sources before running the debate.

2. Assemble the arena.
   - Frontier Optimist: argues why the change is bigger than people think.
   - Skeptical Engineer: attacks feasibility, reliability, hidden complexity, and benchmark theater.
   - Market Realist: asks who pays, who switches, and what distribution channel matters.
   - China Contextualizer: localizes infrastructure, platform, regulation, language, and workflow constraints.
   - Trust Editor: flags privacy, safety, labor, and reputation risks.
   - Audience Editor: turns the winning argument into a short-form creator package.

3. Run three rounds.
   - Opening: each persona gives the strongest version of its argument.
   - Collision: personas attack assumptions, missing evidence, and weak wording.
   - Synthesis: choose the thesis that is both distinctive and defensible.

4. Ship the output.
   - Winner thesis: the version to publish.
   - Strongest objection: the comment section will ask this.
   - Evidence needed: what must be sourced or demonstrated before publishing.
   - Creator package: title, hook, 60-second script, visual beat, and pinned comment.

## Output Shape

Default deliverable:

- Arena setup: thesis, audience, stakes.
- Persona table: role, strongest point, biggest objection.
- Debate transcript: compact, not theatrical filler.
- Scorecard: novelty, evidence, visual potential, controversy, creator fit.
- Publishable POV: one sentence.
- Script refinement: hook, body, turn, close.
- Risk notes: what not to overstate.

## Bundled Tools

Use `scripts/arena_pack.py` when the user wants a reusable debate packet or prompt scaffold:

```bash
python3 scripts/arena_pack.py --thesis "AI agents will make SaaS dashboards disappear" --audience "AI founders"
```

Read `references/persona-deck.md` when customizing roles, adding domain-specific agents, or changing the debate criteria.

## Debate Rules

- Steelman before attacking.
- Mark unsupported claims as hypotheses.
- Prefer named tradeoffs over vague disagreement.
- Do not launder speculation through fictional expert voices.
- End with a decision the creator can publish, not an endless brainstorm.
