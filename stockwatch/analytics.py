from . import api_client


def _quote(ticker: str) -> tuple[str, float, float]:
    price = api_client.get_price(ticker)
    prev = api_client.get_previous_close(ticker)
    change_pct = (price - prev) / prev * 100 if prev else 0.0
    return ticker, price, change_pct


def get_gainers(tickers: list[str], top_n: int = 3) -> list[tuple[str, float, float]]:
    quotes = [_quote(t) for t in tickers]
    quotes.sort(key=lambda q: q[2], reverse=True)
    return quotes[:top_n]


def get_losers(tickers: list[str], top_n: int = 3) -> list[tuple[str, float, float]]:
    quotes = [_quote(t) for t in tickers]
    quotes.sort(key=lambda q: q[2])
    return quotes[:top_n]
