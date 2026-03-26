# Stage: .NET Build
## When to Use
Project has `*.csproj`, `*.fsproj`, or `*.sln` files.
## APR Pattern
```yaml
steps:
  - { name: "Set up .NET", type: "setup", tool: "dotnet", version: "<from global.json>" }
  - { name: "Restore", type: "run", command: "dotnet restore", cache_key: "nuget-{{ hashFiles('**/*.csproj') }}", cache_paths: ["~/.nuget/packages"] }
  - { name: "Build", type: "run", command: "dotnet build --no-restore --configuration Release" }
```
## Caching
Cache `~/.nuget/packages`. Key on `*.csproj` hashes.
## Pitfalls
- Not using `--no-restore` after explicit restore — double restores waste time
- Missing `global.json` — SDK version varies
