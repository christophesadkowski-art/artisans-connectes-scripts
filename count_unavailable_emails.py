#!/usr/bin/env python3
"""Analyse un CSV de contacts : emails et téléphones non disponibles, répartition par département."""

import argparse
import csv
import sys
from collections import Counter

UNAVAILABLE_VALUES = {"non disponible", "non-disponible", "n/a", "na", ""}


def analyze_contacts(
    csv_path: str,
    email_column: str = "email",
    phone_column: str = "telephone",
    department_column: str = "departement",
) -> dict:
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        for column in (email_column, phone_column, department_column):
            if column not in fieldnames:
                raise ValueError(
                    f"Colonne '{column}' introuvable. Colonnes disponibles : {fieldnames}"
                )

        total = 0
        unavailable_emails = 0
        unavailable_phones = 0
        by_department = Counter()
        for row in reader:
            total += 1
            if (row.get(email_column) or "").strip().lower() in UNAVAILABLE_VALUES:
                unavailable_emails += 1
            if (row.get(phone_column) or "").strip().lower() in UNAVAILABLE_VALUES:
                unavailable_phones += 1
            department = (row.get(department_column) or "").strip() or "Inconnu"
            by_department[department] += 1

    return {
        "total": total,
        "unavailable_emails": unavailable_emails,
        "unavailable_phones": unavailable_phones,
        "by_department": by_department,
    }


def graphify(stats: dict, output_path: str) -> None:
    """Génère un graphique en barres des contacts par département."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    departments = sorted(stats["by_department"].items())
    labels = [d for d, _ in departments]
    counts = [c for _, c in departments]

    fig, ax = plt.subplots(figsize=(max(6, len(labels) * 0.6), 5))
    ax.bar(labels, counts, color="#4C72B0")
    ax.set_xlabel("Département")
    ax.set_ylabel("Nombre de contacts")
    ax.set_title("Contacts par département")
    plt.xticks(rotation=45, ha="right")
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compte les emails/téléphones non disponibles et résume les contacts par département."
    )
    parser.add_argument("csv_file", help="Chemin du fichier CSV de contacts")
    parser.add_argument(
        "--email-column",
        default="email",
        help="Nom de la colonne contenant l'email (par défaut : 'email')",
    )
    parser.add_argument(
        "--phone-column",
        default="telephone",
        help="Nom de la colonne contenant le téléphone (par défaut : 'telephone')",
    )
    parser.add_argument(
        "--department-column",
        default="departement",
        help="Nom de la colonne contenant le département (par défaut : 'departement')",
    )
    parser.add_argument(
        "--graph",
        metavar="FICHIER",
        help="Génère un graphique en barres des contacts par département dans FICHIER (ex: departements.png)",
    )
    args = parser.parse_args()

    try:
        stats = analyze_contacts(
            args.csv_file, args.email_column, args.phone_column, args.department_column
        )
    except FileNotFoundError:
        print(f"Erreur : fichier introuvable : {args.csv_file}", file=sys.stderr)
        sys.exit(1)
    except ValueError as exc:
        print(f"Erreur : {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Total de contacts : {stats['total']}")
    print(f"Emails non disponibles : {stats['unavailable_emails']}")
    print(f"Téléphones non disponibles : {stats['unavailable_phones']}")
    print("\nContacts par département :")
    for department, count in sorted(stats["by_department"].items()):
        print(f"  {department} : {count}")

    if args.graph:
        try:
            graphify(stats, args.graph)
        except ImportError:
            print(
                "Erreur : matplotlib est requis pour --graph. Installez-le avec : pip install -r requirements.txt",
                file=sys.stderr,
            )
            sys.exit(1)
        print(f"\nGraphique enregistré : {args.graph}")


if __name__ == "__main__":
    main()
