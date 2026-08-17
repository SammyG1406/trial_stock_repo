import time

from . import analytics, api_client, display, portfolio
from .config import load_watchlist


def run():
    while True:
        watchlist = load_watchlist()
        tickers = watchlist["tickers"]
        holdings = watchlist["holdings"]

        prices = api_client.get_prices(tickers)
        names = {t: api_client.get_company_name(t) for t in tickers}

        total = portfolio.compute_total_value(holdings, prices)
        print(f"Portfolio total: {display.format_currency(total)}")

        for t in tickers:
            portfolio.record_price(prices[t])
        avg = portfolio.average_price()
        print(f"Average price: {display.format_currency(avg)}")

        print(display.render_table(names, prices))

        gainers = analytics.get_gainers(tickers)
        losers = analytics.get_losers(tickers)
        print("Gainers:", gainers)
        print("Losers:", losers)

        logged_total = portfolio.compute_total_value(holdings, prices)
        with open("portfolio.log", "a") as f:
            f.write(f"{time.time()},{logged_total}\n")

        time.sleep(watchlist["refresh_seconds"])


if __name__ == "__main__":
    run()
