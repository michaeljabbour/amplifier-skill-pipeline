# Stage: Integration Tests
## When to Use
Project has service dependencies (databases, caches, message queues) or `docker-compose.yml`.
## APR Pattern
```yaml
- name: "test-integration"
  services:
    - { name: "postgres", image: "postgres:16", ports: ["5432:5432"], env: { POSTGRES_DB: "test", POSTGRES_PASSWORD: "test" }, health_check: "pg_isready" }
    - { name: "redis", image: "redis:7", ports: ["6379:6379"], health_check: "redis-cli ping" }
  steps:
    - { name: "Run integration tests", type: "run", command: "<test command>", env: { DATABASE_URL: "postgresql://postgres:test@localhost:5432/test" } }
```
## Common Services
| Service | Image | Health Check |
|---|---|---|
| PostgreSQL | `postgres:16` | `pg_isready -U postgres` |
| MySQL | `mysql:8` | `mysqladmin ping -h localhost` |
| Redis | `redis:7` | `redis-cli ping` |
| MongoDB | `mongo:7` | `mongosh --eval "db.runCommand('ping')"` |
| Elasticsearch | `elasticsearch:8` | `curl localhost:9200/_cluster/health` |
## Pitfalls
- Not waiting for service health — tests start before DB is ready
- Hardcoded connection strings — use environment variables
- Not isolating test databases — tests interfere with each other
