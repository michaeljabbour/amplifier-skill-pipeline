# Stage: Rust Build
## When to Use
Project has `Cargo.toml`.
## APR Pattern
```yaml
steps:
  - { name: "Set up Rust", type: "setup", tool: "rust", version: "<from rust-toolchain.toml>" }
  - { name: "Build", type: "run", command: "cargo build --release", cache_key: "cargo-{{ hashFiles('Cargo.lock') }}", cache_paths: ["~/.cargo/registry", "~/.cargo/git", "target/"] }
```
## Caching
Cache `~/.cargo/registry`, `~/.cargo/git`, and `target/`. Consider `sccache` for distributed caching.
## Pitfalls
- Not caching `target/` — Rust compilation is extremely slow from scratch
- Use debug builds for CI checks, release for deployment
