from pathlib import Path
import re, html
from urllib.parse import urlparse, parse_qs

base = Path(__file__).parent
source = (base / "mezuzah.he.md").read_text(encoding="utf-8")
staging = "https://staging-f20c-holypearlil.wpcomstaging.com"

ids = {
    "מזוזה היא הנשמה שבפתח": "meaning",
    "הקלף מתחיל באדם שכותב אותו": "scribe",
    "כשרה, מהודרת ומהודרת מן המובחר": "hiddur",
    "חובת בדיקת מזוזות": "checks",
    "באילו פתחים קובעים מזוזה": "doorways",
    "כך קובעים מזוזה": "installation",
    "ברכת קביעת מזוזה": "blessing",
    "מנהגי אשכנז, ספרד ועדות המזרח": "customs",
    "שאלות ששואלים לפני שבוחרים": "faq",
    "מזוזות וקלפים מהקטלוג": "catalog",
    "רוצים לבחור נכון?": "contact",
}

def localize_url(url):
    if url.startswith("https://holypearl.co.il/"):
        parsed = urlparse(url)
        localized = staging + parsed.path
        if parsed.query:
            localized += "?" + parsed.query
        if parsed.fragment:
            localized += "#" + parsed.fragment
        return localized
    return url

def inline(text):
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", escaped)
    def link(match):
        return f'<a href="{html.escape(localize_url(html.unescape(match.group(2))), quote=True)}">{match.group(1)}</a>'
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, escaped)

blocks = []
for block in source.split("\n## ")[1:]:
    title, body = block.split("\n", 1)
    sid = ids.get(title, "section")
    output = []
    list_type = [None]
    def close_list():
        if list_type[0]:
            output.append(f"</{list_type[0]}>")
            list_type[0] = None
    for line in body.strip().splitlines():
        line = line.strip()
        if not line:
            close_list()
            continue
        ordered = re.match(r"^\d+\.\s+(.*)", line)
        bullet = re.match(r"^-\s+(.*)", line)
        faq = re.match(r"^\*\*(.*?\?)\*\*\s*(.*)", line)
        if ordered:
            if list_type[0] != "ol":
                close_list(); output.append('<ol class="hpmez-steps">'); list_type[0] = "ol"
            output.append("<li>" + inline(ordered.group(1)) + "</li>")
        elif bullet:
            if list_type[0] != "ul":
                close_list(); output.append('<ul class="hpmez-list">'); list_type[0] = "ul"
            output.append("<li>" + inline(bullet.group(1)) + "</li>")
        elif faq:
            close_list()
            output.append("<details><summary>" + inline(faq.group(1)) + "</summary><p>" + inline(faq.group(2)) + "</p></details>")
        else:
            close_list()
            output.append("<p>" + inline(line) + "</p>")
    close_list()
    if sid == "blessing":
        output.insert(0, '<figure class="hpmez-blessing-card"><img src="__HP_BLESSING_IMAGE_URL__" alt="ברכת קביעת מזוזה בכתב סת״ם: ברוך אתה ה׳, אלוהינו מלך העולם, אשר קידשנו במצוותיו וציוונו לקבוע מזוזה" loading="lazy"><figcaption>נוסח הברכה לקביעה במקום שחיובו ברור</figcaption></figure>')
    if sid == "scribe":
        output.insert(1, '<figure class="hpmez-story-image"><img src="__HP_SCRIBE_IMAGE_URL__" alt="סופר סת״ם בודק בדקדוק את אותיות הקלף" loading="lazy"><figcaption>כתיבה ובדיקה של קלף מזוזה הן מלאכת קודש הדורשת בקיאות, ריכוז ויראת שמים.</figcaption></figure>')
    if sid == "checks":
        output.insert(1, '<figure class="hpmez-detail-image"><img src="__HP_PARCHMENT_IMAGE_URL__" alt="קלף מזוזה כתוב ביד בכתב סת״ם" loading="lazy"><figcaption>בבדיקה בוחנים כל אות, רווח ונגיעה בקלף.</figcaption></figure>')
    if sid == "catalog":
        output.insert(0, '<div class="hpmez-product-gallery" aria-label="מבחר בתי מזוזה מהקטלוג"><a href="https://staging-f20c-holypearlil.wpcomstaging.com/store/"><img src="__HP_PRODUCT_GLASS_IMAGE_URL__" alt="בית מזוזה מזכוכית בגווני כחול ולבן" loading="lazy"><span>בתי מזוזה מזכוכית</span></a><a href="https://staging-f20c-holypearlil.wpcomstaging.com/?p=2244"><img src="__HP_PRODUCT_JERUSALEM_IMAGE_URL__" alt="בית מזוזה בגוון בהיר בעיצוב חומות ירושלים" loading="lazy"><span>בתי מזוזה בעיצוב ירושלים</span></a><a href="https://staging-f20c-holypearlil.wpcomstaging.com/store/"><img src="__HP_PRODUCT_ACRYLIC_IMAGE_URL__" alt="מבחר בתי מזוזה מאקריליק בגוונים שונים" loading="lazy"><span>בתי מזוזה צבעוניים</span></a></div>')
    classes = ["hpmez-section"]
    if sid == "contact": classes.append("hpmez-contact")
    blocks.append(f'<section class="{" ".join(classes)}" id="hpmez-{sid}"><h2>{html.escape(title)}</h2>{"".join(output)}</section>')

whatsapp = re.search(r"\[התייעצות ב-WhatsApp\]\(([^)]+)\)", source).group(1)

css = """
<style>
.hpmez{--ink:#172e43;--blue:#224b70;--paper:#f9fbfc;--silver:#dce5eb;--muted:#526778;--green:#215c49;background:var(--paper);color:var(--ink);font-family:Arial,sans-serif;font-size:18px;line-height:1.85;direction:rtl}
.hpmez *{box-sizing:border-box}.hpmez a{color:var(--blue);text-underline-offset:5px}.hpmez a:focus-visible,.hpmez summary:focus-visible,.hpmez button:focus-visible{outline:3px solid var(--blue);outline-offset:5px}
.hpmez-shell{max-width:1180px;margin:auto;padding-inline:32px}.hpmez-languages{display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding-block:24px;font-size:14px}.hpmez-languages button{font:inherit;background:transparent;border:1px solid var(--silver);border-radius:6px;padding:7px 13px}.hpmez-languages button[aria-current=true]{background:var(--ink);color:#fff}.hpmez-languages button:disabled{color:var(--muted);border-style:dashed}.hpmez-languages small{color:var(--muted)}
.hpmez-hero{display:grid;grid-template-columns:1.35fr 1fr;gap:65px;align-items:center;padding-block:28px 72px}.hpmez-eyebrow{font-size:14px;letter-spacing:1px;color:var(--muted)}.hpmez h1{font-family:"Times New Roman",serif;font-size:clamp(48px,6.5vw,82px);line-height:1.12;font-weight:400;margin:20px 0 25px;max-width:680px}.hpmez h1 span{color:var(--blue)}.hpmez-hero p{max-width:540px;color:var(--muted);font-size:20px}.hpmez-actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}.hpmez-button{display:inline-block;padding:12px 22px;border-radius:5px;text-decoration:none;background:var(--ink);color:#fff!important;font-size:16px}.hpmez-button--secondary{background:transparent;color:var(--ink)!important;border:1px solid var(--silver)}
.hpmez-hero-image{height:440px;margin:0;position:relative;overflow:hidden;border-radius:180px 180px 8px 8px;background:#fff;border:1px solid var(--silver)}.hpmez-hero-image:after{content:"";position:absolute;inset:auto 12% 0;height:1px;background:linear-gradient(90deg,transparent,var(--silver),transparent)}.hpmez-hero-image img{width:100%;height:100%;display:block;object-fit:contain;padding:42px 24px 25px}.hpmez-caption{font-size:12px;color:var(--muted);margin:8px 0}
.hpmez-layout{display:grid;grid-template-columns:210px minmax(0,1fr);gap:70px;align-items:start}.hpmez-toc{position:sticky;top:25px;font-size:15px;border-top:3px solid var(--blue);padding-top:14px}.hpmez-toc a{display:block;padding:9px 0;text-decoration:none;border-bottom:1px solid var(--silver)}.hpmez article{min-width:0}.hpmez-section{padding:14px 0 35px;border-top:1px solid var(--silver)}.hpmez h2{font-family:"Times New Roman",serif;font-size:34px;line-height:1.35;margin:20px 0;color:var(--ink)}.hpmez-section p{margin:15px 0}.hpmez-steps{list-style:none;padding:0;counter-reset:steps}.hpmez-steps li{counter-increment:steps;position:relative;padding:24px 64px 24px 0;border-bottom:1px solid var(--silver)}.hpmez-steps li:before{content:counter(steps);position:absolute;right:0;top:25px;border:1px solid var(--silver);width:38px;height:38px;text-align:center;line-height:36px;border-radius:50%;color:var(--blue)}.hpmez-list{padding-right:22px}.hpmez-list li{margin:10px 0}.hpmez details{border-bottom:1px solid var(--silver);padding:18px 0}.hpmez summary{cursor:pointer;font-weight:700}.hpmez details p{color:var(--muted)}#hpmez-catalog .hpmez-list{list-style:none;padding:0}#hpmez-catalog .hpmez-list a{display:block;padding:14px 20px;background:#fff;border:1px solid var(--silver);border-radius:5px;text-decoration:none}
.hpmez-story-image,.hpmez-detail-image{margin:26px 0 30px}.hpmez-story-image img{display:block;width:100%;height:360px;object-fit:cover;object-position:center 30%;border-radius:8px}.hpmez-detail-image{display:grid;grid-template-columns:minmax(0,300px) 1fr;gap:22px;align-items:center;background:#fff;border:1px solid var(--silver);border-radius:8px;padding:22px}.hpmez-detail-image img{display:block;width:100%;height:270px;object-fit:contain}.hpmez-story-image figcaption,.hpmez-detail-image figcaption{color:var(--muted);font-size:14px;line-height:1.6;margin-top:8px}.hpmez-blessing-card{max-width:600px;margin:20px auto;text-align:center}.hpmez-blessing-card img{display:block;width:100%;height:auto;border-radius:7px;box-shadow:0 12px 35px #172e4324}.hpmez-blessing-card figcaption{margin-top:8px;color:var(--muted);font-size:13px}.hpmez-product-gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:24px 0}.hpmez-product-gallery a{display:flex;flex-direction:column;background:#fff;border:1px solid var(--silver);border-radius:8px;overflow:hidden;text-decoration:none}.hpmez-product-gallery img{display:block;width:100%;height:230px;object-fit:contain;padding:18px}.hpmez-product-gallery span{padding:13px 16px;border-top:1px solid var(--silver);font-weight:700;font-size:15px}.hpmez-contact{background:var(--ink);color:#fff;padding:24px 30px;border-radius:8px;margin-bottom:40px}.hpmez-contact h2{color:#fff}.hpmez-contact a{display:inline-block;background:#fff;color:var(--ink);padding:12px 22px;text-decoration:none;border-radius:5px}.hpmez-mobile-contact{display:none}
@media(max-width:760px){.hpmez-shell{padding-inline:22px}.hpmez-hero{grid-template-columns:1fr;gap:24px;padding-bottom:36px}.hpmez-hero-image{height:290px;border-radius:110px 110px 8px 8px}.hpmez-hero-image img{padding:26px 18px 15px}.hpmez-hero p{font-size:18px}.hpmez-layout{grid-template-columns:1fr;gap:28px}.hpmez-toc{position:static;display:flex;flex-wrap:wrap;gap:8px}.hpmez-toc strong{width:100%}.hpmez-toc a{border:1px solid var(--silver);padding:6px 10px;border-radius:5px;font-size:13px}.hpmez h2{font-size:29px}.hpmez-steps li{padding-right:52px}.hpmez-story-image img{height:250px}.hpmez-detail-image{grid-template-columns:1fr;text-align:center}.hpmez-detail-image img{height:230px}.hpmez-product-gallery{grid-template-columns:1fr 1fr}.hpmez-product-gallery a:last-child{grid-column:1/-1}.hpmez-product-gallery img{height:190px}.hpmez-languages small{width:100%}.hpmez{padding-bottom:65px}.hpmez-mobile-contact{display:block;position:fixed;bottom:0;left:0;right:0;background:var(--green);color:#fff!important;text-align:center;padding:13px;text-decoration:none;z-index:20}}
@media(prefers-reduced-motion:reduce){.hpmez{scroll-behavior:auto}}
</style>
"""

fragment = css + f"""
<main class="hpmez" lang="he" dir="rtl">
<div class="hpmez-shell">
<div class="hpmez-languages" aria-label="שפת המדריך"><button type="button" aria-current="true">עברית</button><button type="button" disabled lang="en">English</button><button type="button" disabled lang="ru">Русский</button><button type="button" disabled lang="fr">Français</button><button type="button" disabled lang="de">Deutsch</button><small>השפות הנוספות יהיו זמינות לאחר השלמת התרגום.</small></div>
<div class="hpmez-hero">
<div><div class="hpmez-eyebrow">מדריכים לבית היהודי / מזוזות</div><h1>מזוזות לבית ולעסק.<br><span>קדושה מתחילה בפתח.</span></h1><p>המשמעות שבקלף, עבודת הסופר, רמות ההידור והדרך הנכונה לקבוע מזוזה בבית ובעסק.</p><div class="hpmez-actions"><a class="hpmez-button" href="#hpmez-installation">מדריך לקיבוע ↓</a><a class="hpmez-button" href="#hpmez-blessing">ברכת הקביעה</a><a class="hpmez-button hpmez-button--secondary" href="#hpmez-catalog">למזוזות בקטלוג</a></div></div>
<figure><div class="hpmez-hero-image"><img src="__HP_PRODUCT_GLASS_IMAGE_URL__" alt="בית מזוזה מזכוכית בגווני כחול ולבן"></div><figcaption class="hpmez-caption">בית מזוזה מכבד את המצווה ושומר על הקלף שבתוכו</figcaption></figure>
</div>
<div class="hpmez-layout"><nav class="hpmez-toc" aria-label="בעמוד הזה"><strong>בעמוד הזה</strong><a href="#hpmez-meaning">נשמה בפתח</a><a href="#hpmez-scribe">קדושת הסופר</a><a href="#hpmez-hiddur">רמות הידור</a><a href="#hpmez-checks">חובת הבדיקה</a><a href="#hpmez-doorways">אילו פתחים חייבים</a><a href="#hpmez-installation">מדריך לקיבוע</a><a href="#hpmez-blessing">ברכת הקביעה</a><a href="#hpmez-customs">מנהגים ומסורות</a><a href="#hpmez-faq">שאלות נפוצות</a><a href="#hpmez-catalog">מהקטלוג</a></nav><article>{''.join(blocks)}</article></div>
</div>
<a class="hpmez-mobile-contact" data-vars-ga-category="hp_whatsapp_click" href="{html.escape(whatsapp, quote=True)}" rel="noopener" target="_blank">שאלה על מזוזה? כתבו לנו ב-WhatsApp</a>
</main>
"""

(base / "mezuzah-wordpress-fragment.html").write_text(fragment, encoding="utf-8")
(base / "mezuzah-wordpress-local-preview.html").write_text(
    '<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>WordPress fragment QA</title></head><body style="margin:0">' + fragment.replace('__HP_BLESSING_IMAGE_URL__', 'images/mezuzah-blessing.png') + "</body></html>",
    encoding="utf-8",
)
print("Created WordPress fragment and local QA wrapper")

