# HolyPearl Homepage Architecture Brief

**Site:** https://holypearl.co.il · **Brand:** פנינת הקודש  
**Draft page:** WordPress page ID **3702** (unpublished)  
**Live homepage:** page ID **52** — do not modify until approved cutover  

**Purpose:** Customer-intent Judaica homepage with **editorial storytelling** and large photography — not a wireframe of cards and grids.

---

## Design principles

| Do | Don't |
|----|-------|
| Hebrew-first, RTL, warm local brand | SaaS / catalog wireframe |
| Full-bleed and large product photography | Extra card grids or tag chips |
| One life-moments narrative block (4 beats) | Six journey cards, gift grids, trust grids |
| Six real products in horizontal showcase | Generic placeholder products |
| Meet David — portrait + story | Anonymous shop only |
| Intent links in hero (text, not pills) | Dense grids above the fold |
| Scoped CSS on page 3702 only | Publish 3702 or edit page 52 |

**Contact:** דוד ליאני · 052-8133714 · 09-7433826 · רעננה  
**WhatsApp:** `https://wa.me/972528133714`

---

## Section order (6 blocks)

1. **Hero / Intent Gateway** — cinematic photo, headline, story, text links to moments (בית חדש · בר מצווה · חתונה · שבת · בדיקה)
2. **Life moments** — single section, four editorial panels (image + story each): בית חדש, בר מצווה, חתונה, שבת
3. **Featured products** — six real SKUs, horizontal scroll showcase (not a card grid)
4. **Meet David** — large photo, biography, phone + WhatsApp
5. **Need help** — short WhatsApp band
6. **Final CTA** — store visit + contact

---

## 1. Hero

| Element | Copy |
|---------|------|
| Headline | יודאיקה לפי החיים עצמם |
| Story | מזוזות לבית חדש, תפילין לבר מצווה… עם אדם שמכיר את המוצרים ואת הרגעים |
| Question | למה הגעתם היום? |
| Links | בית חדש · בר מצווה · חתונה · שבת · בדיקת מזוזות → `#moments` or product |
| CTAs | גלו מוצרים נבחרים · התייעצות בוואטסאפ |

**Visual:** Full-width lifestyle image with gradient veil (not boxed panel).

---

## 2. Life moments (`#moments`)

One section title: **רגעים שמגיעים עם חיים שלמים**

| Moment | Story angle | CTA target |
|--------|-------------|------------|
| בית חדש | מזוזות, קלפים, בדיקה | `/product-category/mizoza/` |
| בר מצווה | תפילין, טלית, חבילה | bar mitzvah kit product |
| חתונה | הקמת בית יהודי | wedding kit product |
| שבת | אווירה בבית, כלי שבת | `/product-category/shabat/` |

**Layout:** Alternating 50/50 image + copy rows (no cards).

---

## 3. Featured products (`#products`)

Six real products from catalog:

1. קלף למזוזה נוסח אשכנזי  
2. תפילין  
3. ערכת בר מצווה  
4. טלית צמר רחלים תשבץ  
5. מגש חלה שבת עם סכין מהודר  
6. סידור רינת ישראל עור עתיק  

**Layout:** Horizontal scroll strip with large images — not a 3×2 card grid.

---

## 4. Meet David (`#david`)

- Photo (replace with real portrait before launch if available)  
- Story: 15+ years, סופר סת״ם, מכון יחזקאל, personal service  
- Quote line  
- 052-8133714 + WhatsApp  

---

## 5–6. Help + Final CTA

Unchanged intent; minimal bands, no card UI.

---

## Removed from earlier wireframe draft

- Six journey cards + tags  
- Gift finder grid  
- Trust bullet grid  
- Secondary journey compact cards  
- Multiple featured bands with chip rows  
- Separate mezuzot / BM / gifts / shabbat / daily sections  

---

## Implementation artifacts

| File | Use |
|------|-----|
| `css/homepage-intent-draft-3702.css` | Scoped styles |
| `wordpress/page-3702-homepage-markup.html` | BB HTML / plugin asset |
| `wordpress/dist/holypearl-hp3702-draft.zip` | Upload plugin |
| `drafts/html/holypearl-homepage-intent-draft-3702.html` | Browser preview |

---

## Launch checklist

- [ ] Replace David photo with real portrait (optional)  
- [ ] Owner approves copy  
- [ ] Page 3702 stays **Draft**; page 52 unchanged  
- [ ] Remove draft banner before publish  
