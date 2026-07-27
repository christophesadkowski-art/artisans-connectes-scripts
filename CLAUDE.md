# CLAUDE.md

## Contexte du projet

Ce dépôt contient une base de prospection de contacts d'artisans français,
avec un focus géographique sur l'Île-de-France. Les métiers couverts incluent
notamment :

- Chauffagistes
- Maçons
- Électriciens
- Agents immobiliers
- Paysagistes
- Plombiers
- Peintres (peinture en bâtiment)

Les scripts du dépôt servent à analyser, nettoyer et compter les contacts
présents dans ces fichiers CSV (ex. `count_unavailable_emails.py`).

## Règle stricte : ne jamais inventer de données

Quand une information (téléphone, email, SIRET, etc.) est manquante ou
introuvable, elle doit **toujours** être marquée `non disponible`.

Il est strictement interdit d'inventer, de deviner ou de générer une valeur
plausible pour combler un champ vide. Une donnée absente doit rester absente
et explicitement signalée comme telle.

## Format des colonnes CSV

Chaque fichier CSV de contacts doit respecter ces colonnes, dans cet ordre :

| Colonne       | Description                                    |
|---------------|-------------------------------------------------|
| `nom`         | Nom de l'entreprise ou de l'artisan             |
| `metier`      | Métier exercé (ex. "Peinture en bâtiment")      |
| `telephone`   | Numéro de téléphone, ou `non disponible`        |
| `email`       | Adresse email, ou `non disponible`              |
| `departement` | Numéro de département (ex. "75", "77")          |
| `siret`       | Numéro SIRET, ou `non disponible`               |
