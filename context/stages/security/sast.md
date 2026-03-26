# Stage: Static Application Security Testing (SAST)
## When to Use
Projects with enough code to warrant analysis (>1000 lines). Always for security-sensitive apps.
## APR Pattern
```yaml
- name: "sast"
  steps:
    - { name: "Run SAST", type: "run", command: "<semgrep scan --config auto | codeql analyze>" }
```
## Tools
| Tool | Best For | Command |
|---|---|---|
| Semgrep | Fast, multi-language | `semgrep scan --config auto` |
| CodeQL | Deep analysis (GitHub native) | Platform-specific action |
| Bandit | Python-specific | `bandit -r src/` |
## Optimization
- Semgrep is fastest for CI — CodeQL can take 10+ minutes
- Run SAST in parallel with other jobs
