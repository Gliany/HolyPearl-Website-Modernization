# Performance Ownership Baseline

**Issue:** #8  
**Status:** In progress — production audited, staging clone requested  
**Captured:** 2026-08-31 (Asia/Jerusalem)  
**Production:** https://holypearl.co.il/

## Safety boundary

Production settings were inspected read-only. No production plugin, cache, content, database, or DNS setting was changed.

A private WordPress.com staging clone was requested from the Hosting Dashboard. Do not push the staging database to production: the production dashboard reports 41 WooCommerce orders, and a staging database push can overwrite orders created after the clone.

## Current production module audit

| Layer | Current state | Finding |
|---|---|---|
| WordPress.com hosting | Business plan | Platform caching and staging are available. |
| WordPress.com object cache | Platform-managed | WordPress.com documents Memcached object caching as automatically enabled and not disableable. |
| WordPress.com edge/page cache | Platform-managed | Must remain the only page-cache owner. A sampled response included `X-ac: 32.hhn _atomic_ams MISS`. |
| WordPress.com Site Accelerator | Active in rendered HTML | Homepage contained 23 `i*.wp.com` image-CDN references. |
| Autoptimize | Active | JS optimization, non-aggregated defer, inline-JS defer, CSS optimization, and HTML optimization are enabled. CSS/JS aggregation and critical-CSS generation are disabled. |
| WP-Optimize page cache | Disabled | `enable_page_caching` is off. |
| WP-Optimize minify | Disabled | Master minify switch is off. Stored JS/CSS sub-options are inert while the master is off. No `wpo-minify` asset references were found. |
| WP-Optimize database schedule | Disabled | Scheduled cleanup is off. Manual database cleanup remains available. |
| WP-Optimize image features | Inactive | WebP conversion and lazy loading are off. |
| Jetpack Boost | Plugin active, service not configured | The plugin is still on its onboarding screen. No Boost optimization module is active. |
| Smush | Plugin active | 435 images report as optimized; no images remain to optimize. Lazy Load is off; CDN/next-generation formats are not active. |
| Elementor Image Optimization | Inactive plugin | No ownership conflict while inactive. |
| Simple Cache | Inactive plugin | No ownership conflict while inactive. |

Rendered homepage evidence:

- 6 Autoptimize cache asset references
- 0 WP-Optimize minify asset references
- 23 WordPress.com image-CDN references
- 58 observed page assets: 24 scripts, 15 stylesheets, 12 images, 5 fonts, and 2 other
- No browser console errors observed in the sampled load

## Final ownership matrix

| Function | Single owner | Active policy |
|---|---|---|
| Edge/page caching | WordPress.com hosting | Keep plugin page caches disabled. |
| Object cache | WordPress.com Memcached | Platform-managed; no cache plugin or object-cache drop-in. |
| CSS optimization / critical CSS | Autoptimize | CSS minification only. Aggregation and critical-CSS generation remain disabled until separately tested. |
| JavaScript defer/delay | Autoptimize | Defer without aggregation. Jetpack Boost and WP-Optimize JS optimization remain disabled. |
| Image resizing / format delivery | WordPress.com Site Accelerator | Retire duplicate Smush runtime ownership after staging verification. Existing compressed files remain unchanged. |
| Database cleanup | WP-Optimize | Manual use only, with a verified backup. Scheduled cleanup, page cache, and minify remain disabled. |

Jetpack Boost has no assigned function and should be deactivated. Smush has completed historical compression but has no remaining runtime ownership and should be deactivated. Neither plugin should be deleted until production verification is complete.

## Production baseline

WordPress.com mobile performance test:

| Metric | Baseline |
|---|---:|
| Performance score | 65 / 100 |
| First Contentful Paint | 3.47 s |
| Largest Contentful Paint | 5.70 s |
| Cumulative Layout Shift | 0.06 |
| Time to First Byte | 0.17 s |
| Total Blocking Time | 0.04 s |
| Total network payload | 4,708 KiB |

Top opportunities reported:

- Improve image delivery: estimated 3,655 KiB
- Render-blocking requests: estimated 2,600 ms
- Reduce unused JavaScript: estimated 164 KiB
- Reduce unused CSS: estimated 162 KiB
- Improve font display: estimated 240 ms

The WordPress.com test and direct curl samples differ because they use different clients, locations, and cache states. Compare staging before/after using the same method and URL.

## Staging-only change set

Apply in this order:

1. Confirm the staging URL is private and has `WP_ENVIRONMENT_TYPE=staging`.
2. Record the active plugin and settings baseline.
3. Deactivate Jetpack Boost only; do not enroll in the Boost service.
4. Smoke-test all target routes and record console/PHP errors.
5. Deactivate Smush only; do not delete it or its data.
6. Repeat smoke tests and performance measurements.
7. Leave Autoptimize configuration unchanged.
8. Leave WP-Optimize active for manual database cleanup only; keep page cache, minify, scheduled cleanup, WebP, and lazy loading off.
9. Do not sync the staging database to production.

## Smoke-test routes

- Homepage: `/`
- Category: `/product-category/talit/bityosef/`
- Product: `/product/סטנדר-שולחן-עץ/`
- Contact: `/contact/`
- Checkout: `/checkout/`

The production checkout route currently redirects twice to the homepage. This is existing behavior, not a passing checkout workflow.

## Deployment and cache procedure

Cache clearing is a deployment step, not a correctness requirement:

1. Make the equivalent production plugin deactivations manually during an approved window.
2. Verify the five smoke-test routes before clearing caches.
3. Purge the WordPress.com global edge cache once.
4. Clear Autoptimize generated assets only if its configuration changed.
5. Do not repeatedly flush the object cache or use cache clearing to hide a broken configuration.
6. Repeat the same measurements after caches warm.

## Rollback

| Change | Rollback |
|---|---|
| Jetpack Boost deactivation | Reactivate the plugin. Its settings are retained because the plugin is not deleted. |
| Smush deactivation | Reactivate the plugin. Existing compressed media files are not reversed by deactivation. |
| Any Autoptimize regression | Restore the recorded settings; disable only the failing CSS or JS option; never enable a second optimizer as an emergency workaround. |
| WordPress.com cache anomaly | Keep plugin caches off, purge the relevant platform cache once, and contact WordPress.com support if the platform layer remains unhealthy. |
| Production failure | Reactivate the last changed plugin, verify routes, then use the fresh WordPress.com backup if configuration rollback is insufficient. |

## Remaining acceptance evidence

The issue is not ready to close until staging is available and the following are attached:

- Before/after staging metrics using the same environment and method
- Exact request count and transferred bytes
- Homepage, category, product, contact, and checkout smoke-test results
- Browser console and WordPress.com PHP error-log results
- Confirmation that Jetpack Boost and Smush are inactive on staging
- Explicit approval before equivalent production changes

## Authoritative platform guidance

- WordPress.com cache behavior: https://wordpress.com/support/clear-your-sites-cache/
- WordPress.com performance guidance: https://wordpress.com/support/check-your-sites-performance/
- WordPress.com staging behavior and WooCommerce warning: https://wordpress.com/support/how-to-create-a-staging-site/
