# trial_stock_repo

A real-time-ish portfolio tracker for ASX-listed stocks, built on
[yfinance](https://pypi.org/project/yfinance/).

## Setup

```bash
pip install -r requirements.txt
```

## Usage

### Web dashboard

```bash
python -m uvicorn stockwatch.server:app --reload
```

Then open http://127.0.0.1:8000/. The page shows the portfolio total, a
running average price, the holdings table, and the day's gainers/losers,
auto-refreshing on the interval set in `watchlist.json`. It also reports the
backend response time for each refresh, so backend performance changes are
visible directly on the page.

### Terminal loop

```bash
python -m stockwatch.main
```

Prints the same data to stdout on a loop and appends a line to
`portfolio.log` each cycle.

The tracked tickers, share counts, and refresh interval are configured in
`watchlist.json`.
