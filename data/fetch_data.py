#!/usr/bin/env python3
"""
fetch_data.py - build the course data set from public sources.

This course does not ship a data set. Every series used in the labs is public and
is pulled with `yfinance` (Yahoo Finance), so you own the extraction step from the
first week. Run this once and the files land in ./data_out/.

    python fetch_data.py                     # everything, up to today
    python fetch_data.py --end 2026-08-20    # pin the end date (reproducible)
    python fetch_data.py --ticker MSFT       # change the primary asset
    python fetch_data.py --only returns      # just the Week 1 spine

WHY PIN THE END DATE
    The lab prompts in Week 1 say "from 2015-01-01 to today". That is fine for your
    own work, but it means two students never hold the same series and a number you
    printed in March will not reproduce in May. For anything you submit, pass
    --end and record the date you used. The course reference date is 2026-08-20.

OUTPUTS (in ./data_out/)
    returns.csv        primary asset: date, close, simple, log       <- Weeks 1-2 reuse this
    pair_KO_PEP.csv    two closes for the cointegration / pairs labs
    index_GSPC.csv     S&P 500 close and returns
    vix.csv            VIX close (volatility level, Week 5)
    kospi.csv          KOSPI close and returns (Korean comparison)
    short_rate.csv     13-week T-bill yield, in decimals (Week 12)
    MANIFEST.json      what was pulled, when, how many rows, and the row hash
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

try:
    import yfinance as yf
except ImportError:
    sys.exit("yfinance is not installed.  pip install -r requirements.txt")

START = "2015-01-01"
REFERENCE_END = "2026-08-20"  # the date the course materials were checked against

# name -> (ticker, what it is, which weeks need it)
SERIES = {
    "returns":    ("AAPL",  "primary asset, adjusted close",     "1, 2, and any lab that says 'a real asset'"),
    "pair":       (("KO", "PEP"), "two related large caps",      "2 (spurious vs. real), 7 (pairs), 9, 11"),
    "index":      ("^GSPC", "S&P 500 index",                     "3, 4, 6, 10, 16"),
    "vix":        ("^VIX",  "CBOE volatility index",             "5 (compare to your GARCH fit)"),
    "kospi":      ("^KS11", "KOSPI composite",                   "6 (a second market for the VAR)"),
    "short_rate": ("^IRX",  "13-week T-bill discount rate, %",   "12 (Vasicek / CIR calibration)"),
}


def _download(ticker: str, start: str, end: str) -> pd.DataFrame:
    """One ticker, adjusted, flattened to single-level columns."""
    df = yf.download(
        ticker, start=start, end=end,
        auto_adjust=True, progress=False, threads=False,
    )
    if df is None or df.empty:
        raise RuntimeError(f"no rows returned for {ticker} - check the ticker and your connection")
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    return df


def _with_returns(close: pd.Series, name: str) -> pd.DataFrame:
    """Close plus the two return definitions from Week 1 Part 1."""
    out = pd.DataFrame({name: close.astype(float)})
    out["simple"] = out[name].pct_change()
    out["log"] = np.log(out[name]).diff()
    return out.dropna()


def _write(df: pd.DataFrame, path: Path) -> dict:
    df.to_csv(path, index_label="date", float_format="%.6f")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()[:16]
    return {
        "file": path.name,
        "rows": int(len(df)),
        "first": str(df.index.min().date()),
        "last": str(df.index.max().date()),
        "sha256_16": digest,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start", default=START, help=f"start date (default {START})")
    ap.add_argument("--end", default=None,
                    help=f"end date, exclusive. Omit for today; use {REFERENCE_END} to match the slides.")
    ap.add_argument("--ticker", default=SERIES["returns"][0], help="primary asset for returns.csv")
    ap.add_argument("--outdir", default="data_out", help="output directory (default data_out)")
    ap.add_argument("--only", nargs="*", choices=sorted(SERIES), default=sorted(SERIES),
                    help="pull only these series (default: all)")
    args = ap.parse_args()

    end = args.end or str(date.today())
    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)

    print(f"window : {args.start} -> {end}{'' if args.end else '   (not reproducible - pass --end to pin it)'}")
    print(f"outdir : {out.resolve()}\n")

    files, failed = [], []

    def step(key: str, fn):
        if key not in args.only:
            return
        try:
            info = fn()
            files.append(info)
            print(f"  ok   {info['file']:<20} {info['rows']:>5} rows  {info['first']} -> {info['last']}")
        except Exception as exc:                                   # noqa: BLE001
            failed.append({"series": key, "error": f"{type(exc).__name__}: {exc}"})
            print(f"  FAIL {key:<20} {type(exc).__name__}: {exc}")

    step("returns", lambda: _write(
        _with_returns(_download(args.ticker, args.start, end)["Close"], "close"),
        out / "returns.csv"))

    def pair():
        a, b = SERIES["pair"][0]
        df = pd.DataFrame({
            a: _download(a, args.start, end)["Close"].astype(float),
            b: _download(b, args.start, end)["Close"].astype(float),
        }).dropna()
        return _write(df, out / f"pair_{a}_{b}.csv")
    step("pair", pair)

    step("index", lambda: _write(
        _with_returns(_download("^GSPC", args.start, end)["Close"], "close"),
        out / "index_GSPC.csv"))

    step("vix", lambda: _write(
        pd.DataFrame({"close": _download("^VIX", args.start, end)["Close"].astype(float)}).dropna(),
        out / "vix.csv"))

    step("kospi", lambda: _write(
        _with_returns(_download("^KS11", args.start, end)["Close"].dropna(), "close"),
        out / "kospi.csv"))

    def short_rate():
        # ^IRX is quoted in percent; the models in Week 12 want decimals.
        s = _download("^IRX", args.start, end)["Close"].astype(float).dropna() / 100.0
        return _write(pd.DataFrame({"rate": s}), out / "short_rate.csv")
    step("short_rate", short_rate)

    manifest = {
        "generated_utc": pd.Timestamp.utcnow().isoformat(timespec="seconds"),
        "source": "Yahoo Finance via yfinance",
        "start": args.start,
        "end": end,
        "end_pinned": args.end is not None,
        "primary_ticker": args.ticker,
        "yfinance": getattr(yf, "__version__", "unknown"),
        "files": files,
        "failed": failed,
    }
    (out / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")

    print(f"\n{len(files)} file(s) written, {len(failed)} failed.  See {out / 'MANIFEST.json'}.")
    if not args.end:
        print("Reminder: pass --end 2026-08-20 when you need numbers that match the slides.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
