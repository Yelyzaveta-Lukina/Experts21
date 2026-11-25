---
name: consult-experts
description: Ask the Miami doggy day care expert team a question. The orchestrator picks the right experts, has them work together, and returns one combined answer.
argument-hint: "[your question]"
disable-model-invocation: true
context: fork
agent: expert-orchestrator
background: false
---

Answer the following question for the Miami doggy day care project, using the expert team as described in your instructions. Select the right experts, brief them, cross-check their outputs and return one combined answer.

Question: $ARGUMENTS
