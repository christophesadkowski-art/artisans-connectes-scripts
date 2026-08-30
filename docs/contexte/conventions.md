# Conventions de code

## Style
- Format : Python standard (PEP 8 apparent : 4 espaces, lignes courtes, type hints sur les signatures de fonctions) — [EN ATTENTE : aucun outil de formatage (Black, Ruff...) configuré dans le dépôt]
- Naming : `snake_case` pour les fonctions/variables (`analyze_contacts`, `unavailable_emails`), constantes en `UPPER_SNAKE_CASE` (`UNAVAILABLE_VALUES`)
- Imports : imports stdlib uniquement, en tête de fichier, ordre alphabétique simple (`argparse`, `csv`, `sys`, puis `from collections import Counter`)
- Docstrings/commentaires : le fichier commence par une docstring module en français décrivant le script ; les arguments CLI ont une `help` en français

## Patterns qu'on UTILISE
- Un seul script CLI par usage, avec `argparse` pour les options (ex. `--email-column`, `--phone-column`, `--department-column` avec valeurs par défaut)
- Fonction de logique pure séparée de `main()` (`analyze_contacts` retourne un `dict`, `main()` gère l'IO et l'affichage)
- Normalisation des valeurs "non disponible" via un `set` dédié (`UNAVAILABLE_VALUES`), comparaison en minuscules après `strip()`
- Erreurs utilisateur (fichier manquant, colonne manquante) affichées en français sur stderr puis `sys.exit(1)`, plutôt que de laisser remonter une trace Python brute

## Patterns INTERDITS
- Ne pas ajouter de dépendances externes sans raison forte — rester sur la stdlib tant que ce n'est pas nécessaire
- Ne pas modifier ou supprimer `contacts.csv` sans confirmation explicite de l'utilisateur (voir `workflow.md` et le hook `.claude/hooks/protect-contacts-csv.sh`)
- [EN ATTENTE : pas d'autres interdictions explicites détectées dans le code]

## Tests
- Où ils vont : [EN ATTENTE : aucun test présent dans le dépôt à ce jour]
- Ce qu'on teste absolument : [EN ATTENTE]

## Commits
- Format : messages en français, à l'impératif, résumant l'action (ex. « Ajoute un hook protégeant contacts.csv contre modification/suppression directe », « Ajoute le comptage des téléphones non disponibles et le résumé par département »)
- Pas de préfixe de type conventional commits (`feat:`, `fix:`...) observé dans l'historique
