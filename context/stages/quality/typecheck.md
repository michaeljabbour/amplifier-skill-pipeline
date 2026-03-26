# Stage: Type Checking
## When to Use
Project has a type checker configured (pyright, tsc, mypy).
## APR Pattern
```yaml
- name: "typecheck"
  steps:
    - { name: "Type check", type: "run", command: "<pyright src/ | tsc --noEmit | mypy src/>" }
```
## Type Checker Commands
| Language | Checker | Command |
|---|---|---|
| Python | pyright | `pyright src/` |
| Python | mypy | `mypy src/` |
| TypeScript | tsc | `tsc --noEmit` |
## Pitfalls
- Running tsc with `--build` when only checking — `--noEmit` is faster
- Missing type stubs — install `types-*` packages
