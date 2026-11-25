# How to Talk to Your Experts

How to get answers from the Miami doggy day care expert team in Claude Code. The team is 19 experts, plus `expert-orchestrator`, which coordinates them, and `team-builder`, which maintains them. See [expert-roster.md](expert-roster.md) and the root `CLAUDE.md` for the full team.

There are three ways to ask:

| Mode | Who answers | When to use it |
|---|---|---|
| **One expert** | A single specialist | The question sits clearly in one domain |
| **Orchestrated** | `expert-orchestrator` picks 2–7 relevant experts and merges their answers | The question touches several domains (most real decisions) |
| **Whole team** | `expert-orchestrator` runs a full review with every expert | Big milestone reviews, such as a go/no-go or a full business plan check |

---

## 1. Ask one specific expert

Use an @-mention with the agent's name. In the Claude Code prompt, type `@` and pick the agent, or type it out:

```text
@agent-financial-modeler What is our break-even dogs per day if we charge $45 for a single day and $40 on memberships?
```

```text
@agent-zoning-permitting-specialist List, in order, every approval we need before opening a daytime dog daycare in the City of Miami, and flag the biggest timeline risk.
```

```text
@agent-canine-behavior-specialist Draft our temperament evaluation checklist and the criteria for accepting or declining a dog.
```

Or ask in plain language and name the agent:

```text
Ask the veterinary-biosecurity-advisor which vaccines we should require and how to handle a dog that starts coughing mid-day.
```

**Agent names you can use:** `engagement-lead`, `market-research-analyst`, `customer-pricing-strategist`, `competitive-intelligence-analyst`, `financial-modeler`, `funding-franchise-advisor`, `tax-accounting-advisor`, `real-estate-site-advisor`, `facility-buildout-advisor`, `zoning-permitting-specialist`, `business-attorney`, `risk-insurance-manager`, `operations-manager`, `canine-behavior-specialist`, `veterinary-biosecurity-advisor`, `hr-workforce-advisor`, `brand-marketing-strategist`, `digital-growth-marketer`, `technology-systems-advisor`.

---

## 2. Orchestrated questions: several experts, one answer

Start with `/consult-experts` (the most reliable way). Alternatively, say "Use the expert-orchestrator to…" or `@agent-expert-orchestrator`. The orchestrator chooses the experts, runs the independent ones in parallel and the dependent ones in sequence, checks that their numbers agree, and returns **one combined answer**. The answer includes the experts consulted, any disagreements and how they were resolved, and next steps.

### Example prompts

**A. Choosing a location**
```text
/consult-experts We are choosing between a 6,000 sq ft flex space in Wynwood at $24/sq ft NNN and a 7,500 sq ft warehouse in Doral at $18/sq ft NNN. Which should we pursue? Consider demand and competition near each, zoning and permitting risk, build-out cost, and the effect on break-even.
```
*Likely experts:* market-research-analyst, competitive-intelligence-analyst, real-estate-site-advisor → zoning-permitting-specialist → facility-buildout-advisor → financial-modeler → engagement-lead.

**B. Adding overnight boarding**
```text
/consult-experts Should we offer overnight boarding from day one or launch as daytime-only daycare and add boarding later? Look at revenue and margin impact, zoning and classification (pet care center vs kennel), extra staffing, insurance, hurricane-season obligations and customer demand.
```
*Likely experts:* financial-modeler, zoning-permitting-specialist, hr-workforce-advisor, risk-insurance-manager, customer-pricing-strategist, operations-manager.

**C. Pricing and launch plan**
```text
/consult-experts Design our launch pricing and a 90-day pre-opening marketing plan for a premium daycare in Brickell/Edgewater. We want a founding-member offer, but the realised price must stay at or above break-even. Include the expected waitlist target and marketing budget.
```
*Likely experts:* competitive-intelligence-analyst + customer-pricing-strategist → brand-marketing-strategist + digital-growth-marketer → financial-modeler.

**D. Safety and outbreak readiness**
```text
/consult-experts A competitor nearby just had a kennel-cough outbreak. What policies, facility features, staff training and insurance should we have in place before opening so that a fight or disease outbreak doesn't sink us? Give me a prioritised checklist.
```
*Likely experts:* veterinary-biosecurity-advisor + canine-behavior-specialist → operations-manager → hr-workforce-advisor, risk-insurance-manager, business-attorney, facility-buildout-advisor.

**Tips for good orchestrated prompts**
- State the **decision** you need, not only the topic ("Which site should we pursue?" rather than "Tell me about sites").
- Give the **specifics** you have: addresses, rents, sizes, budget, timeline, prices.
- Name the **angles** you care about. The orchestrator uses them to pick experts.
- Ask for the **format** you want ("one-page memo", "prioritised checklist", "table").

---

## 3. Ask the whole team

The orchestrator normally uses the smallest set of experts that covers the question. To involve **everyone**, ask explicitly for a full-team review:

```text
/consult-experts Full team review: consult every expert on the team. Based on the research pack, should we open a doggy day care in Miami in the next 12 months? Each expert should give their bottom line, top risk and top open question for their area, then combine everything into a go/no-go recommendation with conditions and a launch roadmap.
```

Or:

```text
Use the expert-orchestrator to run a full review with all 19 experts of our plan: independent 6,000 sq ft site in Wynwood, $45/day pricing, daycare + grooming, opening in 9 months. Return one combined go/no-go memo.
```

Whole-team runs take longer and use more tokens. Keep them for major milestones.

---

## Other useful commands

| Command | What it does |
|---|---|
| `claude --agent expert-orchestrator` | Starts a session where the orchestrator is the main agent for every prompt |
| `/improve-team Add an expert on grooming services` | Asks `team-builder` to create or improve agents and skills |
| `@agent-team-builder Review all agent descriptions and fix any that overlap` | Same thing, as a direct mention |
| `python3 .claude/skills/agent-skill-authoring/scripts/validate_team.py` | Checks that all agents and skills are wired correctly |

**Reminder:** answers label facts as **Verified / Reported / Estimate**. Legal, tax, insurance and veterinary points are research support, not professional advice.
