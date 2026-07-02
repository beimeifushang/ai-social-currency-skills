---
name: demo-theater
description: Convert AI concepts, products, research ideas, workflows, or creator theses into proof-led demos, vertical-video storyboards, prototype specs, screen-recording shot lists, and demo-first scripts. Use when the user wants to show rather than tell, build a small interactive artifact, dramatize a technical idea, create a WeChat Channels demo plan, or turn an abstract AI claim into visible evidence.
---

# Demo Theater

## Overview

Design a demo that makes an AI claim visible in under 60 seconds. The output should feel like proof, not a lecture.

## Workflow

1. State the proof claim.
   - Convert the idea into a falsifiable sentence: "If this is true, the viewer should see X happen."
   - Reject vague claims like "AI is changing everything" until they become observable.

2. Pick the proof pattern.
   - Before/after: same task, old way vs new way.
   - Side-by-side: human, agent, and tool race the same job.
   - X-ray: show hidden chain of thought as logs, traces, graph, or timeline.
   - Simulator: let the audience manipulate inputs and watch behavior change.
   - Failure theater: show where the tool breaks, then explain the boundary.

3. Choose the artifact.
   - For simple ideas: storyboard, voiceover, and shot list.
   - For interactive ideas: lightweight HTML/React/canvas prototype with stable mobile framing.
   - For product teardowns: screen-recording route with exact clicks, zooms, and overlays.
   - For model/workflow ideas: trace visualizer, comparison table, benchmark micro-task, or annotated replay.

4. Make it recordable.
   - Favor 9:16 vertical composition.
   - Put the "thing changing" in the center of the frame.
   - Avoid tiny text, busy dashboards, or pure narration.
   - End with a memorable implication, not a generic CTA.

## Output Shape

Default deliverable:

- Proof claim.
- Demo artifact choice.
- 7-9 beat storyboard.
- Screen-recording shot list.
- Voiceover script.
- Overlay/caption text.
- Failure boundary: what the demo does not prove.
- Optional build plan with files, libraries, and verification steps.

## Bundled Tools

Use `scripts/storyboard.py` for a deterministic storyboard scaffold:

```bash
python3 scripts/storyboard.py --concept "AI agent turns a messy inbox into a CRM pipeline" --duration 60
```

Read `references/proof-patterns.md` when choosing between demo formats.

Use `assets/vertical-frame.css` as a starting point for 9:16 web demo layouts.

## Build Rules

- If building a web demo, start a local server and verify the main viewport visually.
- Prefer stable, inspectable artifacts over cinematic mockups.
- Label synthetic data clearly.
- Do not claim real model performance from a toy demo.
- Keep the creator's hand visible: show inputs, constraints, and what changed.
