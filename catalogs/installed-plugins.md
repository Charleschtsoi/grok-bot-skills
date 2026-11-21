# Installed plugins

Licence data is taken from local plugin manifests and LICENSE files in the plugin install cache. Repositories are linked when those local files named them. Skill bodies are not vendored here. See [../LICENSING.md](../LICENSING.md).

| Plugin | Version | Registered skills | Licence | Upstream | Notes |
|---|---|---:|---|---|---|
| notion-workspace (`notion-workspace`) | 0.1.0 | 14 | unspecified | — | No license field in plugin.json and no LICENSE file in the install. README describes an official Cursor plugin and gives the marketplace/GitHub install id makenotion/cursor-notion-plugin. License is unverified from local files. Do not redistribute skill bodies. README install id: `makenotion/cursor-notion-plugin`. |
| vercel (`vercel`) | 0.53.0 | 33 | Apache-2.0 | https://github.com/vercel/vercel-plugin |  |
| Figma (`figma`) | 2.2.211 | 17 | unspecified | https://github.com/figma/mcp-server-guide | No OSI license in plugin.json or a LICENSE file. README states that use of the Figma MCP server and related resources (including these skills) is subject to the Figma Developer Terms (https://www.figma.com/legal/developer-terms/). Do not redistribute skill bodies. |
| Parallel (`parallel`) | 0.2.1 | 6 | MIT | https://github.com/parallel-web/parallel-cursor-plugin |  |
| huggingface-skills (`huggingface-skills`) | 1.0.8 | 18 | Apache-2.0 | https://github.com/huggingface/skills |  |
| Firecrawl (`firecrawl`) | 0.12.0 | 19 | MIT | https://github.com/firecrawl/firecrawl-cursor-plugin |  |
| datadog (`datadog`) | 0.7.19 | 4 | Apache-2.0 | https://github.com/datadog-labs/cursor-plugin.git | No license field in plugin.json; LICENSE file is Apache License 2.0; NOTICE names Datadog, Inc. |
| Cloudinary (`cloudinary`) | 1.1.1 | 2 | MIT | https://github.com/cloudinary-devs/cloudinary-plugin | MIT declared in plugin.json; no LICENSE file found in the install root. |
| pstack (`pstack`) | 0.15.46 | 58 | MIT | https://github.com/cursor/plugins |  |
| vercel (`vercel-plugin`) | 0.40.0 | 25 | Apache-2.0 | https://github.com/vercel/vercel-plugin | Apache-2.0 declared in plugin.json; no LICENSE file found in this install root (the cursor-public/vercel install of the same upstream does include an Apache-2.0 LICENSE file). |
| Gmail (`gmail`) | 1.0.0 | 0 | MIT | https://github.com/cursor/plugins | Connector only; no bundled skills. |
| Google Calendar (`google-calendar`) | 1.0.0 | 0 | MIT | https://github.com/cursor/plugins | Connector only; no bundled skills. |
| Google Docs (`google-docs`) | 1.1.0 | 1 | MIT | https://github.com/cursor/plugins |  |
| Google Drive (`google-drive`) | 1.0.1 | 1 | MIT | https://github.com/cursor/plugins |  |
| Google Slides (`google-slides`) | 1.1.0 | 1 | MIT | https://github.com/cursor/plugins |  |
| Context.dev (`context-dev`) | 2.1.0 | 11 | MIT | https://github.com/context-dot-dev/cursor-plugin |  |
| Outlook (`outlook`) | 1.0.0 | 0 | MIT | https://github.com/cursor/plugins | Connector only; no bundled skills. |
| Finance (`finance`) | 1.1.2 | 0 | MIT | https://github.com/cursor/plugins | Connector only; no bundled skills. |

Gmail, Google Calendar, Google Docs, Google Drive, Google Slides, Outlook, Finance, and pstack local manifests point at `https://github.com/cursor/plugins` (paths under that monorepo vary). Vercel’s two installs share upstream `https://github.com/vercel/vercel-plugin`.

