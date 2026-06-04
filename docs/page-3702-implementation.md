# Page 3702 — Apply the intent homepage (2 minutes)

**Fastest path:** upload the plugin zip — no Beaver Builder paste, no separate CSS step.

## Option A — Upload plugin (recommended)

1. Download **`wordpress/dist/holypearl-hp3702-draft.zip`** from this repo (or build: `./scripts/build-hp3702-plugin-zip.sh`).
2. WordPress Admin → **Plugins → Add New → Upload Plugin** → choose the zip → **Install** → **Activate**.
3. **Pages →** open draft page **3702** → confirm status is still **Draft** (do not publish).
4. Click **Preview** on page 3702 — you should see the full intent homepage with amber draft banner.
5. **Page 52 (live בית) is unchanged** — the plugin only runs on page ID `3702`.

To remove later: deactivate plugin **HolyPearl Homepage Draft 3702**.

## Option B — Automated deploy (if you add credentials)

In Cursor / CI, set secrets:

- `HP_WP_USER` — WordPress username  
- `HP_WP_APP_PASSWORD` — Application Password (Users → Profile → Application Passwords)

Then run:

```bash
./scripts/build-hp3702-plugin-zip.sh
./scripts/deploy-hp3702-plugin.sh
```

Optional: `HP_WP_SITE=https://holypearl.co.il` (default).

## Option C — Manual Beaver Builder paste

1. Paste `wordpress/page-3702-homepage-markup.html` into a BB HTML module on page 3702.
2. Add `css/homepage-intent-draft-3702.css` to Astra → Additional CSS (scoped with `.holypearl-hp3702`).

## Files reference

| File | Purpose |
|------|---------|
| `HOLYPEARL_HOMEPAGE_ARCHITECTURE_BRIEF.md` | Architecture |
| `wordpress/plugin/holypearl-hp3702-draft/` | Plugin source |
| `wordpress/dist/holypearl-hp3702-draft.zip` | Ready to upload |
| `drafts/html/holypearl-homepage-intent-draft-3702.html` | Offline preview |

## QA checklist

- [ ] Preview page 3702 on desktop — RTL, journey pills, CTAs  
- [ ] Preview on mobile — hero shortcuts 2×3, no overlap  
- [ ] Spot-check links: mizoza, tpilin, shabat, mezuzah check product  
- [ ] Live homepage `/` still shows page 52 content  
- [ ] Page 3702 remains **Draft**

## Before launch

Remove the amber `.hp3702-draft-banner` from `assets/homepage-content.html` (or deactivate plugin and switch to approved BB layout).
