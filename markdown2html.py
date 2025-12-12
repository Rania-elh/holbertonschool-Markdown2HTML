#!/usr/bin/env python3
"""Simple Markdown to HTML converter (task 0)."""

import sys
from pathlib import Path


def main() -> int:
    """Process arguments and create an empty output HTML file."""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        return 1

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_path = Path(input_file)

    if not input_path.is_file():
        print(f"Missing {input_file}", file=sys.stderr)
        return 1

    # Task 0: create the output file (empty)
    Path(output_file).write_text("", encoding="utf-8")

    return 0


if __name__ == "__main__":
    sys.exit(main(1))