---
name: risk-register
description: Build and maintain the dog daycare risk register (identify, score likelihood × impact, assign owners, define mitigations, triggers and contingency plans). Use for risk assessments, pre-mortems, or whenever a decision has downside exposure.
---

# Risk register & mitigation planning

## Scoring
Likelihood 1–5 (rare → almost certain) × Impact 1–5 (minor → business-ending) = score 1–25. 15–25 is critical, 8–14 high, 4–7 medium, 1–3 low.

## Register columns
`ID | Risk | Category | Cause → Event → Consequence | L | I | Score | Owner (agent/role) | Mitigations (preventive) | Contingency (if it happens) | Early-warning trigger | Status | Review date`

## Seed risks (`docs/08-risks.md`)
1. Dog fights, bites, injuries → behaviour specialist, operations
2. Contagious disease outbreak (CIRDC/pneumovirus in Miami-Dade in 2022; leptospirosis; canine influenza) → veterinary biosecurity
3. Cash shortfall during the ramp-up → financial modeler
4. Zoning, permit or build-out delays and overruns → zoning specialist, facility
5. Hurricanes, flooding, power loss → risk and continuity
6. Heat stress → operations, veterinary
7. Labour cost and turnover → HR
8. Competition and price pressure → pricing, marketing
9. Noise and odour complaints → facility, site
10. Regulatory change (county licensing removed; could return) → attorney, zoning
11. Key-person dependence → HR, engagement lead
12. A viral reputation incident → brand marketing, operations

## Method
1. Start from the seed list, then add risks specific to the decision or plan under review (a pre-mortem: "it is 18 months later and this failed, why?").
2. Score with a short justification. Do not inflate everything.
3. For every high or critical risk: at least one preventive mitigation, one contingency, an owner and a trigger.
4. Show the residual score after mitigation.
5. Recommend which risks need insurance, contracts or SOPs (hand off accordingly).

## Output
The register table sorted by score, the top 5 narrative, and the actions due in the next 30 days.
