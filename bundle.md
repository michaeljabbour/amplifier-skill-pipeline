---
bundle:
  name: cicd
  version: 1.0.0

includes:
  - behaviors/core

agents:
  pipeline-scout:
    source: agents/pipeline-scout.md
  pipeline-architect:
    source: agents/pipeline-architect.md
  platform-generator:
    source: agents/platform-generator.md
  pipeline-auditor:
    source: agents/pipeline-auditor.md
  secrets-assessor:
    source: agents/secrets-assessor.md
  pipeline-documenter:
    source: agents/pipeline-documenter.md

tools: []
---

# CI/CD Pipeline Bundle

Designs, generates, audits, and maintains CI/CD pipelines for applications.

## Entry Points

| Intent | Path |
|---|---|
| New project, no CI/CD | Greenfield: detect → design → generate → verify |
| Migrate from another platform | Migration: audit source → design → generate → verify |
| Pipeline is slow or flaky | Optimization: audit → design improvements → generate → verify |
| Review existing pipeline | Audit: analyze → score → report |

## How It Works

1. **Pipeline Scout** inspects your project and produces a Project Profile
2. **Pipeline Architect** designs an Abstract Pipeline Representation (APR)
3. **Platform Generator** renders the APR into native CI/CD config (GitHub Actions, GitLab CI, Azure DevOps)
4. **Pipeline Auditor** can analyze existing pipelines for improvements
5. **Secrets Assessor** configures secrets when safe, provides guidance when not
6. **Pipeline Documenter** generates human-readable pipeline documentation

## Modes

| Mode | Phase |
|---|---|
| `/cicd-explore` | Discover project tech stack and CI/CD needs |
| `/cicd-design` | Design the Abstract Pipeline Representation |
| `/cicd-audit` | Analyze existing CI/CD configs and score |
| `/cicd-generate` | Render APR into native platform configs |
| `/cicd-verify` | Validate generated configs |
| `/cicd-debug` | Diagnose pipeline issues |

## Recipes

| Recipe | Track |
|---|---|
| `cicd-full-pipeline.yaml` | Autonomous end-to-end generation |
| `cicd-guided-pipeline.yaml` | Interactive with approval gates |
| `cicd-audit-report.yaml` | Standalone audit report |
| `cicd-migration.yaml` | Platform-to-platform migration |
