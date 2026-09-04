# HolyPearl modernization master plan

Updated: 2026-09-04. Tracking: [#10 minimum stack](https://github.com/Gliany/HolyPearl-Website-Modernization/issues/10), [#14 content migration](https://github.com/Gliany/HolyPearl-Website-Modernization/issues/14), [draft PR #19](https://github.com/Gliany/HolyPearl-Website-Modernization/pull/19).

## Approved direction

A Hebrew content-led blog and authority website with an informational product catalog. **Every product remains on the site.** Replace WooCommerce entirely after migration, without losing product content, media, URLs, categories, attributes or SEO metadata.

Prices and purchase buttons become **צרו קשר לפרטים נוספים**, linking to the existing WhatsApp contact with product context. No online shopping in the final architecture.

The authoritative implementation and acceptance plan is [Content and catalog migration](CONTENT-CATALOG-MIGRATION.md). It supersedes earlier selective product-retention wording.

## Architecture and delivery

- Retain Astra and native WordPress editing. Build one lightweight site catalog plugin.
- Inventory all products and dependencies, prove recovery, migrate and verify on staging.
- Preserve product/category/tag URLs; retain /store/ as **קטלוג מוצרים**.
- Keep WooCommerce until every product has a verified catalog replacement. Remove commerce extensions before WooCommerce.
- Deploy selective changes only after production approval; never synchronize a staging database over production.
- Then replace legacy builder dependencies and consolidate styling, analytics, performance and operational services. Retain required platform, security and recovery capabilities.
- Reconsider hosting/cost changes only after final requirements are verified.

## Execution status

Completed earlier in this thread: authorized plugin cleanup. Last verified state: 39 installed/active, zero inactive plugins on each site. See [inventory](../audits/mission-10-2026-09-04/plugin-inventory.csv) and issue #10 execution comments. This documentation update did not re-query live state.

Catalog migration, independent restore rehearsal, builder conversions and new catalog production rollout remain unperformed/unverified. This PR documents the plan; it does not establish an automatic deployment pipeline.

The [initial minimum-stack audit](../audits/mission-10-2026-09-04/minimum-stack-plan.md) is historical baseline material. Its initial plugin counts and no-deployment statements do not describe subsequent authorized cleanup.
