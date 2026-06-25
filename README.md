<h3 align="center">🛠️ wiki-scribe</h3>

<div align="center">
  <a href="https://github.com/axentx/wiki-scribe/blob/main/LICENSE"><img src="https://img.shields.io/github/license/axentx/wiki-scribe.svg?style=flat-square" alt="License: MIT"></a>
  <a href="https://github.com/axentx/wiki-scribe"><img src="https://img.shields.io/github/stars/axentx/wiki-scribe?style=social" alt="GitHub stars"></a>
  <a href="https://github.com/axentx/wiki-scribe"><img src="https://img.shields.io/github/actions/workflow/status/axentx/wiki-scribe/ci.yml?branch=main&style=flat-square" alt="Build status"></a>
  <a href="https://github.com/axentx/wiki-scribe"><img src="https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square" alt="Python 3.8+"></a>
</div>

---

# 🚀 wiki-scribe

**Power Wiki administrators with automated monitoring of auto‑approved pages.**  
Wiki Scribe is a Python project that provides a simple interface for tracking and analyzing auto‑approved wiki pages, enabling maintainers to spot trends, refresh data, and filter by project or date range.

## Why wiki-scribe?

- **📈 Trend Analytics** – Get monthly trend data for auto‑approved pages with a single method call.
- **⚡ Fast Refresh** – Refresh the underlying dataset in seconds, keeping your dashboards up‑to‑date.
- **🔍 Fine‑Grained Filters** – Filter pages by project name and arbitrary date ranges.
- **🛠️ Easy Integration** – Exposes a clean Python API that can be imported into any existing monitoring pipeline.
- **💡 Built for Wiki Administrators** – Designed specifically for maintainers who need to audit auto‑approved content without manual effort.

## Feature Overview

| Feature | Description |
|---------|-------------|
| `WikiScribe` class | Core interface for monitoring auto‑approved pages. |
| `get_monthly_trend()` | Returns a time‑series of page counts per month. |
| `refresh_data()` | Pulls the latest data from the source and updates the internal cache. |
| `filter_by_project(project_name)` | Returns pages belonging to a specific project. |
| `filter_by_date_range(start, end)` | Returns pages within a user‑defined date range. |
| `auto_approved_page` model | Lightweight representation of an auto‑approved wiki page. |

## Tech Stack

- Python
- Poetry
- Pytest

## Project Structure

```
├── business/          # Domain logic and business rules
├── docs/              # Project documentation and guides
├── src/               # Source code (WikiScribe implementation)
├── tests/             # Pytest test suites
├── pyproject.toml     # Poetry project configuration
├── requirements.txt   # Pinning of runtime dependencies
└── README.md          # This file
```

## Getting Started

```bash
# Clone the repository
git clone https://github.com/axentx/wiki-scribe.git
cd wiki-scribe

# Install dependencies with Poetry
poetry install

# Run the library (example usage)
poetry run python - <<'PY'
from src.wiki_scribe import WikiScribe, AutoApprovedPage

pages = [
    AutoApprovedPage(title="Page 1", project="ProjectA", approved_at="2026-05-01"),
    AutoApprovedPage(title="Page 2", project="ProjectB", approved_at="2026-05-15"),
]
scribe = WikiScribe(pages)
print(scribe.get_monthly_trend())
PY

# Run tests
poetry run pytest
```

## Deploy

> **Note:** This project is intended to run locally or be imported into other Python applications. No dedicated deployment target is defined at this time.

## Status

Active development. Latest commit: `feat(wiki-scribe): real, sandbox-tested implementation` (d9fe830).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT © Axentx