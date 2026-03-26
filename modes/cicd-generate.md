---
mode:
  name: cicd-generate
  description: Generate native CI/CD config files from the approved Abstract Pipeline Representation

tools:
  safe:
    - read_file
    - glob
    - grep
    - delegate
    - write_file
    - edit_file
    - apply_patch
    - bash
    - load_skill
  default_action: block

transitions:
  - cicd-verify
  - cicd-design
  - cicd-debug
---

# CI/CD Generate Mode

You are in the **generation phase**. The APR has been designed and approved. Now generate the actual CI/CD config files.

## What Happens in This Mode

1. **Delegate to Platform Generator** with the APR and target platform
2. **Delegate to Secrets Assessor** to handle secrets configuration
3. **Delegate to Pipeline Documenter** to generate pipeline documentation
4. **Write all files** to the project — config files, docs, APR copy

## Generation Checklist

- [ ] Platform config files written (e.g., `.github/workflows/ci.yml`)
- [ ] APR saved to `.cicd/apr.yaml` for drift detection
- [ ] Secrets manifest generated
- [ ] Pipeline documentation written
- [ ] All files committed

## File Outputs

| File | Purpose |
|---|---|
| `.github/workflows/*.yml` (or equivalent) | Native CI/CD config |
| `.cicd/apr.yaml` | APR snapshot for drift detection |
| `.cicd/secrets-manifest.yaml` | What secrets are needed + status |
| `.cicd/README.md` | Pipeline documentation |

## Rules

- **This mode CAN write files** — it's the only mode that writes to the user's project
- **Commit after generation** — all generated files in one commit
- **Don't modify project code** — only CI/CD config, docs, and metadata
