# Holy Pearl (פנינת הקודש) — Master Plan

**Site:** https://holypearl.co.il  
**Last updated:** June 4, 2026  
**Status:** Planning and draft approval — no live site changes without explicit sign-off

---

## 1. North star

Transform **פנינת הקודש** from a product-first online store into a **trusted Judaica authority**: expertise, personal service, and quality assurance — while keeping WooCommerce, the physical store (Ra''anana), and phone-led sales.

| From | To |
|------|-----|
| חנות אונליין / קנה עכשיו | ייעוץ, מומחיות, ביטחון בבחירה |
| Hero product grids and deals | Hero trust plus category guidance |
| Cart-first funnel | דברו עם מומחה / גלו לפי תחום |
| 44 plugins, dual builders | Consolidate stack over time (carefully) |

**Business contact (unchanged):** דוד ליאני · 052-8133714 · 09-7433826 · רעננה

---

## 2. Platform snapshot (audit, read-only)

| Layer | Detail |
|-------|--------|
| Hosting | WordPress.com Business |
| CMS | WordPress 7.0 |
| Theme | Astra (Hever, Varia inactive) |
| Commerce | WooCommerce 10.8.1, 161+ published products |
| Primary builder | Beaver Builder + UABB (most pages) |
| Secondary builder | Elementor (contact + legal; WP.com managed) |
| Active plugins | 44 |
| Live homepage | Page בית (ID 52), static front page |
| Code snippets | Hide WooCommerce Prices, Disable WooCommerce Cart |
| Open orders | 5 active — checkout/account are production-critical |

**Catalog traffic:** Most visits are product and category archive URLs, not only the 10 WordPress pages.

---

## 3. Hard constraints

1. No live edits until copy and structure are approved.
2. Checkout and account — stage changes; orders are live.
3. Cart/pricing snippets — align rebuild with real business flow.
4. Elementor on WP.com — migrate legal/contact with backup; do not remove casually.
5. UTF-8 on Windows — run `node agent-tools/fix-utf8.js` if Hebrew looks corrupted in editor.

---

## 4. Published pages — recommendations

10 published pages. Traffic importance is estimated (role-based, not GA).

| Page | URL | Builder (live) | Traffic | Keep | Merge | Rebuild | Delete later |
|------|-----|----------------|---------|:----:|:-----:|:-------:|:------------:|
| בית | / | Beaver + UABB + WC | Critical | Yes | — | — | — |
| חנות | /store/ | Beaver / UABB | High | Yes | — | — | — |
| עגלת קניות | /cart/ | Beaver + WC | Low–Med | — | — | Yes | Yes |
| קופה | /checkout/ | Beaver + WC | Critical | Yes | — | — | — |
| חשבון אישי | /account/ | Beaver + WC | High | Yes | — | — | — |
| Wishlist | /wishlist/ | Beaver + YITH | Medium | Yes | Yes | — | — |
| צור קשר | /contact/ | BB live; Elementor in admin | High | Yes | Yes | — | — |
| הצהרת נגישות | /accessibility-statement/ | Beaver + snippet | Medium | Yes | — | Yes | — |
| הסכם סודיות | /privacy-policy/ | Elementor EN 2020 | Low–Med | — | Yes | Yes | — |
| תנאי שימוש | /termsconditions/ | Elementor EN 2020 | Low–Med | — | Yes | Yes | — |

**When acting:** (1) Cart/pricing vs phone orders. (2) Elementor legal + contact merge. (3) Homepage rebuild after legal/commerce stable.

---

## 5. Homepage redesign (draft — awaiting approval)

Live בית (ID 52) unchanged. Drafts in workspace only.

**Headline:** המקום שבו בוחרים ביודאיקה בביטחון  
**Eyebrow:** מעל 15 שנות מומחיות ביודאיקה בישראל  
**CTAs:** דברו עם מומחה · גלו לפי תחום  

**Sections:** Hero → Why choose us → תחומי מומחיות (6 cards) → About → Reviews (placeholders) → Articles (3 proposed) → Contact CTA

**Remove after approval:** חנות אונליין, קנה עכשיו, hero product grids, cart-first messaging

**Nav (proposed):** בית · תחומי מומחיות · אודות · מדריכים · צור קשר · חנות (secondary)

**Launch steps:** Approve copy → real testimonials → new BB draft page (not live בית) → QA → Reading settings cutover

---

## 6. Phased roadmap

**Phase 0 (now):** Audits done; homepage draft ready; owner approval pending

**Phase 1:** Align cart/pricing snippets; document purchase path; real reviews

**Phase 2:** Hebrew legal rebuild; merge contact to one builder; accessibility rebuild

**Phase 3:** Build and launch approved homepage on draft page

**Phase 4:** Articles, SEO, plugin rationalization, URL strategy

---

## 7. Workspace artifacts

| File | Purpose |
|------|---------|
| HOLYPEARL_MASTER_PLAN.md | This document |
| canvases/holypearl-homepage-redesign-preview.html | Hebrew browser preview |
| canvases/holypearl-homepage-redesign-draft.canvas.tsx | Canvas + copy |
| canvases/holypearl-wordpress-audit.canvas.tsx | Plugin audit |
| agent-tools/fix-utf8.js | UTF-16 to UTF-8 fix |

---

## 8. Open decisions

1. Commerce model: online checkout vs phone/in-store primary  
2. Homepage tone: more formal/religious?  
3. Real customer testimonials  
4. Blog on-site vs external articles  
5. Homepage cutover timing vs legal rebuild  

---

## 9. Approval checklist

| Item | Approved |
|------|----------|
| Master plan priorities | ☐ |
| Homepage Hebrew copy | ☐ |
| Homepage section order | ☐ |
| Nav changes | ☐ |
| WP draft page build | ☐ |
| Live homepage switch | ☐ |

---

All WordPress work is draft-first. holypearl.co.il is not modified until approved above.