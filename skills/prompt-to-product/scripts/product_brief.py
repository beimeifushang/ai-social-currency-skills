#!/usr/bin/env python3
"""Turn a prompt or workflow into a product MVP brief."""

from __future__ import annotations

import argparse
import json
import re


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def infer_shape(prompt: str) -> str:
    lowered = prompt.lower()
    if any(word in lowered for word in ["browser", "website", "web app", "chrome"]):
        return "Chrome extension"
    if any(word in lowered for word in ["report", "analysis", "brief", "deck"]):
        return "Report generator"
    if any(word in lowered for word in ["team", "internal", "approve", "route"]):
        return "Internal agent"
    if any(word in lowered for word in ["template", "prompt pack", "course"]):
        return "Template pack"
    return "Micro-SaaS"


def build_brief(prompt: str, audience: str) -> dict:
    prompt = clean(prompt)
    shape = infer_shape(prompt)
    product_name = "Workflow Wedge"
    if "creator" in (prompt + audience).lower():
        product_name = "Creator Deal Desk"
    elif "email" in prompt.lower() or "inbox" in prompt.lower():
        product_name = "Inbox Operator"
    elif "report" in prompt.lower():
        product_name = "Instant Analyst"
    return {
        "prompt": prompt,
        "audience": audience,
        "product_name": product_name,
        "product_shape": shape,
        "icp": f"{audience} with a recurring high-friction workflow and enough urgency to pay for speed or judgment.",
        "job_to_be_done": "Turn messy inputs into a reviewed, structured output that can be used immediately.",
        "mvp_scope": [
            "Input intake for the messy source material.",
            "Structured output with editable fields.",
            "Human review and approval step.",
            "Export/share action.",
            "History of prior outputs for reuse.",
        ],
        "anti_features": [
            "Team permissions before first buyer validation.",
            "Complex dashboards before repeated use is proven.",
            "Generic chat interface as the primary product.",
        ],
        "pricing_experiment": [
            "Start with a concierge pilot or paid template.",
            "Test $29-$99/month prosumer pricing or a $300-$1000 business pilot.",
            "Charge for saved time, reduced risk, or faster throughput.",
        ],
        "first_10_customers": [
            "Find operators already doing this workflow manually.",
            "Offer a before/after demo using their real but non-sensitive sample.",
            "Ask for payment or a public testimonial before building integrations.",
        ],
        "kill_test": "If five target users will not share a real sample input or pay for a manual pilot, do not build the app yet.",
        "demo_script": [
            "Show the messy input.",
            "Show the product turning it into structured work.",
            "Show the human approval boundary.",
            "Show the exported result.",
            "Close with who should pay and why now.",
        ],
    }


def render_markdown(brief: dict) -> str:
    return f"""# Prompt To Product Brief: {brief['product_name']}

Audience: {brief['audience']}
Product shape: {brief['product_shape']}

## Source Prompt

{brief['prompt']}

## ICP

{brief['icp']}

## Job To Be Done

{brief['job_to_be_done']}

## MVP Scope

{chr(10).join(f"- {item}" for item in brief['mvp_scope'])}

## Anti-Features

{chr(10).join(f"- {item}" for item in brief['anti_features'])}

## Pricing Experiment

{chr(10).join(f"- {item}" for item in brief['pricing_experiment'])}

## First 10 Customers

{chr(10).join(f"- {item}" for item in brief['first_10_customers'])}

## Kill Test

{brief['kill_test']}

## 60-Second Demo Script

{chr(10).join(f"- {item}" for item in brief['demo_script'])}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Turn a prompt into a product MVP brief.")
    parser.add_argument("--prompt", required=True, help="Prompt, workflow, or automation idea.")
    parser.add_argument("--audience", default="AI operators", help="Target buyer or user audience.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown.")
    args = parser.parse_args()
    brief = build_brief(args.prompt, args.audience)
    print(json.dumps(brief, ensure_ascii=False, indent=2) if args.json else render_markdown(brief))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
