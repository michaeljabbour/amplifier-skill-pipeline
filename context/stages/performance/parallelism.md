# Stage: Parallelism
## Strategies
### Matrix Builds
Run the same job across multiple configurations:
```yaml
matrix:
  enabled: true
  dimensions:
    - { name: "python-version", values: ["3.11", "3.12", "3.13"] }
    - { name: "os", values: ["ubuntu-latest", "macos-latest"] }
  fail_fast: true
```
### Job Splitting
Split independent work into parallel jobs:
- quality (lint + format + typecheck) || test (unit + integration) || security (scan)
### Test Sharding
Split large test suites across workers:
```yaml
matrix:
  dimensions:
    - { name: "shard", values: ["1/4", "2/4", "3/4", "4/4"] }
```
## Pitfalls
- Matrix explosion — 3 Python x 3 OS = 9 jobs. Keep dimensions small.
- `fail_fast: false` when you want — sometimes you need all results
