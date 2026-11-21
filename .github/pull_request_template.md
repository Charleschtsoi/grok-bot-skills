## Summary

<!-- What does this PR add or change? Keep it short. -->

## Type of change

- [ ] Documentation / catalogue / recommendations only
- [ ] New original skill under `custom-skills/<name>/` (not an install into a live library)
- [ ] Template, example, or contributor tooling
- [ ] Fix (typo, link, licence note, safety)

## Skill submissions (if applicable)

- [ ] `SKILL.md` has YAML frontmatter with `name` and `description` (when to use)
- [ ] Steps are generic; no private IDs, paths, credentials, or personal data
- [ ] Dependencies listed; approval and side-effect boundaries are explicit
- [ ] Fictional-fixture acceptance test included (relative path)
- [ ] Provenance/licensing noted; third-party bodies linked, not vendored
- [ ] Example under `_examples/` was used only as a model (if relevant)

## Safety and permissions

- [ ] Minimal permissions; does not instruct auto-running untrusted third-party instructions
- [ ] Does not claim prose can enforce platform approval gates
- [ ] No secrets or PII in the diff

## Licence

- [ ] Original content offered under the repository MIT License
- [ ] No blanket relicense of managed/plugin/upstream material

## Checks

```bash
python3 scripts/validate_catalog.py
```

- [ ] Local validator passes (or explain why not)

## Notes for reviewers

<!-- Optional -->
