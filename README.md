# trial_stock_repo

A terminal-based real-time-ish portfolio tracker for ASX-listed stocks, built on
[yfinance](https://pypi.org/project/yfinance/).

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python -m stockwatch.main
```

The tracked tickers, share counts, and refresh interval are configured in
`watchlist.json`. Each cycle the app prints the current portfolio value, a
running average price, a per-ticker price table, and the day's top gainers
and losers, then appends a log line to `portfolio.log`.
