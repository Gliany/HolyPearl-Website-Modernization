# HolyPearl Website Modernization

This repository is used as the working environment for HolyPearl WordPress
updates.

Before attempting WordPress changes from Cursor Cloud Agent, configure and
verify the required secrets:

1. Read `docs/cursor-cloud-secrets.md`.
2. Configure `HP_WP_USER` and `HP_WP_APP_PASSWORD` in Cursor Secrets or an
   equivalent secure runtime environment.
3. Start a new Cloud Agent task.
4. Run `./scripts/verify-wp-access.sh`.

Do not commit real WordPress credentials.

