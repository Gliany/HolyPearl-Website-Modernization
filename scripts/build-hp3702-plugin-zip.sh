#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PLUGIN_DIR="$ROOT/wordpress/plugin/holypearl-hp3702-draft"
OUT_DIR="$ROOT/wordpress/dist"
ZIP="$OUT_DIR/holypearl-hp3702-draft.zip"

mkdir -p "$OUT_DIR"
rm -f "$ZIP"
(cd "$PLUGIN_DIR/.." && zip -r "$ZIP" holypearl-hp3702-draft -x "*.DS_Store")
echo "Built: $ZIP"
