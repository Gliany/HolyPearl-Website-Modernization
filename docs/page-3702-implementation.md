# Page 3702 — Intent Homepage Implementation

**Status:** Draft only · **Do not publish** · **Do not edit page 52 (live בית)**

## Files

| File | Purpose |
|------|---------|
| `HOLYPEARL_HOMEPAGE_ARCHITECTURE_BRIEF.md` | Section order, copy, constraints |
| `css/homepage-intent-draft-3702.css` | Scoped styles (`.holypearl-hp3702`) |
| `wordpress/page-3702-homepage-markup.html` | Paste into Beaver Builder HTML module |
| `drafts/html/holypearl-homepage-intent-draft-3702.html` | Local browser preview |

## WordPress admin steps

1. **Pages →** open draft page **3702** (not page 52).
2. Confirm status remains **Draft** — never click Publish until owner approval.
3. **Beaver Builder →** edit page 3702:
   - Remove or hide legacy category-first rows from old draft if present.
   - Add one **full-width row** with a single **HTML** module.
   - Paste entire contents of `wordpress/page-3702-homepage-markup.html`.
4. **Load CSS** (choose one):
   - **Astra → Customize → Additional CSS:** paste `css/homepage-intent-draft-3702.css` wrapped in a comment `/* HP3702 draft only */`, **or**
   - **Simple CSS** snippet active only on page 3702 (if your setup supports page-scoped rules), **or**
   - BB row **Advanced → CSS** is too small — prefer global Additional CSS with scope class `.holypearl-hp3702`.
5. **Astra page settings** for 3702: add body class `holypearl-hp3702` if the wrapper div is stripped by the theme (optional; markup already includes wrapper).
6. **Preview** via “Preview as visitor” — compare desktop and mobile RTL.
7. **QA links:** spot-check `/product-category/mizoza/`, `men/tpilin`, `shabat`, mezuzah check product, `/store/`.

## Remove before launch

- `.hp3702-draft-banner` row (amber “טיוטה לעמוד 3702” bar) — delete from HTML or hide via CSS when going live on 3702.

## Cutover (later, separate approval)

- Do **not** change Reading → Homepage until checklist in `HOLYPEARL_HOMEPAGE_ARCHITECTURE_BRIEF.md` is signed.
- Switching front page from 52 → 3702 is a distinct task after visual sign-off.

## Local preview

Open in browser:

`drafts/html/holypearl-homepage-intent-draft-3702.html`

Requires network for Google Fonts and holypearl.co.il CDN images.
