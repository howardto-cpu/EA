import yfinance as yf
from datetime import date

# Tickers: yfinance symbol -> (display name, currency)
TICKERS = {
    "BRK-B":     ("BRK.B",     "USD"),
    "KWEB":      ("KWEB",      "USD"),
    "NKE":       ("NKE",       "USD"),
    "IBIT":      ("IBIT",      "USD"),
    "DTCR":      ("DTCR",      "USD"),
    "ZWU.TO":    ("ZWU.TO",    "CAD"),
    "ZNQ.TO":    ("ZNQ.TO",    "CAD"),
    "ZWB.TO":    ("ZWB.TO",    "CAD"),
    "ETHH-B.TO": ("ETHH-B.TO", "CAD"),
}

today = date.today().strftime("%Y-%m-%d")
rows = []

for yf_symbol, (display, currency) in TICKERS.items():
    try:
        t = yf.Ticker(yf_symbol)
        info = t.fast_info
        price = info.last_price
        prev_close = info.previous_close
        day_high = info.day_high
        day_low = info.day_low
        change_pct = ((price - prev_close) / prev_close) * 100
        sign = "+" if change_pct >= 0 else ""
        rows.append(
            f"| {display:<10} | ${price:.2f} {currency:<3} | {sign}{change_pct:.2f}% | ${day_high:.2f} | ${day_low:.2f} |"
        )
    except Exception as e:
        rows.append(f"| {display:<10} | ERROR | — | — | — |")
        print(f"Error fetching {yf_symbol}: {e}")

header = f"# Stock Check — {today}\n\n"
header += "| Ticker     | Price        | Change  | Day High | Day Low |\n"
header += "|------------|--------------|---------|----------|---------|\n"

output = header + "\n".join(rows) + "\n\n"
output += "*USD: BRK.B, KWEB, NKE, IBIT, DTCR — CAD: ZWU.TO, ZNQ.TO, ZWB.TO, ETHH-B.TO*\n"
output += "*Source: Yahoo Finance*\n"

filepath = f"projects/stocks/{today}.md"
with open(filepath, "w") as f:
    f.write(output)

print(f"Saved {filepath}")
print(output)
