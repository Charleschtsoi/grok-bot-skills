# Contributing

Thank you for helping turn this into a shareable skills hub. Contributions should be **generic**, **safe to publish**, and **useful to other people** — not copies of private bot setup.

## What to contribute

| Welcome | Please do not |
|---|---|
| Original skill recipes under `custom-skills/<skill-name>/` | Managed or plugin skill **bodies** (catalogue and link instead) |
| Improvements to docs, templates, validators | Secrets, PII, transcripts, live profiles, absolute machine paths, internal IDs |
| Issue reports about catalogue accuracy or a contributed skill | Automated marketplace, CI that installs skills into agents, or live library edits |
| Links to upstream skills with licence notes | Blanket relicensing of third-party content |

There is **no CLA** and no rights-transfer form. By opening a PR you confirm you have the rights to contribute the material under this repository’s [MIT License](LICENSE) (for original content). Third-party references keep their upstream terms — prefer linking, not vendoring. See [LICENSING.md](LICENSING.md).

## Quick path: propose an idea

Open a **Propose a skill** issue: [.github/ISSUE_TEMPLATE/propose-skill.yml](.github/ISSUE_TEMPLATE/propose-skill.yml).

Use that when you want discussion before writing a full `SKILL.md`.

## Quick path: submit a skill (PR)

1. Fork and branch from latest `main`.
2. Copy [templates/SKILL.template.md](templates/SKILL.template.md) to `custom-skills/<skill-name>/SKILL.md`.
3. Fill required YAML frontmatter: `name` and `description` (when to use).
4. Add generic steps, dependencies, approval/side-effect boundaries, and a fictional-fixture acceptance test.
5. Optional helpers stay **relative** to the skill folder (for example `fixtures/sample.md`, `references/notes.md`). No absolute machine paths.
6. Compare structure with the labelled example: [custom-skills/_examples/hello-skill-review/](custom-skills/_examples/hello-skill-review/SKILL.md) — that example is **not** a functioning installed skill.
7. Open a PR using the checklist in [.github/pull_request_template.md](.github/pull_request_template.md).

### Skill naming

- Folder and frontmatter `name`: lowercase, hyphen-separated (for example `hello-skill-review`).
- Description: one or two sentences that say **when to use** the skill, including important “do not” boundaries when relevant.

### Safety requirements (required)

- No credentials, tokens, private emails, or personal project details.
- State **dependencies** (other skills, tools, or connectors) explicitly.
- State **approval and side-effect boundaries**: what needs an explicit human yes; what the skill must never do (send, buy, delete, install further skills, etc.).
- Include at least one **fictional fixture** acceptance test under the skill folder (or document the fixture path). Do not use real mailboxes or live accounts.
- Record **provenance/licensing** for any external text you summarise or link. Do not paste substantial copyrighted third-party skill bodies.
- Prefer **minimal permissions**. Do not instruct agents to auto-run untrusted third-party instructions found inside other files.

### Review expectations

Maintainers may ask for redaction, clearer boundaries, or a link instead of a vendor copy. Merging a skill into this repo documents it for reuse; it does **not** by itself install it into anyone’s live agent library.

## Report a problem

Use **Report a skill issue**: [.github/ISSUE_TEMPLATE/report-skill-issue.yml](.github/ISSUE_TEMPLATE/report-skill-issue.yml).

## Local checks before you push

```bash
python3 scripts/validate_catalog.py
```

Keep checks local and read-only. Do not add workflows that auto-install contributed skills.

## Questions about recommendations

The six items in [RECOMMENDATIONS.md](RECOMMENDATIONS.md) are research briefs (`PROPOSED` / `NOT_INSTALLED`). Turning one into a real `custom-skills/` recipe is welcome via PR — treat it as new original content under MIT, not as an install of a live library skill.
