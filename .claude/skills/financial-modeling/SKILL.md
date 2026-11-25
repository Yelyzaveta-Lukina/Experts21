---
name: financial-modeling
description: Build and run the dog daycare financial model (startup budget, 36-month P&L, cash flow, debt service, break-even, scenarios and sensitivities) using the Miami assumptions in docs/04-costs.md. Use for any money question that needs numbers.
---

# Financial modeling & scenario analysis

## Model structure
1. **Assumptions** (one block, each labelled V/R/E with a source): sq ft, capacity, rent and NNN, price per day, discount mix, dogs-per-day ramp, add-on %, wage rates, burden %, staff-hours per day, utilities, insurance, marketing, card fees, loan terms.
2. **Startup budget** (capex + pre-opening + working capital).
3. **Monthly P&L for 36 months** (revenue by line: daycare, boarding, grooming, retail/training; direct labour; occupancy; other opex; EBITDA).
4. **Cash flow** (EBITDA – debt service – capex) and the lowest cash balance.
5. **Break-even** and **sensitivity tables**.

## Base assumptions (from `docs/04-costs.md`; all Estimates unless marked)
| Item | Standard site |
|---|---|
| Size / capacity | 6,000 sq ft / ~70 dogs |
| Rent | $20 base + ~$6 NNN per sq ft per year → ~$13,000/mo (market: $16–17 industrial, ~$20–22 flex; Verified/Reported) |
| Price | $38 realised (ramp) → $42 (target) per dog-day; add-ons +15% |
| Operating days | ~21.7 weekdays/mo (add weekend boarding separately) |
| Labour | ~50 hourly staff-hours/day × $17 × 1.15 burden + GM $5.3k/mo |
| Florida minimum wage | $15.00 from 30 Sep 2026 (Verified) |
| Other opex | utilities $3–4.5k, insurance $0.8–1.5k, supplies $1–1.5k, marketing $1.5–3k, R&M $0.75–1.5k, card fees 3% |
| Startup | Lean $165–370k; Standard $525k–$1.2M; Dogtopia franchise $608k–$1.27M (company) plus 7% royalty and 2% brand fund |
| Ramp | ~25 dogs/day in months 1–6, reaching steady state at 9–18 months |
| Break-even | ~55 dogs/day at $38 |

## Scenarios to run every time
- **Downside / Base / Upside**: vary dogs per day (±15%), price (±$4), and ramp speed (±6 months).
- **Service mix**: daycare only vs. + grooming vs. + boarding (15 nights/day at $60–75).
- **Route**: independent vs. franchise (fees and faster ramp).

## Doing the maths
For anything beyond a few lines, write a short Python script with `Bash` (standard library only, or `csv`) so the numbers are reproducible. Save it and the CSV output to `deliverables/<agent>/`. Show the key tables in the answer.

## Sanity checks
- Labour ≤ ~45–50% of revenue at maturity. Occupancy (rent + NNN) ≤ ~15–20%.
- Minimum cash balance stays positive with at least 1 month of operating costs as a buffer.
- Capacity is never exceeded (dogs per day ≤ ~75–80% of capacity on average).
- Every output number traces back to an assumption.
