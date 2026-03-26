# Stage: Dependency Scanning
## When to Use
Always — every project has dependencies with potential vulnerabilities.
## APR Pattern
```yaml
- name: "dependency-scan"
  steps:
    - { name: "Scan dependencies", type: "run", command: "<npm audit --audit-level=high | pip-audit | govulncheck ./... | cargo audit>" }
```
## Tools by Language
| Language | Tool | Command |
|---|---|---|
| Node.js | npm audit | `npm audit --audit-level=high` |
| Python | pip-audit | `pip-audit` |
| Go | govulncheck | `govulncheck ./...` |
| Rust | cargo-audit | `cargo audit` |
| Any | Trivy | `trivy fs --severity HIGH,CRITICAL .` |
| Any | Snyk | `snyk test` |
## Pitfalls
- Blocking on low-severity findings — filter to HIGH and CRITICAL
- Not running on schedule — new CVEs appear after code freeze
