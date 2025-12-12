#!/usr/bin/python3
"""Markdown2HTML Task 0 - validate args and create output file."""

import sys
import os

if __name__ == "__main__":
    # Vérifie qu'il y a 2 arguments
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    # Vérifie que le Markdown existe
    if not os.path.isfile(md_file):
        sys.stderr.write(f"Missing {md_file}\n")
        sys.exit(1)

    # Crée le fichier HTML vide
    with open(html_file, 'w', encoding='utf-8') as f:
        pass  # rien à écrire pour Task 0

    # Exit avec succès
    sys.exit(0)