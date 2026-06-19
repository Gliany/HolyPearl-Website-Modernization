# Draft category page: שבתות וחגים

This draft work adds an intermediate informational page for Shabbat/Holiday products before WhatsApp.

## Files

- `wordpress/page-shabbat-hagim-draft-markup.html` — markup to paste into the draft WordPress page
- `drafts/html/holypearl-shabbat-hagim-category-draft.html` — offline preview
- Homepage draft links updated in:
  - `wordpress/page-3702-homepage-markup.html`
  - `wordpress/plugin/holypearl-hp3702-draft/assets/homepage-content.html`
  - `drafts/html/holypearl-homepage-intent-draft-3702.html`

## Draft WP setup (do not publish)

1. Create a new **Draft** page in WordPress.
2. Set slug to: `שבתות-וחגים-טיוטה`
3. Paste content from `wordpress/page-shabbat-hagim-draft-markup.html`.
4. Keep status as **Draft**.
5. Preview page 3702 and verify the Shabbat card/button opens this draft page.

## Optional API deploy (still draft-only)

If project secrets are configured (`HP_WP_USER`, `HP_WP_APP_PASSWORD`), run:

```bash
./scripts/deploy-shabbat-hagim-draft-page.sh
```

The script creates/updates this page as **draft** only.

Homepage Shabbat links now point to:

`/%d7%a9%d7%91%d7%aa%d7%95%d7%aa-%d7%95%d7%97%d7%92%d7%99%d7%9d-%d7%98%d7%99%d7%95%d7%98%d7%94/`
