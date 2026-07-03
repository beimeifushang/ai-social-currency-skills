# AI Social Currency Skills

Ten Codex and RedSkill-ready skills for AI tech creators and everyday users who want ideas that feel early, visual, useful, and socially alive.

This repo is built for creators publishing on WeChat Channels, Xiaohongshu, X, Bilibili, YouTube Shorts, TikTok, or any feed where "interesting but accurate" is the real currency.

中文一句话：这是一套给 AI 科技创作者用的“观点与产品操作系统”——先发现被低估的信号，再把观点做成可见 demo，用多代理辩论打磨表达，然后判断什么是真 AI-native，想象下一代界面，并把 prompt 产品化。

## The Six Directions

| Skill | Agent direction | What it does | Social currency |
|---|---|---|---|
| `trend-compounder` | Alpha Signal Scout | Turns AI papers, launches, repos, and messy notes into source-backed creator theses | Publish before consensus, without sounding reckless |
| `demo-theater` | Proof Director | Turns abstract AI ideas into visible proof demos, storyboards, and shot lists | Show the thing happening, not another talking-head take |
| `agent-arena` | Synthetic Panel Host | Runs persona debates to pressure-test tech theses and sharpen scripts | Borrow the energy of a panel, keep the precision of a memo |
| `future-ui-lab` | Interface Futurist | Turns AI workflows into post-chat interface concepts and demo plans | Own the "what comes after chat" conversation |
| `ai-native-roast` | Taste Critic | Scores whether AI products are truly native or just wrapper theater | Build public taste through sharp teardowns |
| `prompt-to-product` | One-Person Studio | Turns prompts and workflows into MVP briefs and launch tests | Show you can turn ideas into products |

## Everyday RedSkill Utilities

| Skill | Chinese title | What it does | Social currency |
|---|---|---|---|
| `timian-huiji-zuiti` | 体面回击嘴替 | Turns awkward or boundary-testing messages into calm, sendable Chinese replies | Gives people wording for high-friction social moments |
| `zhongcao-qingxingji` | 种草清醒机 | Helps users cool down before impulse purchases by separating need from fantasy | Makes shopping anxiety inspectable without killing the fun |
| `yinyang-huiji-ji` | 阴阳怪气回击机 | Generates snarky but bounded comeback options and flags lines that may backfire | Lets people feel witty without crossing into abuse |
| `yuanchuang-biaoda-zhijianguan` | 原创表达质检官 | Diagnoses AI-like writing patterns, weak originality, thin evidence, and low reader trust | Turns generic drafts into more specific, credible creator writing |

## Install

```bash
cp -R skills/* "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Or:

```bash
./install.sh
```

Then start a new Codex thread and invoke a skill explicitly:

```text
Use $trend-compounder to turn these links into a WeChat Channels video thesis.
Use $demo-theater to design a 60-second proof demo for this AI product idea.
Use $agent-arena to pressure-test this take and make it more publishable.
Use $future-ui-lab to turn this workflow into a post-chat AI interface concept.
Use $ai-native-roast to score this AI product and make a spicy teardown.
Use $prompt-to-product to turn this prompt into a sellable MVP plan.
Use $timian-huiji-zuiti to reply to this awkward workplace message without sounding weak.
Use $zhongcao-qingxingji to decide whether I should buy this thing I just got influenced to buy.
Use $yinyang-huiji-ji to make a bounded sarcastic comeback for this passive-aggressive comment.
Use $yuanchuang-biaoda-zhijianguan to make this Xiaohongshu draft feel more original and less generic.
```

## Why These Are "Sexy"

- They are not generic prompt packs; they encode a creator operating system.
- They turn AI news into thesis, thesis into proof, and proof into defensible public taste.
- They turn product taste into a repeatable critique and creation loop.
- They make the creator look early without losing epistemic hygiene.
- They produce artifacts people can quote, remix, and argue with.

## Repo Structure

```text
skills/
  trend-compounder/
  demo-theater/
  agent-arena/
  future-ui-lab/
  ai-native-roast/
  prompt-to-product/
  timian-huiji-zuiti/
  zhongcao-qingxingji/
  yinyang-huiji-ji/
  yuanchuang-biaoda-zhijianguan/
agents/
  alpha-signal-scout.md
  proof-director.md
  synthetic-panel-host.md
  interface-futurist.md
  taste-critic.md
  one-person-studio.md
```

## Quick Demo

```bash
python3 skills/trend-compounder/scripts/signal_brief.py \
  --topic "AI agents replacing dashboards" \
  --notes examples/dashboard-agents-notes.md

python3 skills/demo-theater/scripts/storyboard.py \
  --concept "AI agent turns a messy inbox into a CRM pipeline" \
  --duration 60

python3 skills/agent-arena/scripts/arena_pack.py \
  --thesis "AI agents will make SaaS dashboards disappear" \
  --audience "AI founders"

python3 skills/future-ui-lab/scripts/interface_canvas.py \
  --workflow "an AI agent monitors creator sponsorship deals and drafts negotiation moves" \
  --audience "AI creators"

python3 skills/ai-native-roast/scripts/roast_score.py \
  --product "CRM with chatbot that writes follow-up emails" \
  --features "chat, email drafts, contact search"

python3 skills/prompt-to-product/scripts/product_brief.py \
  --prompt "Summarize messy brand emails into creator deal terms and negotiation risks" \
  --audience "MCN operators"
```

## Publishing Philosophy

The strongest AI creator account is not the loudest one. It is the one that can repeatedly do three things:

1. Notice the non-obvious signal.
2. Prove the idea on screen.
3. Defend the take when smart people push back.
4. Judge what is actually AI-native.
5. Imagine the next interface.
6. Productize the workflow.
7. Turn everyday friction into useful AI-native utilities.
8. Raise the trust and originality of AI-assisted writing.

That is what these skills are designed to operationalize.
