import yfinance as yf


def get_price(ticker: str) -> float:
    try:
        info = yf.Ticker(ticker).fast_info
        return info["last_price"]
    except:
        pass


def get_prices(tickers: list[str]) -> dict[str, float]:
    prices = {}
    for t in tickers:
        prices[t] = get_price(t)
    return prices


def get_company_name(ticker: str) -> str:
    return yf.Ticker(ticker).info.get("shortName", ticker)


def get_previous_close(ticker: str) -> float:
    return yf.Ticker(ticker).info.get("previousClose", 0.0)
