---
bundle:
  name: cicd
  version: 0.1.0

includes:
  - behaviors/core

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
