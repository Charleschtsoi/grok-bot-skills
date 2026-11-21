# Provenance and source notes

## What this draft is

A **public-safe consolidation** of a read-only inventory of skills available to Charlie’s Grok Bot fleet, prepared for [github.com/Charleschtsoi/grok-skills](https://github.com/Charleschtsoi/grok-skills).

The catalogues in [`catalogs/`](catalogs/manifest.json) were produced from a local scan and packaged as a public-safe archive (sha256 `6b6a002e411ce1280d5ab546518237b0b83f62a619f633ae009855687be12434`). This repository draft uses that archive. It does **not** re-fetch private bot files, personas, transcripts, or live profiles.

Inventory timestamp recorded in the archive: **21 Nov 2026, Asia/Hong_Kong (UTC+8)**.

## What was scanned (high level)

- Shared custom skill library (empty at inventory time)
- Managed platform skill catalogue (names and “when to use” descriptions)
- Installed plugin manifests and registered plugin skills (names, descriptions, relative paths inside the plugin, local licence fields)
- Extra `SKILL.md` files present under plugin installs but not registered in the live catalogue
- Narrow evidenced-use checks against a local chat index and agent personas (not full history)

## What was intentionally omitted

- Managed and plugin skill **bodies** (recipes), for provenance and licensing reasons — catalogue and link only
- Agent personas, transcripts, routines definitions
- Secrets, PII, absolute machine paths, internal numeric IDs, personal plans
- Web research or “recommended new skills” (deferred to a later pass)

## Catalogue is not installation

| Action | Effect on agent skills |
|---|---|
| Clone or browse this repository | None — docs and catalogues only |
| Install this repo as a package or submodule | Still none — this is not a skill runtime |
| Install / enable a plugin upstream (see [installed-plugins.md](catalogs/installed-plugins.md)) | That plugin may register skills in the product |
| Platform-managed skills | Provided by the product; listed here by name only |

## Ownership and usage

- Skills listed here are **globally shared** availability at inventory time.
- Do **not** invent per-agent ownership.
- Do **not** treat “available” as “used”. Evidenced-use notes in [INVENTORY.md](INVENTORY.md) and [`catalogs/manifest.json`](catalogs/manifest.json) are narrow and incomplete.

## Validation

[`scripts/validate_catalog.py`](scripts/validate_catalog.py) checks that documented counts, duplicate/overlap lists, and relative Markdown links stay consistent with the JSON catalogues.
