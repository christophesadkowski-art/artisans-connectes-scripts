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

## Aucun autre piège confirmé à ce jour
Aucun problème d'encodage, de doublon de contact ou d'incohérence de format téléphone n'a été rencontré ou confirmé jusqu'ici — inutile d'anticiper des correctifs pour des cas non observés. Points de vigilance à surveiller si le CSV grossit ou change de source, sans qu'il s'agisse de pièges déjà constatés :
- **Doublons de contacts** : rien dans le script ne détecte ou ne fusionne une même entreprise apparaissant plusieurs fois.
- **Formats de téléphone hétérogènes** : les numéros dans `contacts.csv` ne sont pas normalisés (espaces, `+33`, etc.) ; le script ne fait que comparer aux valeurs "non disponible", il n'interprète pas le format.
- **Encodage** : `contacts.csv` est lu en UTF-8 explicite (`open(..., encoding="utf-8")`) et contient des caractères accentués ; un fichier réenregistré en Latin-1/CP1252 (ex. depuis Excel) romprait cette lecture.

Mettre à jour cette section avec un cas réel (symptôme, cause, solution) dès qu'un de ces points — ou un autre — cause effectivement un problème.
