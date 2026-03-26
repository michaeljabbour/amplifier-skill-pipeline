# Stage: Release
## When to Use
Project publishes releases (GitHub Releases, changelogs, package publishing).
## APR Pattern
```yaml
- name: "release"
  condition: "trigger == tag AND tag matches v*"
  steps:
    - { name: "Generate changelog", type: "run", command: "conventional-changelog -p angular -i CHANGELOG.md -s" }
    - { name: "Create release", type: "run", command: "gh release create $TAG --generate-notes" }
```
## Pitfalls
- Not generating changelogs — users need to know what changed
- Manual release creation — automate from tag push
