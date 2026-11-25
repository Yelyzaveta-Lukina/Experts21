---
name: staffing-scheduling-model
description: Convert expected dogs per hour and ratio policy into shifts, headcount, staff-hours and labour cost for a dog daycare under Florida wage rules. Use for staffing plans, schedules, labour budgets or ratio trade-offs.
---

# Staffing model & scheduling

## Inputs
- Dog count by hour (typical curve: drop-off 7–9am, peak 9am–4pm, pickup 5–7pm).
- Ratio policy: 1:10–12 large/high-energy, up to 1:15 calm/small; at least 1 handler per occupied room (`docs/06-staffing.md`).
- Non-floor roles: front desk/client care, manager, bather/groomer, cleaning, overnight (if boarding).
- Wages (Florida minimum **$15.00 from 30 Sep 2026**; animal caretakers in the Miami metro averaged **$17.45** in BLS May 2023) and **burden 12–18%**.

## Calculation
1. For each hour: `handlers needed = Σ over rooms of ceil(dogs in room ÷ ratio)`, with at least 1 per open room.
2. Add front desk coverage (peaks need 2 people), plus cleaning time if not done by handlers.
3. Sum the staff-hours per day. Base case: **~50 hourly staff-hours/day for 55–65 dogs**.
4. `Monthly labour = staff-hours/day × operating days × wage × (1 + burden) + salaried roles`.
5. `Labour % = labour ÷ revenue` (target ≤ 45%; base model ~50%).

## Shift templates (example)
Early 6:30–2:30 (opening, drop-offs) · Mid 9:00–5:00 (peak) · Late 11:00–7:30 (pickups, closing) · Part-time peaks 7–11 and 3–7. Overlap at 11–2 covers lunches and rest-time cleaning.

## Rules and levers
- Never let the ratio slip at peak to save money. Flex the start and end of the day instead.
- Use reservations (bookings required by 8pm the day before) to forecast headcount.
- Cross-train front desk and handlers.
- Overtime above 40 hours/week costs 1.5×, so cap scheduled hours at ~38.
- Track the forecast vs. actual dogs, and the labour %, weekly.

## Output
An hourly coverage table, a weekly schedule grid, FTE and headcount (with the part-time mix), monthly labour cost and %, and sensitivity (±10 dogs, ±$1/hr wage, ratio 1:12 vs 1:15).
