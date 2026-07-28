# Notes

- Les hooks personnalisés (`.claude/settings.json`) ne se sont pas montrés fiables dans cet environnement Cloud lors d'un test réel : le hook de protection de `contacts.csv` (`.claude/hooks/protect-contacts-csv.sh`, censé exiger une confirmation explicite avant modification) n'a pas bloqué une édition directe du fichier. Ne pas s'y fier comme garde-fou principal — continuer à relire les diffs manuellement avant validation.
