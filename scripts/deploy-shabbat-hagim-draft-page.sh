#!/usr/bin/env bash
# Create or update the Shabbat/Holidays intermediate page as Draft.
# Requires:
#   HP_WP_USER
#   HP_WP_APP_PASSWORD
# Optional:
#   HP_WP_SITE (default from project docs)

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SITE="${HP_WP_SITE:-[REDACTED]}"
SLUG="%d7%a9%d7%91%d7%aa%d7%95%d7%aa-%d7%95%d7%97%d7%92%d7%99%d7%9d-%d7%98%d7%99%d7%95%d7%98%d7%94"
TITLE="שבתות וחגים"
MARKUP_FILE="$ROOT/wordpress/page-shabbat-hagim-draft-markup.html"

if [[ -z "${HP_WP_USER:-}" || -z "${HP_WP_APP_PASSWORD:-}" ]]; then
  echo "Missing HP_WP_USER or HP_WP_APP_PASSWORD."
  exit 1
fi

if [[ ! -f "$MARKUP_FILE" ]]; then
  echo "Missing markup file: $MARKUP_FILE"
  exit 1
fi

AUTH="$(printf '%s:%s' "$HP_WP_USER" "$HP_WP_APP_PASSWORD" | base64 -w0 2>/dev/null || printf '%s:%s' "$HP_WP_USER" "$HP_WP_APP_PASSWORD" | base64)"
CONTENT_ESCAPED="$(MARKUP_FILE="$MARKUP_FILE" python3 - <<'PY'
import json
import os
from pathlib import Path
print(json.dumps(Path(os.environ["MARKUP_FILE"]).read_text(encoding="utf-8")))
PY
)"

echo "Searching for existing draft page by slug..."
PAGE_JSON="$(curl -sS -H "Authorization: Basic $AUTH" "$SITE/wp-json/wp/v2/pages?slug=$SLUG&context=edit")"
PAGE_ID="$(echo "$PAGE_JSON" | python3 - <<'PY'
import json,sys
data=json.load(sys.stdin)
if isinstance(data,list) and data:
    print(data[0].get("id",""))
PY
)"

if [[ -n "$PAGE_ID" ]]; then
  echo "Updating existing page id=$PAGE_ID as draft..."
  curl -sS -X POST \
    -H "Authorization: Basic $AUTH" \
    -H "Content-Type: application/json" \
    -d "{\"status\":\"draft\",\"title\":\"$TITLE\",\"content\":$CONTENT_ESCAPED}" \
    "$SITE/wp-json/wp/v2/pages/$PAGE_ID" | python3 -m json.tool
else
  echo "Creating new draft page..."
  curl -sS -X POST \
    -H "Authorization: Basic $AUTH" \
    -H "Content-Type: application/json" \
    -d "{\"status\":\"draft\",\"slug\":\"$SLUG\",\"title\":\"$TITLE\",\"content\":$CONTENT_ESCAPED}" \
    "$SITE/wp-json/wp/v2/pages" | python3 -m json.tool
fi

echo ""
echo "Done. Page remains draft (not published)."
