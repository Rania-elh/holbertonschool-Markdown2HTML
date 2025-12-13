#!/usr/bin/python3
import sys
import os

# Task 0: vérifier les arguments et le fichier Markdown
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

if not os.path.isfile(sys.argv[1]):
    print(f"Missing {sys.argv[1]}", file=sys.stderr)
    sys.exit(1)

# Tout est bon → rien afficher
sys.exit(0)