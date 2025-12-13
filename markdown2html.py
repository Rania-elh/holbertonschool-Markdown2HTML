#!/usr/bin/python3
"""
Markdown to HTML - Task 0
"""

import sys
import os

if __name__ == "__main__":
    # Not enough arguments
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    # Markdown file does not exist
    if not os.path.isfile(sys.argv[1]):
        sys.stderr.write(f"Missing {sys.argv[1]}\n")
        sys.exit(1)

    # SUCCESS: do absolutely nothing else
    sys.exit(0)
