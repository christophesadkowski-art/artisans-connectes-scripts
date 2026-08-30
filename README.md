# artisans-connectes-scripts

Scripts d'analyse et d'outillage pour les contacts d'artisans (CSV, emails, téléphones, répartition par département).

## MarkItDown — arrête de payer ton PDF deux fois

### Le problème

Quand un PDF est uploadé dans Claude, chaque page est transformée en image en plus du texte extrait, et les deux sont facturés : 1 500 à 3 000 tokens par page pour le texte, plus l'image de chaque page en plus. Un contrat de 20 pages peut brûler 60 000 tokens avant même de poser une question.

### La solution : MarkItDown

[MarkItDown](https://github.com/microsoft/markitdown) est l'outil gratuit et open source de Microsoft qui convertit PDF, Word, Excel, PowerPoint (et plus) en Markdown propre, en conservant titres et tableaux. Une fois le document en Markdown, il n'y a plus d'image de page : Claude ne lit que du texte et ne facture que les mots.

### Installation

```bash
pip install -r requirements.txt
```

Cela installe `markitdown[all]` (conversion en ligne de commande) et `markitdown-mcp` (serveur MCP).

### Convertir un fichier

```bash
markitdown contrat.pdf -o contrat.md
```

Ou via le script fourni dans ce dépôt :

```bash
scripts/convert_to_markdown.sh contrat.pdf
```

Dépose ensuite le fichier `.md` dans Claude au lieu du PDF original.

### Configuration MCP (une fois pour toutes)

Avec le serveur MCP officiel, Claude Desktop convertit automatiquement chaque fichier déposé.

1. Installe le serveur : `pip install markitdown-mcp` (déjà inclus dans `requirements.txt`)
2. Ouvre la config Claude Desktop (Paramètres → Développeur → Modifier la config) et ajoute :

   ```json
   {
     "mcpServers": {
       "markitdown": {
         "command": "markitdown-mcp"
       }
     }
   }
   ```

3. Redémarre Claude Desktop.

### Récapitulatif

| Étape | Ce qui se passe |
|---|---|
| Tu as un document | PDF, Word ou Excel que tu uploaderais normalement |
| MarkItDown le convertit | Une commande, du Markdown propre en sortie |
| Claude reçoit du texte pur | Pas d'images, pas de double facturation |
| Tu paies une fraction | Mêmes réponses, beaucoup moins de tokens |
