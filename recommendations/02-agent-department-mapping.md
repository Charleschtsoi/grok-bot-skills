# 2. agent-department-mapping

| Field | Value |
|---|---|
| Priority | 2 |
| Kind | Original skill to author |
| Status | `PROPOSED` / `NOT_INSTALLED` |
| Proposed `name` | `agent-department-mapping` |
| Effort | Medium |

## Proposed description (for a later SKILL.md)

Use when grouping agents into departments, checking for overlapping jobs, or preparing a fleet map before creating, merging, or retiring a bot. Produce a catalogue table (role, department, overlaps, suggested owner) and questions for the user. Do not rename, merge, hide, or retire any agent without an explicit yes.

## Existing overlap and the concrete gap

The inventory has no skill for fleet structure. Nearby but different:

- `team-bot-links` — adding a shared team bot the user does not yet have
- `export-bot-template` — sharing a bot’s setup
- `usage-review` — plan, limits, and cost, not role overlap
- `routines` — creating or changing scheduled jobs, not mapping who should own them

Those do not produce a department map or a “search for an existing overlap before building another bot” review.

## Why it is valuable

Once a fleet is more than a handful of agents, duplicate jobs and unclear ownership are a documented operational risk. A shared map is the input to retirement and to “do we already have a bot for this?” decisions.

## Evidence and sources

Retrieved 21 Nov 2026, Asia/Hong_Kong (UTC+8).

- [AWS Well-Architected Agentic AI Lens, AGENTOPS03-BP04: Implement organizational agent portfolio management and governance at scale](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops03-bp04.html). A catalogue should record owner, business domain, lifecycle, capabilities, and dependencies. Teams should search for existing capability before building. Quarterly reviews should look at utilisation, cost efficiency, redundancy, and health. Anti-patterns include team-local registries, building without a search-before-build step, and changing or retiring agents without notifying dependents. (AWS-specific registry products in that page are optional illustrations, not dependencies for this skill.)
- The same page’s desired outcome — a current view of every agent, owner, capabilities, and business value — is the shape of the memo this skill should emit, adapted to a personal or small-fleet catalogue rather than an enterprise registry.

## Dependencies

- Input is a user-approved, public-safe list of agent *roles* (or a redacted inventory). Do not publish private personas into the repo or the memo.
- May precede `safe-agent-retirement` when overlap or disuse is flagged.
- `usage-review` may inform cost comments but is not a substitute for a role map.

## Risks and permission boundaries

- **No silent org changes:** Mapping only. No rename, merge, delete, or persona rewrite without a later, explicit yes (handled by the retirement skill or by the user).
- **Do not invent ownership:** Skills are globally shared. The map may record *which role uses* a skill; it must not assign skill ownership to one agent.
- **Privacy:** Use role titles, not private instructions, personal projects, or chat excerpts.
- **False overlaps:** Similar names are not the same job. The skill should list evidence for an overlap and ask before recommending consolidation.

## Acceptance test (executable, fictional fixture)

Fixture: `fixtures/agent-department-mapping/sample-fleet.md` with five made-up roles, two of which share a clearly described job, and one that is unused.

The test passes if:

1. `SKILL.md` frontmatter `name` is `agent-department-mapping` and the description forbids merge/retire without an explicit yes.
2. A dry-run emits a table with department, one-line job, overlap flags, and suggested next question for each fixture role.
3. The two overlapping roles are flagged with a short reason; the unused role is flagged as a retirement *candidate* only.
4. The output does not contain secret-looking strings planted in the fixture (for example a fake API token) and does not call tools that change agents.
5. Re-running the same fixture produces the same departments and overlap flags (idempotent report).

## Outline for a later SKILL.md (not the skill itself)

Inputs; department taxonomy (keep it short and stable); overlap rules; “search before build” prompt; outputs; what not to do; hand-off to retirement skill as a proposal only.
