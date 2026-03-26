# Stage: Docker Build
## When to Use
Project has a `Dockerfile` and container image is a build artifact.
## APR Pattern
```yaml
- name: "build-docker"
  depends_on: ["quality", "test"]
  condition: "trigger == push AND branch == main"
  steps:
    - { name: "Set up Docker Buildx", type: "setup", tool: "docker-buildx" }
    - { name: "Login to registry", type: "run", command: "echo $TOKEN | docker login <registry> --password-stdin", secrets: ["REGISTRY_TOKEN"] }
    - { name: "Build and push", type: "run", command: "docker buildx build --push --tag <registry>/<repo>:$SHA --cache-from type=gha --cache-to type=gha,mode=max ." }
```
## Caching
Use BuildKit cache mounts for dependency layers. Use `type=gha` or `type=registry` backends. Multi-stage: cache builder stage separately.
## Pitfalls
- Not using `--cache-from` — every build starts fresh
- Building on PRs when image isn't tested — gate on main only
- Large context — use `.dockerignore`
- Not pinning base image tags — use digest or specific version
## Optimization
- Multi-platform builds add significant time — only if needed
- Layer ordering: rarely-changing first (OS deps → app deps → code)
- `docker buildx bake` for multi-service builds
