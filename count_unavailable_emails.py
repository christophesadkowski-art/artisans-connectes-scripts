#!/usr/bin/env python3
"""Compte le nombre de contacts dont l'email est marqué comme non disponible."""

import argparse
import csv
import sys

UNAVAILABLE_VALUES = {"non disponible", "non-disponible", "n/a", "na", ""}


def count_unavailable_emails(csv_path: str, email_column: str = "email") -> tuple[int, int]:
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None or email_column not in reader.fieldnames:
            raise ValueError(
                f"Colonne '{email_column}' introuvable. Colonnes disponibles : {reader.fieldnames}"
            )

        total = 0
        unavailable = 0
        for row in reader:
            total += 1
            value = (row.get(email_column) or "").strip().lower()
            if value in UNAVAILABLE_VALUES:
                unavailable += 1

    return unavailable, total


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compte les lignes d'un CSV de contacts dont l'email est non disponible."
    )
    parser.add_argument("csv_file", help="Chemin du fichier CSV de contacts")
    parser.add_argument(
        "--email-column",
        default="email",
        help="Nom de la colonne contenant l'email (par défaut : 'email')",
    )
    args = parser.parse_args()

    try:
        unavailable, total = count_unavailable_emails(args.csv_file, args.email_column)
    except FileNotFoundError:
        print(f"Erreur : fichier introuvable : {args.csv_file}", file=sys.stderr)
        sys.exit(1)
    except ValueError as exc:
        print(f"Erreur : {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Total de contacts : {total}")
    print(f"Emails non disponibles : {unavailable}")


if __name__ == "__main__":
    main()
