# HolyPearl (פנינת הקודש)

Planning repository for https://holypearl.co.il — documentation and drafts only.

**Live site:** unchanged. Nothing here deploys automatically.

## Contents

| Folder | Purpose |
|--------|---------|
| strategy/ | Master plan, homepage copy |
| drafts/html/ | Homepage HTML previews |
| audits/ | Plugin, pages, maintenance reviews |
| seo/ | SEO migration plan |
| css/ | Design tokens (Astra / Simple CSS) |
| snippets/ | Code Snippets inventory |
| docs/ | Index |

## Excluded

Secrets, wp-config.php, DB dumps, uploads, cache, backups, logs, premium plugin source.

## GitHub

    cd holypearl
    git init
    git add .
    git commit --trailer "Co-authored-by: Cursor <cursoragent@cursor.com>" -m "Initial HolyPearl planning repository"

Use a private repo if snippet PHP exports are added later.