#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt.

The line: our alerting looked healthy the whole incident, because the
metric the alert watches died together with the exporter that emits it
-- the classic observability trap where a green dashboard means "no
signal", not "no problem". It is spoken in first person, uses correct
jargon (dashboard, metric, alert, exporter), lands in one sentence, and
turns on a twist a developer recognises instantly.

Deterministic: no randomness, no network, no clock, no environment
input. The same bytes are written on every run.
"""

import os

ENTRY = (
    "The dashboard stayed green the whole time \u2014 "
    "the metric we alert on died with the exporter, "
    "so we've been flying blind for six hours."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
