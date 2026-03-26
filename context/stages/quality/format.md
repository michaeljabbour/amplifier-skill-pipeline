# Stage: Format Checking
## When to Use
Project has a formatter configured.
## APR Pattern
```yaml
- name: "format-check"
  steps:
    - { name: "Check formatting", type: "run", command: "<ruff format --check src/ | prettier --check . | gofmt -l .>" }
```
## Formatter Commands
| Language | Formatter | Check Command |
|---|---|---|
| Python | ruff format | `ruff format --check src/` |
| JS/TS | prettier | `npx prettier --check .` |
| Go | gofmt | `gofmt -l . (fail if output)` |
| Rust | rustfmt | `cargo fmt -- --check` |
## Note
Format checking should be `--check` mode in CI — don't auto-fix, just report. Developers should run formatters locally.
