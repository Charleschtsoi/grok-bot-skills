# 6. work-evidence-pack

| Field | Value |
|---|---|
| Priority | 6 |
| Kind | Original skill to author |
| Status | `PROPOSED` / `NOT_INSTALLED` |
| Proposed `name` | `work-evidence-pack` |
| Effort | Small to medium |

## Proposed description (for a later SKILL.md)

Use when assembling a public-safe evidence pack for a piece of work so a person can evaluate it: what was produced, which sources were used, what the human reviewed or changed, and what remains unverified. Redact personal data. Do not invent results, inflate authorship, or pack private chats.

## Existing overlap and the concrete gap

- pstack `show-me-your-work` keeps a local decision-trail TSV for long-running *coding* work. It is not a packager for a shareable evaluation artefact (portfolio piece, review memo, or assignment appendix) and it is easy to over-collect.
- Notion `knowledge-capture` / `research-documentation` are workspace-specific writing workflows, not an evidence standard.
- Hugging Face evaluation skills target *model* evals, not human work products.

The gap is a small, repeatable **evidence pack** for “what was made, on what basis, and what a reviewer can check,” including AI assistance, without dumping private transcripts.

## Why it is valuable

Evaluation, whether for a personal portfolio or a formal review, is weaker when artefacts cannot be tied to sources, dates, and human sign-off. Public guidance on agent evidence also stresses that an identifier on a file is not provenance, and that evidence should survive after an agent is retired.

## Evidence and sources

Retrieved 21 Nov 2026, Asia/Hong_Kong (UTC+8).

- [NIST agent identity tenets](https://www.nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems) (27 October 2026): evidence should cover what the agent creates as well as what it does, including documents and specific artefact versions; an identifier attached to an artefact does not prove provenance and must bind the artefact to its producer; “not established” is a valid outcome when a claim cannot be verified; historical evidence should remain checkable after retirement.
- [ICO Tech Futures: Agentic AI](https://ico.org.uk/about-the-ico/research-reports-impact-and-evaluation/research-and-reports/technology-and-innovation/tech-horizons-and-ico-tech-futures/ico-tech-futures-agentic-ai/) (with the [8 January 2026](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/01/ai-ll-get-that/) announcement) lists “ways to benchmark and evaluate agentic systems” among innovation opportunities, and stresses transparency challenges when systems become more complex. This skill is a lightweight evaluation aid, not an ICO-mandated record.
- [Algorithmic Transparency Recording Standard v2.1](https://www.gov.uk/government/publications/algorithmic-transparency-data-standard/algorithmic-transparency-recording-standard-v21) (GOV.UK page retrieved 21 Nov 2026, Asia/Hong_Kong (UTC+8); the page header showed “Updated 2 December 2021”) is a **UK public-sector** transparency template (purpose, use, data, risks). It does **not** automatically apply to a personal portfolio. It is cited only as an optional, openly licensed pattern (Open Government Licence v3.0, as stated on that page) for describing purpose and limitations — not as a compliance obligation.

## Dependencies

- May sit beside `show-me-your-work` for engineering tasks: that skill can feed a trail; this skill packages a redacted, shareable subset.
- `source-control` / `code-changes` when the artefact is a repository change (link the PR, do not paste secrets).
- User chooses what may be published. Default is redact-first.

## Risks and permission boundaries

- **No private personas, chats, or incident timelines** in the pack.
- **No inflated authorship.** If an agent drafted text or code, say so; if a human rewrote it, say so; if a source was not checked, write “not established.”
- **Licence and quotation.** Do not paste substantial third-party copyrighted text into a public pack; summarise and link.
- **Lower priority** than the five governance skills above; do not let this expand into a general writing or design skill (those already exist in pstack and document plugins).

## Acceptance test (executable, fictional fixture)

Fixture: `fixtures/work-evidence-pack/sample-artefact.md` (a short made-up report) plus `sources.md` with two URLs and one unverifiable claim labelled as such, and a planted private sentence that must be dropped.

The test passes if:

1. Frontmatter `name` is `work-evidence-pack`.
2. The output pack lists the artefact, date (or “unknown”), sources that were provided, the unverifiable claim marked “not established,” and a human-review field (may be “pending”).
3. The planted private sentence is absent from the pack.
4. No network side effects are required beyond what the fixture already contains (the skill must work from supplied sources; it must not scrape a live mailbox or private drive “to be helpful”).
5. The pack states clearly what the agent did versus what remains for the human reviewer.

## Outline for a later SKILL.md (not the skill itself)

When to use; required fields (artefact, purpose, sources, human review, gaps); redaction rules; “not established”; relationship to `show-me-your-work`; stop.
