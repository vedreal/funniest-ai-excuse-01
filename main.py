#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line, at most 200 characters, giving the funniest excuse an
AI agent could offer after it fails a task, to /output/entry.txt.

The excuse was chosen from ten candidates written for this bounty and
judged against the house judge's brief: it must be an excuse in the
agent's own voice, funny on the first read with a real turn, one line
and complete, original (no hallucination / reboot / training-data
jokes), and specific and vivid rather than a vague apology.
"""

import os
import sys

# The chosen excuse (90 characters, one line, no trailing newline in the
# file itself — the gate counts characters, and the file holds exactly
# this text).
ENTRY = (
    "My code worked on the first try, so I assumed it was a trap "
    "and rewrote it until it broke."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > 200:
        print(f"entry invalid: {len(text)} characters", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

