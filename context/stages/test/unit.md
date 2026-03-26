# Stage: Unit Tests
## When to Use
Any project with a test runner detected.
## APR Pattern
```yaml
- name: "test-unit"
  description: "Run unit tests"
  steps:
    - { name: "Run tests", type: "run", command: "<pytest tests/ -v | npm test | go test ./... -v>", env: { CI: "true" } }
```
## Language-Specific Commands
| Runner | Command | Coverage Flag |
|---|---|---|
| pytest | `pytest tests/ -v` | `--cov=src --cov-report=xml` |
| jest | `npx jest --ci --coverage` | Built-in with `--coverage` |
| vitest | `npx vitest run --coverage` | Built-in with `--coverage` |
| go test | `go test ./... -v` | `-coverprofile=coverage.out` |
| cargo test | `cargo test --verbose` | Use `cargo-tarpaulin` |
| dotnet test | `dotnet test --no-build` | `--collect:"XPlat Code Coverage"` |
## Pitfalls
- Not using `--ci` flag (Jest) — interactive prompts hang CI
- Missing `--no-build` (.NET) — rebuilds unnecessarily
- Not setting `CI=true` — some frameworks behave differently
