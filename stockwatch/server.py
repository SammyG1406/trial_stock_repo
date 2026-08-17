import time
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from . import analytics, api_client, portfolio
from .config import load_watchlist

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    watchlist = load_watchlist()
    return templates.TemplateResponse(
        request, "index.html", {"refresh_seconds": watchlist["refresh_seconds"]}
    )


@app.get("/api/portfolio")
def get_portfolio():
    start = time.perf_counter()

    watchlist = load_watchlist()
    tickers = watchlist["tickers"]
    holdings = watchlist["holdings"]

    prices = api_client.get_prices(tickers)
    names = {t: api_client.get_company_name(t) for t in tickers}

    total = portfolio.compute_total_value(holdings, prices)
    for t in tickers:
        portfolio.record_price(prices[t])
    avg = portfolio.average_price()

    rows = [
        {"ticker": t, "name": names[t], "price": prices[t]}
        for t in sorted(prices)
    ]
    gainers = [
        {"ticker": t, "price": price, "change_pct": change_pct}
        for t, price, change_pct in analytics.get_gainers(tickers)
    ]
    losers = [
        {"ticker": t, "price": price, "change_pct": change_pct}
        for t, price, change_pct in analytics.get_losers(tickers)
    ]

    elapsed_ms = (time.perf_counter() - start) * 1000

    return {
        "total": total,
        "average": avg,
        "rows": rows,
        "gainers": gainers,
        "losers": losers,
        "elapsed_ms": round(elapsed_ms, 1),
    }
