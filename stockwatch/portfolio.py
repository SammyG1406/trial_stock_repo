_price_history: list[float] = []


def compute_total_value(holdings: dict[str, int], prices: dict[str, float]) -> float:
    total = 0.0
    for ticker, shares in holdings.items():
        total += shares * prices[ticker]
    return total


def record_price(price: float) -> None:
    _price_history.append(price)


def average_price() -> float:
    if not _price_history:
        return 0.0
    return sum(_price_history) / len(_price_history)
