#!/usr/bin/env python3
"""Lightweight validator for Sales Sheet Builder Markdown outputs."""

from __future__ import annotations

import re
import sys
import argparse
from pathlib import Path


WORKBOOK_REQUIRED_SECTIONS = [
    "Sales Sheet Research Brief",
    "JTBD Map",
    "Positioning And Alternative Map",
    "Gap Analysis",
    "Feature, Benefit, Outcome Map",
    "Evidence Log",
    "Final Sales Sheet Copy",
    "Missing Proof",
    "Optional Variants",
]

REVISION_WORKBOOK_SECTIONS = [
    "Input And Feedback Notes",
    "What Changed",
]

PUBLISHED_REQUIRED_SECTIONS = [
    "Buyer-Facing Sales Sheet",
]

INTERNAL_FRAMEWORK_PHRASES = [
    "jtbd map",
    "job executor",
    "core functional job",
    "differentiator thesis",
    "evidence log",
    "gap analysis",
    "strategy matrix",
    "four-question pitch",
]

REVISION_PHRASES = [
    "feedback",
    "prior output",
    "prior draft",
    "revision",
    "what changed",
    "tune",
    "tuning",
]

DISCOURAGED_PHRASES = [
    "orchestration",
    "activation",
    "unlock",
    "revolutionize",
    "transformation",
    "autonomous",
    "agentic",
    "platform of platforms",
    "single pane of glass",
    "ai-powered growth engine",
    "seamless",
    "supercharge",
    "next-generation",
    "end-to-end",
    "robust",
    "powerful",
]

ALLOWED_CONTEXT_PHRASES = [
    "autonomous ai sdr",
]

PLACEHOLDER_PATTERN = re.compile(
    r"(\bTBD\b|\bTODO\b|\[insert\b|\[add\b|lorem ipsum|example\.com)",
    re.IGNORECASE,
)
NUMBER_PATTERN = re.compile(
    r"(?<![\w/])(?:"
    r"\d+(?:\.\d+)?%"
    r"|\$\d[\d,]*(?:\.\d+)?(?:k|m|b)?"
    r"|\d[\d,]*(?:\.\d+)?(?:x|k|m|b)"
    r"|\d[\d,]*(?:\.\d+)?\s+(?:hours?|days?|weeks?|months?|years?)"
    r")",
    re.IGNORECASE,
)


def section_present(text: str, section: str) -> bool:
    pattern = re.compile(rf"^#+\s*(?:[A-Z]\.\s*)?{re.escape(section)}", re.IGNORECASE | re.MULTILINE)
    return bool(pattern.search(text))


def line_has_source_context(lines: list[str], index: int) -> bool:
    window = "\n".join(lines[max(0, index - 2) : min(len(lines), index + 3)]).lower()
    return "http" in window or "source" in window or "evidence log" in window or "cited" in window


def missing_sections(text: str, required_sections: list[str]) -> list[str]:
    return [section for section in required_sections if not section_present(text, section)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Sales Sheet Builder Markdown outputs.")
    parser.add_argument(
        "--mode",
        choices=["auto", "published", "workbook"],
        default="auto",
        help="Validation structure to enforce. Default: auto accepts either a compressed published sheet or full workbook.",
    )
    parser.add_argument("markdown_file", help="Markdown file to validate.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = Path(args.markdown_file)
    if not path.exists():
        print(f"Missing file: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    warnings: list[str] = []
    errors: list[str] = []

    missing_published = missing_sections(text, PUBLISHED_REQUIRED_SECTIONS)
    missing_workbook = missing_sections(text, WORKBOOK_REQUIRED_SECTIONS)

    if args.mode == "published":
        for section in missing_published:
            errors.append(f"Missing required published section: {section}")
    elif args.mode == "workbook":
        for section in missing_workbook:
            errors.append(f"Missing required workbook section: {section}")
    elif missing_published and missing_workbook:
        errors.append("Output does not match the published or workbook structure.")
        errors.append("Missing published sections: " + ", ".join(missing_published))
        errors.append("Missing workbook sections: " + ", ".join(missing_workbook))

    if PLACEHOLDER_PATTERN.search(text):
        errors.append("Output contains placeholder text such as TODO, TBD, or [insert].")

    lower_for_phrase_scan = lower
    for allowed_phrase in ALLOWED_CONTEXT_PHRASES:
        lower_for_phrase_scan = lower_for_phrase_scan.replace(allowed_phrase, "")

    found_phrases = sorted({phrase for phrase in DISCOURAGED_PHRASES if phrase in lower_for_phrase_scan})
    if found_phrases:
        warnings.append("Discouraged phrases found: " + ", ".join(found_phrases))

    lines = text.splitlines()
    for index, line in enumerate(lines):
        if "|" in line:
            continue
        if NUMBER_PATTERN.search(line) and not line_has_source_context(lines, index):
            warnings.append(f"Numeric claim may need a nearby source on line {index + 1}: {line.strip()[:120]}")

    is_published_shape = not missing_published
    is_workbook_shape = not missing_workbook

    if args.mode == "published" or (args.mode == "auto" and is_published_shape and not is_workbook_shape):
        word_count = len(re.findall(r"\b[\w'-]+\b", text))
        if word_count > 900:
            warnings.append(f"Published sales sheet is long ({word_count} words). Consider compressing below 900 words.")
        found_internal = sorted({phrase for phrase in INTERNAL_FRAMEWORK_PHRASES if phrase in lower})
        if found_internal:
            warnings.append("Published sales sheet includes internal framework language: " + ", ".join(found_internal))
        if section_present(text, "Sales Sheet Research Brief") or section_present(text, "JTBD Map") or section_present(text, "Evidence Log"):
            warnings.append("Published sales sheet appears to include workbook sections. Move them to a separate workbook.")
    else:
        if "one clear buyer" not in lower and "primary buyer" not in lower:
            warnings.append("Output may not explicitly identify the primary buyer.")

        for phrase in ["status quo", "reference competitor", "economic competitor", "differentiator thesis", "deficiency", "big idea", "downside impact", "job executor", "core functional job"]:
            if phrase not in lower:
                warnings.append(f"Output may be missing positioning language: {phrase}")

        if "additional increase" not in lower and "additional decrease" not in lower:
            warnings.append("Output may be missing the additional increase/decrease created by the new approach.")

        is_revision = any(phrase in lower for phrase in REVISION_PHRASES)
        if is_revision:
            for section in REVISION_WORKBOOK_SECTIONS:
                if not section_present(text, section):
                    warnings.append(f"Revision workbook may be missing section: {section}")

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")

    if errors:
        return 1

    print("Sales sheet structure validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
