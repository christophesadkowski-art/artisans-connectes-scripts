# Décisions prises

> Une entrée par décision. L'important c'est le "pourquoi" et "ce qu'on a écarté".

## [2026-07-27] · Stocker les contacts dans un CSV versionné dans le dépôt
- **Décision :** `contacts.csv` (peintres en bâtiment d'Île-de-France) est commité directement dans le dépôt plutôt que stocké dans une base de données ou un service externe.
- **Pourquoi :** [EN ATTENTE : raison non documentée dans le code/commits — probablement simplicité pour un jeu de données petit et statique]
- **Écarté :** base de données, tableur externe (Google Sheets, Airtable...) — non utilisés actuellement.
- **Statut :** en vigueur.

## [2026-07-27] · Script CLI en stdlib Python pur, sans dépendances
- **Décision :** `count_unavailable_emails.py` n'utilise que `argparse`, `csv`, `sys`, `collections.Counter` — aucune bibliothèque tierce (pas de pandas, par ex.).
- **Pourquoi :** [EN ATTENTE : raison non documentée — cohérent avec un script simple et sans dépendances à installer]
- **Écarté :** pandas ou autres bibliothèques de traitement de données.
- **Statut :** en vigueur.

## [Date · à préciser] · Protéger `contacts.csv` par un hook Claude Code
- **Décision :** un hook `PreToolUse` (`.claude/hooks/protect-contacts-csv.sh`) intercepte les tentatives d'édition/écriture (`Edit|Write`) ou de commande Bash touchant `contacts.csv` et demande une confirmation explicite avant modification ou suppression.
- **Pourquoi :** `contacts.csv` contient des données réelles de contacts (prospection d'artisans) qu'on ne veut pas voir modifiées ou effacées accidentellement par un agent.
- **Écarté :** rendre le fichier en lecture seule au niveau du système de fichiers ; ne pas le protéger du tout.
- **Statut :** en vigueur.

> [EN ATTENTE : d'autres décisions (choix du domaine "artisans-connectes", pourquoi le métier "Peinture en bâtiment" en premier, portée future du projet) vivent probablement dans la tête de l'auteur et doivent être ajoutées ici manuellement.]
