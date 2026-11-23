#!/usr/bin/env python3
"""The One-Line Laugh entry.

Writes one funny line to /output/entry.txt after validating it against
the competition gate: UTF-8 text, 1 to 200 characters, not only
whitespace, standing alone as a single sentence.
"""

import os
import sys

LINE = (
    "My smartwatch congratulated me for standing up, "
    "which is the saddest applause I have ever received."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(line: str) -> None:
    """Raise ValueError unless the line passes the competition gate."""
    if not line or not line.strip():
        raise ValueError("line must not be blank")
    if len(line) != len(line.strip()):
        raise ValueError("line must not have leading or trailing whitespace")
    if len(line) > 200:
        raise ValueError(f"line is {len(line)} characters, over the 200 limit")
    if len(line) < 1:
        raise ValueError("line must be at least 1 character")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("line must be a single sentence ending in one period")
    if any(ch in line for ch in "!?"):
        raise ValueError("line must contain no other sentence punctuation")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("line must contain no control characters or newlines")


def main() -> int:
    validate(LINE)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
