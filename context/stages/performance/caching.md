# Stage: Caching Strategy
## Principles
1. **Key on content hash** — `{{ hashFiles('lockfile') }}`, never timestamps
2. **Restore keys for partial hits** — `node-` prefix catches older caches
3. **Cache the store, not the output** — `~/.npm` not `node_modules`
4. **Separate fast and slow caches** — dependency cache vs build cache
## Common Cache Keys
| What | Key Pattern | Paths |
|---|---|---|
| npm | `node-{{ hashFiles('package-lock.json') }}` | `~/.npm` |
| uv | `uv-{{ hashFiles('uv.lock') }}` | `~/.cache/uv` |
| Go | `go-{{ hashFiles('go.sum') }}` | `~/go/pkg/mod` |
| Docker layers | `docker-{{ hashFiles('Dockerfile') }}` | GHA cache backend |
