# HolyPearl minimum-stack mission — 2026-09-04

> Historical initial audit. The approved [Content and catalog migration plan](../../strategy/CONTENT-CATALOG-MIGRATION.md) supersedes conflicting direction and migration steps below. All products must remain as catalog entries; WooCommerce is removed only after complete migration. Counts and no-deployment statements below describe the initial snapshot, before subsequent authorized plugin cleanup. See issue #10 for execution history.

Status: **In progress**. Inventory and proposed architecture completed; migration, restore rehearsal, and production deployment **Not tested / not performed**.
Tracks [issue #10](https://github.com/Gliany/HolyPearl-Website-Modernization/issues/10).
Related: [#14 content migration](https://github.com/Gliany/HolyPearl-Website-Modernization/issues/14), [#8 / PR #18 performance ownership](https://github.com/Gliany/HolyPearl-Website-Modernization/pull/18), #13 images, #15–#16 hosting.

## Decision and scope

The approved target is a Hebrew content-led blog/authority site: articles, topic navigation, search, informational pages, and contact/consultation. Commerce is a migration dependency.
This document is the current minimum-stack work plan. Older catalog/keep-WooCommerce options in local planning documents are superseded for this mission.
No live WordPress changes, database cleanup, plan downgrade, or hosting migration were performed.

## Verified baseline

| Area | Current evidence |
|---|---|
| Production plugins | 49 installed; 44 active; 5 inactive; API reports no available updates |
| Staging plugins | 49 installed; 42 active; 7 inactive; API reports 3 available updates |
| Theme | Astra returned by theme.active on both sites; theme version not returned |
| Homepage | Production page 3702 is published and configured as page_on_front; native HTML block |
| Editorial | 10 published pages and 1 published article; 18 pages and 2 posts across queried non-trash statuses |
| Blog archive | page_for_posts=0; no dedicated posts page configured |
| Permalinks | /%year%/%monthnum%/%day%/%postname%/; preserve during this migration |
| Commerce surface | Public sitemaps list 161 product, 42 product-category, 63 product-tag URLs |
| Runtime concern | Elementor 4.2.0-dev2 and Elementor Beta 1.1.4 active on both sites |
| Production backup | API: active; last successful 2026-09-04 10:20:55, latest attempt finished, last_attempt_failed=false |
| Staging backup | API: active; last successful 2026-09-03 12:06:01, latest attempt finished, last_attempt_failed=false |
| Recovery verification | Independent export and actual restore rehearsal not verified |

Backup timestamps above are exactly as returned by the API; no timezone was supplied.
The site-list overview reported only 1/0 active plugins and implausible storage values; those fields are excluded from capacity planning. Counts use the dedicated plugin.list endpoint.
Sitemap membership does not establish Google indexation, complete product inventory, product relevance, or working destinations.

### Staging drift and prior completed work

Jetpack Boost and Smush are already inactive on staging, while active on production. This matches [PR #18 staging execution](https://github.com/Gliany/HolyPearl-Website-Modernization/pull/18#issuecomment-5473953741), dated 2026-08-31.
Do not repeat those removals or claim them as new work.
MonsterInsights is 11.1.3 on staging vs 11.2.0 production; Events Calendar 6.17.3.1 vs 6.17.4; UserFeedback 1.11.3 vs 1.11.4.
Record these differences when comparing tests; do not blindly synchronize databases.
The earlier PR records successful smoke checks but no comparable pre/post performance improvement.
Its module findings remain historical until the admin settings are rechecked.

## Proposed minimum architecture

These are technical recommendations; no new plugin is authorized or installed by this document.
Role owners below define responsibility, not assignments to a named person.

| Capability | Proposed owner | Rationale / exit gate |
|---|---|---|
| Theme and site layout | Existing Astra; site maintainer | Preserve current styling and avoid a simultaneous theme migration |
| Editing and new layouts | Built-in WordPress block editor; content editor | Use core blocks for new articles/pages; keep existing working HTML blocks initially |
| Legacy builders | Beaver Builder and Elementor temporarily; maintainer | Convert each dependent page, saved template and module before removing |
| SEO metadata and sitemap | AIOSEO; SEO maintainer | Preserve existing settings and metadata rather than migrate SEO providers |
| Redirects | One verified redirect mechanism; SEO maintainer | Existing capability/license unknown; select only after checking AIOSEO/platform support |
| Platform connection, CDN, images | WordPress.com / required Jetpack modules; maintainer | Preserve managed services and recheck scope before #15/#16 |
| CSS/JS optimization | Autoptimize during transition; maintainer | Existing owner in PR18; retain until measured evidence supports removing it |
| Backup | WordPress.com recovery plus verified independent export; maintainer | Keep UpdraftPlus while independent full backup/restore is unresolved |
| Security | Platform protections plus required existing controls; maintainer | Audit Sucuri/Jetpack modules before any reduction |
| Spam protection | Akismet; maintainer | Public comments currently enabled; verify configured service before relying on it |
| Accessibility | WP Accessibility plus semantic layouts/manual checks; maintainer | Retain controls through migration; plugin presence is not accessibility compliance |
| Analytics | One selected pageview/event collector; owner decision needed | Keep MonsterInsights temporarily; determine actual use of Jetpack Stats/GA/Meta |
| Contact | Existing verified phone/WhatsApp actions and map; content editor | Replace WP Call Button with native accessible link only after mobile test |
| Forms | Existing required form implementation, if any; maintainer | WPForms inactive; delivery and form owner unknown; no speculative new form plugin |
| Custom CSS | One version-controlled stylesheet; maintainer | Export and reconcile Simple CSS, Simple Custom CSS, theme CSS and inline styles |
| Custom PHP | Audited version-controlled site code where warranted; maintainer | Export active Code Snippets first; never assume inventory text is executable backup |
| Commerce | None in final architecture; content editor + SEO maintainer | Preserve content, records, and URLs under #14 before removing WooCommerce |

The plugin matrix classifies all 49 installed plugins: 6 Essential, 30 Temporary migration dependency, 11 Remove after replacement, 2 Remove now on staging candidates.
“Essential” means retain for this migration or a currently required capability; it is not a perpetual requirement.
“Remove now on staging” is a candidate queue, not permission to execute: all recovery, dependency and exact-change approval gates still apply.
No defensible final plugin count or financial saving is claimed before module, snippet, service and license verification.

## Page and template migration map

| Public route / content | Observed dependency | Target and exit test |
|---|---|---|
| / — page 3702 | wp:html | Preserve layout; validate links, scoped CSS, mobile RTL, accessibility and images |
| /contact/ — page 414 | wp:fl-builder/layout | Core blocks with preserved copy, phone action and map; verify #store-map anchor and inbound homepage link |
| Published article 3274 | wp:fl-builder/layout | Core article blocks; preserve existing dated URL, headings, media, SEO and internal links |
| /privacy-policy/ — 2499 | wp:html | Preserve rendering; separate copy review for content-led site |
| /termsconditions/ — 2495 | wp:html | Preserve rendering; separate copy review for content-led site |
| /accessibility-statement/ — 3365 | Plain HTML; historical snippet dependency unresolved | Preserve behavior; resolve visible contact placeholders and validate claims separately |
| /cart/, /checkout/, /account/ — 57/58/59 | fl-builder/layout + WooCommerce shortcodes | Retire only after historical-record/access decision and tested replacement/redirect policy |
| /store/ — 56 | Empty saved content; commerce rendering may be supplied by WooCommerce | Replace with approved topic landing route; determine exact URL in #14 |
| /wishlist/ — 771 | YITH shortcode | Retire after verifying user impact and replacement route |
| Product / category / tag URLs | WooCommerce data/templates and possible addon modules | Review all 266 sitemap entries; preserve useful content and assign relevant destinations |
| Draft/private content and saved templates | Not fully inspected | Inventory internally; do not publish raw private content in GitHub |
| Header/footer/widgets/menus | Not inspected | Audit theme options, builder templates, icons, cart links and contact actions |

No absence of builder markers in post_content proves absence of builder dependency: metadata, templates, widgets and CSS require inspection.
The old local claim that page 3702 must remain a draft is stale; current production settings and pages.get establish it is live. This task did not change that state.
The URL register deliberately leaves destinations blank rather than assigning every product to the homepage.

## Module and service ownership audit

| Area | Available evidence | Remaining verification |
|---|---|---|
| Autoptimize | Active on both sites; PR18 identifies sole active CSS/JS owner | Current JS/CSS options, exclusions, cache behavior |
| Jetpack Boost | Inactive staging; active production | PR18 says unused onboarding/modules; recheck before production rollout |
| Smush | Inactive staging; active production | PR18 reports optimized originals, no active lazy load/CDN/next-gen delivery; check upload behavior |
| WP-Optimize | Active both; PR18 says cache/minify/scheduled cleanup off | Current settings and any schedules; do not run cleanup |
| Jetpack/platform | Active both; successful backup status | Active module list, image delivery, analytics, scan, forms, subscriptions, email dependencies |
| Sucuri | Active both | Hardening, scan, firewall and incident ownership |
| MonsterInsights / Meta / Mailchimp | Plugins active | Actual credentials/connections, events, feeds, campaigns, consent and business requirement; redact secrets |
| OptinMonster / UserFeedback | Plugins active | Current connection, active campaigns/surveys and required data exports |
| Code Snippets | Plugin active; local June inventory lists four active snippets | Current code/status/scope and safe exports; historical titles are not current code evidence |
| Theme / CSS / builder modules | Astra active; page content inspected | Theme version, saved templates, responsive CSS, addon modules and missing-block risks |
| External services | Incomplete | Registrar/DNS/email, backup destinations, search tools, paid licenses, renewal cost and owner |

Browser inspection reached a WordPress.com sign-in screen. Authenticated admin UI is required for these settings and snippet exports; the connector's successful plugin listing does not supply them.
Do not invent new credentials or publish settings exports containing secrets.

## Staged execution sequence and rollback

1. **Recovery gate.** Export a full independent backup plus plugin options, snippet code, SEO/redirect settings and uploads. Preserve an isolated copy of the current staging content. Prove restore in a disposable environment, without overwriting the existing staging work or production. Verify restored records/content and editor access. Current API backup status alone does not pass this gate.
2. **Baseline gate.** Complete private/draft/template and module inventory, match relevant production/staging versions deliberately, capture desktop/mobile screenshots, navigation/contact/search/editor smoke results and public request metrics. Block all outbound staging marketing and real form/email sends through an approved test setup.
3. **First candidates.** After gates 1–2, propose deactivation of Elementor Beta and Starter Templates individually on staging. Preserve options and files. Validate editor, homepage, contact, article and template behavior after each. Rollback: reactivate the exact plugin/version and restore its settings if needed. Deactivating Elementor Beta does not downgrade Elementor 4.2.0-dev2; resolve the developer binary as a separate tested stable-version migration.
4. **Content migration.** Convert contact and article 3274 to core blocks on staging, preserving URLs/copy/media; then audit remaining templates/private drafts. Rollback each page to its captured content/metadata revision. Remove dependent Beaver addons before core only after zero needed modules remain. Apply the same dependency gate to Elementor, CoBlocks, Layout Grid, Gutenberg plugin and Classic Editor.
5. **Commerce migration #14.** Inventory the full product database in addition to sitemap URLs; preserve restricted historical records outside GitHub. Convert useful content, map and test redirects, update menus/internal links/schema. Disable commerce extensions individually, then WooCommerce last. Rollback: restore per-page data, redirect configuration and exact plugin set in staging. Never push a cloned staging database over production.
6. **CSS/icons/contact consolidation.** Reconcile styles before disabling duplicate CSS plugins, Font Awesome or WP Call Button. Verify keyboard focus, phone/WhatsApp actions, responsive layouts and map anchor. Rollback with saved stylesheet/options and reactivation.
7. **Marketing, AMP and ops cleanup.** Remove only unused campaigns/collectors; preserve one event owner. Retire AMP URLs with verified canonicals/redirects. Preserve backup/security coverage. No database-table deletion or automated cleanup.
8. **Inactive file cleanup.** The five already-inactive production plugins and any newly inactive components can be removed only after export, uninstall-effect review and concrete deletion approval. Inactive status is not evidence that their stored data is disposable.
9. **Acceptance and rollout.** Attach before/after evidence, exact versions/settings changed, restore path and per-route checks to #10. Obtain explicit owner approval for production. Deploy selective changes; monitor errors/redirects and maintain rollback artifacts. Reopen #15/#16 cost comparison only with the final requirements.

### Required acceptance checks

- Homepage, category, article, contact, search, menus and editor save/preview work.
- Hebrew/RTL at mobile/tablet/desktop, keyboard focus, skip link, headings, labels and contrast remain usable.
- Tel/WhatsApp/map links work; forms use approved test destinations and delivery is verified.
- No missing blocks, exposed shortcodes, PHP fatals or new browser errors.
- Every retired public URL has a reviewed relevant destination, expected HTTP status, no chain and correct canonical.
- SEO metadata, sitemap membership, structured data, robots behavior and analytics events match the target.
- Repeated comparable request/byte/TTFB/LCP/CLS measurements distinguish improvements from noise.
- Independent restore succeeds; no customer/order data or secrets enter GitHub.
- Staging remains isolated and current; no entire database synchronization to production.

## Cost, risk and editorial impact

| Option | Cost status | Impact |
|---|---|---|
| Retain existing stack | Current bills/licenses not checked | Least immediate change, continued maintenance and overlapping responsibilities |
| Astra + core blocks + selected services | No new license proposed; savings unverified | Fewer dependencies after migration; training and per-page conversion required |
| WordPress.com downgrade #15 | Not evaluated here | Can remove operational capabilities; decide only after recovery/staging needs are resolved |
| Hosting migration #16 | Not evaluated here | Adds migration and ongoing operations work; compare after stack requirements are fixed |

Do not reuse the June local dollar amounts as current billing evidence.
Major risks: developer-version Elementor compatibility, unexported PHP, hidden builder metadata, lost product content/SEO, missed marketing/forms/security dependencies and staging database overwrites.

## Remaining blockers and next action

**Next action:** authenticated read-only admin inspection of module settings, active snippets and backup/export controls.
Then prepare the independent restore rehearsal. Do not begin plugin deactivation while recovery is unproven.
The first two deactivation candidates are documented above so the later confirmation can name exact plugins, site and rollback.

Completed: connector inventory, published-page dependency inspection, public URL register, target architecture, classification and removal sequence.
Not tested: module parity, snippet export, independent backup restoration, page conversions, redirects, plugin removal and production deployment.
Issue #10 remains open.

## Evidence and sources

- plugin-inventory.csv: all 49 installed plugins with production/staging versions, classifications and gates.
- evidence.json: sanitized connector observations; no raw private content or credentials.
- commerce-url-register.csv: 266 public sitemap entries, with unassigned destinations.
- Live WordPress.com MCP reads on 2026-09-04: plugin.list, theme.active, settings.get, pages.list/get, posts.list/get and backup.rewind_status.
- [Public sitemap index](https://holypearl.co.il/sitemap.xml), fetched over HTTP on 2026-09-04.
- [WordPress block editor documentation](https://wordpress.org/documentation/article/wordpress-block-editor/) supports the built-in editor approach.
- [Elementor rollback documentation](https://elementor.com/help/rolling-back-to-a-previous-version-of-elementor/) is a reference for planning the separate stable-version rehearsal, not proof of site compatibility.
- PR18 observations are attributed historical evidence; local June audits informed the unresolved-dependency checklist only.
