# Glossaire et entités

## Termes du domaine
- **Artisan** → dans ce projet, un professionnel du bâtiment (ex. peintre en bâtiment) identifié comme prospect/contact, avec ses coordonnées et sa localisation.
- **Non disponible** → valeur conventionnelle utilisée dans `contacts.csv` (et reconnue par le script sous les formes `"non disponible"`, `"non-disponible"`, `"n/a"`, `"na"` ou chaîne vide) pour indiquer qu'une information (email, téléphone, SIRET) n'a pas pu être trouvée pour ce contact.
- **Département** → division administrative française identifiée par son code à 2 chiffres (ex. `75`, `92`, `77`) ; utilisée ici comme axe de regroupement géographique des contacts.
- **SIRET** → identifiant d'établissement français (14 chiffres) ; présent comme colonne dans `contacts.csv` mais non exploité par le script actuel.

## Entités principales
- **Contact (ligne de `contacts.csv`)** → représente une entreprise artisanale. Champs : `nom` (raison sociale), `metier` (ex. "Peinture en bâtiment"), `telephone`, `email`, `departement` (code à 2 chiffres), `siret`.

## Sigles et noms internes
- **IDF** → Île-de-France, la région couverte par le jeu de données actuel de `contacts.csv`.
- [EN ATTENTE : pas d'autres sigles ou noms de modules internes détectés dans le code à ce jour.]
