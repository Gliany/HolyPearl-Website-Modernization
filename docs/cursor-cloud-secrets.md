# Cursor Cloud Agent secrets for HolyPearl WordPress

This repository expects WordPress credentials to be injected at runtime. Real
secret values must never be committed to GitHub.

## Required runtime variables

| Variable | Purpose |
| --- | --- |
| `HP_WP_SITE` | WordPress site origin, for example `https://holypearl.co.il` |
| `HP_WP_USER` | WordPress username or email for an account allowed to edit pages |
| `HP_WP_APP_PASSWORD` | WordPress Application Password for that user |

`.env.example` contains placeholders only. `.env` and `.env.*` are ignored by
Git so local values are not accidentally committed.

## Root cause of the current failure

The current Cursor Cloud Agent runtime does not expose `HP_WP_SITE`,
`HP_WP_USER`, or `HP_WP_APP_PASSWORD`. The repository also had no committed
environment setup documentation or verification tooling. As a result, the agent
could open WordPress admin but could not authenticate or verify edit access.

## Configure secrets in Cursor

1. Open Cursor in the browser.
2. Go to the workspace or repository settings for this repository:
   `Gliany/HolyPearl-Website-Modernization`.
3. Open the Cloud Agent environment or secrets configuration.
4. Add these runtime secrets:
   - `HP_WP_SITE`
   - `HP_WP_USER`
   - `HP_WP_APP_PASSWORD`
5. Save the environment/secrets configuration.
6. Start a new Cloud Agent task after saving. Existing agents may not receive
   newly added secrets.

Use a WordPress Application Password, not your normal WordPress password. In
WordPress admin this is usually created from **Users -> Profile -> Application
Passwords**.

## Verify the setup

Run:

```bash
./scripts/verify-wp-access.sh
```

The verifier is read-only. It only performs authenticated `GET` requests:

- `GET /wp-json/wp/v2/users/me`
- `GET /wp-json/wp/v2/pages/3702?context=edit`
- `GET /wp-json/wp/v2/pages/52?context=edit`

It does not create, update, publish, or delete anything.

## Expected success output

```text
[ok] HP_WP_SITE is set
[ok] HP_WP_USER is set
[ok] HP_WP_APP_PASSWORD is set
[ok] authenticated as WordPress user <id>
[ok] page 3702 edit access confirmed (status: draft)
[ok] page 52 edit access confirmed (status: publish)
[ok] WordPress access verification completed without modifying content
```

The page 52 status may differ if the site changes, but the verifier should still
report edit access for both pages.

