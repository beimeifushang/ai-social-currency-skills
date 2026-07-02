#!/usr/bin/env python3
"""Create a reusable multi-agent debate packet for a tech thesis."""

from __future__ import annotations

import argparse
import json


PERSONAS = [
    (
        "Frontier Optimist",
        "Argue why the shift is larger, faster, and more behavior-changing than consensus expects.",
    ),
    (
        "Skeptical Engineer",
        "Attack reliability, hidden complexity, eval quality, integration cost, and benchmark theater.",
    ),
    (
        "Market Realist",
        "Ask who pays, who switches, what budget moves, and which distribution channel wins.",
    ),
    (
        "China Contextualizer",
        "Localize around platforms, regulation, procurement, language, and everyday workflows.",
    ),
    (
        "Trust Editor",
        "Flag privacy, safety, copyright, provenance, labor, and reputation risk.",
    ),
    (
        "Audience Editor",
        "Turn the strongest defensible argument into a short-form creator package.",
    ),
]


def build_pack(thesis: str, audience: str) -> dict:
    personas = [
        {
            "name": name,
            "mission": mission,
            "opening_prompt": f"Given the thesis '{thesis}' for {audience}, {mission} Give one strong point and one objection.",
        }
        for name, mission in PERSONAS
    ]
    return {
        "thesis": thesis,
        "audience": audience,
        "personas": personas,
        "rounds": [
            "Opening: each persona gives the strongest version of its position.",
            "Collision: each persona attacks the weakest assumption in another role's argument.",
            "Synthesis: choose the most novel defensible claim and name what evidence is still needed.",
        ],
        "scorecard": {
            "novelty": "Would a smart AI viewer hear a new thought?",
            "evidence": "Can the claim survive source checks?",
            "visual_potential": "Can it be shown on screen?",
            "controversy": "Will thoughtful people disagree?",
            "creator_fit": "Does it match the creator's audience and voice?",
        },
        "publishable_output": [
            "One-sentence POV",
            "Strongest objection",
            "Evidence to verify",
            "60-second script spine",
            "Pinned comment that invites serious disagreement",
        ],
    }


def render_markdown(pack: dict) -> str:
    persona_rows = [
        f"| {item['name']} | {item['mission']} | `{item['opening_prompt']}` |"
        for item in pack["personas"]
    ]
    score_rows = [f"| {key} | {value} |" for key, value in pack["scorecard"].items()]
    return f"""# Agent Arena Pack

Thesis: {pack['thesis']}
Audience: {pack['audience']}

## Personas

| Persona | Mission | Opening prompt |
|---|---|---|
{chr(10).join(persona_rows)}

## Debate Rounds

{chr(10).join(f"- {item}" for item in pack['rounds'])}

## Scorecard

| Criterion | Question |
|---|---|
{chr(10).join(score_rows)}

## Publishable Output

{chr(10).join(f"- {item}" for item in pack['publishable_output'])}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a multi-agent debate packet.")
    parser.add_argument("--thesis", required=True, help="The thesis to pressure-test.")
    parser.add_argument("--audience", default="AI tech creators", help="Target audience.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown.")
    args = parser.parse_args()

    pack = build_pack(args.thesis, args.audience)
    if args.json:
        print(json.dumps(pack, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(pack))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
