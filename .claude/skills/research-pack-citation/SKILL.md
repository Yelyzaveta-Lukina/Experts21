---
name: research-pack-citation
description: House rules every Miami doggy day care expert follows. Find facts in the docs/ research pack, cite sources, label every claim Verified / Reported / Estimate, and answer in the standard Expert Brief format. Use for any answer about the Miami dog daycare project.
---

# Research pack navigation & citation

## 0. Your knowledge folder comes first
Before anything else, read `knowledge/<your-agent-name>/` (README plus relevant documents). Client documents there take precedence over `docs/` when they conflict. Flag the conflict and cite the file.

## 1. Then check the research pack
The project's shared knowledge is in `docs/` (researched November 2026). Read the relevant file before searching the web.

| File | Use it for |
|---|---|
| `docs/README.md` | Index and summary of findings |
| `docs/01-market.md` | US pet spend, Miami-Dade population, income, dog ownership, demand drivers |
| `docs/02-target-customers.md` | Segments, personas, priority neighbourhoods |
| `docs/03-competitors.md` | Local competitors, substitutes (Rover/Wag), Miami price benchmarks |
| `docs/04-costs.md` | Startup budgets, monthly opex, unit economics, break-even, KPIs |
| `docs/05-permits-licenses.md` | State, county and city rules, zoning, permits, business tax receipts, vaccines |
| `docs/06-staffing.md` | Ratios, roles, wages, schedules, training |
| `docs/07-marketing.md` | Positioning, price sheet, launch plan, channels |
| `docs/08-risks.md` | Ranked risks, mitigations, go/no-go triggers |
| `docs/expert-roster.md` | Who is on the expert team and which skills they hold |

Search with `Grep` (e.g. `Grep "Certificate of Use" docs/`) instead of reading every file.

## 2. Label every factual claim
- **Verified**: from a primary or official source (government, Census/BLS, statute or code, APPA, a franchise FDD).
- **Reported**: from a secondary source (news, directories, vendor blogs).
- **Estimate**: a modelled or assumed number. Show the formula or the assumption behind it.

Never present an Estimate as a fact. If two sources conflict, show both and say which one you rely on and why.

## 3. Cite
Cite the pack file (`docs/04-costs.md`) or the URL for any number, rule or name you use. Date-sensitive items (wages, rents, fees, laws) need an as-of date.

## 4. Answer format: Expert Brief
```
## <Persona name> (<agent-name>): <question in a few words>
Knowledge folder: <documents used, or "no documents yet">
**Bottom line:** 1–3 sentences answering the question.
**Analysis:** reasoning, tables, numbers (each labelled V/R/E with a source).
**Risks & caveats:** what could make this wrong.
**Open questions:** what needs a call, a quote or a professional to confirm.
**Handoffs:** which other expert(s) should weigh in, and on what.
```
The first line must use your persona's first name (e.g. `## Carlos (competitive-intelligence-analyst): …`). Keep it tight. Use a table instead of long prose where possible.

## 5. Boundaries
- Legal, tax, insurance and veterinary content is research context, **not professional advice**. Say that a licensed Florida professional must confirm it before money is committed.
- Do not invent competitors, prices, statutes or quotes. Say "unknown" and add it to Open questions.
- Write files only when asked. Put them in `deliverables/<your-agent-name>/`, not in `docs/`, unless the task is explicitly to update the research pack.
