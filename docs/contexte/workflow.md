# Workflow

## Avant de toucher quoi que ce soit
1. Lire `decisions.md` et `erreurs-connues.md` pour ne pas rouvrir un débat déjà tranché ou retomber dans un piège connu.
2. Si le changement touche `contacts.csv` : s'attendre à une demande de confirmation explicite (hook `.claude/hooks/protect-contacts-csv.sh`), car ce fichier contient des données réelles de prospection.
3. [EN ATTENTE : pas de convention de branche documentée — vérifier avec l'auteur avant de créer une branche.]

## Pour faire un changement
1. [EN ATTENTE : aucune suite de tests n'existe — pas de "tests d'abord" possible tant qu'il n'y en a pas.]
2. Implémenter le changement dans `count_unavailable_emails.py` (ou tout nouveau script), en respectant les conventions (`conventions.md`) : stdlib uniquement, messages/erreurs en français, fonctions de logique séparées de `main()`.
3. Vérifier manuellement en exécutant le script sur `contacts.csv`, par ex. :
   `python3 count_unavailable_emails.py contacts.csv`
4. [EN ATTENTE : pas de linter/typecheck configuré dans le dépôt.]

## Avant de considérer quelque chose comme terminé
- [ ] Le script s'exécute sans erreur sur `contacts.csv` et produit une sortie cohérente.
- [ ] `contacts.csv` n'a pas été modifié ou supprimé sans confirmation explicite de l'utilisateur.
- [ ] Le message de commit est en français, à l'impératif, et décrit l'action (voir historique existant).
- [EN ATTENTE : pas de checklist de build/tests automatisée — à compléter si le projet se dote d'outils de test.]

## Deploy
[EN ATTENTE : ce dépôt ne contient ni pipeline de déploiement ni CI/CD. Les scripts s'exécutent localement en ligne de commande ; aucune publication/automatisation n'est documentée à ce jour.]
