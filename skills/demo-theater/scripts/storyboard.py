#!/usr/bin/env python3
"""Generate a vertical-video demo storyboard scaffold."""

from __future__ import annotations

import argparse
import json


BEATS = [
    ("Cold open", "Show the outcome first, before explaining the setup."),
    ("Proof claim", "Say the falsifiable claim in one sentence."),
    ("Old way", "Show the slow or fragile baseline."),
    ("Input", "Reveal the exact prompt, file, data, or constraint."),
    ("Transformation", "Show the AI/tool/agent doing visible work."),
    ("X-ray", "Expose logs, steps, intermediate state, or decisions."),
    ("Result", "Compare output quality against the baseline."),
    ("Boundary", "Name what the demo does not prove."),
    ("Takeaway", "End with the strategic implication."),
]


def build_storyboard(concept: str, duration: int, audience: str) -> dict:
    seconds = max(30, min(duration, 120))
    beat_length = max(3, seconds // len(BEATS))
    rows = []
    cursor = 0
    for index, (name, intent) in enumerate(BEATS, 1):
        start = cursor
        end = seconds if index == len(BEATS) else min(seconds, cursor + beat_length)
        cursor = end
        rows.append(
            {
                "beat": index,
                "time": f"{start:02d}-{end:02d}s",
                "name": name,
                "screen": f"{intent} Keep the central visual tied to: {concept}.",
                "voiceover": voiceover_line(name, concept, audience),
                "overlay": overlay_line(name),
            }
        )
    return {
        "concept": concept,
        "audience": audience,
        "duration": seconds,
        "proof_claim": f"Make this visible on screen: {concept}. The viewer should see a meaningful before/after change, not just hear an explanation.",
        "storyboard": rows,
        "recording_notes": [
            "Compose in 9:16 and keep the changing element in the center.",
            "Use synthetic data unless real data is cleared for publishing.",
            "Make the final frame readable as a standalone screenshot.",
        ],
    }


def voiceover_line(name: str, concept: str, audience: str) -> str:
    mapping = {
        "Cold open": f"Start with the finished result: {concept}.",
        "Proof claim": f"For {audience}, the claim is simple: can this remove a real step, not just make a nicer demo?",
        "Old way": "Here is the baseline workflow most people still tolerate.",
        "Input": "Now watch the exact input; this is where weak demos usually hide the trick.",
        "Transformation": "The interesting part is not that AI answers, but that it moves the workflow forward.",
        "X-ray": "Look at the trace: this is the machinery behind the magic.",
        "Result": "Now compare the result against the baseline.",
        "Boundary": "This does not prove the whole market has changed; it proves this boundary moved.",
        "Takeaway": "The strategic question is who gets leverage when this becomes ordinary.",
    }
    return mapping[name]


def overlay_line(name: str) -> str:
    overlays = {
        "Cold open": "Show the result first",
        "Proof claim": "What would prove it?",
        "Old way": "Baseline",
        "Input": "Same input, visible constraints",
        "Transformation": "Watch the workflow move",
        "X-ray": "Trace, not vibes",
        "Result": "Before vs after",
        "Boundary": "What this does not prove",
        "Takeaway": "The new leverage point",
    }
    return overlays[name]


def render_markdown(pack: dict) -> str:
    rows = []
    for item in pack["storyboard"]:
        rows.append(
            f"| {item['time']} | {item['name']} | {item['screen']} | {item['voiceover']} | {item['overlay']} |"
        )
    return f"""# Demo Storyboard: {pack['concept']}

Audience: {pack['audience']}
Duration: {pack['duration']}s

## Proof Claim

{pack['proof_claim']}

## Storyboard

| Time | Beat | Screen | Voiceover | Overlay |
|---|---|---|---|---|
{chr(10).join(rows)}

## Recording Notes

{chr(10).join(f"- {note}" for note in pack['recording_notes'])}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a demo storyboard.")
    parser.add_argument("--concept", required=True, help="AI concept or demo idea.")
    parser.add_argument("--duration", type=int, default=60, help="Target duration in seconds.")
    parser.add_argument("--audience", default="AI tech viewers", help="Target audience.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown.")
    args = parser.parse_args()

    pack = build_storyboard(args.concept, args.duration, args.audience)
    if args.json:
        print(json.dumps(pack, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(pack))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
