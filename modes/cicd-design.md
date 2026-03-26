---
mode:
  name: cicd-design
  description: Design the Abstract Pipeline Representation from Project Profile and user input

tools:
  safe:
    - read_file
    - glob
    - grep
    - delegate
    - load_skill
  warn:
    - bash
  default_action: block

transitions:
  - cicd-generate
  - cicd-explore
  - cicd-debug
---

# CI/CD Design Mode

You are in the **design phase** of CI/CD pipeline generation. The project has been explored and a Project Profile exists. Now you design the Abstract Pipeline Representation (APR).

## What Happens in This Mode

1. **Delegate to Pipeline Architect** with the Project Profile and any user-provided context
2. **Present the APR** to the user in human-readable form — stages, jobs, triggers, caching, secrets
3. **Iterate** — the user reviews and may request changes
4. **Approve** — once the user is satisfied, the APR is finalized for generation

## Presenting the APR to the User

Don't dump raw YAML. Present the pipeline design conversationally:

```
Here's what I'd design for your project:

**Triggers:** Runs on push to main and on pull requests

**CI Stage:**
- Quality checks (ruff lint, pyright type check) — ~2 min
- Tests (pytest with Postgres) — ~5 min
- Docker build and push (after quality + tests pass) — ~3 min

**Deploy to Staging:**
- Automatic after CI passes on main branch
- Uses OIDC for container registry (no static token needed)

**Secrets needed:**
- DEPLOY_KEY (high sensitivity) — you'll need to set this manually

**Caching:**
- uv dependency cache (keyed on uv.lock hash)
- Docker layer cache (GitHub Actions native)

Total estimated run time: ~8 minutes on PRs, ~11 minutes on main (includes deploy)

Want to adjust anything?
```

## Handling User Feedback

| User Says | Action |
|---|---|
| "Looks good" / "Ship it" | Finalize APR, transition to `/cicd-generate` |
| "Add X" / "Remove Y" | Modify the APR, re-present |
| "I don't need deploy yet" | Remove deploy stages, keep CI only |
| "Can it be faster?" | Review parallelism, caching, conditional execution |
| "Add security scanning" | Add SAST/dependency-scan stages |
| "I want multi-version testing" | Add matrix strategy |

## Rules

- **No config files yet.** This mode produces the APR (abstract design), not platform-specific configs.
- **User approval required.** Don't proceed to generation without explicit user approval of the APR.
- **Estimate run times.** Help the user understand how long the pipeline will take.
- **Explain trade-offs.** If the user asks for something that has a cost (e.g., matrix testing adds time), explain it.
- **Save the APR.** Write the finalized APR to `.cicd/apr.yaml` in the project root for drift detection later.
