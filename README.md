<h3 align="center">🛠️ Wiki Scribe</h3>

<div align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/language-Python%203.8-blue.svg" alt="Language: Python 3.8">
  <img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="Build: passing">
  <img src="https://img.shields.io/github/stars/axentx/wiki-scribe.svg" alt="GitHub stars">
</div>

---

# 🚀 Wiki Scribe

**Power wiki administrators with automated, spoiler‑free monitoring of auto‑approved pages.**  
Wiki Scribe automatically tracks and reports on the health of your wiki, giving you instant visibility into new content, trends, and potential issues—without the risk of accidental spoilers.

## Why Wiki Scribe?

- **📈 Trend Analytics** – Get monthly and custom‑range views of auto‑approved pages with a single command.
- **🔍 Targeted Filtering** – Drill down by project, date range, or status to focus on what matters.
- **⚡ Zero‑Config Poetry** – Install and run with a single `poetry install` and `poetry run`.
- **🛡️ Spoiler‑Safe** – Built‑in detection and redaction prevent accidental cross‑contamination between arcs or chapters.
- **🧪 Test‑Driven** – All features are covered by Pytest, ensuring reliability as your wiki grows.
- **🛠️ Extensible API** – Expose a clean `WikiScribe` class that can be integrated into larger monitoring pipelines.
- **🚀 Early‑Stage, Production‑Ready** – Proven in sandbox tests and ready for real‑world deployment.

## Feature Overview

| Feature | Description |
|---------|-------------|
| Auto‑Approved Page Tracking | Monitor pages that have passed the auto‑approval pipeline. |
| Monthly Trend Reporting | View the number of approved pages per month in a concise table. |
| Project & Date Range Filters | Slice data by project name and arbitrary date ranges. |
| Data Refresh | Pull the latest data from the source wiki feed on demand. |
| Spoiler Detection & Redaction | Automatically identify and redact spoiler content before reporting. |
| CLI Interface | Simple command‑line tool for quick access to analytics. |
| Test Suite | Comprehensive Pytest coverage for all core functionalities. |

## Tech Stack

- Python
- Poetry
- Pytest

## Project Structure

```
wiki-scribe/
├── business/          # Business logic and domain models
├── docs/              # Documentation, PRD, ROADMAP, etc.
├── src/               # Core library code
│   └── wiki_scribe/   # Package source
├── tests/             # Pytest test cases
├── pyproject.toml     # Poetry configuration
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

# Run the CLI to see available commands
poetry run wiki-scribe --help
```

### Running Tests

```bash
poetry run pytest
```

## Deploy

> Wiki Scribe is a lightweight library intended to run locally or be imported into larger monitoring pipelines.  
> No container or cloud deployment is required.  
> If you wish to expose it as a service, simply wrap the CLI in a FastAPI or Flask app and deploy to your preferred platform.

## Status

Active development – last commit `ee374ac` (2026‑06‑23) added real, sandbox‑tested implementation.

## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md) guide for details on how to contribute.

## License

MIT © Axentx