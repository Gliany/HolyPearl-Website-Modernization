#!/usr/bin/env bash
# Deploy HolyPearl HP3702 plugin via WordPress REST API (requires Application Password).
#
# Usage:
#   export HP_WP_USER='your-wp-username'
#   export HP_WP_APP_PASSWORD='xxxx xxxx xxxx xxxx xxxx xxxx'
#   ./scripts/deploy-hp3702-plugin.sh
#
# Does NOT publish page 3702. Activates plugin only.

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SITE="${HP_WP_SITE:-https://holypearl.co.il}"
ZIP="$ROOT/wordpress/dist/holypearl-hp3702-draft.zip"

if [[ -z "${HP_WP_USER:-}" || -z "${HP_WP_APP_PASSWORD:-}" ]]; then
  echo "Missing HP_WP_USER or HP_WP_APP_PASSWORD."
  echo "Create an Application Password in WP Admin → Users → Profile."
  exit 1
fi

if [[ ! -f "$ZIP" ]]; then
  "$ROOT/scripts/build-hp3702-plugin-zip.sh"
fi

AUTH="$(printf '%s:%s' "$HP_WP_USER" "$HP_WP_APP_PASSWORD" | base64 -w0 2>/dev/null || printf '%s:%s' "$HP_WP_USER" "$HP_WP_APP_PASSWORD" | base64)"

echo "Uploading plugin..."
UPLOAD_JSON="$(curl -sS -X POST \
  -H "Authorization: Basic $AUTH" \
  -H "Content-Disposition: attachment; filename=holypearl-hp3702-draft.zip" \
  -H "Content-Type: application/zip" \
  --data-binary @"$ZIP" \
  "$SITE/wp-json/wp/v2/plugins")"

PLUGIN_SLUG="$(echo "$UPLOAD_JSON" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('plugin','') or d.get('code',''))" 2>/dev/null || true)"

if [[ -z "$PLUGIN_SLUG" || "$PLUGIN_SLUG" == *"rest_"* ]]; then
  echo "Upload failed:"
  echo "$UPLOAD_JSON" | python3 -m json.tool 2>/dev/null || echo "$UPLOAD_JSON"
  exit 1
fi

echo "Activating $PLUGIN_SLUG ..."
curl -sS -X POST \
  -H "Authorization: Basic $AUTH" \
  -H "Content-Type: application/json" \
  -d "{\"status\":\"active\"}" \
  "$SITE/wp-json/wp/v2/plugins/$PLUGIN_SLUG" | python3 -m json.tool

echo ""
echo "Done. Preview draft page 3702 in WP admin (keep status Draft)."
echo "Live homepage page 52 is unchanged."
