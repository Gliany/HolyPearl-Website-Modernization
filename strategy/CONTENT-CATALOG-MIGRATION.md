# HolyPearl: Content Website with a Product Catalog

Approved direction: 2026-09-04. Documentation recorded after leaving Plan Mode.
Tracking: [minimum stack #10](https://github.com/Gliany/HolyPearl-Website-Modernization/issues/10), [content migration #14](https://github.com/Gliany/HolyPearl-Website-Modernization/issues/14), [draft PR #19](https://github.com/Gliany/HolyPearl-Website-Modernization/pull/19).

Status: approved plan; catalog implementation and migration not yet performed. This document supersedes earlier wording that allowed retaining only selected useful products or replacing the catalog with topic pages.

## Goal and approved decisions

Build a Hebrew content-led blog and authority website with the minimum necessary plugins. Replace WooCommerce entirely with a lightweight informational catalog. Every product stays; online shopping goes. Retain Astra and native WordPress editing.

- Preserve product names, descriptions, images, galleries, categories, tags, attributes and SEO metadata. Preserve publication state: drafts/private products stay unpublished.
- Display sizes, materials, colors and variations as information without prices or inventory controls.
- Replace prices and purchase buttons with **צרו קשר לפרטים נוספים**.
- Use the existing WhatsApp number **052-813-3714** (wa.me/972528133714), with a URL-encoded Hebrew message containing the product name and canonical URL: "שלום, אשמח לפרטים נוספים על {product_name}: {product_url}". Retain a phone link.
- Keep /store/ as the catalog landing page; use **קטלוג מוצרים** in navigation.
- Remove carts, checkout, online payments, customer accounts, wishlists, sale badges and purchase messaging.
- Unavailable products may remain informational entries. Do not discard a product because it no longer supports a sale.

## Implementation and migration

1. Create one version-controlled HolyPearl catalog plugin for a separate product content type, categories/tags, galleries, informational attributes and contact actions. No new page builder or catalog framework.
2. Use native WordPress editing. Preserve existing product IDs, slugs, publication states, media references and taxonomy relationships during conversion.
3. Preserve /product/, /product-category/ and /product-tag/ URLs; article permalinks remain unchanged. Avoid competing rewrite registrations during the WooCommerce-to-catalog cutover.
4. Inventory the complete product database, including private/draft entries and variations. The earlier sitemap's 161 products, 42 categories and 63 tags are a baseline, not a complete database inventory.
5. Provide repeatable migration with a dry-run report and per-product original/converted records. Stop on missing content or URL conflicts. Preserve variation-specific text/images alongside attributes.
6. Preserve historical orders and customer records privately. Do not delete their tables or put exports, credentials or private content in GitHub.
7. Replace WooCommerce templates, widgets, shortcodes and menu dependencies. Disable commerce extensions before WooCommerce, after the replacement catalog is ready.
8. Redirect retired cart, checkout and wishlist pages to /store/ and the retired account page to /contact/. Remove obsolete internal links.
9. Preserve AIOSEO metadata and catalog sitemap coverage. Remove price/offer/availability markup and use informational page and breadcrumb structured data.
10. Hide prices in all public output, including structured data, public metadata/API responses, search and cached pages. Disable purchasing endpoints rather than only hiding buttons.

## Verification and rollout

- Work on staging first with a verified backup and recovery path. Validate recovery before changing product records.
- Reconcile every source product with its catalog entry: content, galleries, attributes, publication state, identifiers and taxonomy relationships.
- Check every known product/category/tag URL, canonicals, redirects and sitemap membership.
- Test Hebrew RTL, mobile/tablet/desktop layouts, keyboard access, search, category navigation, editor save/preview, galleries and WhatsApp links. Verify the link without sending a message.
- Confirm shopping controls and purchasing endpoints are unavailable and no prices remain in public output.
- Record implementation, exact plugin changes, before/after evidence, limitations and rollback steps under #10/#14 and the implementing PR.
- Deploy selective changes after production approval. Never overwrite production with the staging database; re-inventory production for content changes before migration.
- Delete commerce plugins only after the production catalog passes verification; retain private recovery artifacts. Continue legacy-builder and duplicate-plugin cleanup separately.

## Defaults and boundaries

Existing styling and editorial content are the baseline; a full redesign, hosting migration and data-table cleanup are outside this migration.
Success is a complete usable catalog and fewer dependencies, not an arbitrary plugin count.
The last verified cleanup state in this thread was 39 installed/active plugins and zero inactive on each site. This is historical execution evidence, not a fresh inventory performed by this documentation update.
WooCommerce remains required until every product is migrated and checked. Approval of this plan is not evidence that migration or production deployment has occurred.
