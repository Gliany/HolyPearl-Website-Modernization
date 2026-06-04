# HolyPearl Homepage Architecture Brief

**Site:** https://holypearl.co.il · **Brand:** פנינת הקודש  
**Draft page:** WordPress page ID **3702** (unpublished)  
**Live homepage:** page ID **52** — do not modify until approved cutover  

**Purpose:** Reposition the homepage from product-category navigation (“מזוזות / תפילין / טליתות”) to **customer-intent journeys** — “למה הגעתם היום?” — while reusing WooCommerce URLs and the existing Astra + Beaver Builder stack.

---

## Design principles

| Do | Don't |
|----|-------|
| Hebrew-first, RTL, warm local Judaica store | SaaS landing page |
| Large readable type, full-width sections, max-width content | Tiny Elementor/Woo boxed cards |
| Fast product discovery via journeys | Old catalog-first hero |
| WhatsApp as guidance, not the whole page | WhatsApp-only consultation page |
| Reuse `/product-category/` and `/product/` links | Rebuild entire theme |
| Scoped CSS on draft page 3702 only | Publish 3702 or edit page 52 |

**Contact (unchanged):** דוד ליאני · 052-8133714 · 09-7433826 · רעננה  
**WhatsApp:** `https://wa.me/972528133714`

---

## Section order (11 blocks)

1. **Hero / Intent Gateway** — headline, subhead, primary + secondary CTA, 4–6 journey shortcuts above the fold  
2. **Primary Journey Grid** — six situation cards  
3. **Featured Journey: Home + Mezuzot**  
4. **Featured Journey: Bar Mitzvah**  
5. **Gift Finder**  
6. **Shabbat & Holidays**  
7. **Daily Prayer & Essentials**  
8. **Need Help Choosing?** — short WhatsApp block  
9. **Local Trust**  
10. **Secondary Journeys** — compact links  
11. **Final CTA** — WhatsApp + phone  

---

## 1. Hero / Intent Gateway

| Element | Copy |
|---------|------|
| Headline | פנינת הקודש ברעננה — יודאיקה לפי החיים עצמם |
| Subheadline | מזוזות לבית חדש, תפילין לבר מצווה, מתנות עם משמעות, מוצרי שבת וחג, סידורים ויודאיקה — עם הכוונה אישית כשצריך. |
| Primary CTA | בחרו לפי צורך → `#journeys` |
| Secondary CTA | התייעצות בוואטסאפ → WhatsApp |

**Quick journeys (6):** בית חדש · בר מצווה · מתנה · שבת וחג · בדיקת מזוזות · תפילה ויום־יום  

**Mobile:** Headline → 4–6 shortcuts (2-column grid) → primary CTA → secondary WhatsApp. No dense product grid above fold.

---

## 2. Primary Journey Grid

Anchor: `#journeys` · Section title: **למה הגעתם היום?**

| Journey | Situation line | Tags (examples) | CTA |
|---------|----------------|-----------------|-----|
| בית חדש ומזוזות | עברתם דירה או בונים בית — מתחילים במזוזות ובתי מזוזה. | מזוזות, בתי מזוזה, קלפים, בדיקה, ייעוץ | התחילו עם בית חדש |
| בר מצווה | בוחרים תפילין, טלית וסידור בלי לחץ. | תפילין, טלית, סידור, תיק, כיפה | לחבילת בר מצווה |
| מתנות עם משמעות | מתנה שמכבדת את האירוע והמקבל. | יולדת, בית חדש, יום הולדת, מנהל | מצאו מתנה |
| שבת וחגים | כלים ואווירה לשבת ולמועדים. | פמוטים, קידוש, חלה, זמירות | לשבת וחג |
| בדיקת מזוזות | תיאום בדיקת סת״ם בבית או בחנות. | בדיקה, תיקון, ייעוץ | לתיאום בדיקה |
| תפילה ויום־יום | סידורים, מחזורים ותשמישי תפילה. | סידור, תהילים, כיפה, ציצית | ליום־יום |

---

## 3. Featured: Home + Mezuzot

Anchor: `#home-mezuzot` · Chips: מזוזות · בתי מזוזה · קלפים · בדיקות סת״ם · ייעוץ לקביעת מזוזות  
**Primary CTA:** התחילו עם מזוזות לבית · **Secondary:** לתיאום בדיקת מזוזות  

**URLs:** `/product-category/mizoza/` · בדיקה product slug  

---

## 4. Featured: Bar Mitzvah

Anchor: `#bar-mitzvah` · Items: תפילין, טלית, סידור, תיק, כיפה, תהילים  
**Kashrut levels:** בסיס / מהודר / מהודר מן המהודר (copy + WhatsApp — not separate SKUs unless catalog supports)  
**CTA:** עזרה לבחירת חבילת בר מצווה  

**URLs:** `men/tpilin`, `talit`, `men/kipot`, `men/ttcovers`, bar-mitzvah kit product  

---

## 5. Gift Finder

Anchor: `#gifts` · Paths: יולדת · בית חדש · יום הולדת · מנהל/עובד · רב/מורה  
**CTA:** מצאו מתנה  

---

## 6. Shabbat & Holidays

Anchor: `#shabbat` · Items: פמוטים, גביעי קידוש, כיסויי חלה, זמירות, בירכונים + seasonal note  
**CTA:** למוצרי שבת וחג  

**URLs:** `shabat`, `klibit`, `חגים-ויום-טוב`  

---

## 7. Daily Prayer & Essentials

Anchor: `#daily` · Items: סידורים, מחזורים, תהילים, הלכה, כיפות, ציציות, טליתות  
**CTA:** למוצרי תפילה ויום־יום  

---

## 8. Need Help Choosing?

Copy: לא בטוחים מה מתאים? כתבו לנו מה האירוע או הצורך, ונכוון אתכם למוצרים המתאימים.  
**CTA:** שלחו שאלה בוואטסאפ  

---

## 9. Local Trust

Bullets: חנות מקומית ברעננה · יחס אישי לפני ואחרי · מוצרים שנבחרים בקפידה · עזרה ברורה בלי לחץ · ניסיון במזוזות, בר מצווה, מתנות ושבתות  

---

## 10. Secondary Journeys

Compact cards: חתונה והקמת בית · תיירים ומזכרות · ספרי קודש · כיפות וציציות · מוצרים לפי קטגוריה (`/store/`)  

---

## 11. Final CTA

Copy: לא בטוחים מאיפה להתחיל? כתבו לנו מה אתם מחפשים ונכוון אתכם.  
**Primary:** שלחו וואטסאפ · **Secondary:** 052-8133714  

---

## Implementation artifacts (this repo)

| File | Use |
|------|-----|
| `css/homepage-intent-draft-3702.css` | Paste into Simple CSS / BB row CSS — scoped to `.holypearl-hp3702` |
| `drafts/html/holypearl-homepage-intent-draft-3702.html` | Browser preview (full page) |
| `wordpress/page-3702-homepage-markup.html` | Beaver Builder HTML module body |
| `docs/page-3702-implementation.md` | WP admin steps — draft only |

---

## Launch checklist

- [ ] Owner approves Hebrew copy and section order  
- [ ] Paste markup + CSS into page **3702** only  
- [ ] QA desktop + mobile RTL  
- [ ] Confirm page 52 unchanged and 3702 **Draft**  
- [ ] After approval: optional front-page switch (separate task)  
