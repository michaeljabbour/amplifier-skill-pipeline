# Stage: Environment Promotion
## When to Use
Project deploys to multiple environments (dev, staging, production).
## APR Pattern
```yaml
stages:
  - name: "deploy-staging"
    depends_on: ["ci"]
    condition: "trigger == push AND branch == main"
    environment: "staging"
  - name: "deploy-production"
    depends_on: ["deploy-staging"]
    condition: "trigger == push AND branch == main"
    environment: "production"
```
## Promotion Rules
| Environment | Trigger | Approval | Branch |
|---|---|---|---|
| dev | Push to any branch | None | Any |
| staging | Push to main | None or auto | main |
| production | After staging succeeds | Required (manual) | main |
## Pitfalls
- Deploying to production without staging verification
- Missing approval gates on production
- Not gating on specific branch — deploys from feature branches
