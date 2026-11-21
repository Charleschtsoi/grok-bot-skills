# Licensing and redistribution notes

Updated 21 Nov 2026 for the community skills-hub direction. Plugin licence rows below still come from **local install metadata** recorded in the inventory pass (not a fresh web re-check of every upstream).

## What the MIT License covers

This repository’s [LICENSE](LICENSE) (MIT, Copyright © 2026 Charleschtsoi) applies to **repository-original** material, including:

- Documentation authored for this repo (`README.md`, `CONTRIBUTING.md`, inventory/recommendation prose as published here, templates, examples, scripts)
- Future **original** skill recipes contributed under `custom-skills/` (unless a file explicitly says otherwise)
- Issue/PR templates and other repo scaffolding created here

You are free to use, modify, and redistribute that material under MIT terms.

There is **no CLA**. Contributors keep their copyright; by contributing original content they offer it under the same MIT terms. Contributors must have the rights to do so.

## What MIT here does **not** cover

| Material | Treatment |
|---|---|
| Platform-managed skill **bodies** | Product-managed. Not in this repo. Catalogue lists names/descriptions as **references only** — not a licence grant and not a relicense. |
| Plugin / third-party skill **bodies** | Remain under their upstream licences. Prefer **link**, do not vendor in this pass. |
| Upstream plugin source trees | Keep original licences (see table). Do not blanket-relicense. |
| Copied substantial third-party skill text | Not allowed as a “MIT contribution.” Summarise and link; if an explicit later decision vendors a work, keep its original licence notice. |
| External collections (e.g. [`anthropics/skills`](https://github.com/anthropics/skills)) | **Licences vary by folder.** Review individual terms. |

Catalogue markdown/JSON describe **availability**. They are not a redistribution of the underlying recipes and do not claim copyright ownership of managed or third-party skills.

## Policy for contributions and catalogues

- **Do not copy** platform-managed skill bodies into the repo.
- **Do not copy** plugin skill bodies by default, even when a local manifest declares MIT or Apache-2.0. Record origin and licence; leave vendoring to an explicit, per-work decision.
- When a local manifest or README named an upstream URL, that URL is listed so the repo can link rather than vendor.
- Proposed skills in [RECOMMENDATIONS.md](RECOMMENDATIONS.md) are briefs only (`NOT_INSTALLED`). When authored as originals under `custom-skills/`, they fall under repo MIT unless stated otherwise.
- Safety: review and verify locally before trusting any contributed skill. Prose cannot enforce platform controls.

## Per-plugin summary (inventory metadata)

| Plugin | Declared or detected licence | Upstream (from local files) | Redistribute bodies in this repo? |
|---|---|---|---|
| Cloudinary | MIT (plugin.json; no LICENSE file in install root) | https://github.com/cloudinary-devs/cloudinary-plugin | No (link only) |
| Context.dev | MIT (plugin.json and LICENSE file) | https://github.com/context-dot-dev/cursor-plugin | No (link only) |
| Datadog | Apache-2.0 (LICENSE file; not declared in plugin.json). NOTICE: Datadog, Inc. | https://github.com/datadog-labs/cursor-plugin.git | No (link only) |
| Figma | Unspecified OSI licence. README binds use to [Figma Developer Terms](https://www.figma.com/legal/developer-terms/) | https://github.com/figma/mcp-server-guide | No (link only) |
| Firecrawl | MIT | https://github.com/firecrawl/firecrawl-cursor-plugin | No (link only) |
| Hugging Face Skills | Apache-2.0 | https://github.com/huggingface/skills | No (link only) |
| Notion workspace | Unverified (no license field, no LICENSE file) | README install id `makenotion/cursor-notion-plugin` only | No (link only) |
| Parallel | MIT | https://github.com/parallel-web/parallel-cursor-plugin | No (link only) |
| Vercel (cursor-public install) | Apache-2.0 (plugin.json and LICENSE file) | https://github.com/vercel/vercel-plugin | No (link only) |
| Vercel (vercel-plugin install) | Apache-2.0 (plugin.json; no LICENSE file in this install root) | https://github.com/vercel/vercel-plugin | No (link only) |
| pstack | MIT | https://github.com/cursor/plugins (tree/main/pstack per homepage) | No (link only) |
| Gmail, Google Calendar, Google Docs, Google Drive, Google Slides, Outlook, Finance | MIT | https://github.com/cursor/plugins (paths vary; Finance homepage also cites https://grok.com/connectors) | No skill bodies for connectors without skills; Docs/Drive/Slides each register one skill — still link only |

## Platform-managed skills

Treated as product-managed recipes, not as user-owned files. Catalogue only.

## Catalogue vs installation

Having this repository on disk (or installing it as a Git dependency) does **not** install managed, plugin, or custom skills into an agent. See [PROVENANCE.md](PROVENANCE.md) and [README.md](README.md).
