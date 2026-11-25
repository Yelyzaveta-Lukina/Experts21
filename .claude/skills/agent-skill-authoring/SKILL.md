---
name: agent-skill-authoring
description: Create, edit and validate this project's Claude Code subagents (.claude/agents/*.md) and skills (.claude/skills/*/SKILL.md) following the official formats and the team's conventions, and keep the roster, orchestrator routing table and CLAUDE.md in sync. Use when adding, improving, renaming or removing agents or skills.
---

# Agent & skill authoring

## Official formats (code.claude.com/docs/en/sub-agents, /skills)
**Subagent** = `.claude/agents/<name>.md`. YAML frontmatter then the system prompt in Markdown. Required fields: `name` (lowercase-hyphenated here, no `:`), `description` (when to delegate; keep it short, since the combined descriptions of all subagents have a ~15k-token budget). Optional fields used here: `tools`, `disallowedTools`, `model` (`inherit`), `color` (red|blue|green|yellow|purple|orange|pink|cyan), `skills` (YAML list: the **full content is preloaded** at startup, max 32), `maxTurns`, `effort`, `memory`. Subagents can nest up to 3 levels below the main conversation. Subagents don't see the parent conversation, only their prompt, the delegation message, CLAUDE.md and preloaded skills.

**Skill** = `.claude/skills/<skill-name>/SKILL.md`. Frontmatter: `name` (= directory name), `description` (key use case first; description + `when_to_use` is truncated at 1,536 chars). Optional: `when_to_use`, `argument-hint`, `disable-model-invocation` (true = cannot be auto-invoked **or preloaded into subagents**), `user-invocable` (false = hidden from the / menu), `allowed-tools`, `context: fork` + `agent: <subagent>` + `background: false` (run the skill as that subagent and wait for it), `model`, `effort`. Body under 500 lines; move detail to supporting files. `$ARGUMENTS`, `${CLAUDE_SKILL_DIR}` substitutions are available.

## Team conventions
- **Expert agents**: `model: inherit`; `disallowedTools: Agent` (only the orchestrator and team-builder spawn agents); tools `Read, Glob, Grep, Write, Edit, WebSearch, WebFetch, Skill` (+ `Bash` only if they compute); `skills:` **always starts with `research-pack-citation`**; colour by domain (strategy purple, business blue, finance green, real estate/technical orange, legal/risk red, operations yellow, people cyan, marketing pink).
- Agent body sections: role intro → Mission → Read first (docs) → Focus areas → Key facts → How you work → Handoffs → Boundaries.
- Skill bodies: purpose → facts/benchmarks with V/R/E labels and doc references → method → output. Specific to the Miami dog daycare; no generic filler.
- Knowledge skills are model-invocable (so they can be preloaded). Entry-point skills (`consult-experts`, `improve-team`) use `context: fork` and `disable-model-invocation: true`.
- Names: agents use role nouns (`financial-modeler`); skills use capability nouns (`financial-modeling`).

## Procedure: add or change an agent
1. Check the roster (`docs/expert-roster.md`) for overlap. Prefer improving an existing agent to adding a near-duplicate. Keep the team at **10–50 agents**.
2. Write or edit `.claude/agents/<name>.md` following the conventions. Wire `skills:` (only existing skill names).
3. Add or update its row in the **routing table** in `.claude/skills/expert-team-orchestration/SKILL.md`.
4. Update `docs/expert-roster.md` (role table, skill "Used by" lists, loadout table) and the team table in `CLAUDE.md`.
5. Run the validator (below).

## Procedure: add or change a skill
1. Create `.claude/skills/<skill-name>/SKILL.md` (directory name = `name`).
2. Add the skill to every agent that should preload it, and to the roster's skills table.
3. Run the validator.

## Procedure: improve existing agents/skills
Look for: vague descriptions (delegation misfires), stale facts (wages, fees, laws, with date), missing handoffs, skills preloaded but unused, overlap between agents, missing V/R/E labels. Optionally test-run the changed agent with one realistic question and check the result against its Output section. Record what changed in the commit message.

## Validate
```bash
python3 .claude/skills/agent-skill-authoring/scripts/validate_team.py
```
It checks the frontmatter, name/file consistency, that every preloaded skill exists, preload count ≤ 32, the team size (10–50), orphan skills, roster coverage in the orchestrator, and the description budget. Fix all ERRORs; review the WARNs.
