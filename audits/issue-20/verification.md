# Issue 20 verification — 2026-09-05

## Delivered on staging
Page 3702, https://staging-f20c-holypearlil.wpcomstaging.com/ . User authorized this staging package. Production unchanged.

- Wedding shortcut resolves to the wedding card; mezuzah-check shortcut resolves to the checking card. Each ID exists exactly once.
- Six customer-facing copy replacements remove internal commerce/architecture wording.
- Added one /store/ CTA: לכל המוצרים בקטלוג. Catalog keyboard activation reached /store/.
- Preserved ראו איך מגיעים לחנות at /contact/#store-map. Keyboard activation reached that URL; exactly one map anchor, alt text מפת התמצאות והגעה לפנינת הקודש, חנות 57.
- Corrected the help-button WhatsApp prefill typo. No WhatsApp message sent or telephone call initiated.
- Added MonsterInsights categories: 12 hp_whatsapp_click, 4 hp_phone_click, 1 hp_directions_click, 1 hp_catalog_click. No new JavaScript event listener or plugin.

## Evidence
Editor returned Page updated. First save increased revisions from 34 to 35, revision link 3783; both saves were read back and matched the intended editor string exactly. Original editor markup was retained in the active browser session before editing; use WordPress revisions for persistent recovery.

Browser click tests reached #hp3702-wedding and #hp3702-mezuzah-check, and verified matching headings. Existing card layout/images preserved. A narrow viewport reported 319px (304px document client width), one grid column, RTL direction and no horizontal overflow. Screenshot inspected at wedding destination. Browser console returned no captured errors during this check.

Anonymous HTTP checks after saving: staging and production returned 200. Staging has 18 custom event attributes and the new catalog CTA, with old architecture copy absent. Production has zero of those attributes, no new catalog CTA, and retains old copy. Each HTML response had one gtag loader reference; this is NOT proof of no duplicate events.

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

Production has a different hero CTA from staging. Re-read production and prepare a selective patch after approval; do not paste staging markup wholesale or copy its media hostname. No production deployment, plugin changes, catalog migration or Git merge occurred.
