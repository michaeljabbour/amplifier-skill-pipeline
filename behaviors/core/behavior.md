---
behavior:
  name: cicd-core
  description: Core behavior providing shared context for all CI/CD bundle agents

context:
  - context/instructions.md
  - context/philosophy.md
---

# CI/CD Core Behavior

This behavior provides the shared context that all agents in the CI/CD bundle inherit.

## What's Included

- **Instructions** — Entry point detection, routing logic, agent and mode reference
- **Philosophy** — Design principles governing pipeline generation and auditing

## Data Model References

Agents that need the data model schemas should @mention them directly:

- `@cicd:context/schemas/project-profile.md` — For agents that produce or consume Project Profiles
- `@cicd:context/schemas/apr-schema.md` — For agents that produce, consume, or render APRs

These are NOT included in the core behavior because not every agent needs both schemas. The Pipeline Scout needs Project Profile but not APR. The Platform Generator needs APR but not Project Profile. Each agent @mentions only what it uses.
