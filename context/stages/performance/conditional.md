# Stage: Conditional Execution
## When to Use
Skip unnecessary work based on what changed.
## Patterns
### Path Filtering
```yaml
triggers:
  - type: "push"
    paths: ["src/**", "tests/**"]
    paths_ignore: ["docs/**", "*.md", "*.txt"]
```
### Branch Conditions
```yaml
condition: "branch == main"           # Deploy only from main
condition: "trigger == pull_request"   # PR-only checks
condition: "trigger == tag"            # Release on tags
```
### Change Detection
For monorepos, detect which packages changed:
```yaml
steps:
  - { name: "Detect changes", type: "run", command: "turbo run build --filter=[HEAD^1]" }
```
## Optimization
- Skip heavy E2E tests when only docs changed
- Skip Docker build when only tests changed
- Run full suite on main, filtered on PRs
