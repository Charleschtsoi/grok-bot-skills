# grok-skills

A **shareable skills hub**: browse what is available, reuse ideas freely, and contribute original skills others can use under MIT.

This repository is friendly to cloning, forking, and pull requests. It is **not** an installer. Cloning it does **not** install managed platform skills, plugin skills, or custom skills into any agent.

## Current state (honest)

| What you will find | Status |
|---|---|
| Catalogue of managed + plugin skills (names, descriptions, upstream pointers) | Published — bodies omitted on purpose |
| Research shortlist of six proposed original skills | `PROPOSED` / `NOT_INSTALLED` — briefs only |
| Installable original skills under `custom-skills/` | **Zero** today (placeholder + example template only) |

Inventory snapshot (21 Nov 2026): **0** custom, **71** managed, **210** plugin entries (**191** unique names), **18** installed plugins. Details: [INVENTORY.md](INVENTORY.md).

## Quick start

### 1. Browse what already exists

- Human inventory: [INVENTORY.md](INVENTORY.md)
- Managed names/descriptions: [catalogs/managed-skills.md](catalogs/managed-skills.md)
- Plugin skills + upstream links: [catalogs/plugin-skills.md](catalogs/plugin-skills.md) · [catalogs/installed-plugins.md](catalogs/installed-plugins.md)

To use a **plugin** skill in your own environment, install or enable that plugin from its upstream (linked in the catalogue). This repo only points there.

### 2. Review suggested additions

Six governance-oriented originals are proposed for later authoring. They are documentation, not live skills: [RECOMMENDATIONS.md](RECOMMENDATIONS.md) · [recommendations/](recommendations/README.md).

### 3. Contribute a skill others can reuse

1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. Copy [templates/SKILL.template.md](templates/SKILL.template.md)
3. Compare with the labelled **example** (not a functioning skill): [custom-skills/_examples/hello-skill-review/](custom-skills/_examples/hello-skill-review/SKILL.md)
4. Open a PR, or start with a [Propose a skill](https://github.com/Charleschtsoi/grok-skills/issues/new?template=propose-skill.yml) issue

Contributed original skills and docs in this repo are free to use, modify, and redistribute under the [MIT License](LICENSE). See [LICENSING.md](LICENSING.md) for what MIT covers and what it does **not**.

## Safety before you trust a skill

- Review instructions locally. Prefer linking upstream over vendoring third-party bodies.
- Treat contributed skill text as untrusted until you verify it: no secrets, no private paths, no “run this tool that sends mail/buys things” without an explicit human yes.
- A skill file is prose. It **cannot** enforce platform approval gates, Auto-review, or connector permissions.
- No warranties: MIT “AS IS”. Catalogue entries are availability references, not endorsements.

## Docs map

| Document | Purpose |
|---|---|
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to propose and submit skills |
| [LICENSING.md](LICENSING.md) | MIT scope, exclusions, plugin licence pointers |
| [INVENTORY.md](INVENTORY.md) | Fleet catalogue counts and limitations |
| [RECOMMENDATIONS.md](RECOMMENDATIONS.md) | Proposed (not installed) originals |
| [SOURCES.md](SOURCES.md) | Research sources and extraction caveats |
| [PROVENANCE.md](PROVENANCE.md) | Where the inventory/research came from |
| [custom-skills/](custom-skills/README.md) | Home for future contributed originals |
| [templates/SKILL.template.md](templates/SKILL.template.md) | Submission template |
| [catalogs/](catalogs/README.md) | Machine- and human-readable catalogues |

## Validation (local, read-only)

```bash
python3 scripts/validate_catalog.py
```

Checks catalogue/recommendation counts, relative Markdown links, issue-form YAML, and the example/template skill frontmatter. It does not install skills or write to any agent library.

## Licence (short)

- **Repository-original** docs, scripts, templates, examples, and future contributed skill recipes in this repo: [MIT](LICENSE) © 2026 Charleschtsoi — free to use, modify, and redistribute.
- **Managed / plugin / upstream** skill bodies and descriptions: **not** relicensed here. Catalogue rows are references only. Keep upstream terms; prefer link over copy. Details: [LICENSING.md](LICENSING.md).
