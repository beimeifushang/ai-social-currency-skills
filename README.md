# AI Social Currency Skills

Three Codex skills and three agent directions for AI tech creators who want ideas that feel early, visual, and defensible.

This repo is built for creators publishing on WeChat Channels, X, Bilibili, YouTube Shorts, TikTok, or any feed where "interesting but accurate" is the real currency.

中文一句话：这是一套给 AI 科技创作者用的“观点操作系统”——先发现被低估的信号，再把观点做成可见的 demo，最后用多代理辩论把表达打磨到既性感又能防守。

## The Three Directions

| Skill | Agent direction | What it does | Social currency |
|---|---|---|---|
| `trend-compounder` | Alpha Signal Scout | Turns AI papers, launches, repos, and messy notes into source-backed creator theses | Publish before consensus, without sounding reckless |
| `demo-theater` | Proof Director | Turns abstract AI ideas into visible proof demos, storyboards, and shot lists | Show the thing happening, not another talking-head take |
| `agent-arena` | Synthetic Panel Host | Runs persona debates to pressure-test tech theses and sharpen scripts | Borrow the energy of a panel, keep the precision of a memo |

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
```

## Why These Are "Sexy"

- They are not generic prompt packs; they encode a creator operating system.
- They turn AI news into thesis, thesis into proof, and proof into defensible public taste.
- They make the creator look early without losing epistemic hygiene.
- They produce artifacts people can quote, remix, and argue with.

## Repo Structure

```text
skills/
  trend-compounder/
  demo-theater/
  agent-arena/
agents/
  alpha-signal-scout.md
  proof-director.md
  synthetic-panel-host.md
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
```

## Publishing Philosophy

The strongest AI creator account is not the loudest one. It is the one that can repeatedly do three things:

1. Notice the non-obvious signal.
2. Prove the idea on screen.
3. Defend the take when smart people push back.

That is what these skills are designed to operationalize.
