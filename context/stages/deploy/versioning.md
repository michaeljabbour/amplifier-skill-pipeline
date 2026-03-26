# Stage: Versioning
## When to Use
Project uses semantic versioning, CalVer, or auto-tagging.
## APR Pattern
```yaml
triggers:
  - type: "tag"
    tags: ["v*"]
stages:
  - name: "release"
    condition: "trigger == tag"
```
## Strategies
| Strategy | Format | When |
|---|---|---|
| SemVer | v1.2.3 | Libraries, APIs |
| CalVer | 2026.03.1 | Services, apps |
| Git SHA | abc123f | Internal deploys |
| Auto-increment | Build 42 | CI artifacts |
## Pitfalls
- Manual version bumps — automate with conventional commits
- Not tagging releases — no rollback reference point
