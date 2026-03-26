# Stage: Secrets Scanning
## When to Use
Always — leaked secrets are the most common security incident.
## APR Pattern
```yaml
- name: "secrets-scan"
  steps:
    - { name: "Scan for secrets", type: "run", command: "<gitleaks detect --source . | trufflehog filesystem .>" }
```
## Tools
| Tool | Command |
|---|---|
| gitleaks | `gitleaks detect --source . --verbose` |
| TruffleHog | `trufflehog filesystem .` |
## Note
GitHub has built-in secret scanning for public repos. This stage adds scanning for private repos and pre-commit detection.
