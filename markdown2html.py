#!/usr/bin/env python3
"""Simple Markdown to HTML placeholder script."""

import sys
from pathlib import Path


def main() -> int:
    """Validate arguments and create the output file."""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        return 1

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.is_file():
        print(f"Missing {input_path.name}", file=sys.stderr)
        return 1

    # Placeholder: copy content as-is; conversion will be added in later steps.
    output_path.write_text(input_path.read_text(encoding="utf-8"), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())

