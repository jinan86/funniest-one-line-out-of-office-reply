#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — make.fun entry.

Writes a single one-line out-of-office auto-reply to /output/entry.txt.
Stdlib only, fully deterministic: the same bytes on every run.
"""

import os

ENTRY = "I'm on a brief sabbatical from being useful. Normal service resumes when I remember my password."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

# Gate note (competition.yaml): /output/entry.txt must be UTF-8 text of
# 1-160 characters, not only whitespace. ENTRY above is 96 characters,
# one line, no trailing newline, so it passes the gate as written.
