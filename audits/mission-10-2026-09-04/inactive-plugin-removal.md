# Inactive plugin removal — 2026-09-04

Explicit user authorization: disable production Smush and delete all inactive plugins on staging and production. Jetpack versus Jetpack Boost on production awaits clarification; neither changed there.

Deleted on both sites: Elementor Beta, Image Optimization, Livemesh Addons for Beaver Builder, Simple Cache, Starter Templates, The Events Calendar, WPForms Lite, Yoast SEO, and Smush (deactivated first on production). Also deleted already-inactive Jetpack Boost on staging.

MCP uninstall previews inspected before deletion; previews did not enumerate saved-data effects. Each uninstall returned deleted. Fresh plugin.list confirms production 40 installed / 40 active / 0 inactive; staging 39 installed / 39 active / 0 inactive. Production Jetpack and Jetpack Boost remain active; staging Jetpack remains active.

Five routes on each site returned HTTP 200 without detected fatal-error markers: homepage, contact, article 3274, tefillin category, tefillin product. These checks do not establish editor/save, full visual or transaction compatibility. Livemesh package is now absent; no new security scan run.

This execution supersedes prior installed counts and inactive statuses. Historical inventory rows remain for audit history with deleted status and last observed version.
