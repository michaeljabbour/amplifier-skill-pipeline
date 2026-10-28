# Pipeline

Turn a project’s actual build and release needs into a reviewable pipeline across CI platforms.

## Consolidated capability

Portable method: [skills/pipeline/SKILL.md](skills/pipeline/SKILL.md). Install with `python3 scripts/capability.py install --dest ~/.agents/skills`. See [consolidation and runtime boundaries](docs/CONSOLIDATION.md). The retained source guide below documents the optional original host integration and historical evidence; it is not a new outcome claim.

## Retained source guide

### amplifier-bundle-cicd

An Amplifier application bundle that designs, generates, audits, and maintains CI/CD pipelines for applications.

## What It Does

Point this bundle at any project and it will:

1. **Detect** your tech stack — languages, frameworks, build tools, test runners, Docker, existing CI configs
2. **Design** a pipeline — choosing stages, jobs, triggers, caching, security scanning, and deployment gating
3. **Generate** native CI/CD configs — GitHub Actions (deep support), GitLab CI, Azure DevOps
4. **Document** the pipeline — what it does, why each stage exists, how to customize
5. **Manage secrets** — configure them when safe, guide you when not
6. **Revisit** later — audit, optimize, migrate, or update as your project evolves

## Four Entry Points

| You say... | The bundle does... |
|---|---|
| "Set up CI/CD for this project" | **Greenfield** — detects your project, designs a pipeline, generates configs |
| "Migrate from Jenkins to GitHub Actions" | **Migration** — analyzes your current pipeline, maps to new platform |
| "My pipeline is slow" | **Optimization** — audits your pipeline, identifies bottlenecks, proposes fixes |
| "Review my pipeline" | **Audit** — analyzes and scores your pipeline against best practices |

## Architecture

The bundle separates **pipeline design** from **platform rendering** using an Abstract Pipeline Representation (APR):

```
Your Project --> Pipeline Scout --> Project Profile
                                        |
                                Pipeline Architect --> APR (platform-agnostic)
                                                        |
                                                Platform Generator --> Native CI/CD Config
```

This means:
- One pipeline design serves multiple platforms
- Migration is just re-rendering an APR to a different platform
- Auditing compares APR intent vs. actual config (drift detection)

## Platforms

| Platform | Support Level |
|---|---|
| GitHub Actions | Deep — full idioms, optimization, validation |
| GitLab CI | Solid — correct configs with platform idioms |
| Azure DevOps | Solid — correct configs with platform idioms |

## Quick Start

```
# Interactive — guided pipeline design
/cicd-explore

# Autonomous — end-to-end, hands-off
"Set up CI/CD for this project, go autonomous"

# Audit only
"Audit my pipeline"
```

## Bundle Structure

```
amplifier-bundle-cicd/
  bundle.md                  -- Thin router (entry point)
  context/
    instructions.md          -- Routing logic and agent reference
    philosophy.md            -- Design principles
    schemas/
      project-profile.md    -- What Pipeline Scout produces
      apr-schema.md          -- Abstract Pipeline Representation
    stages/                  -- Composable stage primitives
    platforms/               -- Platform-specific rendering context
  agents/                    -- Specialized agents
  behaviors/core/            -- Shared context all agents inherit
  modes/                     -- Workflow phase modes
  recipes/                   -- Workflow recipes
```

## License

MIT
