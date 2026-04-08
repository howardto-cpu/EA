# Skill: Stock Check

Run this skill every weekday at 4 PM EST (near market close).

## Tickers to Watch

| Ticker     | Exchange | Notes              |
|------------|----------|--------------------|
| BRK.B      | NYSE     | Berkshire Hathaway |
| KWEB       | NYSE     | China Internet ETF |
| NKE        | NYSE     | Nike               |
| IBIT       | NASDAQ   | iShares Bitcoin Trust |
| DTCR       | NASDAQ   | —                  |
| ZWU.TO     | TSX      | BMO Covered Call Utilities ETF |
| ZNQ.TO     | TSX      | BMO NASDAQ 100 CAD Hedged ETF |
| ZWB.TO     | TSX      | BMO Covered Call Canadian Banks ETF |
| ETHH-B.TO  | TSX      | Purpose Ether CAD ETF Non-Currency Hedged |

## Steps

1. For each ticker above, fetch the current quote:
   - **US tickers** (BRK.B, KWEB, NKE, IBIT, DTCR): use https://stockanalysis.com/stocks/[TICKER]/ or https://stockanalysis.com/etf/[TICKER]/
   - **CAD tickers** (ZWU.TO, ZNQ.TO, ZWB.TO, ETHH-B.TO): use https://www.theglobeandmail.com/investing/markets/stocks/[TICKER without .TO, append -T]/ (e.g. ZWB.TO → ZWB-T, ZNQ.TO → ZNQ-T, ETHH-B.TO → ETHH-B-T)

2. For each ticker, collect:
   - Current price (in the native currency — USD for US tickers, CAD for .TO tickers)
   - Daily % change (e.g., +1.2% or -0.8%)
   - Day high
   - Day low

3. Format the results as a markdown table (see Output Format below).

4. Save the file to: `projects/stocks/YYYY-MM-DD.md` using today's date.

## Output Format

```markdown
# Stock Check — YYYY-MM-DD

| Ticker     | Price    | Change  | Day High | Day Low |
|------------|----------|---------|----------|---------|
| BRK.B      | $xxx.xx  | +x.xx%  | $xxx.xx  | $xxx.xx |
| KWEB       | $xx.xx   | -x.xx%  | $xx.xx   | $xx.xx  |
| NKE        | $xxx.xx  | +x.xx%  | $xxx.xx  | $xxx.xx |
| IBIT       | $xx.xx   | +x.xx%  | $xx.xx   | $xx.xx  |
| DTCR       | $xx.xx   | -x.xx%  | $xx.xx   | $xx.xx  |
| ZWU.TO     | $xx.xx   | +x.xx%  | $xx.xx   | $xx.xx  |
| ZNQ.TO     | $xx.xx   | +x.xx%  | $xx.xx   | $xx.xx  |
| ZWB.TO     | $xx.xx   | +x.xx%  | $xx.xx   | $xx.xx  |
| ETHH.B.TO  | $xx.xx   | +x.xx%  | $xx.xx   | $xx.xx  |

*USD tickers: BRK.B, KWEB, NKE, IBIT, DTCR*
*CAD tickers: ZWU.TO, ZNQ.TO, ZWB.TO, ETHH-B.TO*
```

5. Confirm the file was saved successfully.
