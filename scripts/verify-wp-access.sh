#!/usr/bin/env bash
set -euo pipefail

required_vars=(HP_WP_SITE HP_WP_USER HP_WP_APP_PASSWORD)

for var_name in "${required_vars[@]}"; do
  if [[ -z "${!var_name:-}" ]]; then
    echo "[error] $var_name is not set" >&2
    echo "Configure Cursor Secrets, then start a new Cloud Agent task." >&2
    exit 1
  fi
  echo "[ok] $var_name is set"
done

site="${HP_WP_SITE%/}"
tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

request_json() {
  local label="$1"
  local path="$2"
  local body_file="$tmp_dir/${label}.json"
  local status_file="$tmp_dir/${label}.status"

  curl --silent --show-error \
    --user "$HP_WP_USER:$HP_WP_APP_PASSWORD" \
    --header "Accept: application/json" \
    --output "$body_file" \
    --write-out "%{http_code}" \
    "$site$path" > "$status_file"

  local status
  status="$(<"$status_file")"

  if [[ "$status" != "200" ]]; then
    echo "[error] $label returned HTTP $status" >&2
    python3 - "$body_file" <<'PY' >&2
import json
import sys

path = sys.argv[1]
try:
    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
except Exception:
    print("Unable to parse WordPress response body.")
    raise SystemExit(0)

code = payload.get("code")
message = payload.get("message")
if code:
    print(f"WordPress code: {code}")
if message:
    print(f"WordPress message: {message}")
PY
    exit 1
  fi

  printf '%s\n' "$body_file"
}

user_body="$(request_json "users-me" "/wp-json/wp/v2/users/me?context=edit&_fields=id")"
user_id="$(python3 - "$user_body" <<'PY'
import json
import sys

with open(sys.argv[1], "r", encoding="utf-8") as handle:
    payload = json.load(handle)

user_id = payload.get("id")
if not isinstance(user_id, int):
    raise SystemExit("Authenticated user response did not include a numeric id.")
print(user_id)
PY
)"
echo "[ok] authenticated as WordPress user $user_id"

check_page_access() {
  local page_id="$1"
  local body_file
  body_file="$(request_json "page-$page_id" "/wp-json/wp/v2/pages/$page_id?context=edit&_fields=id,status")"

  local parsed
  parsed="$(python3 - "$body_file" "$page_id" <<'PY'
import json
import sys

path = sys.argv[1]
expected_id = int(sys.argv[2])

with open(path, "r", encoding="utf-8") as handle:
    payload = json.load(handle)

page_id = payload.get("id")
status = payload.get("status")

if page_id != expected_id:
    raise SystemExit(f"Expected page id {expected_id}, got {page_id!r}.")
if not isinstance(status, str) or not status:
    raise SystemExit(f"Page {expected_id} response did not include status.")

print(status)
PY
)"

  echo "[ok] page $page_id edit access confirmed (status: $parsed)"
}

check_page_access 3702
check_page_access 52

echo "[ok] WordPress access verification completed without modifying content"

