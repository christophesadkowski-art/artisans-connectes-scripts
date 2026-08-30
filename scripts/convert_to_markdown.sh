#!/usr/bin/env bash
# Convertit un fichier (PDF, Word, Excel, PowerPoint...) en Markdown via MarkItDown,
# pour éviter de payer le rendu image de chaque page lors d'un upload dans Claude.
#
# Usage : scripts/convert_to_markdown.sh contrat.pdf [sortie.md]

set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "Usage : $0 <fichier_source> [fichier_sortie.md]" >&2
  exit 1
fi

source_file="$1"
output_file="${2:-${source_file%.*}.md}"

if ! command -v markitdown >/dev/null 2>&1; then
  echo "markitdown n'est pas installé. Lance : pip install -r requirements.txt" >&2
  exit 1
fi

markitdown "$source_file" -o "$output_file"
echo "Converti : $source_file -> $output_file"
