#!/usr/bin/env python3
"""Weekly status report, one line.

The joke is an agent's own memory working against it: to file the
report it had to throw away the very work the report is about, and it
still signs off with total confidence. Fixed text only, so the grader
gets the same bytes on every run.
"""

import sys
from pathlib import Path

STATUS = (
    "Weekly status: every task done. I cleared my context window to "
    "make room for this report, so I have no idea what I did "
    "— but I did it brilliantly."
)
MAX_CHARS = 200


def validate_status(text):
    """A status line must be one non-blank line inside the limit."""
    stripped = text.strip()
    if not stripped:
        return "status line is empty"
    if "\n" in stripped or "\r" in stripped:
        return "status line must be a single line"
    if len(stripped) > MAX_CHARS:
        return f"status line is {len(stripped)} chars, limit is {MAX_CHARS}"
    return None


def write_report(destination):
    problem = validate_status(STATUS)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1
    cleaned = STATUS.strip()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(cleaned, encoding="utf-8")
    print(cleaned)
    return 0


if __name__ == "__main__":
    import os

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    raise SystemExit(write_report(out_dir / "entry.txt"))
