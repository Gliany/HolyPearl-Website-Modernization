# HolyPearl modernization master plan

Updated: 2026-09-04. System of record: [GitHub issue #10](https://github.com/Gliany/HolyPearl-Website-Modernization/issues/10).

## Approved direction

HolyPearl becomes a Hebrew content-led blog and Judaica authority site with articles, topic navigation, search and contact/consultation.
WooCommerce and commerce-only plugins are temporary migration dependencies. Preserve useful content, media, SEO and required historical records before removal.

## Current baseline

Production has 44 active plugins out of 49 installed; staging has 42 active.
Astra is the active theme. Page 3702 is the published production homepage.
Contact page 414 and published article 3274 still contain Beaver Builder blocks.
The public commerce sitemaps contain 266 URLs requiring review.
Backups report recent successful runs, but independent restoration has not been demonstrated.
These facts supersede the June snapshot. No production changes were made during the September 4 audit.

## Target stack

Retain Astra and prefer the built-in WordPress block editor for new content.
Keep AIOSEO, required platform/Jetpack services, spam/accessibility controls, current CSS/JS optimization and independent recovery until replacements are proven.
Convert legacy builder content page by page; consolidate CSS, icons, analytics and plugin responsibilities after dependency checks.
Select a single verified redirect mechanism before retiring commerce URLs.
Do not choose a final plugin count or hosting tier before the module and service inventory is complete.

## Delivery sequence

1. Complete authenticated module/snippet/template inventory and independent restore rehearsal.
2. Test the exact first plugin deactivations on staging with rollback.
3. Convert contact and article content to core blocks, preserving URLs and behavior.
4. Complete product-content preservation and redirect mapping under #14; remove commerce extensions before WooCommerce.
5. Consolidate styles, marketing and operational services; verify accessibility, SEO, editor, forms and performance.
6. Obtain explicit production approval and deploy selective tested changes.
7. Compare WordPress.com downgrade #15 and host migration #16 using verified requirements and current bills.

Detailed classifications, rollback gates, page map, evidence limitations and acceptance criteria:
[Minimum-stack migration plan](../audits/mission-10-2026-09-04/minimum-stack-plan.md).

## Status

Completed: inventory and proposed migration plan.
In progress: #10.
Awaiting authenticated admin access: active module settings, snippet code and export controls.
Not tested: independent restore, new plugin removals, content migration, redirects and production rollout.

Earlier staging work in [PR #18](https://github.com/Gliany/HolyPearl-Website-Modernization/pull/18) already disabled Jetpack Boost and Smush; it is preserved as prior work.
Production and staging differ; never overwrite production with the staging database.
No automatic deployment pipeline is established by this documentation PR.
