# CLAUDE.md

## Audits en lecture seule

Pour tout audit en lecture seule (ex. vérification de `contacts.csv`, des pages TinyPages), utiliser l'agent intégré **Explore** plutôt qu'un agent personnalisé.

Ce dépôt ne définit aucun agent personnalisé dans `.claude/agents/` à ce jour, et aucun type d'agent nommé `audit-conformite` (ou équivalent) n'existe parmi les agents intégrés disponibles. Explore est un agent en lecture seule fiable (outils Read/Grep/Glob/Bash lecture seule, pas d'Edit/Write) et convient donc par construction aux tâches d'audit qui ne doivent pas modifier les fichiers.
