# Skills inventory (public draft)

Generated 21 Nov 2026, Asia/Hong_Kong (UTC+8) from a read-only scan of the Grok Bot fleet on the shared box. This is a catalogue of skills **available** to agents, plus a short note on **evidenced use**. It is not a dump of skill recipes, personas, or transcripts.

Intended home: [github.com/Charleschtsoi/grok-skills](https://github.com/Charleschtsoi/grok-skills).

## Counts

| Category | Count | What is in this repository |
|---|---:|---|
| Custom (user-authored) skills | 0 | README in [`custom-skills/`](custom-skills/README.md) only |
| Managed platform skills | 71 | Names and descriptions; no bodies — [`catalogs/managed-skills.md`](catalogs/managed-skills.md) |
| Plugin skill entries | 210 | Names, descriptions, plugin origin, licence pointers; no bodies — [`catalogs/plugin-skills.md`](catalogs/plugin-skills.md) |
| Unique plugin skill names | 191 | 19 names are registered by both Vercel plugin installs |
| Installed plugins | 18 | 14 ship skills; 4 are connectors with no registered skills — [`catalogs/installed-plugins.md`](catalogs/installed-plugins.md) |
| Extra `SKILL.md` files inside plugin installs but not in the live catalogue | 39 | Listed in [`catalogs/unregistered-plugin-skill-files.json`](catalogs/unregistered-plugin-skill-files.json); not treated as available |

Skills are **globally shared**. This draft does not assign a skill to one agent as owner. “Available” means the live catalogue has it. “Evidenced” means a persona or local chat index referred to it as a skill.

## Available skills

### Custom

The shared user skill library was empty at inventory time. There are no sanitised skill files to publish yet.

### Managed platform skills

71 Grok Bot / Cursor managed skills (booking, shopping, site playbooks, scheduling, code-changes, routines, sign-in, and similar). Full list: [catalogs/managed-skills.md](catalogs/managed-skills.md).

These recipes stay in the product. This repo only lists names and the official “when to use” descriptions.

### Plugin skills

Registered skills come from:

- **pstack** — 58 (engineering workflow and principle skills)
- **Vercel** — 33 in one install, 25 in a second install, with 19 overlapping names
- **Firecrawl** — 19
- **Hugging Face Skills** — 18
- **Figma** — 17
- **Notion workspace** — 14
- **Context.dev** — 11
- **Parallel** — 6
- **Datadog** — 4
- **Cloudinary** — 2
- **Google Docs / Drive / Slides** — 1 each

Full list: [catalogs/plugin-skills.md](catalogs/plugin-skills.md). Plugin origins and licences: [catalogs/installed-plugins.md](catalogs/installed-plugins.md) and [LICENSING.md](LICENSING.md).

Gmail, Google Calendar, Outlook, and Finance are installed as connectors and register **no** skills.

### Present in a runtime catalogue, not on disk here

`canvas` and `consumer-pages` were visible in a runtime skill list during inventory, but no local body or cache entry was found. `canvas` also appears in fleet chats as a skill to load. Treat these as references only.

## Evidenced use (narrow)

A local chat index and agent personas were checked for skill references. Most available skills had **no** evidence in that pass. This is **not** a complete history of every invocation.

Evidenced at higher confidence (persona tells the agent to follow or apply the skill):

- `code-changes` (managed)
- `routines` (managed)
- `poteto-mode` (pstack plugin) — named as the standard for coding bots

Also mentioned in chats as “&lt;name&gt; skill” or “load the …”:

- `routines`, `scheduling`, `flight-booking` (managed)
- `canvas` (no local body)
- `pstack` (plugin name / setup, not necessarily the `setup-pstack` skill)

Mentions of the same words as ordinary language, or as nicknames for routines (for example a “job-search pulse”), were **not** counted as skill use.

## What this draft does not include

- Skill recipe bodies (managed or plugin)
- Agent personas, transcripts, routines definitions, or internal IDs
- Installed custom skills (still none). Research suggestions for new skills are tracked separately in [RECOMMENDATIONS.md](RECOMMENDATIONS.md) as `PROPOSED` / `NOT_INSTALLED` only

## Limitations

- Inventory is local and read-only. Upstream licences were not re-checked on the web in this pass.
- Routine definitions were not stored in the local agent automation folders, so routine-to-skill mapping is incomplete.
- Chat evidence covers the local search index only, not a complete history of every invocation.
- Two Vercel plugin installs overlap; do not double-count their shared names.

## Repository layout

```
.
├── README.md
├── CONTRIBUTING.md
├── LICENSE                 ← MIT for repository-original material
├── INVENTORY.md
├── RECOMMENDATIONS.md
├── SOURCES.md
├── LICENSING.md
├── PROVENANCE.md
├── catalogs/
├── recommendations/
├── templates/SKILL.template.md
├── custom-skills/
│   ├── README.md
│   └── _examples/          ← labelled examples only
├── .github/                ← issue forms + PR template
└── scripts/validate_catalog.py
```
