# Stage: Node.js Build
## When to Use
Project has `package.json`.
## APR Pattern
```yaml
steps:
  - { name: "Set up Node.js", type: "setup", tool: "node", version: "<from .nvmrc>" }
  - { name: "Install dependencies", type: "run", command: "<npm ci | yarn install --frozen-lockfile | pnpm install --frozen-lockfile>", cache_key: "node-{{ hashFiles('<lockfile>') }}" }
  - { name: "Build", type: "run", command: "npm run build" }
```
## Package Manager Detection
| Lockfile | Manager | Install Command |
|---|---|---|
| `package-lock.json` | npm | `npm ci` |
| `yarn.lock` | yarn | `yarn install --frozen-lockfile` |
| `pnpm-lock.yaml` | pnpm | `pnpm install --frozen-lockfile` |
| `bun.lockb` | bun | `bun install --frozen-lockfile` |
## Caching
Cache the package manager store, not `node_modules`. Key on lockfile hash.
## Pitfalls
- `npm install` instead of `npm ci` — doesn't respect lockfile
- Caching `node_modules` — platform-specific binaries break across OS
- Missing `.nvmrc` — node version varies between runs
