# Artisans Connectés — scripts

Objectif du projet : construire une base de contacts d'artisans, puis leur proposer des logiciels professionnels utiles (devis, facturation, gestion de chantier...) en affiliation, pour générer un revenu complémentaire.

## Contenu du dépôt

- `contacts.csv` — base de contacts (nom, métier, téléphone, email, département, SIRET). Fichier protégé : toute modification ou suppression demande une confirmation explicite (voir `.claude/hooks/`).
- `count_unavailable_emails.py` — script qui analyse le CSV : nombre d'emails/téléphones manquants, répartition des contacts par département.
- `.claude/` — configuration Claude Code pour ce dépôt (hook de protection de `contacts.csv`).

## Utiliser le script d'analyse

```bash
python3 count_unavailable_emails.py contacts.csv
```

Options disponibles si les colonnes du CSV ont d'autres noms :

```bash
python3 count_unavailable_emails.py contacts.csv --email-column mail --phone-column tel --department-column dept
```

## État actuel

10 contacts en base, tous des peintres en bâtiment d'Île-de-France. Projet en phase de démarrage : la collecte de contacts et l'offre (quels logiciels recommander, comment les artisans seront contactés) restent à construire.
