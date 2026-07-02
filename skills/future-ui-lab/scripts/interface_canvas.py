#!/usr/bin/env python3
"""Generate a future AI interface concept pack."""

from __future__ import annotations

import argparse
import json
import re


PATTERNS = {
    "agent canvas": ["agent", "multi-step", "tool", "workflow", "delegate", "plan"],
    "ambient inbox": ["monitor", "inbox", "email", "signal", "alert", "triage"],
    "simulation cockpit": ["simulate", "pricing", "forecast", "strategy", "scenario", "planning"],
    "memory surface": ["memory", "relationship", "crm", "creator", "sales", "personal"],
    "camera layer": ["camera", "visual", "screen", "image", "physical"],
    "command rail": ["browser", "app", "shortcut", "existing", "dashboard"],
    "live object": ["document", "contract", "brief", "profile", "plan", "artifact"],
}


def compact(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def choose_pattern(workflow: str) -> str:
    lowered = workflow.lower()
    scores = {
        pattern: sum(1 for word in words if word in lowered)
        for pattern, words in PATTERNS.items()
    }
    winner, score = max(scores.items(), key=lambda item: item[1])
    return winner if score else "agent canvas"


def build_pack(workflow: str, audience: str) -> dict:
    workflow = compact(workflow)
    pattern = choose_pattern(workflow)
    interface_name = {
        "agent canvas": "Trace Canvas",
        "ambient inbox": "Signal Inbox",
        "simulation cockpit": "Leverage Cockpit",
        "memory surface": "Living Memory Board",
        "camera layer": "Reality Overlay",
        "command rail": "Action Rail",
        "live object": "Live Brief",
    }[pattern]
    return {
        "workflow": workflow,
        "audience": audience,
        "interface_name": interface_name,
        "pattern": pattern,
        "one_line": f"{interface_name} turns '{workflow}' into a visible control surface instead of another chat thread.",
        "old_ui_replaced": "dashboard, spreadsheet, inbox, or chat prompt depending on the current workflow",
        "core_screen": [
            "Left: live inputs and context",
            "Center: primary workflow object",
            "Right: AI actions, trace, and approval queue",
            "Bottom: human controls for pause, edit, approve, rollback",
        ],
        "interaction_beats": [
            "User drops in the raw workflow material.",
            "AI turns it into a visible object with states and risks.",
            "User edits constraints rather than rewriting prompts.",
            "AI proposes next actions with traceable reasons.",
            "User approves, corrects, or rolls back the action.",
        ],
        "agency_boundary": [
            "AI may draft, rank, simulate, and route.",
            "AI may not commit external actions without approval.",
            "Every automated action must expose source, reason, and rollback.",
        ],
        "demo_plan": [
            "0-5s: Show the old interface pain.",
            f"5-15s: Reveal {interface_name} as the new object-centered interface.",
            "15-35s: Show the AI transforming state on screen.",
            "35-50s: Interrupt and correct the AI.",
            "50-60s: Close with the new UI thesis.",
        ],
    }


def render_markdown(pack: dict) -> str:
    return f"""# Future UI Concept: {pack['interface_name']}

Audience: {pack['audience']}
Pattern: {pack['pattern']}

## One-Line Concept

{pack['one_line']}

## Workflow

{pack['workflow']}

## Old UI Replaced

{pack['old_ui_replaced']}

## Core Screen

{chr(10).join(f"- {item}" for item in pack['core_screen'])}

## Interaction Beats

{chr(10).join(f"- {item}" for item in pack['interaction_beats'])}

## Agency Boundary

{chr(10).join(f"- {item}" for item in pack['agency_boundary'])}

## 60-Second Demo Plan

{chr(10).join(f"- {item}" for item in pack['demo_plan'])}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a future AI interface concept pack.")
    parser.add_argument("--workflow", required=True, help="AI workflow or product idea.")
    parser.add_argument("--audience", default="AI creators", help="Target audience.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown.")
    args = parser.parse_args()
    pack = build_pack(args.workflow, args.audience)
    print(json.dumps(pack, ensure_ascii=False, indent=2) if args.json else render_markdown(pack))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
