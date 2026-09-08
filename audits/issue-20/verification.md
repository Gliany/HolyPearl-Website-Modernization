# Issue 20 verification — updated 2026-09-08

## Delivered on staging
Page 3702 was delivered first to staging and then selectively deployed to https://holypearl.co.il/ with explicit user authorization. Production media URLs and settings were preserved.

- Wedding shortcut resolves to the wedding card; mezuzah-check shortcut resolves to the checking card. Each ID exists exactly once.
- Six customer-facing copy replacements remove internal commerce/architecture wording.
- Added one /store/ CTA: לכל המוצרים בקטלוג. Catalog keyboard activation reached /store/.
- Preserved ראו איך מגיעים לחנות at /contact/#store-map. The production contact-page map module now has exactly one `store-map` anchor; a cache-busted public browser check landed directly on the map with alt text מפת התמצאות והגעה לפנינת הקודש, חנות 57.
- Corrected the help-button WhatsApp prefill typo. No WhatsApp message sent or telephone call initiated.
- Added MonsterInsights categories: 12 hp_whatsapp_click, 4 hp_phone_click, 1 hp_directions_click, 1 hp_catalog_click. No new JavaScript event listener or plugin.

## Evidence
Editor returned Page updated. First save increased revisions from 34 to 35, revision link 3783; both saves were read back and matched the intended editor string exactly. Original editor markup was retained in the active browser session before editing; use WordPress revisions for persistent recovery.

Browser click tests reached #hp3702-wedding and #hp3702-mezuzah-check, and verified matching headings. Existing card layout/images preserved. A narrow viewport reported 319px (304px document client width), one grid column, RTL direction and no horizontal overflow. Screenshot inspected at wedding destination. Browser console returned no captured errors during this check.

Anonymous HTTP checks after the final production save returned 200. Both sites have 18 custom event attributes and the catalog CTA, with old architecture copy absent. Final production counts match staging: 12 hp_whatsapp_click, 4 hp_phone_click, 1 hp_directions_click and 1 hp_catalog_click. Each HTML response had one gtag loader reference; this is NOT proof of no duplicate events.

## Analytics
Staging MonsterInsights Lite 11.2.0 UI showed a configured GA4 profile. Enhanced link attribution enabled; anchor tracking disabled. Administrator and Editor excluded from tracking. Settings were inspected, not changed.

Use the plugin's [documented custom link attribution](https://www.monsterinsights.com/docs/custom-link-attribution/): category becomes GA4 event name and overrides built-in detection. Existing phone/outbound behavior is relabeled, not supplemented by another listener. Only selected contact/catalog CTAs receive attributes; ordinary anchor navigation is untagged.

GA4 receipt is NOT VERIFIED. Before production rollout, check these events using a non-excluded, consent-appropriate test session and GA4 Realtime/DebugView. Confirm one event per activation and distinguish clicks from real conversations, calls, directions usage or sales. Check GA4 enhanced-measurement overlap and confirm staging data is filtered/separated from production reporting. Do not disable role exclusions to test.

## Outstanding verification
- Desktop/tablet and exact 390px mobile widths: requested viewport overrides did not change reported width (remained 319px). No pass claimed for those breakpoints.
- Full anonymous visual/interactive behavior: HTTP verified; interactive browser used a signed-in session, including an administrator-only survey notice.
- End-to-end analytics receipt/consent/duplicate audit remains pending.
- Actual phone calling/WhatsApp sending intentionally not performed.

## Rollback and release
Use staging page 3702 revisions to restore the pre-September-5 content (August 31 last edit), or reverse the bounded manifest after confirming no intervening changes. The manifest records exact copy and anchor edits. Do not restore the whole site/database.

Production was selectively updated on September 8 and saved as WordPress revision 34. The hero CTA now matches staging: ראו איך מגיעים לחנות at `/contact/#store-map`, categorized as hp_directions_click. The production contact-page map module was then published with HTML ID `store-map`. Fresh anonymous HTTP returned 200 with exactly one matching ID, and a cache-busted browser check at `/contact/?hp_verify=20260908-map-2#store-map` scrolled directly to the map. A fresh public comparison found no homepage link differences after normalizing site hostnames. No plugin changes, catalog migration or database copy occurred.

