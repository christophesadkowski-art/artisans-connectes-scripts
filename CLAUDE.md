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

Le comptage par département doit toujours inclure une catégorie `Inconnu`
pour regrouper les lignes dont le département est vide, comme le fait déjà
le script `count_unavailable_emails.py`.

## Métiers cibles

Les 7 métiers ciblés par cette base de prospection sont :

1. Chauffagistes
2. Maçons
3. Électriciens
4. Agents immobiliers
5. Paysagistes
6. Plombiers
7. Peintres (peinture en bâtiment)

## Audits en lecture seule

Pour tout audit en lecture seule (ex. vérification de `contacts.csv`, des pages TinyPages), utiliser l'agent intégré **Explore** plutôt qu'un agent personnalisé.

Ce dépôt ne définit aucun agent personnalisé dans `.claude/agents/` à ce jour, et aucun type d'agent nommé `audit-conformite` (ou équivalent) n'existe parmi les agents intégrés disponibles. Explore est un agent en lecture seule fiable (outils Read/Grep/Glob/Bash lecture seule, pas d'Edit/Write) et convient donc par construction aux tâches d'audit qui ne doivent pas modifier les fichiers.
