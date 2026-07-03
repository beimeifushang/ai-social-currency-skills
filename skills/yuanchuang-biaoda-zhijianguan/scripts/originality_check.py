#!/usr/bin/env python3
"""Originality and human-readability checks for Chinese drafts.

This script is intentionally heuristic. It does not predict or bypass any
platform detector. It highlights patterns that often make a draft feel generic,
over-templated, weakly evidenced, or low-trust to human readers.
"""

import argparse
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path


TEMPLATE_PATTERNS = [
    r"随着.+?(?:发展|进步|普及)",
    r"(?:在当今|如今|当前|近年来).+?(?:越来越|愈发)",
    r"(?:众所周知|不可否认|毋庸置疑|值得注意的是)",
    r"(?:首先|其次|再次|最后|此外|另外|与此同时|更重要的是)",
    r"(?:总而言之|综上所述|总的来说|由此可见)",
    r"(?:深入|全面|系统)(?:地)?(?:分析|探讨|研究)",
    r"(?:具有|拥有)(?:重要|深远|积极|巨大)(?:的)?(?:意义|价值|影响)",
    r"(?:有效|高效|切实)(?:地)?(?:推动|促进|提升|加强)",
    r"(?:赋能|助力|打造|构建).{0,12}(?:生态|闭环|体系|能力)",
]

TRANSITION_WORDS = (
    "首先", "其次", "再次", "最后", "此外", "另外", "因此", "然而", "不过",
    "与此同时", "不仅如此", "更重要的是", "事实上", "实际上", "换言之",
    "也就是说", "具体来说", "简而言之", "从而", "进而",
)

ABSTRACT_WORDS = (
    "能力", "价值", "效率", "体验", "生态", "闭环", "体系", "赋能", "升级",
    "优化", "提升", "增长", "机会", "挑战", "趋势", "竞争力", "影响力",
)

FIRST_PERSON = ("我", "我们", "自己", "亲身", "遇到", "踩坑", "发现", "试过")
EVIDENCE_MARKERS = (
    "截图", "数据", "报告", "采访", "来源", "链接", "案例", "实验", "测试",
    "复盘", "对比", "样本", "日期", "月份", "季度",
)


def load_text(args):
    if args.text:
        return args.text
    if args.input:
        path = Path(args.input)
        if not path.exists():
            print(f"ERROR: file not found: {args.input}", file=sys.stderr)
            sys.exit(1)
        return path.read_text(encoding="utf-8")
    print("ERROR: provide --input or --text", file=sys.stderr)
    sys.exit(1)


def split_sentences(text):
    return [s.strip() for s in re.split(r"[。！？!?；;]", text) if len(s.strip()) > 2]


def coefficient_of_variation(values):
    if len(values) < 2:
        return None
    avg = sum(values) / len(values)
    if avg == 0:
        return None
    variance = sum((value - avg) ** 2 for value in values) / len(values)
    return math.sqrt(variance) / avg


def count_occurrences(words, text):
    return sum(text.count(word) for word in words)


def analyze(text):
    compact = re.sub(r"\s+", "", text)
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    sentences = split_sentences(text)
    char_count = len(compact)

    template_hits = []
    for pattern in TEMPLATE_PATTERNS:
        for match in re.finditer(pattern, text):
            template_hits.append({
                "text": match.group(0)[:80],
                "start": match.start(),
                "pattern": pattern,
            })

    transition_count = count_occurrences(TRANSITION_WORDS, text)
    abstract_count = count_occurrences(ABSTRACT_WORDS, text)
    first_person_count = count_occurrences(FIRST_PERSON, text)
    evidence_count = count_occurrences(EVIDENCE_MARKERS, text)
    number_count = len(re.findall(r"\d+(?:\.\d+)?%?|[一二三四五六七八九十]+个|[一二三四五六七八九十]+次", text))
    quote_count = len(re.findall(r"[“「].+?[”」]", text))

    sentence_lengths = [len(s) for s in sentences]
    paragraph_lengths = [len(p) for p in paragraphs]
    sentence_cv = coefficient_of_variation(sentence_lengths)
    paragraph_cv = coefficient_of_variation(paragraph_lengths)

    starters = []
    for sentence in sentences:
        clean = re.sub(r"^[\s,，、：:]+", "", sentence)
        if len(clean) >= 3:
            starters.append(clean[:3])
    repeated_starters = {k: v for k, v in Counter(starters).items() if v >= 3}

    issues = []
    risk = 0

    if template_hits:
        risk += min(28, len(template_hits) * 4)
        issues.append({
            "type": "template_phrases",
            "severity": "high" if len(template_hits) >= 4 else "medium",
            "detail": f"发现 {len(template_hits)} 处模板表达，容易让文章显得像通用稿。",
        })

    transition_density = transition_count / max(len(sentences), 1)
    if transition_density > 0.28:
        risk += 14
        issues.append({"type": "transition_density", "severity": "high", "detail": f"过渡词密度 {transition_density:.1%}，结构痕迹偏重。"})
    elif transition_density > 0.14:
        risk += 7
        issues.append({"type": "transition_density", "severity": "medium", "detail": f"过渡词密度 {transition_density:.1%}，略显条理化。"})

    if sentence_cv is not None and len(sentences) >= 6:
        if sentence_cv < 0.24:
            risk += 12
            issues.append({"type": "uniform_sentences", "severity": "high", "detail": f"句长变异系数 {sentence_cv:.2f}，节奏过齐。"})
        elif sentence_cv < 0.34:
            risk += 6
            issues.append({"type": "uniform_sentences", "severity": "medium", "detail": f"句长变异系数 {sentence_cv:.2f}，句式略单一。"})

    if paragraph_cv is not None and len(paragraphs) >= 4 and paragraph_cv < 0.22:
        risk += 8
        issues.append({"type": "uniform_paragraphs", "severity": "medium", "detail": f"段落长度变异系数 {paragraph_cv:.2f}，段落形状偏整齐。"})

    if repeated_starters:
        risk += 6
        detail = "、".join(f"「{key}」x{value}" for key, value in repeated_starters.items())
        issues.append({"type": "repeated_starters", "severity": "medium", "detail": f"句首重复：{detail}。"})

    abstract_ratio = abstract_count / max(len(sentences), 1)
    if abstract_ratio > 1.2:
        risk += 10
        issues.append({"type": "abstract_wording", "severity": "medium", "detail": f"抽象大词约 {abstract_count} 处，读者可能看不到具体画面。"})

    authenticity_anchors = first_person_count + evidence_count + number_count + quote_count
    if char_count > 300 and authenticity_anchors < 3:
        risk += 12
        issues.append({"type": "thin_original_material", "severity": "high", "detail": "真实材料锚点偏少：缺少经历、数字、案例、引用或来源。"})

    trust_bonus = min(24, authenticity_anchors * 3)
    originality_score = max(0, min(100, 100 - risk + trust_bonus // 2))
    risk = max(0, min(100, risk))

    if originality_score >= 85:
        grade = "可直接发或小修"
    elif originality_score >= 70:
        grade = "需要局部增强"
    elif originality_score >= 50:
        grade = "需要明显重写"
    else:
        grade = "建议回到真实材料重写"

    return {
        "stats": {
            "characters": char_count,
            "paragraphs": len(paragraphs),
            "sentences": len(sentences),
            "sentence_cv": sentence_cv,
            "paragraph_cv": paragraph_cv,
        },
        "scores": {
            "ai_like_risk": risk,
            "originality_score": originality_score,
            "grade": grade,
        },
        "signals": {
            "template_hits": template_hits[:20],
            "transition_count": transition_count,
            "abstract_word_count": abstract_count,
            "first_person_count": first_person_count,
            "evidence_marker_count": evidence_count,
            "number_count": number_count,
            "quote_count": quote_count,
            "repeated_starters": repeated_starters,
        },
        "issues": issues,
        "recommended_patches": recommend_patches(issues),
    }


def recommend_patches(issues):
    patch_map = {
        "template_phrases": "删除万能开头和总结句，直接写具体事件、冲突或反常识观察。",
        "transition_density": "少用首先/其次/此外，改成因果、转折或场景推进。",
        "uniform_sentences": "加入短句、反问、停顿和一两个更长的解释句，制造自然节奏。",
        "uniform_paragraphs": "让重点段更长，转折段更短，不要每段都像同一个模具。",
        "repeated_starters": "改掉重复句首，让句子从动作、场景、判断、细节分别进入。",
        "abstract_wording": "把抽象词换成可见动作、具体对象、数字或人的反应。",
        "thin_original_material": "补真实经历、截图来源、具体数字、反例或你自己的取舍标准。",
    }
    return [patch_map[item["type"]] for item in issues if item["type"] in patch_map]


def format_text(report):
    lines = []
    stats = report["stats"]
    scores = report["scores"]
    lines.append("═══ 原创表达质检报告 ═══")
    lines.append(f"字数: {stats['characters']} | 段落: {stats['paragraphs']} | 句子: {stats['sentences']}")
    lines.append(f"AI 腔风险: {scores['ai_like_risk']}/100 | 原创表达分: {scores['originality_score']}/100 | 评级: {scores['grade']}")
    if report["issues"]:
        lines.append("\n── 主要问题 ──")
        for item in report["issues"]:
            lines.append(f"- [{item['severity']}] {item['detail']}")
    else:
        lines.append("\n没有发现明显模板化问题。")
    if report["recommended_patches"]:
        lines.append("\n── 优先补丁 ──")
        for patch in report["recommended_patches"]:
            lines.append(f"- {patch}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Check Chinese drafts for originality and generic AI-like writing patterns.")
    parser.add_argument("--input", "-i", help="Input markdown or text file")
    parser.add_argument("--text", "-t", help="Inline text")
    parser.add_argument("--format", "-f", choices=["text", "json"], default="text")
    args = parser.parse_args()

    report = analyze(load_text(args))
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(format_text(report))


if __name__ == "__main__":
    main()
