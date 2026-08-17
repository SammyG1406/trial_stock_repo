def format_currency(value: float) -> str:
    return f"${value:,.2f}"


def render_table(names: dict[str, str], prices: dict[str, float]) -> str:
    rows = list(prices.items())
    rows.sort(key=lambda r: r[0])
    lines = []
    for ticker, price in rows:
        name = names.get(ticker, ticker)
        lines.append(f"{ticker:10s} {name:25s} {format_currency(price)}")
    return "\n".join(lines)
