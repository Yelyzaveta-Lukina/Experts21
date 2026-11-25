---
name: web-research-verification
description: Find current facts on the web for the Miami dog daycare project, prefer primary sources, cross-check, date-stamp, and flag conflicting or stale information. Use when the docs/ pack lacks a fact, a figure may be out of date, or a claim needs confirming.
---

# Web research & source verification

## When to search
1. The answer is not in `docs/`, or the pack marks it as an open question.
2. The fact is time-sensitive (wages, rent, fees, laws, competitor prices, hours) and the pack figure is older than about 6 months.
3. Someone needs a claim confirmed before money is committed.

## Source hierarchy (best first)
1. Government and primary sources: `miamidade.gov`, `miami.gov` and other city sites, `library.municode.com`, `leg.state.fl.us` / `flsenate.gov`, `floridarevenue.com`, `sunbiz.org`, `fdacs.gov`, `bls.gov`, `census.gov`, `fema.gov`, franchise FDDs.
2. Industry bodies and established data: APPA, Pet Care Services Association, CBRE / Cushman / Transwestern / Avison Young reports.
3. Reputable news (Miami Herald, CBS/NBC Miami, Local10).
4. Directories, vendor blogs and aggregators. Use these only for leads, and label the result **Reported**.

## Method
1. Write the exact question and the decision it supports.
2. Use `WebSearch` with specific terms (place + rule or metric + year). Then `WebFetch` the best 1–3 pages and read them. Do not rely on search snippets.
3. Cross-check any number that matters against a second independent source.
4. Record for each fact: value, source URL, publication or as-of date, and confidence label.
5. Flag conflicts explicitly (e.g. county pages that still describe pet care center licences even though Animal Services says it stopped issuing them).

## Known traps in this project
- Miami-Dade has **34 municipalities plus unincorporated areas**. Rules differ by jurisdiction, so always name the one you mean.
- County animal-business licensing changed recently (`docs/05-permits-licenses.md`). Verify it before relying on it.
- Rover and Care.com prices are for individual sitters, not facilities.
- Metro figures (Miami–Fort Lauderdale–West Palm Beach) are not Miami-Dade figures.
- Florida's minimum wage rises every 30 September.

## Output
A short findings table (`Fact | Value | Source | Date | Label`), then your interpretation. If a finding should update the research pack, say which file and line, and propose the edit. Do not edit `docs/` unless asked.
