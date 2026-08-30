# Architecture

## En une phrase
Un dépôt de scripts pour exploiter des listes de contacts d'artisans (actuellement des peintres en bâtiment d'Île-de-France) : compter les emails/téléphones manquants et répartir les contacts par département.

## Stack
- Langage / runtime : Python 3 (script `#!/usr/bin/env python3`, module `argparse`/`csv` de la stdlib uniquement)
- Framework principal : aucun — script CLI autonome, pas de dépendances externes
- Base de données : aucune — les données vivent dans `contacts.csv`, un fichier CSV versionné dans le dépôt
- Services externes : [EN ATTENTE : aucun connu à ce jour]

## Carte des dossiers
- `count_unavailable_emails.py` → script CLI unique : analyse `contacts.csv`, compte les emails/téléphones "non disponible" et résume les contacts par département
- `contacts.csv` → jeu de données réel de contacts (peintres en bâtiment IDF) : colonnes `nom,metier,telephone,email,departement,siret`
- `.claude/settings.json` → configuration des hooks Claude Code (PreToolUse)
- `.claude/hooks/protect-contacts-csv.sh` → hook qui exige une confirmation explicite avant toute modification/suppression de `contacts.csv`

## Flux de données
`contacts.csv` est lu en entrée par `count_unavailable_emails.py` via `csv.DictReader`. Le script parcourt chaque ligne, compte les valeurs vides ou marquées "non disponible" pour les colonnes email et téléphone, et agrège les contacts par département (`Counter`). Le résultat est imprimé sur stdout ; en cas de fichier introuvable ou de colonne manquante, une erreur est écrite sur stderr et le script sort avec un code non nul.

## Ce qui N'EXISTE PAS (et ne doit pas être créé)
- Pas de base de données ni d'ORM — le CSV est la seule source de données
- Pas de dépendances tierces (pas de `requirements.txt`/`pyproject.toml`) — rester sur la stdlib Python
- Pas de suite de tests, pas de CI, pas de README à ce jour — [EN ATTENTE : à ajouter si le projet grandit]
- Pas de serveur web ni d'API — c'est un outil en ligne de commande
