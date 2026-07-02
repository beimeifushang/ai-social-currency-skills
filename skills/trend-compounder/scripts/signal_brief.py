#!/usr/bin/env python3
"""Create a compact AI creator signal brief from raw notes."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


URL_RE = re.compile(r"https?://\S+")

TAGS = {
    "agent": ["agent", "agents", "workflow", "tool call", "automation"],
    "model": ["model", "llm", "multimodal", "reasoning", "benchmark"],
    "open-source": ["open source", "oss", "github", "weights", "apache", "mit"],
    "product": ["launch", "pricing", "product", "api", "integration"],
    "trust": ["privacy", "safety", "copyright", "regulation", "provenance"],
    "china": ["wechat", "douyin", "china", "alibaba", "tencent", "baidu"],
}


def read_notes(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    if not sys.stdin.isatty():
        return sys.stdin.read()
    return ""


def split_items(text: str) -> list[str]:
    lines = []
    for raw in text.splitlines():
        cleaned = raw.strip(" -\t")
        if cleaned:
            lines.append(cleaned)
    if lines:
        return lines
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return paragraphs


def detect_tags(text: str) -> list[str]:
    lowered = text.lower()
    found = []
    for tag, needles in TAGS.items():
        if any(needle in lowered for needle in needles):
            found.append(tag)
    return found or ["general"]


def compact(text: str, limit: int = 110) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "..."


def build_brief(topic: str, notes: str, audience: str) -> dict:
    items = split_items(notes)
    all_text = "\n".join(items)
    tags = detect_tags(all_text + " " + topic)
    urls = URL_RE.findall(all_text)

    ledger = []
    for index, item in enumerate(items[:12], 1):
        ledger.append(
            {
                "id": index,
                "source_or_note": compact(item, 140),
                "urls": URL_RE.findall(item),
                "tags": detect_tags(item),
                "claim_to_verify": compact(re.sub(URL_RE, "", item), 120),
            }
        )

    primary_tag = tags[0]
    wedges = [
        f"{topic}: the hidden shift is not the tool, but the workflow it starts to own.",
        f"For {audience}, the underpriced question is who gets leverage once {primary_tag} becomes routine.",
        "The spicy take: the demo is already visible, but distribution and trust decide who captures value.",
    ]

    hooks = [
        f"Everyone is watching the model. I think the real story is what {topic} does to the interface.",
        "This looks like an AI feature, but it may be a workflow land grab.",
        "The demo is impressive. The more interesting question is who cannot ignore it next.",
    ]

    return {
        "topic": topic,
        "audience": audience,
        "tags": tags,
        "source_count": len(items),
        "url_count": len(urls),
        "ledger": ledger,
        "narrative_wedges": wedges,
        "hooks": hooks,
        "script_spine": [
            "0-5s: Name the surprising shift.",
            "5-20s: Show one concrete source-backed signal.",
            "20-40s: Explain the tension smart people will argue about.",
            "40-55s: Name the winner, loser, or new behavior.",
            "55-60s: Add the guardrail: what would make this take wrong.",
        ],
        "guardrails": [
            "Verify dates, pricing, benchmarks, and release status before publishing.",
            "Do not turn early demos into adoption claims.",
            "Separate source-supported facts from creator interpretation.",
        ],
    }


def render_markdown(brief: dict) -> str:
    rows = []
    for row in brief["ledger"]:
        rows.append(
            f"| {row['id']} | {row['source_or_note']} | {', '.join(row['tags'])} | {row['claim_to_verify']} |"
        )
    ledger = "\n".join(rows) if rows else "| - | No notes provided | - | Add sources before publishing |"

    return f"""# Signal Brief: {brief['topic']}

Audience: {brief['audience']}
Detected tags: {', '.join(brief['tags'])}
Sources/notes: {brief['source_count']} items, {brief['url_count']} URLs

## Signal Ledger

| # | Source or note | Tags | Claim to verify |
|---|---|---|---|
{ledger}

## Narrative Wedges

{chr(10).join(f"- {item}" for item in brief['narrative_wedges'])}

## Hooks

{chr(10).join(f"- {item}" for item in brief['hooks'])}

## 60-Second Spine

{chr(10).join(f"- {item}" for item in brief['script_spine'])}

## Guardrails

{chr(10).join(f"- {item}" for item in brief['guardrails'])}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an AI creator signal brief.")
    parser.add_argument("--topic", required=True, help="The trend, thesis, or topic to frame.")
    parser.add_argument("--notes", help="Path to a notes file. Reads stdin when omitted.")
    parser.add_argument("--audience", default="AI tech creators", help="Target audience.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown.")
    args = parser.parse_args()

    brief = build_brief(args.topic, read_notes(args.notes), args.audience)
    if args.json:
        print(json.dumps(brief, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(brief))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
