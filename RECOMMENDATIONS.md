# Recommended skill additions

Generated 21 Nov 2026, Asia/Hong_Kong (UTC+8). All six items are **`PROPOSED` / `NOT_INSTALLED`**. They are recommendations for later authoring into this repository, not live library changes, not executable skills, and not installs.

Research package source archive sha256: `999df77985e4763c1b7fa0391e824e49c65c3cd7fdbabee774efcd580421b901`.

## How this list was built

The 21 Nov 2026 inventory found **0** custom skills, **71** managed platform skills, and **210** plugin skill entries (**191** unique names). The remaining gaps that motivated this shortlist are fleet work: reviewing outbound actions after something goes wrong, grouping similar agents and spotting overlap, and retiring unused agents with a handover — plus practical reviews of privacy/permissions, third-party skill provenance, and evidence for evaluating work products.

Existing managed skills already cover the *moment of action* for mail and payments (`send-on-behalf`, `agent-email`, `purchases`, `in-chat-forms`) and the *creation* of recurring jobs or reusable recipes (`routines`, `skill-authoring`). Plugin pstack already has workflow and review skills (including decision-trail and catch-up style workflows). This shortlist does not propose duplicates of those.

No recommendation claims that a skill file can enforce a platform approval gate. Platform controls, Auto-review settings, and connector permissions stay authoritative.

## Shortlist (priority order)

| Priority | Proposed skill | Kind | Status | Why it is first |
|---:|---|---|---|---|
| 1 | [outbound-approval-review](recommendations/01-outbound-approval-review.md) | Original skill to author | PROPOSED / NOT_INSTALLED | Highest-leverage gap: post-event review and regression checks for high-impact outbound actions |
| 2 | [agent-department-mapping](recommendations/02-agent-department-mapping.md) | Original skill to author | PROPOSED / NOT_INSTALLED | Needed before retirement or overlap decisions; gives the fleet a shared map |
| 3 | [safe-agent-retirement](recommendations/03-safe-agent-retirement.md) | Original skill to author | PROPOSED / NOT_INSTALLED | Completes the lifecycle once overlap or disuse is identified; requires an explicit yes before any retire step |
| 4 | [external-skill-provenance-review](recommendations/04-external-skill-provenance-review.md) | Original skill to author | PROPOSED / NOT_INSTALLED | This repo will attract third-party skill ideas; review before install, do not vendor bodies by default |
| 5 | [fleet-privacy-permission-review](recommendations/05-fleet-privacy-permission-review.md) | Original skill to author | PROPOSED / NOT_INSTALLED | Periodic least-privilege and personal-data review; not a substitute for legal advice |
| 6 | [work-evidence-pack](recommendations/06-work-evidence-pack.md) | Original skill to author | PROPOSED / NOT_INSTALLED | Useful evaluation aid; lower urgency than the governance skills above |

## Kind: original versus install/reuse

Every shortlisted item is an **original skill to author** in [`custom-skills/`](custom-skills/README.md) later, under this repo’s own terms, after user approval.

Searches of official Agent Skills material, Cursor plugin docs, and the public [`anthropics/skills`](https://github.com/anthropics/skills) repository did not turn up a ready-made skill that does fleet department mapping, retirement handover, post-event approval review, or a skill-supply-chain review for this product. Official document-oriented example skills in that repository overlap existing managed slide/document workflows and Google Docs/Drive/Slides plugin skills and were **not** shortlisted. Licences in `anthropics/skills` **vary by folder**; review individual folder terms before any reuse (do not assume a single repo-wide Apache-2.0 grant).

Where a public framework exists (NIST AI RMF, OWASP Agentic Skills Top 10, UK Government Security retirement guidance, AWS Agentic AI Lens, ICO Tech Futures), the recommendation is to **link and apply** it inside an original skill, not to copy the framework body into the repo.

## Explicit non-goals

- Do not auto-install or write these into the live Grok Bot skill library from this draft.
- Do not create monitors, routines, or standing healthchecks as part of accepting these recommendations (pstack-style healthchecks and the managed `routines` / `usage-review` skills already exist).
- Do not copy licensed third-party skill or checklist bodies into the repo in this pass.
- Do not promise that a skill can block a send, purchase, or delete that the platform would otherwise allow.
- Do not choose a blanket copyright licence for third-party material in this pass.

## Considered and not recommended now

| Idea | Decision |
|---|---|
| Install Anthropic example document skills (`docx`, `pdf`, `pptx`, `xlsx`) | Overlaps managed `slides` / `slides-executor` and Google Docs/Drive/Slides plugin skills. Upstream README says examples are for demonstration/education and may differ from production behaviour. Folder licences vary — review each skill’s terms before any reuse. |
| A general “fleet healthcheck” or transcript-audit skill | Too close to existing pstack review/catch-up workflows and to usage or routine skills already catalogued. |
| Tightening `send-on-behalf` by rewriting it in this repo | That skill is platform-managed. A parallel “always ask first” recipe would be a duplicate and still could not enforce the gate. The gap is *after-the-fact review and regression checks*. |
| Vendoring the OWASP Agentic Skills Top 10 checklist | Useful as a linked reference (CC BY-SA 4.0). The project was still in public review / incubator material when retrieved. Link, do not copy the white paper or checklist into this repo. |

## Limitations of this research pass

- Supporting pages were retrieved and checked with direct URL fetches on 21 Nov 2026, Asia/Hong_Kong (UTC+8), where extraction succeeded. Some publisher pages could not be extracted in this pass; those URLs are listed in [SOURCES.md](SOURCES.md) as unverified and are not used as evidence.
- Official Hong Kong PCPD pages and PDFs on AI and agentic AI were located by search but could not be extracted here (edge-bot challenge returned an interstitial). They are listed in [SOURCES.md](SOURCES.md) as unverified-in-this-pass, not used as evidence.
- The OWASP Agentic Skills Top 10 site described a v1 public review / 2026 edition. Treat it as a current framework, not a frozen standard.
- Chat and persona evidence from the inventory pass is used only at the level of “which catalogue skills already exist.” No private personas, timelines, or incident details are included here.
- Recommendations are not legal, compliance, or security-audit conclusions.
