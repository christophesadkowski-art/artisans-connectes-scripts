# Décisions prises

> Une entrée par décision. L'important c'est le "pourquoi" et "ce qu'on a écarté".

## [2026-07-27] · Stocker les contacts dans un CSV versionné dans le dépôt
- **Décision :** `contacts.csv` (peintres en bâtiment d'Île-de-France) est commité directement dans le dépôt plutôt que stocké dans une base de données ou un service externe.
- **Pourquoi :** simplicité — le jeu de données est petit et statique pour l'instant, aucune infra externe n'est nécessaire pour l'exploiter. *(Hypothèse raisonnable, non confirmée par l'auteur : à corriger si la vraie raison diffère.)*
- **Écarté :** base de données, tableur externe (Google Sheets, Airtable...) — non utilisés actuellement.
- **Statut :** en vigueur ; à revoir si le volume de contacts ou le nombre de métiers/régions couverts grandit significativement.

## [2026-07-27] · Script CLI en stdlib Python pur, sans dépendances
- **Décision :** `count_unavailable_emails.py` n'utilise que `argparse`, `csv`, `sys`, `collections.Counter` — aucune bibliothèque tierce (pas de pandas, par ex.).
- **Pourquoi :** le script doit pouvoir tourner avec juste `python3`, sans étape d'installation (`pip install`) — cohérent avec un besoin simple (compter/regrouper des lignes) où une dépendance comme pandas serait disproportionnée. *(Hypothèse raisonnable, non confirmée par l'auteur.)*
- **Écarté :** pandas ou autres bibliothèques de traitement de données.
- **Statut :** en vigueur.

## [Date · à préciser] · Protéger `contacts.csv` par un hook Claude Code
- **Décision :** un hook `PreToolUse` (`.claude/hooks/protect-contacts-csv.sh`) intercepte les tentatives d'édition/écriture (`Edit|Write`) ou de commande Bash touchant `contacts.csv` et demande une confirmation explicite avant modification ou suppression.
- **Pourquoi :** `contacts.csv` contient des données réelles de contacts (prospection d'artisans) qu'on ne veut pas voir modifiées ou effacées accidentellement par un agent.
- **Écarté :** rendre le fichier en lecture seule au niveau du système de fichiers ; ne pas le protéger du tout.
- **Statut :** en vigueur.

## [Date · à préciser] · Portée du projet non figée
- **Décision :** en l'absence d'indication contraire de l'auteur, ce dépôt est traité comme un outil ponctuel — le script et le CSV actuels (peintres en bâtiment IDF), sans engagement à l'étendre à d'autres métiers, régions, ou à un usage de prospection/emailing.
- **Pourquoi :** rien dans le code, les commits ou les échanges ne confirme une ambition plus large ; éviter de sur-construire (abstractions, options génériques) tant que ce n'est pas demandé.
- **Écarté :** généraliser dès maintenant le script pour d'autres métiers/départements, ou construire une brique d'emailing/prospection, avant qu'un besoin réel ne se présente.
- **Statut :** hypothèse par défaut — à corriger dès que l'auteur précise la portée réelle voulue (ex. extension à d'autres métiers, ou usage en amont d'une campagne de contact).
