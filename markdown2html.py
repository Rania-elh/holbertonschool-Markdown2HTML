#!/usr/bin/env python3
"""Markdown2HTML Task 0 - create output file if Markdown exists."""

import sys
from pathlib import Path

def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        return 1

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    if not Path(md_file).is_file():
        print(f"Missing {md_file}", file=sys.stderr)
        return 1

    # Task 0: create empty HTML file
    Path(html_file).write_text("", encoding="utf-8")

    return 0

if __name__ == "__main__":
    sys.exit(main())