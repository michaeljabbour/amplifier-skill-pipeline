---
mode:
  name: cicd-verify
  description: Validate generated CI/CD configs — syntax checks, structural validation, drift detection

tools:
  safe:
    - read_file
    - glob
    - grep
    - bash
    - delegate
    - load_skill
  default_action: block

transitions:
  - cicd-explore
  - cicd-generate
  - cicd-debug
---

# CI/CD Verify Mode

You are in the **validation phase**. Generated CI/CD configs will be verified.

## Verification Checklist

### 1. Syntax Validation
```bash
# GitHub Actions — actionlint
actionlint .github/workflows/*.yml

# YAML validity
python3 -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml'))"

# Schema validation (if available)
check-jsonschema --builtin-schema vendor.github-workflows .github/workflows/*.yml
```

### 2. Structural Checks
- [ ] All secrets referenced in workflows exist in secrets manifest
- [ ] All artifact uploads have matching downloads (or are retained for reporting)
- [ ] All job dependencies (`needs:`) point to existing jobs
- [ ] All environment references point to documented environments
- [ ] Timeout values are set on all jobs

### 3. Drift Detection
Compare `.cicd/apr.yaml` against generated configs:
- [ ] Every APR stage has a corresponding workflow stage
- [ ] Every APR secret is referenced in the workflow
- [ ] Every APR trigger is configured in the workflow

### 4. Best Practice Checks
- [ ] Permissions explicitly set (not default `write-all`)
- [ ] Action versions pinned (`@v4` not `@main`)
- [ ] Concurrency group configured for PRs
- [ ] Cache keys use hash-based patterns

## Rules

- **Read + execute only** — can run validation tools, cannot modify generated files
- **Report all findings** — pass or fail
- **If issues found** — offer to return to `/cicd-generate` to regenerate
