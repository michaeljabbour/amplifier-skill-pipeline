# Stage: Linting
## When to Use
Any project with a configured linter.
## APR Pattern
```yaml
- name: "lint"
  steps:
    - { name: "Run linter", type: "run", command: "<ruff check src/ | eslint . | golangci-lint run>" }
```
## Linter Commands
| Language | Linter | Command |
|---|---|---|
| Python | ruff | `ruff check src/` |
| JS/TS | eslint | `npx eslint .` |
| Go | golangci-lint | `golangci-lint run` |
| Rust | clippy | `cargo clippy -- -D warnings` |
| .NET | dotnet format | `dotnet format --verify-no-changes` |
## Optimization
- Lint runs fast — put in the quality job, run first to fail fast
- Cache linter state when possible (eslint `--cache`)
