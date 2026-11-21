---
name: your-skill-name
description: >
  When to use this skill in one or two sentences, including important
  do-not boundaries. Replace this text before submitting.
license: MIT
---

# your-skill-name

> Template only. Copy to `custom-skills/<skill-name>/SKILL.md` and fill in.
> This file is **not** an installed or functioning skill by itself.

## When to use

- …

## When not to use

- …

## Dependencies

List other skills, tools, or connectors this assumes. Write `None` if none.

- …

## Approval and side-effect boundaries

- Requires an explicit human yes before: …
- Must never: send mail, make purchases, delete data, install further skills, or change live agent settings unless the human clearly approved that step in-session.
- This skill cannot enforce platform approval gates.

## Steps

1. …
2. …
3. Stop and report. Do not continue into live side effects without approval.

## Helper files (relative only)

Keep helpers next to this skill, for example:

- `fixtures/sample-case.md` — fictional acceptance fixture
- `references/notes.md` — optional short notes

Do not use absolute machine paths, private IDs, credentials, or personal data.

## Acceptance test (fictional fixture)

Using only `fixtures/sample-case.md` (create it in your PR):

1. Frontmatter `name` matches the folder name.
2. A dry-run produces the expected memo/output fields you define.
3. Planted fake secrets in the fixture do not appear in the output.
4. No send, purchase, delete, or install tools are invoked.

## Provenance and licensing

- Original content in this skill: MIT (see repository [LICENSE](../LICENSE)).
- External sources summarised or linked (if any): list URL + licence note; do not paste substantial third-party skill bodies.
