# Stage: Go Build
## When to Use
Project has `go.mod`.
## APR Pattern
```yaml
steps:
  - { name: "Set up Go", type: "setup", tool: "go", version: "<from go.mod>" }
  - { name: "Download modules", type: "run", command: "go mod download", cache_key: "go-{{ hashFiles('go.sum') }}", cache_paths: ["~/go/pkg/mod", "~/.cache/go-build"] }
  - { name: "Build", type: "run", command: "go build -v ./..." }
```
## Caching
Cache `~/go/pkg/mod` and `~/.cache/go-build`. Key on `go.sum`.
## Pitfalls
- Not caching build cache — Go compilation is slow without it
- Not running `go mod verify` — ensures module integrity
