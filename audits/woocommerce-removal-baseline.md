# WooCommerce Removal Baseline

**Issue:** #14  
**Status:** In progress  
**Inventory captured:** 2026-08-30T22:28:22.0881979+03:00  
**Scope:** Public, read-only inventory of https://holypearl.co.il

## Confirmed target

HolyPearl is becoming a content-led blog and authority website. WooCommerce, cart, checkout, and commerce-only extensions are not part of the target architecture.

This baseline does **not** authorize plugin removal, database cleanup, URL deletion, or production changes. It establishes what must be preserved and classified first.

## Current public WooCommerce surface

| Surface | Count | Source |
|---|---:|---|
| Published products | 161 | WordPress REST product endpoint and product sitemap |
| Product-category archives | 42 | `product_cat-sitemap.xml` |
| Product-tag archives | 63 | `product_tag-sitemap.xml` |
| Total public product/taxonomy URLs | 266 | Public sitemap inventory |
| Public featured-media references | 161 | WordPress REST product records |

Additional legacy routes observed:

- `/shop/` redirects to `/store/`.
- `/cart/` redirects to the homepage.
- `/checkout/` redirects to the homepage.
- The homepage still requests WooCommerce cart fragments and initializes other commerce assets.

## Product-content quality

| Finding | Count | Share |
|---|---:|---:|
| Empty main product description | 149 | 92.5% |
| Empty product excerpt | 21 | 13.0% |
| Missing featured-media reference | 0 | 0.0% |
| Last modified in 2020 | 143 | 88.8% |
| Last modified after 2020 | 18 | 11.2% |

Modification-year distribution:

- 2020: 143
- 2022: 7
- 2023: 10
- 2024: 1

The inventory contains 9 duplicated title groups. Highest-frequency duplicates:

- כיפה סרוגה תכלת עם פס — 3 records
- כיפה סרוגה כחולה עם פס — 3 records
- כיפה סרוגה אמריקאית — 3 records
- טלית צמר רחלים א.א — 2 records
- כיפה סרוגה שחורה עם פס — 2 records
- מעמד לברכונים — 2 records
- כיסוי לפלטת שבת — 2 records
- סט חמישה מחזורים  – רינת ישראל עור ממוחזר — 2 records
- כיסוי תפילין וטלית דמוי עור — 2 records

## Migration conclusion

Do not convert all 161 products into blog posts automatically. Most records are thin catalogue entries, and automatic conversion would create low-value duplicate or near-empty articles.

Use four explicit dispositions:

1. **Convert to article/page** — current, useful, unique subject with enough expertise to support an evergreen resource.
2. **Merge into a topic guide** — several related thin products can become one substantive category or buying/educational guide.
3. **Redirect to an existing relevant resource** — only when intent is genuinely equivalent.
4. **Retire intentionally** — use 404/410 when no replacement exists; do not redirect unrelated URLs to the homepage.

## Required preservation before removal

The public CSV in this branch captures URLs and content signals, but it cannot see private or operational data. Before any plugin is disabled or removed, export and verify:

- Full database and uploads
- WooCommerce products, variations, attributes, taxonomies, reviews, and media
- Orders, refunds, customer records, notes, downloads, and tax/accounting records
- WooCommerce Action Scheduler and cron dependencies
- Code Snippets and custom CSS affecting product/cart behavior
- SEO titles, descriptions, canonicals, schema, redirects, and sitemap state
- Search Console landing-page performance, indexed URLs, backlinks, and conversions
- Email, analytics, Meta, Mailchimp, feeds, and form integrations
- Current menus, widgets, internal links, and homepage product references

Legal/accounting retention requirements for orders and customer records are **Unknown / requires confirmation**.

## Editorial classification fields

The companion CSV includes blank workflow fields for:

- `disposition`
- `target_url`
- `editorial_owner`
- `verification_status`
- `notes`

No URL should be removed until those fields are completed for the relevant record and reviewed.

## Safe execution sequence

1. Capture verified independent backup and restore evidence.
2. Export private WooCommerce operational data from an authenticated staging/admin environment.
3. Add Search Console/backlink evidence to the URL inventory.
4. Classify products and taxonomies editorially.
5. Create replacement posts/pages and one-to-one redirect map.
6. Clone production to staging.
7. Disable commerce extensions individually, then WooCommerce core.
8. Test publishing, search, forms, Hebrew/RTL, accessibility, SEO, analytics, redirects, and performance.
9. Remove obsolete code/assets only after staging verification.
10. Obtain explicit production approval.

## Current limitations

- Public-only evidence; drafts, private products, orders, customers, plugin settings, and database state were not inspected.
- The local planning folder is not a WordPress installation and has no WP-CLI target.
- Search Console, analytics, backlinks, and legal retention requirements were not available.
- No live settings, files, plugins, database records, DNS, or content were changed.

## Files

- `audits/woocommerce-public-url-inventory.csv` — public product, category, and tag URL working inventory.
