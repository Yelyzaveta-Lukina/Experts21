# Experts21: Miami Doggy Day Care Expert Team

This project is a **team of Claude Code expert agents** that advise a consultant planning a **doggy day care in Miami, Florida (Miami-Dade County)**. The agents share one research pack (`docs/`) and a library of reusable skills. An orchestrator combines their work into single answers, and a meta agent maintains the team.

## Layout

```
docs/                     Research pack (market, customers, competitors, costs, permits, staffing, marketing, risks)
docs/expert-roster.md     The roster: roles, skills, which agent uses which skill, file mapping
.claude/agents/           21 project subagents (19 experts + orchestrator + team-builder)
.claude/skills/           34 project skills (30 domain + 2 team + 2 entry points)
knowledge/<agent>/        Each agent's private knowledge folder (read before every answer; README says what belongs)
deliverables/<agent>/     Where agents write files when asked (created on demand)
```

## How to use the team

Example prompts are in [`docs/how-to-talk-to-your-experts.md`](docs/how-to-talk-to-your-experts.md).

| You want… | Do this |
|---|---|
| A combined answer from several experts | `/consult-experts Should we open in Wynwood or Doral?`, or ask: "Use the expert-orchestrator to …" |
| One specific expert | `@agent-financial-modeler what is break-even at $45/day?`, or ask: "Ask the zoning-permitting-specialist …" |
| A new expert or skill, or to improve existing ones | `/improve-team add an expert on grooming services`, or "Use the team-builder to …" |
| The whole session to run as the orchestrator | `claude --agent expert-orchestrator` |
| To check the team's wiring | `python3 .claude/skills/agent-skill-authoring/scripts/validate_team.py` |

**Routing rule for the main conversation:** send questions about the daycare project that span more than one domain (or where you're unsure who should answer) to `expert-orchestrator`. Single-domain questions can go straight to the matching expert. The orchestrator can call experts (nesting is allowed up to 3 levels). Experts cannot spawn agents (`disallowedTools: Agent`); they list handoffs instead.

## The team

| Name | Agent | Model | Role | Use for |
|---|---|---|---|---|
| Marisol | `expert-orchestrator` | opus | Orchestrator | Any multi-domain question; picks experts, coordinates them, merges into one answer |
| Theo | `team-builder` | opus | Meta agent | Creating and improving agents and skills; keeps everything in sync and validated |
| Elena | `engagement-lead` | opus | Engagement Lead | Strategy, go/no-go, roadmap, trade-offs |
| Marcus | `market-research-analyst` | sonnet | Market Research Analyst | Demand sizing, demographics, neighbourhoods |
| Priya | `customer-pricing-strategist` | sonnet | Customer & Pricing Strategist | Segments, personas, prices, packages, memberships |
| Carlos | `competitive-intelligence-analyst` | haiku | Competitive Intelligence Analyst | Competitors, substitutes, gaps |
| Frank | `financial-modeler` | opus | Financial Modeler (FP&A) | Budgets, P&L, cash flow, break-even, what-ifs |
| Fiona | `funding-franchise-advisor` | opus | Funding & Franchise Advisor | SBA and loans, investors, franchise vs independent |
| Tomás | `tax-accounting-advisor` | opus | Tax & Accounting Advisor | Sales tax, business tax receipts, payroll tax, bookkeeping |
| Rosa | `real-estate-site-advisor` | sonnet | Real Estate & Site Selection Advisor | Locations, rent, leases |
| Bruno | `facility-buildout-advisor` | sonnet | Facility Design & Build-out Advisor | Layout, drainage, HVAC, flooring, build-out cost |
| Zoe | `zoning-permitting-specialist` | opus | Zoning & Permitting Specialist | Zoning, permits, Certificate of Use, timelines |
| Adrian | `business-attorney` | opus | Business & Regulatory Attorney (research role) | Entity, contracts, waivers, liability, compliance |
| Rita | `risk-insurance-manager` | opus | Insurance, Risk & Continuity Manager | Risk register, insurance, hurricane and heat plans |
| Olivia | `operations-manager` | sonnet | Daycare Operations Manager | Daily operations, SOPs, capacity, quality |
| Kai | `canine-behavior-specialist` | sonnet | Canine Behavior & Playgroup Specialist | Temperament tests, playgroups, fight prevention |
| Vera | `veterinary-biosecurity-advisor` | sonnet | Veterinary Health & Biosecurity Advisor | Vaccines, illness, outbreaks, cleaning |
| Hana | `hr-workforce-advisor` | sonnet | HR & Workforce Advisor | Hiring, pay, training, retention, employment compliance |
| Bianca | `brand-marketing-strategist` | sonnet | Brand & Marketing Strategist | Positioning, brand, messaging, launch |
| Diego | `digital-growth-marketer` | sonnet | Digital Growth & Partnerships Marketer | SEO, social, ads, reviews, partnerships |
| Tariq | `technology-systems-advisor` | haiku | Technology & Systems Advisor | Booking software, payments, webcams, website |

Why each agent has its model, and each persona's voice and working style, are in `docs/agent-brains.md`. Which skills each agent preloads is listed in `docs/expert-roster.md` (Parts 2–4) and in each agent's `skills:` frontmatter.

## Conventions (all agents)

- **The knowledge folder comes first, then the research pack.** Every agent reads `knowledge/<agent-name>/` before answering. Drop client documents there (quotes, leases, notes) and they take precedence over `docs/`.
- **Research pack:** Use `docs/` as the shared fact base; research the web only for gaps or stale facts, and date-stamp the results.
- **Label every claim** as **Verified** (primary source), **Reported** (secondary source) or **Estimate** (modelled). Cite the doc file or URL.
- **Shared baseline numbers** (from `docs/04-costs.md`, Estimates): 6,000 sq ft standard site, ~70-dog capacity, rent ~$13k/month, realised price $38 → $42/day, break-even ~55 dogs/day, labour ~50% of revenue, Florida minimum wage $15.00 from 30 Sep 2026. Experts should use these unless the question changes them, so the answers stay consistent.
- **Expert Brief** output format: Bottom line → Analysis → Risks & caveats → Open questions → Handoffs (defined in the `research-pack-citation` skill).
- **Not professional advice:** legal, tax, insurance and veterinary outputs are research support. A Florida-licensed professional must confirm them before money is committed.
- Agents write files only when asked, under `deliverables/<agent-name>/`. Do not edit `docs/` unless the task is to update the research pack.

## Maintaining the team

- Use `team-builder` (or `/improve-team`) for changes. It follows the `agent-skill-authoring` skill.
- When adding or renaming an agent, update all four together: the agent file, the routing table in `.claude/skills/expert-team-orchestration/SKILL.md`, `docs/expert-roster.md`, and the team table above.
- Keep the team at **10–50 agents** and each agent at ≤ 32 preloaded skills. Run the validator before committing.
- Formats follow the official docs: [subagents](https://code.claude.com/docs/en/sub-agents) and [skills](https://code.claude.com/docs/en/skills).
