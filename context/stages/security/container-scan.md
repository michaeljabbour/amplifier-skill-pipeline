# Stage: Container Image Scanning
## When to Use
Project builds Docker images.
## APR Pattern
```yaml
- name: "container-scan"
  depends_on: ["build-docker"]
  steps:
    - { name: "Scan image", type: "run", command: "trivy image --severity HIGH,CRITICAL <image:tag>" }
```
## Tools
| Tool | Command |
|---|---|
| Trivy | `trivy image --severity HIGH,CRITICAL <image>` |
| Grype | `grype <image>` |
| Snyk Container | `snyk container test <image>` |
## Pitfalls
- Scanning before push — scan the built image, not the Dockerfile
- Not filtering severity — low/medium findings create noise
