---
name: prospection-artisans
description: Use this skill whenever the user asks to find, search for, or build a list of French artisan/tradesperson contacts for a prospection database — e.g. "trouve-moi des plombiers dans le 77", "cherche des électriciens en Île-de-France", "complète la base avec des chauffagistes", "recherche des maçons/paysagistes/agents immobiliers/peintres par département". Also use it when asked to fill in missing contact fields (téléphone, email, SIRET) for existing rows, or to add new rows to the CSV contact files in this repo. Trigger on any of the 7 target trades (chauffagiste, maçon, électricien, agent immobilier, paysagiste, plombier, peintre en bâtiment) combined with a search/sourcing intent, especially when an Île-de-France department is mentioned (75, 77, 78, 91, 92, 93, 94, 95). Do not use this skill for CSV analysis/counting/deduplication tasks (see count_unavailable_emails.py / detect_duplicates.py) — this skill is specifically about sourcing new contact data.
---

# Prospection d'artisans français

## Méthode de recherche principale

Pour trouver des contacts d'artisans avec des coordonnées vérifiables, utilise
en priorité une requête de recherche de la forme :

```
[métier] "mentions légales" siret téléphone email
```

Exemple concret pour un plombier en Seine-et-Marne :

```
plombier 77 "mentions légales" siret téléphone email
```

Cette formulation cible les pages "mentions légales" des sites d'entreprises,
qui contiennent quasi systématiquement le SIRET, le téléphone et l'email de
contact officiels — des données bien plus fiables qu'un simple annuaire.

Adapter le département (ou la ville) et le métier selon la demande, en
gardant la structure `[métier] [zone] "mentions légales" siret téléphone email`.

## Mise en garde sur PagesJaunes

PagesJaunes (et annuaires similaires) ne doivent pas être la source
principale : les numéros affichés y sont souvent des numéros de
redirection/tracking (call tracking) et non les lignes directes de
l'entreprise, et les emails y sont rarement présents. Si PagesJaunes est
utilisé en complément, croiser systématiquement avec le site officiel de
l'entreprise (mentions légales) avant de valider une donnée.

## Codes département (Île-de-France)

Le champ `departement` du CSV attend le code à deux chiffres, pas le nom de
la zone. Codes utiles pour l'Île-de-France :

| Département      | Code |
|-------------------|------|
| Paris              | 75   |
| Seine-et-Marne     | 77   |
| Yvelines           | 78   |
| Essonne            | 91   |
| Hauts-de-Seine     | 92   |
| Seine-Saint-Denis  | 93   |
| Val-de-Marne       | 94   |
| Val-d'Oise         | 95   |

## Règle stricte : ne jamais inventer de données

Comme rappelé dans `CLAUDE.md`, il est strictement interdit d'inventer, de
deviner ou de générer une valeur plausible (téléphone, email, SIRET, etc.).
Si une information n'est pas trouvée après recherche, le champ correspondant
doit être renseigné avec `non disponible` — jamais laissé vide, jamais rempli
par une supposition.
