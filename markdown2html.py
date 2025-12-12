#!/usr/bin/python3
"""Markdown2HTML Task 0 - validate args and create output file."""

import sys
from pathlib import Path

if __name__ == "__main__":
    # Vérifie qu'il y a 2 arguments
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    # Vérifie que le Markdown existe
    if not Path(md_file).is_file():
        sys.stderr.write(f"Missing {md_file}\n")
        exit(1)

    # Crée le fichier HTML vide
    Path(html_file).write_text("", encoding="utf-8")

    exit(0)