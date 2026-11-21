# custom-skills

Home for **original**, reusable skill recipes contributed to this hub.

## Current state

| Kind | Count |
|---|---:|
| Installable / published original skills | **0** |
| Contributor example (not functioning, not installed) | 1 — [`_examples/hello-skill-review/`](_examples/hello-skill-review/SKILL.md) |

At inventory time the shared live library also had no custom skills. Proposed research briefs under [`../recommendations/`](../recommendations/README.md) remain `PROPOSED` / `NOT_INSTALLED` until someone authors a real recipe here.

## Layout

```
custom-skills/
  README.md                 ← this file
  _examples/                ← labelled examples only (not live skills)
    hello-skill-review/
  <your-skill-name>/        ← future contributions
    SKILL.md
    fixtures/               ← fictional acceptance fixtures
    references/             ← optional relative helpers
```

Copy [`../templates/SKILL.template.md`](../templates/SKILL.template.md) when starting a contribution. Follow [`../CONTRIBUTING.md`](../CONTRIBUTING.md).

## Important

- Managed and plugin skills are catalogued under [`../catalogs/`](../catalogs/README.md) and are **not** vendored here.
- Putting a skill in this folder documents it for reuse under MIT; it does **not** by itself install it into an agent.
- Review and verify locally before trusting any contributed skill.
