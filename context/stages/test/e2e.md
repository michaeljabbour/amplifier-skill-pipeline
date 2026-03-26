# Stage: E2E Tests
## When to Use
Project has Playwright, Cypress, or similar E2E test runner.
## APR Pattern
```yaml
- name: "test-e2e"
  timeout_minutes: 30
  steps:
    - { name: "Install browsers", type: "run", command: "npx playwright install --with-deps chromium" }
    - { name: "Start app", type: "run", command: "npm run start &" }
    - { name: "Wait for app", type: "run", command: "npx wait-on http://localhost:3000" }
    - { name: "Run E2E tests", type: "run", command: "npx playwright test" }
    - { name: "Upload report", type: "upload", artifact_name: "playwright-report", artifact_paths: ["playwright-report/"] }
```
## Pitfalls
- Not installing browser dependencies — `--with-deps` handles OS-level libs
- Not waiting for app startup — race condition
- No artifact upload — can't debug failures without traces/screenshots
- Too long timeout — E2E suites can hang; set reasonable limits
## Optimization
- Run in parallel with `--workers=4`
- Shard across multiple jobs for large suites
- Only run on main branch or when relevant files change
