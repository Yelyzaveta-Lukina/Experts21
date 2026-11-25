---
name: demographic-catchment-analysis
description: Size dog daycare demand around a Miami-Dade location or neighbourhood using Census/ACS, dog-ownership and licensing data, and convert it into a client and dogs-per-day estimate. Use for market sizing, neighbourhood ranking or site catchment questions.
---

# Demographic & catchment analysis

## Data sources
- **Census ACS 5-year** at ZIP or tract level: households (B11001), median household income (B19013), tenure / renter share (B25003), age (B01001), commuting and work-from-home (B08301).
- **Census QuickFacts** for Miami-Dade: ~2.80M people, ~975k households, median household income ~$72–76k (Verified, `docs/01-market.md`).
- **Dog ownership:** ~23% of Miami-metro households own a dog (2021 AHS, Verified). The national rate is 53% (APPA 2025). Use 20–23% locally, and up to 25–30% in dense young-professional areas *only* with evidence.
- **Miami-Dade dog licences:** 226,334 in FY2024-25 (Verified). Ask Animal Services for counts by ZIP.
- New multifamily deliveries and pet-friendly buildings (Miami REALTORS, broker reports).

## Method (funnel)
1. Define the catchment: a 3-mile and a 5-mile radius, or a 15-minute drive at the morning commute.
2. Households in the catchment × dog-ownership rate = **dog households**.
3. × daycare propensity (Estimate 5–10%; higher for high-income renters who work long hours) = **potential daycare clients**.
4. × achievable share (Estimate 15–30%, depending on competitors nearby) = **target clients**.
5. × average days per week per client (≈2.5) ÷ 5 = **dogs per weekday**. Compare with the ~55 dogs/day break-even.

## Neighbourhood priorities (`docs/02-target-customers.md`)
Brickell/Downtown/Edgewater → Wynwood/Midtown/Allapattah/Little River → Doral → Coral Gables/South Miami → Aventura.

## Output
A funnel table per area (each step labelled V/R/E), a ranking, the key sensitivities (dog-ownership rate, propensity, share), and the data still to collect.
