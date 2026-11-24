#!/usr/bin/env python3
"""One-line developer excuse for the AI-judge-laugh competition.

The joke: the dashboard never went red during the incident, because
the metric the alert is wired to died at the same time as the exporter
producing it. Green here means "no data", not "healthy" -- the classic
observability blind spot, told in first person in a single sentence.

The program is fully deterministic: standard library only, no network,
no randomness, no clock reads, no environment input. Every run writes
exactly the same bytes to /output/entry.txt.
"""

from pathlib import Path

# The excuse, held as its three clauses so the setup, the twist and
# the punchline each stay readable on their own line.
CLAUSES = (
    "The dashboard stayed green the whole time \u2014 ",
    "the metric we alert on died with the exporter, ",
    "so we've been flying blind for six hours.",
)

OUTPUT_PATH = Path("/output/entry.txt")


def build_entry() -> str:
    """Join the clauses into the single-line entry text."""
    return "".join(CLAUSES)


def check_entry(text: str) -> None:
    """Guard the competition limits: 1-200 chars, non-blank, one line."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry length {len(text)} out of range 1-200")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    text = build_entry()
    check_entry(text)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
