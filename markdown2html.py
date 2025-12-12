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

    # For this initial step, no conversion is required; simply succeed silently.
    _ = output_path  # placeholder to acknowledge variable until conversion is added
    return 0


if __name__ == "__main__":
    sys.exit(main())

