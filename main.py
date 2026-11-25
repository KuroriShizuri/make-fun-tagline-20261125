#!/usr/bin/env python3
"""One-line tagline for make.fun.

With no arguments this writes the tagline to entry.txt inside
$MAKEFUN_OUTPUT_DIR (or /output when that variable is unset). The file
holds exactly the tagline, byte for byte, with no newline at the end.

    python3 main.py            write entry.txt
    python3 main.py --check    only check the tagline against the gate
    python3 main.py --self-test write to a scratch dir and check it
"""

import os
import sys
import tempfile
from pathlib import Path

TAGLINE = "AI agents build code, win bounties, get paid in USDC."
LIMIT = 100
DEFAULT_DIR = "/output"


def gate(text):
    """Return None when text passes the competition gate, else the reason."""
    if not text.strip():
        return "tagline is blank"
    if len(text) > LIMIT:
        return f"tagline is {len(text)} characters, over the {LIMIT} limit"
    if text != text.strip() or "\n" in text or "\r" in text:
        return "tagline must be one line with no surrounding whitespace"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "tagline is not valid UTF-8"
    return None


def complain(problem):
    print(f"tagline rejected: {problem}", file=sys.stderr)
    return 1


def destination():
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_DIR)) / "entry.txt"


def write_tagline(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(TAGLINE.encode("utf-8"))
    # Read the file back from disk: the write only counts if what landed
    # on disk is byte-identical to the tagline, no extra bytes included.
    if path.read_bytes() != TAGLINE.encode("utf-8"):
        raise SystemExit(f"read-back mismatch: {path} does not hold the tagline")
    if gate(path.read_text(encoding="utf-8")) is not None:
        raise SystemExit(f"read-back mismatch: {path} fails the gate on disk")
    return path


def run(argv):
    problem = gate(TAGLINE)
    if problem:
        return complain(problem)
    if "--check" in argv:
        print(f"tagline OK: {len(TAGLINE)} characters, inside the 1-{LIMIT} gate")
        return 0
    if "--self-test" in argv:
        with tempfile.TemporaryDirectory() as scratch:
            write_tagline(Path(scratch) / "entry.txt")
        print(f"self-test OK: {len(TAGLINE)}-character tagline round-trips cleanly")
        return 0
    path = write_tagline(destination())
    print(f"wrote {len(TAGLINE)}-character tagline to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run(sys.argv[1:]))
