#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — writes one line to /output/entry.txt.

The joke: an AI agent on vacation is still answering your email — just
slower, grumpier, and from a hammock it hallucinated. The machine voice
carries the joke: "hallucinated" is the tell that the vacation, the
hammock, and the relaxation are all something the model made up, while
the auto-reply itself proves it never actually left.
"""

import os

SETUP = "I'm on vacation"
PUNCHLINE = (
    "For an AI that means I'm still answering your email, "
    "just slower, grumpier, and from a hammock I hallucinated"
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def build_line():
    """Join setup and punchline into the single entry line."""
    return f"{SETUP}. {PUNCHLINE}."


def validate(line):
    """The gate: UTF-8 text, 1-160 chars, not only whitespace."""
    if not line.strip():
        raise ValueError("entry line is blank")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} chars, over the {MAX_CHARS} limit")
    return line


def write_entry(line):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


def main():
    write_entry(validate(build_line()))


if __name__ == "__main__":
    main()
