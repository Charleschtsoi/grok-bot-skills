# grok-skills

Public draft catalogue of skills **available** to Charlie’s Grok Bot fleet.

This repository is an **inventory and set of pointers**. It is not a skill installer, not a runtime skill library, and not a redistribution of managed or third-party skill recipes.

Cloning or browsing this repo does **not** install skills into any agent. Skills remain where the platform and plugins already provide them. When custom skills exist, sanitised copies may later live under [`custom-skills/`](custom-skills/README.md).

## Snapshot (21 Nov 2026, Asia/Hong_Kong / UTC+8)

| Category | Count | In this repo |
|---|---:|---|
| Custom (user-authored) skills | 0 | Placeholder only — none found in the shared library |
| Managed platform skills | 71 | Names and descriptions; bodies omitted |
| Plugin skill entries | 210 | Names, descriptions, plugin origin, licence pointers; bodies omitted |
| Unique plugin skill names | 191 | 19 names registered by both Vercel plugin installs |
| Installed plugins | 18 | 14 with skills; 4 connectors with none |

Skills are **globally shared** across agents. “Available” means the live catalogue listed the skill at inventory time. “Evidenced” means a persona or local chat index referred to it as a skill — that evidence is narrow and is **not** full usage history. Do not treat availability as ownership or as proof of use.

## Proposed additions (research only)

Six original skills are **proposed** to fill fleet-governance gaps. All are `PROPOSED` / `NOT_INSTALLED` — documentation for later authoring, not executable skills and not live installs. See [RECOMMENDATIONS.md](RECOMMENDATIONS.md).

| Priority | Proposed skill |
|---:|---|
| 1 | Outbound approval review |
| 2 | Agent department mapping |
| 3 | Safe agent retirement |
| 4 | External skill provenance review |
| 5 | Fleet privacy / permission review |
| 6 | Work evidence pack |

## Docs

| Document | Purpose |
|---|---|
| [INVENTORY.md](INVENTORY.md) | Human-readable inventory, counts, evidenced-use notes, limitations |
| [RECOMMENDATIONS.md](RECOMMENDATIONS.md) | Shortlist of proposed original skills (not installed) |
| [SOURCES.md](SOURCES.md) | Research sources, unverified URLs, extraction limitations |
| [recommendations/](recommendations/README.md) | One brief per proposed skill |
| [LICENSING.md](LICENSING.md) | Redistribution policy and per-plugin licence pointers from local install metadata |
| [PROVENANCE.md](PROVENANCE.md) | Source of the draft, what was scanned, what was intentionally omitted |
| [catalogs/README.md](catalogs/README.md) | Index of catalogue files |
| [catalogs/manifest.json](catalogs/manifest.json) | Machine-readable summary counts and overlap lists |
| [catalogs/recommendations.json](catalogs/recommendations.json) | Machine-readable recommendations index |
| [catalogs/managed-skills.md](catalogs/managed-skills.md) | Managed platform skill catalogue |
| [catalogs/plugin-skills.md](catalogs/plugin-skills.md) | Plugin skill catalogue |
| [catalogs/installed-plugins.md](catalogs/installed-plugins.md) | Installed plugins and upstream links |
| [custom-skills/README.md](custom-skills/README.md) | Placeholder for future sanitised custom skills |

## Validation

Run a lightweight check that catalogue counts, recommendation briefs, Vercel name overlaps, and relative Markdown links stay consistent:

```bash
python3 scripts/validate_catalog.py
```

## Repository content policy

- Preserve this public inventory as catalogue metadata and documentation only.
- Do **not** copy platform-managed or plugin skill bodies into this draft.
- Do **not** add secrets, PII, transcripts, live profiles, absolute machine paths, internal numeric IDs, or personal plans.
- This repo does **not** claim copyright ownership of third-party or platform skills. See [LICENSING.md](LICENSING.md).
