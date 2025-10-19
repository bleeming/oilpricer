# OilPricer

Small Python utility to fetch, process and analyze oil price time series for modeling and reporting.

## Features
- Download oil price time series from configurable data sources.
- Cleaning, resampling and simple enrichment helpers.
- Lightweight forecasting helpers and evaluation metrics.
- CSV/JSON output and optional plotting helpers.

## Project layout
- `oilpricer/` — package source
- `scripts/` — command-line helpers
- `tests/` — unit tests
- `pyproject.toml` — packaging metadata

## Requirements
- uv for package management (see installation)
Recommended: use a dedicated virtual environment (uv will manage one for you).

## Installation (using uv)
This project uses uv for package management. If you don't have uv, install it with pip:

```bash
pip install uv
```

Install project dependencies and create the managed environment:

```bash
# install dependencies declared in pyproject.toml / requirements
uv install
# drop into the managed environment (optional)
uv shell
```

Run commands inside the environment directly with uv:

```bash
uv run python -m oilpricer.fetch --config config.yml --start 2020-01-01 --end 2023-01-01
```

Fallback: you can use a regular venv and pip:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage
As command-line modules:

```bash
uv run python -m oilpricer.fetch --config config.yml --start 2020-01-01 --end 2023-01-01
uv run python -m oilpricer.process --input data/raw.csv --output data/clean.csv
```

From Python:

```python
from oilpricer import fetch, process

df = fetch.get_prices("WTI", start="2020-01-01")
clean = process.clean_prices(df)
```

## Testing
Run tests with pytest (inside uv environment or your venv):

```bash
uv run pytest -q
# or, if inside uv shell / venv:
pytest -q
```

## Development
- Format with black/isort and run linters before committing.
- Add unit tests for new features and update CHANGELOG.
- Use feature branches and descriptive commits.

## Contributing
Fork, create a branch, add tests and a clear PR. Refer to the issue or feature discussion in the PR description.

## Contact
Add maintainer contact or GitHub handle here.