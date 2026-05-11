# Crypto Trading Robot for Binance and BitMEX

A Python desktop prototype for monitoring crypto markets, managing exchange state, and running rule-based trading strategies against Binance and BitMEX-style exchange APIs.

> **Status:** Prototype / educational trading system. Review the code, run against testnet or paper-trading infrastructure first, and never deploy real capital without independent validation.

## Why this repository exists

This project is structured to demonstrate practical trading-system concerns that recruiters and engineering reviewers look for:

- **Exchange abstractions:** normalized market, contract, balance, order, and trade models for multiple venues.
- **Strategy orchestration:** reusable strategy base class with concrete technical-analysis strategies.
- **Risk controls:** balance allocation, take-profit, stop-loss, and position-state checks around order placement.
- **Operational visibility:** logging for market-data timing, order activity, and strategy decisions.
- **Desktop workflow:** a Tkinter-oriented entry point for GUI-based control and monitoring.

This repository is currently implemented in **Python**. If you are reviewing it for C++/C# trading-engine expertise, treat it as an architecture and product prototype; pair it with language-specific repositories for direct C++/C# evidence.

## Features

- Binance and BitMEX client integration points from the application entry point.
- Market-data candle parsing from trade ticks, including missing-candle handling.
- Technical strategies:
  - **Technical Strategy:** RSI + MACD signal confirmation.
  - **Breakout Strategy:** candle breakout with minimum-volume filtering.
- Position lifecycle management for opening positions and checking take-profit / stop-loss exits.
- SQLite-backed workspace persistence for watchlists and configured strategies.
- Input validators for integer and floating-point GUI fields.
- GitHub Actions Pylint workflow across Python 3.8, 3.9, and 3.10.

## Repository layout

```text
.
├── main.py                    # Application entry point, logging setup, client wiring, GUI startup
├── strategies.py              # Strategy base class plus technical and breakout strategy implementations
├── models.py                  # Exchange-normalized balance, candle, contract, order, and trade models
├── database.py                # SQLite workspace storage for watchlists and strategies
├── utils.py                   # GUI input validation helpers
├── StartBot.bat               # Windows launcher for the virtual-environment Python interpreter
├── .github/workflows/pylint.yml
└── README.md
```

## Architecture overview

```text
Exchange API clients
        │
        ▼
Normalized models ──► Strategy engine ──► Order/risk decisions
        │                    │
        ▼                    ▼
SQLite workspace       GUI logs and controls
```

### Core flow

1. `main.py` configures console/file logging and creates Binance and BitMEX client objects.
2. The GUI root receives those clients and controls user-facing bot workflows.
3. Strategies receive normalized contracts, balances, candles, trades, and exchange metadata.
4. Incoming trades update candles; new-candle events trigger strategy checks.
5. When a signal is produced, the strategy calculates order size, opens a position, and monitors take-profit / stop-loss thresholds.

## Getting started

### Prerequisites

- Python 3.8+
- Exchange API credentials for testnet or paper-trading use
- Python packages used by the codebase, including:
  - `pandas`
  - `python-dateutil`
  - Tkinter support for your Python distribution

> The current repository snapshot references `connectors` and `interface` packages from `main.py`. Ensure those packages are present in your local checkout or restore them before running the full desktop application.

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install pandas python-dateutil
```

### Run

```bash
python main.py
```

On Windows, you can also use:

```bat
StartBot.bat
```

## Configuration and security

- Use **testnet credentials** while developing.
- Store API keys outside source control, for example in environment variables or a local ignored config file.
- Rotate any credentials that have ever been committed or shared.
- Keep `database.db`, runtime logs, and virtual environments out of production commits unless intentionally publishing sample fixtures.
- Validate exchange permissions so the bot cannot withdraw funds.

## Testing and quality checks

Basic checks used for this snapshot:

```bash
python -m py_compile main.py utils.py strategies.py database.py models.py
```

The repository also includes a Pylint workflow under `.github/workflows/pylint.yml` for push-time static analysis.

## Roadmap

To make this repository stronger for professional trading-firm review:

- Move API credentials to environment-based configuration.
- Add unit tests for candle parsing, signal generation, position sizing, and stop logic.
- Add typed exchange-client interfaces and mock clients for deterministic tests.
- Add a `requirements.txt` or `pyproject.toml` for reproducible installs.
- Add Docker or a documented local-dev bootstrap script.
- Add backtesting fixtures and performance metrics.
- Add C++/C# implementations or companion repositories if the recruiting goal is to demonstrate expert-level C++/C# specifically.

## Risk disclaimer

This project is for educational and prototyping purposes only. Cryptocurrency trading is risky, exchange APIs can change, and automated systems can lose money quickly. Do not trade real funds until you have reviewed the code, tested it thoroughly, validated the strategy independently, and understood all operational risks.
