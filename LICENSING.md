# Licensing and redistribution notes

Drafted 21 Nov 2026, Asia/Hong_Kong (UTC+8) from **local install metadata only** (no web licence re-check in this pass).

This file records what local plugin manifests and LICENSE files declared. It does **not** grant rights, claim ownership of third-party or platform material, or add a licence covering those works.

## Policy for this repository draft

- This draft is an inventory and a set of pointers.
- **Do not copy** platform-managed skill bodies into the repo.
- **Do not copy** plugin skill bodies into the repo in this pass, even when a local manifest declares MIT or Apache-2.0. Those licences may allow redistribution, but this draft records origin and licence and leaves vendoring to a later, explicit decision.
- When a local manifest or README named an upstream URL, that URL is listed so the repo can link rather than vendor.
- Inventory markdown and machine-readable catalogues in this repository describe availability; they are not a redistribution of the underlying skill recipes.

## Per-plugin summary

| Plugin | Declared or detected licence | Upstream (from local files) | Redistribute bodies in this draft? |
|---|---|---|---|
| Cloudinary | MIT (plugin.json; no LICENSE file in install root) | https://github.com/cloudinary-devs/cloudinary-plugin | No |
| Context.dev | MIT (plugin.json and LICENSE file) | https://github.com/context-dot-dev/cursor-plugin | No |
| Datadog | Apache-2.0 (LICENSE file; not declared in plugin.json). NOTICE: Datadog, Inc. | https://github.com/datadog-labs/cursor-plugin.git | No |
| Figma | Unspecified OSI licence. README binds use to [Figma Developer Terms](https://www.figma.com/legal/developer-terms/) | https://github.com/figma/mcp-server-guide | No |
| Firecrawl | MIT | https://github.com/firecrawl/firecrawl-cursor-plugin | No |
| Hugging Face Skills | Apache-2.0 | https://github.com/huggingface/skills | No |
| Notion workspace | Unverified (no license field, no LICENSE file) | README install id `makenotion/cursor-notion-plugin` only | No |
| Parallel | MIT | https://github.com/parallel-web/parallel-cursor-plugin | No |
| Vercel (cursor-public install) | Apache-2.0 (plugin.json and LICENSE file) | https://github.com/vercel/vercel-plugin | No |
| Vercel (vercel-plugin install) | Apache-2.0 (plugin.json; no LICENSE file in this install root) | https://github.com/vercel/vercel-plugin | No |
| pstack | MIT | https://github.com/cursor/plugins (tree/main/pstack per homepage) | No |
| Gmail, Google Calendar, Google Docs, Google Drive, Google Slides, Outlook, Finance | MIT | https://github.com/cursor/plugins (paths vary; Finance homepage also cites https://grok.com/connectors) | No skill bodies (these are mostly connectors; Docs/Drive/Slides each register one skill) |

## Platform-managed skills

Treated as product-managed recipes, not as user-owned files. Catalogue only.

## Custom skills

None were present in the shared library, so no custom-skill licence is recorded.

## Catalogue vs installation

Having this repository on disk (or installing it as a Git dependency) does **not** install managed or plugin skills into an agent. Skills are provided by the platform and by the plugins listed above. See [PROVENANCE.md](PROVENANCE.md).
