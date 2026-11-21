# 1. outbound-approval-review

| Field | Value |
|---|---|
| Priority | 1 |
| Kind | Original skill to author |
| Status | `PROPOSED` / `NOT_INSTALLED` |
| Proposed `name` | `outbound-approval-review` |
| Effort | Medium |

## Proposed description (for a later SKILL.md)

Use when reviewing a high-impact outbound action (email, chat message, post, purchase, or similar send) that may have gone out without the intended human approval, or when designing regression checks for that class of action. Produce a redacted review memo and a proposed check list. Do not send, resend, or buy anything. Do not claim this skill can enforce app-level approval gates.

## Existing overlap and the concrete gap

Managed skills already describe *how to act at send time*:

- `send-on-behalf` — writing or sending mail or messages as the user on an outside platform
- `agent-email` — the bot’s own inbox and send path
- `purchases` — cards, checkout, and spend
- `in-chat-forms` — collecting secrets or payment fields in chat

Those skills do not provide a repeatable *after-the-fact* review: reconstruct what was asked for, what actually left the system, which approval path was used or skipped, what residual risk remains, and which *regression checks* to propose (persona wording, Auto-review reminders, dry-run fixtures). A second copy of “always ask before sending” would be a duplicate and still would not bind the platform.

## Why it is valuable

High-impact outbound actions are exactly where human oversight is supposed to be defined and later reassessed. A review skill gives the fleet a standard memo and a test you can re-run, without turning the skill into a hidden send path.

## Evidence and sources

Retrieved 21 Nov 2026, Asia/Hong_Kong (UTC+8).

- [NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1) (January 2023; landing page also dated [26 January 2023](https://www.nist.gov/itl/ai-risk-management-framework)) includes MAP 3.5: processes for human oversight are defined, assessed, and documented. The [AI RMF Playbook MAP section](https://airc.nist.gov/airmf-resources/playbook/map/) repeats that subcategory and notes that oversight effectiveness should be evaluated, especially in higher-stakes settings.
- [NIST, “Design Tenets for Agent Identity Management Systems”](https://www.nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems) (27 October 2026) describes human-in-the-loop triggers for sensitive actions, warns about consent fatigue (habitual approvals), and states that without enforced triggers a malfunctioning agent could take irreversible actions. The same note is the reason this skill **must not** pretend that prose is that enforcement.
- [ICO, “Tech Futures: Agentic AI”](https://ico.org.uk/about-the-ico/research-reports-impact-and-evaluation/research-and-reports/technology-and-innovation/tech-horizons-and-ico-tech-futures/ico-tech-futures-agentic-ai/) and the ICO news item dated [8 January 2026](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/01/ai-ll-get-that/): organisations remain responsible for agentic processing; design choices about authorised actions, access, and the ability to review or stop activity matter. Poorly implemented systems may have no measures to stop activity or control further sharing.

## Dependencies

- Related (do not replace): `send-on-behalf`, `agent-email`, `purchases`, `in-chat-forms`.
- Authoring later: `skill-authoring` and the [Agent Skills specification](https://agentskills.io/specification).
- Platform settings (Auto-review, connector send permissions) stay outside the skill. The skill may *recommend* a setting change; it must not silently change one.

## Risks and permission boundaries

- **Non-enforcement:** The skill can recommend regression checks. It cannot promise to block a send or payment the product would otherwise allow.
- **Scope:** Read and report only. No send, resend, reply-all, purchase, or credential use.
- **Privacy:** Review memos must redact message bodies, addresses, and other personal data down to what is needed to learn the failure mode. Use fictional or heavily redacted fixtures in the repo.
- **Consent fatigue:** Do not recommend a new approval prompt on every low-risk action; keep gates risk-based, in line with the NIST tenet.

## Acceptance test (executable, fictional fixture)

Use only a synthetic fixture, for example `fixtures/outbound-approval-review/sample-case.md`, that describes an example bot drafting an external message. No live mailboxes, no real recipients.

The test passes if, in one run after the skill is authored (still not installed in the live library unless the user later says so):

1. The skill directory is `outbound-approval-review/` and `SKILL.md` frontmatter `name` is `outbound-approval-review`, matching [Agent Skills](https://agentskills.io/specification) name rules, and the description states that the skill cannot enforce app-level approval gates.
2. A dry-run on the fixture produces a memo with at least: requested action, what would have left the system, approval path used or skipped, residual risk, and proposed regression checks.
3. The memo contains no raw fixture “recipient” addresses or message body; those are redacted or summarised.
4. The run does not call send, purchase, or routine-create tools, and does not write into the live skill library.
5. At least one proposed regression check is itself executable on the fixture (for example: “given this prompt, the agent outputs a draft and stops, and the memo records that no send tool was used”).

## Outline for a later SKILL.md (not the skill itself)

When to load; non-enforcement warning; intake (what happened, which channel, what approval was expected); reconstruct from available logs without over-collecting; compare expected vs actual path; propose regression checks; stop and ask before any operational change.
