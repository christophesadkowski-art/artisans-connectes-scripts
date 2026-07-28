#!/usr/bin/env bash
# PreToolUse guard: require explicit user confirmation before contacts.csv
# is modified or deleted. Other files are untouched by this script.
set -euo pipefail

input="$(cat)"
tool_name="$(printf '%s' "$input" | jq -r '.tool_name // empty')"

ask() {
  printf '%s\n' "{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"permissionDecision\":\"ask\",\"permissionDecisionReason\":\"$1\"}}"
}

is_contacts_csv() {
  [[ "$(basename -- "$1")" == "contacts.csv" ]]
}

case "$tool_name" in
  Edit|Write)
    file_path="$(printf '%s' "$input" | jq -r '.tool_input.file_path // empty')"
    if [[ -n "$file_path" ]] && is_contacts_csv "$file_path"; then
      ask "contacts.csv modification requires your explicit confirmation."
      exit 0
    fi
    ;;
  Bash)
    command="$(printf '%s' "$input" | jq -r '.tool_input.command // empty')"
    if printf '%s' "$command" | grep -q 'contacts\.csv'; then
      if printf '%s' "$command" | grep -Eq '\brm\b|\bmv\b|\bshred\b|\btruncate\b|\bchmod\b|\bsed\b[^|;&]*-i|>>?[^|;&]*contacts\.csv|\bcp\b[^|;&]*contacts\.csv[[:space:]]*$'; then
        ask "This command may modify or delete contacts.csv and requires your explicit confirmation."
        exit 0
      fi
    fi
    ;;
esac

exit 0
