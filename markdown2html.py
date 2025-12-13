#!/usr/bin/python3
import sys
import os

def main():
    # Vérifier le nombre d'arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Vérifier si le fichier markdown existe
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(f"Missing {filename}", file=sys.stderr)
        sys.exit(1)

    # Si tout est bon : ne rien afficher
    sys.exit(0)

if __name__ == "__main__":
    main()
