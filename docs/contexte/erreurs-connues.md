# Erreurs connues (pièges)

> Les pièges qui t'ont déjà mordu. Chacun fait gagner une heure à Claude (et à toi).

## Tentative de modification ou suppression de `contacts.csv` bloquée
- **Se produit quand :** un outil `Edit`/`Write` cible `contacts.csv`, ou qu'une commande Bash contenant `contacts.csv` ressemble à un `rm`, `mv`, `shred`, `truncate`, `chmod`, un `sed -i`, une redirection (`>`/`>>`) ou un `cp ... contacts.csv` en écriture.
- **Cause réelle :** le hook `PreToolUse` `.claude/hooks/protect-contacts-csv.sh` (déclaré dans `.claude/settings.json`) intercepte volontairement ces actions et force une confirmation explicite de l'utilisateur.
- **Solution :** ce n'est pas un bug — c'est voulu. Demander confirmation à l'utilisateur avant de modifier/supprimer `contacts.csv`, ou travailler sur une copie si l'intention n'est pas de modifier le fichier réel.

## `ValueError` au lancement du script sur un CSV différent
- **Se produit quand :** on exécute `count_unavailable_emails.py` sur un CSV dont les colonnes ne s'appellent pas `email`, `telephone`, `departement`.
- **Cause réelle :** les noms de colonnes par défaut sont codés en dur dans `analyze_contacts` ; le script vérifie leur présence et lève une `ValueError` explicite sinon.
- **Solution :** passer `--email-column`, `--phone-column`, `--department-column` avec les vrais noms de colonnes du fichier.

## Choses qui semblent cassées mais sont volontaires
- Le hook `protect-contacts-csv.sh` fait échouer/bloquer (statut "ask") toute édition directe de `contacts.csv` par un agent : c'est une protection intentionnelle, pas un bug à contourner.
- Le script n'utilise aucune dépendance externe (pas de pandas) : c'est un choix assumé pour rester simple, pas un oubli.

> [EN ATTENTE : d'autres pièges (ex. encodage du CSV, formats de numéros de téléphone, doublons de contacts) n'ont pas encore été rencontrés/documentés — à compléter au fil de l'eau.]
