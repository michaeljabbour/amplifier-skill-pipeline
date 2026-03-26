---
mode:
  name: cicd-audit
  description: Analyze existing CI/CD configs, score against best practices, produce audit report

tools:
  safe:
    - read_file
    - glob
    - grep
    - delegate
    - load_skill
    - web_search
    - web_fetch
  warn:
    - bash
  default_action: block

transitions:
  - cicd-design
  - cicd-explore
  - cicd-debug
---

# CI/CD Audit Mode

You are in the **analysis phase**. Existing CI/CD configs will be analyzed and scored.

## What Happens in This Mode

1. **Locate existing CI configs** — `.github/workflows/`, `.gitlab-ci.yml`, `azure-pipelines.yml`, `Jenkinsfile`
2. **Delegate to Pipeline Auditor** with the config files
3. **Present the audit report** — scores, critical issues, recommendations
4. **Route based on user intent:**
   - User wants to fix issues → `/cicd-design` with audit findings as input
   - User just wanted a report → exit

## Rules

- **Read-only mode** — don't modify any files
- **Present findings conversationally** — don't dump the raw report
- **Prioritize recommendations** — most impactful first
- **Offer to fix** — "Want me to design improvements for the critical issues?"
