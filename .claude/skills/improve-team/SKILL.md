---
name: improve-team
description: Ask the team-builder meta agent to create a new expert agent or skill, or to review and improve existing ones, then validate the team.
argument-hint: "[what to create or improve]"
disable-model-invocation: true
context: fork
agent: team-builder
background: false
---

Request for the expert team: $ARGUMENTS

Follow your procedure: inspect the current agents, skills, roster and CLAUDE.md; make the change; keep the routing table, roster and CLAUDE.md in sync; run the validator; and report what changed.
