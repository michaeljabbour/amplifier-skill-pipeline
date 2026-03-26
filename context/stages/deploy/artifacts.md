# Stage: Artifact Management
## When to Use
Pipeline produces artifacts that need to be shared between jobs or retained.
## APR Pattern
```yaml
artifacts:
  - name: "build-output"
    produced_by: "build"
    consumed_by: ["deploy"]
    paths: ["dist/", "build/"]
    retention_days: 30
  - name: "test-results"
    produced_by: "test"
    consumed_by: null
    paths: ["test-results/", "coverage/"]
    retention_days: 14
```
## Guidelines
- Upload only what's needed — not entire `node_modules`
- Set retention appropriate to purpose (test reports: 14d, releases: 90d)
- Use artifacts for inter-job data, not caching (cache is for speed, artifacts for data)
