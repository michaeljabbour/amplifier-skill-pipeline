# Stage: Python Build
## When to Use
Project has `pyproject.toml`, `setup.py`, or `requirements.txt`.
## APR Pattern
```yaml
steps:
  - { name: "Set up Python", type: "setup", tool: "python", version: "<from .python-version>" }
  - { name: "Install dependencies", type: "run", command: "<uv sync --frozen | pip install -r requirements.txt>", cache_key: "<uv-{{ hashFiles('uv.lock') }}>" }
```
## Package Manager Detection
| Signal | Manager | Install Command |
|---|---|---|
| `uv.lock` | uv | `uv sync --frozen` |
| `poetry.lock` | poetry | `poetry install --no-interaction` |
| `Pipfile.lock` | pipenv | `pipenv install --deploy` |
| `requirements.txt` | pip | `pip install -r requirements.txt` |
## Caching
uv: `~/.cache/uv` keyed on `uv.lock`. pip: `~/.cache/pip` keyed on `requirements*.txt`.
## Pitfalls
- Not pinning Python version — use `.python-version`
- Missing `--frozen` flag — lockfile must be source of truth in CI
