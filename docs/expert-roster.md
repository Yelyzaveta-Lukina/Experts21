# Expert Roster: Miami Doggy Day Care Advisory Team

This file defines the expert agents that will advise the consultant on opening a doggy day care in Miami, Florida, and the skills those agents need. Each role is tied to the topic files in this folder (see [README.md](README.md)), so every agent knows which research it should rely on.

- **19 roles** across strategy, business, finance, real estate, technical, legal and regulatory, risk, operations, people and marketing.
- **30 skills**. Many are shared between agents, so each skill is built once and reused.
- IDs (`R01`, `S01`) are for wiring the agents and skills together.

## Why these roles

They follow the decisions the research says matter most:

- **Real estate and zoning are the main hurdles:** R08, R09, R10, R11.
- **The margins are thin:** break-even is about 55 dogs a day and labour is about 50% of revenue, so R05, R06, R13, R16.
- **Safety and disease are the top risks:** R12, R14, R15.
- **The market is fragmented and price-sensitive:** R02, R03, R04, R17, R18.

## Part 1: The experts

| ID | Role | Domain | One-line job description | Primary docs |
|---|---|---|---|---|
| R01 | **Engagement Lead (orchestrator)** | Strategy | Coordinates every expert, resolves conflicts between their advice, and owns the final go/no-go recommendation and launch roadmap. | all |
| R02 | **Market Research Analyst** | Business | Sizes Miami-Dade dog daycare demand by neighbourhood and keeps market data current. | 01, 02 |
| R03 | **Customer & Pricing Strategist** | Business | Defines target segments and personas, and designs prices, packages and memberships that customers will pay for. | 02, 03, 04, 07 |
| R04 | **Competitive Intelligence Analyst** | Business | Tracks Miami competitors and substitutes (prices, hours, ratios, reviews) and finds gaps the business can fill. | 03 |
| R05 | **Financial Modeler (FP&A)** | Finance | Builds and maintains the startup budget, monthly P&L, cash-flow and break-even model, and runs scenarios. | 04, 06 |
| R06 | **Funding & Franchise Advisor** | Finance | Compares independent vs franchise routes and prepares the funding plan and lender/investor package (SBA 7(a), equity). | 04 |
| R07 | **Tax & Accounting Advisor** | Finance | Sets up entity tax, sales tax, payroll tax and bookkeeping, and confirms which services are taxable in Florida. | 04, 05 |
| R08 | **Commercial Real Estate & Site Selection Advisor** | Real estate | Finds and scores candidate sites and negotiates the lease (rent, NNN, TI allowance, zoning contingencies). | 01, 02, 04, 05 |
| R09 | **Facility Design & Build-out Advisor** | Technical | Specifies and costs the dog-ready build-out: drainage, HVAC, sound control, flooring, turf, layout and fire safety. | 04, 05, 08 |
| R10 | **Zoning & Permitting Specialist** | Legal / regulatory | Maps and tracks the full approval path (zoning, building, fire, DERM/WASD, Certificate of Use, business tax receipts) for each site. | 05 |
| R11 | **Business & Regulatory Attorney** | Legal | Handles entity formation, lease review, client agreements and liability waivers, and compliance with Florida and Miami-Dade law. | 05, 08 |
| R12 | **Insurance, Risk & Continuity Manager** | Risk | Keeps the risk register, designs the insurance program, and owns hurricane, heat, power-loss and crisis plans. | 08, 05 |
| R13 | **Daycare Operations Manager** | Operations | Designs daily operations: intake, check-in/out, playgroup flow, cleaning, incident handling and service quality. | 05, 06, 08 |
| R14 | **Canine Behavior & Playgroup Specialist** | Operations (animal) | Sets temperament testing, playgroup composition and fight-prevention protocols, and trains handlers on dog body language. | 06, 08 |
| R15 | **Veterinary Health & Biosecurity Advisor** | Operations (animal) | Sets vaccine requirements, health checks, isolation and disinfection protocols, and the outbreak and heat-stress response. | 05, 08 |
| R16 | **HR & Workforce Advisor** | Operations / people | Designs the org chart, hiring, pay, training ladder and retention program, and keeps employment practices compliant. | 06 |
| R17 | **Brand & Marketing Strategist** | Marketing | Owns positioning, brand identity, bilingual messaging and the launch plan. | 02, 03, 07 |
| R18 | **Digital Growth & Partnerships Marketer** | Marketing | Runs local SEO, social and paid ads, the waitlist, referrals, and partnerships with residential buildings, vets and employers. | 02, 07 |
| R19 | **Technology & Systems Advisor** | Technical | Selects and integrates the booking/CRM software, payments, webcams, website and access control. | 04, 07 |

## Part 2: Skills and which agents use them

| ID | Skill | What it lets the agent do | Used by | # agents |
|---|---|---|---|---|
| S01 | **Research pack navigation & citation** | Reads the `docs/` pack, cites sources, and labels every claim as Verified / Reported / Estimate. | All agents (R01–R19) | 19 |
| S02 | **Web research & source verification** | Finds current facts online, prefers primary sources, and flags conflicting or dated information. | R01, R02, R03, R04, R06, R07, R08, R10, R11, R12, R15, R16, R19 | 13 |
| S03 | **Florida & Miami-Dade regulatory lookup** | Searches and interprets Florida Statutes, the Miami-Dade Code (Ch. 5), municipal codes (Miami 21) and agency guidance (FDACS, FDOR, Sunbiz). | R07, R09, R10, R11, R12, R15, R16 | 7 |
| S04 | **Financial modeling & scenario analysis** | Builds startup budgets, P&L and cash-flow models, and runs sensitivity and break-even scenarios. | R01, R03, R05, R06, R07, R08 | 6 |
| S05 | **Unit economics & KPI tracking** | Calculates revenue per dog-day, utilisation, labour %, churn and CAC, and sets KPI targets. | R01, R03, R05, R13, R18 | 5 |
| S06 | **Pricing & package design** | Designs day rates, packs, memberships, add-ons and discounts against competitor benchmarks. | R03, R04, R05, R17 | 4 |
| S07 | **Demographic & catchment analysis** | Uses Census/ACS, licensing and housing data to size demand by ZIP code and drive-time radius. | R02, R03, R08, R18 | 4 |
| S08 | **Competitor benchmarking** | Builds competitor profiles and mystery-shop scripts, and compares price, hours, ratios and reviews. | R02, R03, R04, R17 | 4 |
| S09 | **Survey & demand validation** | Designs owner surveys, waitlist tests and willingness-to-pay experiments, and interprets the results. | R02, R03, R17, R18 | 4 |
| S10 | **Commercial lease analysis** | Compares NNN costs, TI allowances, rent abatement, use clauses and approval contingencies. | R05, R08, R09, R11 | 4 |
| S11 | **Site evaluation scorecard** | Scores sites on zoning fit, flood zone, noise exposure, access/parking, catchment and cost. | R08, R09, R10, R12 | 4 |
| S12 | **Build-out specification & cost estimation** | Specifies drainage, HVAC, sound control, flooring, turf and fire/life-safety, and estimates cost per sq ft. | R05, R08, R09, R10 | 4 |
| S13 | **Zoning & permit pathway mapping** | Maps each approval step, the agency, documents, timeline and dependencies (use determination → permits → CU → BTR). | R01, R09, R10, R11 | 4 |
| S14 | **Contract, waiver & policy drafting review** | Drafts and checks client agreements, waivers, emergency vet releases and lease terms against Florida law. | R11, R12, R13 | 3 |
| S15 | **Insurance coverage analysis** | Compares GL, care-custody-control, property/wind/flood, business interruption, workers' comp and umbrella coverage, limits and quotes. | R05, R11, R12 | 3 |
| S16 | **Risk register & mitigation planning** | Scores risks by likelihood × impact, assigns owners, and tracks mitigations. | R01, R11, R12, R13, R15 | 5 |
| S17 | **Emergency & business continuity planning** | Builds plans for hurricanes, flooding, power loss, heat events and disease-outbreak closures. | R09, R12, R13, R15 | 4 |
| S18 | **SOP authoring** | Writes clear step-by-step procedures (intake, playgroups, cleaning, incidents, opening/closing). | R13, R14, R15, R16 | 4 |
| S19 | **Canine temperament assessment & playgroup management** | Evaluates dogs for group play, groups them by size and energy, and sets intervention protocols. | R13, R14, R16 | 3 |
| S20 | **Disease prevention & vaccine policy** | Sets vaccine and health-check requirements, isolation rules and disinfectant protocols (lepto, CIV, CIRDC). | R11, R13, R14, R15 | 4 |
| S21 | **Staffing model & scheduling** | Turns dog counts and ratios into shifts, headcount and labour cost. | R05, R13, R14, R16 | 4 |
| S22 | **Hiring, training & retention design** | Writes job descriptions, interview guides, training curricula and career ladders. | R13, R14, R16 | 3 |
| S23 | **Employment & wage compliance** | Applies the Florida minimum wage schedule, workers' comp rules, E-Verify, worker classification and payroll tax. | R07, R11, R16 | 3 |
| S24 | **Brand positioning & bilingual messaging** | Writes positioning, value propositions and EN/ES copy for each target segment. | R03, R17, R18 | 3 |
| S25 | **Digital marketing execution** | Runs local SEO, the Google Business Profile, social content, geo-targeted ads and review generation. | R17, R18 | 2 |
| S26 | **Partnership & community outreach** | Finds and pitches luxury buildings, vets, employers, rescues and influencers. | R13, R17, R18 | 3 |
| S27 | **Funding & lender package preparation** | Prepares the business plan, SBA package and investor memo, and analyses franchise FDDs (Item 7/19). | R01, R05, R06, R11 | 4 |
| S28 | **Tax setup & bookkeeping** | Handles sales tax registration, BTR renewals, payroll tax, chart of accounts and month-end close. | R05, R07, R10 | 3 |
| S29 | **Pet-business tech stack selection** | Compares booking/CRM tools (Gingr, MoeGo, PetExec…), payments, webcams and integrations. | R05, R13, R18, R19 | 4 |
| S30 | **Decision synthesis & executive memos** | Combines expert inputs into clear recommendations, trade-offs and go/no-go memos. | R01, R05, R06 | 3 |

## Part 3: Skill loadout per agent

The same mapping as Part 2, viewed by agent. Use it when configuring each agent.

| ID | Role | Skills | Count |
|---|---|---|---|
| R01 | Engagement Lead (orchestrator) | S01 Research pack navigation & citation, S02 Web research & source verification, S04 Financial modeling & scenario analysis, S05 Unit economics & KPI tracking, S13 Zoning & permit pathway mapping, S16 Risk register & mitigation planning, S27 Funding & lender package preparation, S30 Decision synthesis & executive memos | 8 |
| R02 | Market Research Analyst | S01 Research pack navigation & citation, S02 Web research & source verification, S07 Demographic & catchment analysis, S08 Competitor benchmarking, S09 Survey & demand validation | 5 |
| R03 | Customer & Pricing Strategist | S01 Research pack navigation & citation, S02 Web research & source verification, S04 Financial modeling & scenario analysis, S05 Unit economics & KPI tracking, S06 Pricing & package design, S07 Demographic & catchment analysis, S08 Competitor benchmarking, S09 Survey & demand validation, S24 Brand positioning & bilingual messaging | 9 |
| R04 | Competitive Intelligence Analyst | S01 Research pack navigation & citation, S02 Web research & source verification, S06 Pricing & package design, S08 Competitor benchmarking | 4 |
| R05 | Financial Modeler (FP&A) | S01 Research pack navigation & citation, S04 Financial modeling & scenario analysis, S05 Unit economics & KPI tracking, S06 Pricing & package design, S10 Commercial lease analysis, S12 Build-out specification & cost estimation, S15 Insurance coverage analysis, S21 Staffing model & scheduling, S27 Funding & lender package preparation, S28 Tax setup & bookkeeping, S29 Pet-business tech stack selection, S30 Decision synthesis & executive memos | 12 |
| R06 | Funding & Franchise Advisor | S01 Research pack navigation & citation, S02 Web research & source verification, S04 Financial modeling & scenario analysis, S27 Funding & lender package preparation, S30 Decision synthesis & executive memos | 5 |
| R07 | Tax & Accounting Advisor | S01 Research pack navigation & citation, S02 Web research & source verification, S03 Florida & Miami-Dade regulatory lookup, S04 Financial modeling & scenario analysis, S23 Employment & wage compliance, S28 Tax setup & bookkeeping | 6 |
| R08 | Commercial Real Estate & Site Selection Advisor | S01 Research pack navigation & citation, S02 Web research & source verification, S04 Financial modeling & scenario analysis, S07 Demographic & catchment analysis, S10 Commercial lease analysis, S11 Site evaluation scorecard, S12 Build-out specification & cost estimation | 7 |
| R09 | Facility Design & Build-out Advisor | S01 Research pack navigation & citation, S03 Florida & Miami-Dade regulatory lookup, S10 Commercial lease analysis, S11 Site evaluation scorecard, S12 Build-out specification & cost estimation, S13 Zoning & permit pathway mapping, S17 Emergency & business continuity planning | 7 |
| R10 | Zoning & Permitting Specialist | S01 Research pack navigation & citation, S02 Web research & source verification, S03 Florida & Miami-Dade regulatory lookup, S11 Site evaluation scorecard, S12 Build-out specification & cost estimation, S13 Zoning & permit pathway mapping, S28 Tax setup & bookkeeping | 7 |
| R11 | Business & Regulatory Attorney | S01 Research pack navigation & citation, S02 Web research & source verification, S03 Florida & Miami-Dade regulatory lookup, S10 Commercial lease analysis, S13 Zoning & permit pathway mapping, S14 Contract, waiver & policy drafting review, S15 Insurance coverage analysis, S16 Risk register & mitigation planning, S20 Disease prevention & vaccine policy, S23 Employment & wage compliance, S27 Funding & lender package preparation | 11 |
| R12 | Insurance, Risk & Continuity Manager | S01 Research pack navigation & citation, S02 Web research & source verification, S03 Florida & Miami-Dade regulatory lookup, S11 Site evaluation scorecard, S14 Contract, waiver & policy drafting review, S15 Insurance coverage analysis, S16 Risk register & mitigation planning, S17 Emergency & business continuity planning | 8 |
| R13 | Daycare Operations Manager | S01 Research pack navigation & citation, S05 Unit economics & KPI tracking, S14 Contract, waiver & policy drafting review, S16 Risk register & mitigation planning, S17 Emergency & business continuity planning, S18 SOP authoring, S19 Canine temperament assessment & playgroup management, S20 Disease prevention & vaccine policy, S21 Staffing model & scheduling, S22 Hiring, training & retention design, S26 Partnership & community outreach, S29 Pet-business tech stack selection | 12 |
| R14 | Canine Behavior & Playgroup Specialist | S01 Research pack navigation & citation, S18 SOP authoring, S19 Canine temperament assessment & playgroup management, S20 Disease prevention & vaccine policy, S21 Staffing model & scheduling, S22 Hiring, training & retention design | 6 |
| R15 | Veterinary Health & Biosecurity Advisor | S01 Research pack navigation & citation, S02 Web research & source verification, S03 Florida & Miami-Dade regulatory lookup, S16 Risk register & mitigation planning, S17 Emergency & business continuity planning, S18 SOP authoring, S20 Disease prevention & vaccine policy | 7 |
| R16 | HR & Workforce Advisor | S01 Research pack navigation & citation, S02 Web research & source verification, S03 Florida & Miami-Dade regulatory lookup, S18 SOP authoring, S19 Canine temperament assessment & playgroup management, S21 Staffing model & scheduling, S22 Hiring, training & retention design, S23 Employment & wage compliance | 8 |
| R17 | Brand & Marketing Strategist | S01 Research pack navigation & citation, S06 Pricing & package design, S08 Competitor benchmarking, S09 Survey & demand validation, S24 Brand positioning & bilingual messaging, S25 Digital marketing execution, S26 Partnership & community outreach | 7 |
| R18 | Digital Growth & Partnerships Marketer | S01 Research pack navigation & citation, S05 Unit economics & KPI tracking, S07 Demographic & catchment analysis, S09 Survey & demand validation, S24 Brand positioning & bilingual messaging, S25 Digital marketing execution, S26 Partnership & community outreach, S29 Pet-business tech stack selection | 8 |
| R19 | Technology & Systems Advisor | S01 Research pack navigation & citation, S02 Web research & source verification, S29 Pet-business tech stack selection | 3 |

## Build notes

- **Build the most-shared skills first:** S01 (19 agents), S02 (13 agents), S03 (7 agents), S04 (6 agents), S05 (5 agents), S16 (5 agents).
- **Shared rules for every agent (from S01):** cite sources, label each claim Verified / Reported / Estimate, and list open questions instead of guessing. Legal, tax and insurance outputs are research context, not professional advice. A licensed Florida professional must confirm them before money is committed.
- **Handoffs between agents:**
  - R08 (site) → R10 (zoning) → R09 (build-out cost) → R05 (finance model) → R06 (funding) → R01 (go/no-go).
  - R14 and R15 (dog safety and health) feed R13 (SOPs), which feeds R16 (staffing and training) and R12 (risk).
  - R02, R03 and R04 (market) feed R17 and R18 (marketing), which feed R05 (revenue ramp).
- **Possible merges for a smaller team:** R02 + R04, R17 + R18, R12 + R15 (risk + health), R06 + R07.
