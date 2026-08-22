# Practice Data

**This course ships no data set, by design.** Every series the labs use is public, and
pulling it yourself is the first exercise — a model is only as honest as the extraction
that fed it. One script does the whole job.

```bash
pip install -r requirements.txt
python fetch_data.py --end 2026-08-20
```

Six CSVs land in `data_out/`. That is the entire data footprint of the sixteen weeks.

---

## What gets pulled

All of it comes from Yahoo Finance through [`yfinance`](https://pypi.org/project/yfinance/),
adjusted for splits and dividends (`auto_adjust=True`), daily, from 2015-01-01.

| File | Ticker | What it is | First needed |
|---|---|---|---|
| `returns.csv` | `AAPL` | primary asset — close, simple return, log return | **Week 1 Part 1** |
| `pair_KO_PEP.csv` | `KO`, `PEP` | two related large caps, closes only | Week 2 Part 3 |
| `index_GSPC.csv` | `^GSPC` | S&P 500 — close and both returns | Week 3 |
| `vix.csv` | `^VIX` | CBOE volatility index, close | Week 5 Part 2 |
| `kospi.csv` | `^KS11` | KOSPI composite — close and both returns | Week 6 |
| `short_rate.csv` | `^IRX` | 13-week T-bill yield, **converted to decimals** | Week 12 |

`returns.csv` is the spine. Week 1 Lab 1 creates it; Labs 2 and 3 reuse it; Week 2 runs
ADF and KPSS on it and on the underlying price level. From Week 3 onward the labs say
"a real asset" or "a real index" without naming one — that is deliberate, and any of
these files answers it.

Change the primary asset whenever you like:

```bash
python fetch_data.py --ticker MSFT --only returns
```

---

## Pin the end date

The lab prompts say *"from 2015-01-01 to today"*. For exploration that is fine. For
anything you hand in it is not: two students never hold the same series, and a number
you printed in March will not reproduce in May.

```bash
python fetch_data.py --end 2026-08-20      # the course reference date
```

Every run writes `data_out/MANIFEST.json` with the window, the row counts, the date range
and a short SHA-256 of each file. Quote the manifest in your write-up and your results
become checkable. Treat the hashes as a self-check between your own runs rather than a
guarantee — vendors do occasionally restate history, and a changed hash on an unchanged
command is itself worth noticing.

At the reference date the pull is 2,849–2,925 rows per series, 2015-01-02 through
2026-08-19.

---

## Weeks that need nothing

Most of the practice cases are hand-worked from numbers printed on the slide, so no
download is involved at all:

- **Week 9 Part 3, nowcasting** — the lab *builds* a few monthly indicators from one
  common factor plus a quarterly target. It is synthetic on purpose, so you can see the
  ragged-edge machinery work against a known truth. No macro vendor, no API key.
- **Weeks 2, 3, 6, 10, 11, 12, 14** — the simulation cases fix a seed and generate their
  own paths. Reproducibility is exact.
- **Every "Worked by Hand" case** — the price paths, returns and matrices are printed on
  the slides. Match every digit before you run anything.

---

## If Yahoo is unreachable

Yahoo has no service guarantee and campus networks sometimes block it. Symptoms are an
empty frame, a `JSONDecodeError`, or a long hang.

1. **Upgrade first.** `pip install -U yfinance` — most breakages are fixed within days.
2. **Slow down.** Rate limiting looks like intermittent empty frames. Re-run; the script
   already uses `threads=False`.
3. **Switch source.** [Stooq](https://stooq.com/) needs no key and covers US equities and
   indices: `pip install pandas-datareader`, then
   `pandas_datareader.data.DataReader("AAPL", "stooq", start, end)` — note it returns
   newest-first, so `.sort_index()`. For US macro and Treasury series,
   [FRED](https://fred.stlouisfed.org/) is the reference source and its CSV endpoint needs
   no key.
4. **Any CSV with a date index and a close column works.** Nothing in the labs depends on
   the vendor. If you already hold a price history you trust, point the labs at it.

---

## Licensing

The price data belongs to its providers and is pulled under their terms for classroom use.
Nothing in this repository redistributes it — you extract your own copy, which is the
point of the exercise.
