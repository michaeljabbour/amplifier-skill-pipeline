# Stage: Coverage Reporting
## When to Use
Always — coverage provides signal on test quality.
## APR Pattern
```yaml
steps:
  - { name: "Run tests with coverage", type: "run", command: "<test command with coverage flags>" }
  - { name: "Upload coverage", type: "upload", artifact_name: "coverage-report", artifact_paths: ["coverage.xml", "coverage/"] }
```
## Coverage Thresholds
Recommend setting minimum thresholds:
- **New projects:** Start at current coverage, ratchet up over time
- **Mature projects:** 80%+ line coverage is a reasonable target
- **Don't block on coverage alone** — 100% coverage with bad tests is worse than 70% with good tests
## Pitfalls
- Coverage as a merge gate without exceptions — some code is hard to test and that's OK
- Not tracking coverage trends — single snapshot is less useful than direction
- Measuring coverage of generated code — exclude generated files
