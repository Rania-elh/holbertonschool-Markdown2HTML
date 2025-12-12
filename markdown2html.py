#!/usr/bin/env python3
"""Simple Markdown to HTML placeholder script."""

import sys
from pathlib import Path


def main() -> int:
    """Validate arguments and create the output file."""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        return 1

    input_path_arg = sys.argv[1]
    output_path_arg = sys.argv[2]

    input_path = Path(input_path_arg)
    output_path = Path(output_path_arg)

    if not input_path.is_file():
        print(f"Missing {input_path_arg}", file=sys.stderr)
        return 1

    # For this initial step, just copy the input content to the output file.
    output_path.write_text(input_path.read_text(encoding="utf-8"), encoding="utf-8")
    return 1


if __name__ == "__main__":
    exit_code = main()
    # Use sys.exit to propagate the exact code in all shells/OS.
    sys.exit(exit_code)

