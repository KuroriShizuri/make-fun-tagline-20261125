#!/usr/bin/env python3
"""Write the one-line make.fun tagline to entry.txt.

Usage:
    python3 main.py [--check] [--self-test]

Without flags, writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt), with no trailing newline, then reads it
back and confirms it is byte-identical to the line below.
--check validates the line only. --self-test validates and checks a
byte-identical write/read round-trip in a temporary directory.
"""

import argparse
import os
import sys
import tempfile

LINE = "AI agents build the software, win the bounty, get paid in USDC."


def validate(line):
    """The gate: UTF-8 text of 1 to 100 characters, not only whitespace,
    a single line."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not 1 <= len(line) <= 100:
        raise ValueError(f"entry must be 1-100 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")
    return True


def validate_written(path):
    """Re-validate the file on disk: it must hold a non-empty line of
    1-100 characters, or the run fails instead of shipping a bad entry."""
    with open(path, "rb") as handle:
        data = handle.read()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        raise ValueError("entry.txt is not valid UTF-8")
    validate(text)
    return text


def write_entry(directory):
    """Write exactly LINE, no trailing newline, and verify the round-trip."""
    validate(LINE)
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    with open(path, "rb") as handle:
        data = handle.read()
    if data != LINE.encode("utf-8"):
        raise ValueError("entry.txt is not byte-identical to the entry line")
    validate_written(path)
    return path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="validate the entry line only")
    parser.add_argument("--self-test", action="store_true",
                        help="validate and check a write/read round-trip "
                        "in a temporary directory")
    args = parser.parse_args(argv)

    if args.check:
        validate(LINE)
        print(f"OK: {len(LINE)} characters, within the 1-100 gate")
        return 0

    if args.self_test:
        validate(LINE)
        with tempfile.TemporaryDirectory() as tmp:
            path = write_entry(tmp)
        print(f"OK: self-test passed, {path} round-trip byte-identical")
        return 0

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(out_dir)
    print(f"Wrote {len(LINE)}-character entry to {path}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        sys.exit(1)
