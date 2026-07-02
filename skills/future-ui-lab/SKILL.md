---
name: future-ui-lab
description: Design post-chat AI interfaces, future UI concepts, agent canvases, ambient workflows, multimodal product interactions, and visual demo plans from AI workflows or product ideas. Use when the user asks for next-generation interface ideas, "chat is not enough" concepts, AI-native UX, spatial/voice/camera/agent UI patterns, future product demos, interaction storyboards, or creator content about where software interfaces are going.
---

# Future UI Lab

## Overview

Turn an AI workflow into an interface concept that feels like the next interaction layer, not a chatbot bolted onto old software. Optimize for a concept a creator can explain, sketch, prototype, and record.

## Workflow

1. Extract the workflow primitive.
   - Identify the user's job, the input signal, the decision loop, and the output artifact.
   - Name the current interface: dashboard, form, search box, spreadsheet, chat, timeline, inbox, canvas, camera, or voice.
   - Identify what the AI changes: intent capture, planning, memory, delegation, simulation, monitoring, or exception handling.

2. Choose the future UI pattern.
   - Use `references/interface-primitives.md` when deciding between agent canvas, live object, ambient inbox, camera layer, command rail, simulation cockpit, or memory surface.
   - Favor interfaces where state is visible and controllable. Avoid magical black boxes.
   - For creator content, choose patterns that can be demonstrated in 60 seconds.

3. Design the interaction.
   - Define the first screen, primary object, user control, AI agency boundary, and failure recovery.
   - Specify what the user sees changing on screen.
   - Include how the user interrupts, edits, audits, or approves the AI.

4. Package the concept.
   - Give the interface a memorable name.
   - Produce a 9:16 visual storyboard and optional prototype scaffold.
   - State the old UI it replaces and what remains necessary.
   - Add a "why now" argument tied to model/tooling capabilities, not vague futurism.

## Output Shape

- Interface name.
- One-line concept.
- Workflow primitive.
- Old UI replaced.
- Future UI pattern.
- Core screen layout.
- Interaction beats.
- Agency and trust boundary.
- 60-second creator demo plan.
- Prototype notes: files, components, states, and verification steps.

## Bundled Tools

Use `scripts/interface_canvas.py` for a first-pass concept pack:

```bash
python3 scripts/interface_canvas.py --workflow "an AI agent monitors creator sponsorship deals and drafts negotiation moves" --audience "AI creators"
```

Read `references/interface-primitives.md` when selecting the interface pattern.

Use `assets/interface-lab.css` as a starter stylesheet for futuristic but readable 9:16 UI demos.

## Quality Bar

- Make state visible.
- Give the human a control surface.
- Make the AI's agency boundary explicit.
- Prefer one new interaction primitive over a pile of features.
- Avoid vague neon futurism; every visual choice should explain behavior.
