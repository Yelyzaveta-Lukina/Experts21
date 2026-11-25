# Progress Log

A running record of what has been built and decided, so any new session (or person) can pick up where we left off.

## 2026-11-25: Session 1

**Built (all on `main`)**
1. Research pack `docs/01`–`08` plus the index `docs/README.md` (market, customers, competitors, costs, permits, staffing, marketing, risks).
2. `docs/expert-roster.md`: 19 expert roles and 30 shared skills.
3. Claude Code team: 21 subagents in `.claude/agents/` (19 experts + `expert-orchestrator` + `team-builder`) and 34 skills in `.claude/skills/`. Wiring is checked by `.claude/skills/agent-skill-authoring/scripts/validate_team.py`.
4. `CLAUDE.md` (how the team works) and `docs/how-to-talk-to-your-experts.md` (example prompts).
5. `docs/agent-brains.md`: models (9 opus / 10 sonnet / 2 haiku), personas (e.g. Rosa, Frank, Zoe), and knowledge folders `knowledge/<agent>/` that agents read before answering.
6. Sample (training) documents in `knowledge/real-estate-site-advisor/`: a Wynwood landlord offer and a broker listing.

**Work done with the team**
- Rosa (`real-estate-site-advisor`) reviewed the sample Wynwood offer. Verdict: **do not sign as written**. See `deliverables/real-estate-site-advisor/2026-11-25-wynwood-lease-review.md`.

**Open threads / possible next steps**
- Run `/consult-experts` on the Wynwood offer so the zoning, build-out, attorney and finance experts weigh in together.
- A Brickell lease document was mentioned but was never committed to GitHub. Add it to `knowledge/real-estate-site-advisor/` if it exists.
- Replace the sample documents with real quotes and listings as they arrive.
- Open questions remain in each `docs/0X` file (e.g. confirming the state law behind the county licence change, and franchise presence in Miami-Dade).
