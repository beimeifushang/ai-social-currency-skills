#!/usr/bin/env python3
"""Score whether an AI product is truly AI-native."""

from __future__ import annotations

import argparse
import json
import re


DIMENSIONS = [
    "workflow_ownership",
    "model_leverage",
    "interface_transformation",
    "data_flywheel",
    "trust_boundary",
    "distribution_wedge",
]

KEYWORDS = {
    "workflow_ownership": ["agent", "approve", "route", "monitor", "workflow", "tool", "autonomous", "task"],
    "model_leverage": ["reasoning", "retrieval", "multimodal", "voice", "vision", "tool", "eval", "memory"],
    "interface_transformation": ["canvas", "trace", "object", "timeline", "overlay", "sidecar", "workflow"],
    "data_flywheel": ["feedback", "learn", "history", "proprietary", "crm", "records", "memory"],
    "trust_boundary": ["audit", "approval", "permission", "privacy", "source", "rollback", "review"],
    "distribution_wedge": ["niche", "vertical", "community", "marketplace", "channel", "buyer", "team"],
}


def score_dimension(text: str, dimension: str) -> int:
    lowered = text.lower()
    hits = sum(1 for word in KEYWORDS[dimension] if word in lowered)
    if hits >= 4:
        return 5
    if hits >= 2:
        return 4
    if hits == 1:
        return 3
    if any(word in lowered for word in ["chat", "summarize", "draft", "generate"]):
        return 2
    return 1


def verdict(avg: float) -> str:
    if avg >= 4:
        return "AI-native"
    if avg >= 3:
        return "AI-assisted"
    if avg >= 2:
        return "AI-wrapped"
    return "AI theater"


def build_score(product: str, features: str) -> dict:
    text = re.sub(r"\s+", " ", f"{product} {features}").strip()
    scores = {dimension: score_dimension(text, dimension) for dimension in DIMENSIONS}
    avg = round(sum(scores.values()) / len(scores), 2)
    weakest = min(scores, key=scores.get)
    strongest = max(scores, key=scores.get)
    return {
        "product": product,
        "features": features,
        "scores": scores,
        "average": avg,
        "verdict": verdict(avg),
        "strongest_dimension": strongest,
        "weakest_dimension": weakest,
        "spicy_line": spicy_line(verdict(avg), weakest),
        "constructive_rebuild": rebuild_move(weakest),
        "guardrail": "Treat this as a heuristic from the provided description; verify real product behavior before publishing.",
    }


def spicy_line(label: str, weakest: str) -> str:
    if label == "AI-native":
        return "This is not a wrapper; it is trying to own the work loop."
    if weakest == "interface_transformation":
        return "The product may have AI inside, but the interface is still wearing old clothes."
    if weakest == "workflow_ownership":
        return "The AI answers questions but does not yet own the job."
    if weakest == "trust_boundary":
        return "The demo wants agency, but the product has not earned trust."
    return "The AI is present, but the native wedge is still hiding."


def rebuild_move(weakest: str) -> str:
    moves = {
        "workflow_ownership": "Pick one recurring workflow loop and let the AI move it from input to reviewed output.",
        "model_leverage": "Use model capability beyond generic generation: retrieval, tools, multimodal input, or evals.",
        "interface_transformation": "Replace the chat surface with a visible object, trace, approval queue, or canvas.",
        "data_flywheel": "Capture feedback and workflow history so the product improves with use.",
        "trust_boundary": "Add sources, permissions, approval, rollback, and audit trail.",
        "distribution_wedge": "Choose a sharper buyer and urgent trigger before adding features.",
    }
    return moves[weakest]


def render_markdown(score: dict) -> str:
    rows = [f"| {key} | {value}/5 |" for key, value in score["scores"].items()]
    return f"""# AI Native Roast Score

Product: {score['product']}
Verdict: {score['verdict']} ({score['average']}/5)

## Scorecard

| Dimension | Score |
|---|---|
{chr(10).join(rows)}

## Sharp Read

{score['spicy_line']}

## Strongest Dimension

{score['strongest_dimension']}

## Weakest Dimension

{score['weakest_dimension']}

## Constructive Rebuild

{score['constructive_rebuild']}

## Guardrail

{score['guardrail']}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Score whether an AI product is AI-native.")
    parser.add_argument("--product", required=True, help="Product description.")
    parser.add_argument("--features", default="", help="Feature list or notes.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown.")
    args = parser.parse_args()
    score = build_score(args.product, args.features)
    print(json.dumps(score, ensure_ascii=False, indent=2) if args.json else render_markdown(score))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
