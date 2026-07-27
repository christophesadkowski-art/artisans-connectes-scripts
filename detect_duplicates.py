#!/usr/bin/env python3
"""Signale les doublons potentiels dans un CSV de contacts en croisant téléphone et SIRET.

Deux lignes sont considérées comme un doublon potentiel uniquement si leur
téléphone ET leur SIRET (normalisés) correspondent tous les deux. Les lignes
dont le téléphone ou le SIRET est marqué `non disponible` (ou vide) sont
exclues de la comparaison, car une donnée absente ne peut jamais être traitée
comme une valeur réelle (voir CLAUDE.md).

Ce script ne supprime et ne modifie jamais le CSV source : il se contente de
signaler les groupes de doublons potentiels.
"""

import argparse
import csv
import re
import sys
from collections import defaultdict

UNAVAILABLE_VALUES = {"non disponible", "non-disponible", "n/a", "na", ""}


def normalize_phone(raw_phone: str) -> str:
    digits_only = re.sub(r"[\s.\-()]", "", raw_phone)
    if digits_only.startswith("+33"):
        digits_only = "0" + digits_only[3:]
    elif digits_only.startswith("0033"):
        digits_only = "0" + digits_only[4:]
    return digits_only


def normalize_siret(raw_siret: str) -> str:
    return re.sub(r"[\s.\-]", "", raw_siret)


def find_duplicates(
    csv_path: str,
    phone_column: str = "telephone",
    siret_column: str = "siret",
    name_column: str = "nom",
) -> list:
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        for column in (phone_column, siret_column, name_column):
            if column not in fieldnames:
                raise ValueError(
                    f"Colonne '{column}' introuvable. Colonnes disponibles : {fieldnames}"
                )

        groups = defaultdict(list)
        for line_number, row in enumerate(reader, start=2):
            phone = (row.get(phone_column) or "").strip()
            siret = (row.get(siret_column) or "").strip()
            if phone.lower() in UNAVAILABLE_VALUES or siret.lower() in UNAVAILABLE_VALUES:
                continue

            key = (normalize_phone(phone), normalize_siret(siret))
            groups[key].append(
                {
                    "line": line_number,
                    "nom": row.get(name_column, ""),
                    "telephone": phone,
                    "siret": siret,
                }
            )

    return [rows for rows in groups.values() if len(rows) > 1]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Signale les doublons potentiels (téléphone ET SIRET identiques) sans les supprimer."
    )
    parser.add_argument("csv_file", help="Chemin du fichier CSV de contacts")
    parser.add_argument(
        "--phone-column",
        default="telephone",
        help="Nom de la colonne contenant le téléphone (par défaut : 'telephone')",
    )
    parser.add_argument(
        "--siret-column",
        default="siret",
        help="Nom de la colonne contenant le SIRET (par défaut : 'siret')",
    )
    parser.add_argument(
        "--name-column",
        default="nom",
        help="Nom de la colonne contenant le nom de l'entreprise (par défaut : 'nom')",
    )
    parser.add_argument(
        "--output",
        help="Chemin d'un CSV de rapport listant les doublons détectés (optionnel)",
    )
    args = parser.parse_args()

    try:
        duplicate_groups = find_duplicates(
            args.csv_file, args.phone_column, args.siret_column, args.name_column
        )
    except FileNotFoundError:
        print(f"Erreur : fichier introuvable : {args.csv_file}", file=sys.stderr)
        sys.exit(1)
    except ValueError as exc:
        print(f"Erreur : {exc}", file=sys.stderr)
        sys.exit(1)

    if not duplicate_groups:
        print("Aucun doublon potentiel détecté (téléphone + SIRET identiques).")
        return

    print(f"{len(duplicate_groups)} groupe(s) de doublons potentiels détecté(s) :\n")
    for group_id, rows in enumerate(duplicate_groups, start=1):
        print(f"Groupe {group_id} (téléphone={rows[0]['telephone']}, siret={rows[0]['siret']}) :")
        for row in rows:
            print(f"  ligne {row['line']} : {row['nom']}")
        print()

    if args.output:
        with open(args.output, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["groupe", "ligne", "nom", "telephone", "siret"])
            writer.writeheader()
            for group_id, rows in enumerate(duplicate_groups, start=1):
                for row in rows:
                    writer.writerow(
                        {
                            "groupe": group_id,
                            "ligne": row["line"],
                            "nom": row["nom"],
                            "telephone": row["telephone"],
                            "siret": row["siret"],
                        }
                    )
        print(f"Rapport écrit dans : {args.output}")


if __name__ == "__main__":
    main()
