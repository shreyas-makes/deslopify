#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path


PATTERNS = [
    (r"\bhere's the thing\b", "throat-clearing opener"),
    (r"\b(at the end of the day|end of the day)\b", "cliche closer"),
    (r"\b(let that sink in)\b", "cliche emphasis"),
    (r"\b(that being said)\b", "formulaic pivot"),
    (r"\bin today's (fast-paced|rapidly changing)\b", "generic setup"),
    (r"\b(it is important to|it's important to)\b", "softened directive"),
    (r"\bthere (are|were) a few key\b", "vague quantifier"),
    (r"\bnot only\b.+\bbut also\b", "template contrast"),
    (r"\bnot\b.+\bbut\b", "template contrast"),
    (r"\bultimately\b", "softened conclusion"),
    (r"\b(elevate|leverage|harness|unlock)\b", "corporate filler"),
    (r"\b(in the world of|in the realm of)\b", "generic scene-setting"),
    (r"\bthe key (is|to)\b", "predictable framing"),
    (r"\b(it's worth noting|it is worth noting)\b", "hedged aside"),
    (r"\b(as we (all )?know)\b", "assumptive aside"),
]


def load_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"Error: failed to read {path}: {exc}", file=sys.stderr)
        raise SystemExit(1)


def scan(text: str) -> list[tuple[int, str, str]]:
    hits: list[tuple[int, str, str]] = []
    lines = text.splitlines()
    for idx, line in enumerate(lines, start=1):
        for pattern, label in PATTERNS:
            if re.search(pattern, line, flags=re.IGNORECASE):
                hits.append((idx, label, line.strip()))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Flag common AI-tell phrases in a Markdown draft."
    )
    parser.add_argument("path", help="Path to the draft file to scan.")
    args = parser.parse_args()

    path = Path(args.path)
    text = load_text(path)
    hits = scan(text)

    if not hits:
        print("No AI-tell patterns detected.")
        return 0

    print("AI-tell patterns detected:")
    for line_no, label, snippet in hits:
        print(f"- line {line_no}: {label} -> {snippet}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
