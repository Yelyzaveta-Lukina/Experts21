---
name: site-evaluation-scorecard
description: Score and rank candidate Miami-Dade sites for a dog daycare on zoning fit, catchment, access, flood and hurricane exposure, noise adjacency, building suitability and cost. Use when shortlisting or comparing locations.
---

# Site evaluation scorecard

## Knock-out checks (fail any one = drop the site or escalate)
1. Zoning prohibits the use, or needs a contested public hearing (see `permit-pathway-mapping`).
2. Shares a wall with, or sits right next to, homes with no realistic sound mitigation.
3. No feasible way to connect floor drains to the sanitary sewer.
4. Ground floor in a high-risk flood zone with a history of flooding (check FEMA flood map / Miami-Dade flood zone viewer and elevation).

## Weighted criteria (score each 1–5)
| Criterion | Weight | Notes |
|---|---|---|
| Catchment demand (dog households, income, renters) | 20% | `demographic-catchment-analysis` |
| Commute convenience and drop-off (parking, curbside, traffic direction in the morning) | 15% | |
| Zoning / permitting ease | 15% | By right > Warrant > Exception |
| Building suitability (clear height, column spacing, existing plumbing, HVAC capacity, ~4,000–8,000 sq ft) | 15% | |
| All-in occupancy cost (effective $/sq ft) | 15% | `commercial-lease-analysis` |
| Outdoor space possibility | 5% | |
| Competition intensity within 3 miles | 10% | `competitor-benchmarking` |
| Climate resilience (flood zone, elevation, wind rating, generator feasibility) | 5% | |

`Total = Σ score × weight`, giving a value from 1 to 5. Show the sensitivity: does the top site change if catchment or cost weights move ±5 points?

## Data sources
Miami-Dade Property Appraiser (parcel, zoning, owner), City GIS / MuniMap (Miami 21 transect), FEMA flood maps, Google Maps (drive times at 8am), broker flyers, site visit (noise, smell, access).

## Output
A ranked table, knock-out results, the top 3 with pros and cons, and the next diligence steps for each.
