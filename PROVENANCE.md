# Provenance and source notes

## What this repository is

A **public-safe consolidation** of a read-only inventory of skills available to Charlie’s Grok Bot fleet, plus a community contribution path, prepared for [github.com/Charleschtsoi/grok-skills](https://github.com/Charleschtsoi/grok-skills).

The community-hub layer (README quick starts, [CONTRIBUTING.md](CONTRIBUTING.md), templates, issue/PR forms, MIT for repository-original material) does not change the inventory facts: catalogue references remain non-installing, and original installable skills under `custom-skills/` remain zero until someone contributes and merges a real recipe.

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
- Live installs, routines, personas, or third-party skill body copies from the recommendations pass

## Recommendations research (follow-on)

A separate public-safe research package (sha256 `999df77985e4763c1b7fa0391e824e49c65c3cd7fdbabee774efcd580421b901`) proposed six original skills. Adapted docs live in [RECOMMENDATIONS.md](RECOMMENDATIONS.md), [SOURCES.md](SOURCES.md), and [recommendations/](recommendations/README.md). All remain `PROPOSED` / `NOT_INSTALLED`.

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
