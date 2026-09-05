# HolyPearl current state

Updated: 2026-09-05. Start here for future tasks. Tracking: [#20](https://github.com/Gliany/HolyPearl-Website-Modernization/issues/20).

## Approved goal
Hebrew content and expert guidance, a complete informational product catalog, and qualified WhatsApp/phone inquiries and store visits. Keep EVERY product, its publication state, media, attributes, metadata and existing URLs. Retain Astra and native WordPress editing; build one lightweight catalog plugin. No online shopping in the target architecture.

Authoritative migration specification: [CONTENT-CATALOG-MIGRATION.md](strategy/CONTENT-CATALOG-MIGRATION.md). Keep WooCommerce until migration, reconciliation and recovery are verified. Do not infer readiness from a plugin count.

## Current implementation
- Production homepage is page 3702, observed at the root URL in the September 5 review. Earlier June documents describing page 52 as the current homepage and 3702 as draft-only are historical.
- Staging homepage 3702 is published within staging. Updated under #20: correct wedding/checking anchor targets, practical Hebrew copy, catalog CTA, fixed WhatsApp prefill typo, and existing MonsterInsights custom event attributes. Existing directions CTA retained.
- Production content, settings and plugins were not changed in #20.
- Last documented September 4 plugin count: 39 active/installed on each site, zero inactive. Not re-inventoried in #20.
- Full catalog migration and independent restore rehearsal remain unperformed/unverified.
- Local folder is documentation/drafts, not a Git checkout or runnable WordPress site. No automatic deployment pipeline is established.

## Tracking and verification
MonsterInsights Lite has a configured GA4 profile on staging. Administrator/Editor roles are excluded from tracking. Homepage markup now distinguishes hp_whatsapp_click, hp_phone_click, hp_directions_click and hp_catalog_click using the existing plugin; no new tracker/plugin installed. Markup and navigation verified; GA4 receipt, consent behavior and duplicate-event audit remain unverified.

Read [verification](audits/issue-20/verification.md) for the exact boundary before production approval.

## Document precedence
1. This current-state summary for execution status, and the September 4 catalog specification for architecture.
2. Latest dated issue execution evidence (#10, #14, #20).
3. Older audits and PRs are historical evidence only. PR #17's selective-retention proposal is superseded. PR #5 targets an older homepage structure; do not deploy it wholesale.
4. June architecture/specification/work/review files and old SEO migration wording do not override the current catalog specification.

## Next work
Complete outstanding verification and review the staged #20 changes before selective production approval. Then #13 image optimization; #14 catalog migration with #10 dependency cleanup; #8/#11/#12 remaining consolidation. Re-evaluate #9 after stack changes. Hosting #15/#16 follows the final requirements.

## Efficient task handoff
Read this file, the relevant issue and only its linked artifacts. Record completed/verified/not-tested/deployed separately. Reuse the current design and assets. Batch related changes. Preserve private operational data outside GitHub. Never sync staging database over production.
