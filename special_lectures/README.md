# Special lectures

Stand-alone lectures that go beyond a single unit. Where a supplementary note answers one
question from class, a special lecture takes a whole topic that the course spreads over
several units and runs it end to end in one sitting.

Like the supplementary notes, each deck ships in **English and Korean**: `_EN` and `_KR`
carry the same slides and the same numbers.

| Lecture | Topic | Pages | Relates to |
|---|---|---|---|
| SL01 | [Cointegration — Engle–Granger, Johansen and the ECM](SL01_Cointegration_EG_Johansen_ECM_EN.pdf) · [한국어](SL01_Cointegration_EG_Johansen_ECM_KR.pdf) | 45 | U02 Part 3 — Spurious Regression and Cointegration; U07 — Cointegration and Error Correction |
| SL02 | [The Engle–Granger Two-Step Procedure](SL02_Engle_Granger_Two_Step_EN.pdf) · [한국어](SL02_Engle_Granger_Two_Step_KR.pdf) | 24 | U07 Part 2 — Testing Cointegration |
| SL03 | [Modern Pairs Trading — Ten Techniques](SL03_Modern_Pairs_Trading_EN.pdf) · [한국어](SL03_Modern_Pairs_Trading_KR.pdf) | 43 | U07 Part 3 — Error Correction and Pairs; builds on SL01 |
| SL04 | [Pairs Trading in Korea — Korean Stock Pairs and KOSPI200 Cash–Futures](SL04_Pairs_Trading_in_Korea_EN.pdf) · [한국어](SL04_Pairs_Trading_in_Korea_KR.pdf) | 31 | SL03 applied to the Korean market |
| SL05 | [Pairs Trading, Empirical Validation I — Six Tests on Real US ETF Data](SL05_Pairs_Trading_Empirical_Validation_I_EN.pdf) · [한국어](SL05_Pairs_Trading_Empirical_Validation_I_KR.pdf) | 32 | SL03 tested on real data |
| SL06 | [Pairs Trading, Empirical Validation II — Single Stocks, Intraday Data, Pre-registered Thresholds and Korean Data](SL06_Pairs_Trading_Empirical_Validation_II_EN.pdf) · [한국어](SL06_Pairs_Trading_Empirical_Validation_II_KR.pdf) | 29 | Closes what SL05 left open; corrects SL04 with real data |

## What each lecture covers

**SL01 · Cointegration — Engle–Granger, Johansen and the ECM.** Prices that wander apart
but share one long-run equilibrium, from the test to the error-correction model. Four
sections: foundations (stationary versus nonstationary series, spurious regression, the
I(d) ladder, the definition of cointegration); Engle–Granger for two assets (levels OLS,
residual ADF against MacKinnon critical values, a pairs-trade round trip worked to its P&L);
Johansen when there is more than one relation (the VECM rank, the eigenvalue problem, trace
and maximum-eigenvalue tests, a three-asset basket and a five-asset system with two
relations); and the ECM (speed of adjustment and half-life, a one-off income bonus traced
through consumption, weak exogeneity, the five-asset adjustment matrix, and where the ECM is
used beyond trading).

**SL02 · The Engle–Granger Two-Step Procedure.** The two-asset test in depth, one step per
section: Step 0 pins down the order of integration with an ADF on each level; Step 1 runs
the cointegrating regression in levels and keeps the residual, with the hedge ratio and
super-consistency; Step 2 tests that residual for a unit root — no constant, one-sided,
lags chosen to whiten it — and reads the statistic against MacKinnon tables, not the
ordinary ADF table. It closes with the statsmodels and R routines that get the critical
values right, and one pairs trade from entry at +2σ to exit at the mean.

SL02 zooms in on the Engle–Granger part of SL01; the two share the simulated pair and its
round-trip arithmetic.

### The pairs-trading series — SL03 to SL06

Four lectures meant to be read in order, after SL01. Cointegration says whether a spread
exists; this series asks how to trade it, where that changes in Korea, and whether the
claims survive real data.

**SL03 · Modern Pairs Trading — Ten Techniques.** Ten current techniques, each with its
formula, procedure and worked numbers, grouped by the job they do: selection (PCA factor
residuals, sparse mean-reverting portfolios, a clustering filter), dynamics (Kalman
time-varying hedge ratio, copula signals, regime detection), timing (the cost-aware optimal
OU band, a reinforcement-learning band, deep-learning signals) and validation (the Deflated
Sharpe Ratio). Built on US large caps and ETFs; the examples are simulations.

**SL04 · Pairs Trading in Korea — Korean Stock Pairs and KOSPI200 Cash–Futures.** The same
formulas under Korean inputs: the 0.20% sell-side tax from 2026, short-selling and
stock-borrow limits that remove 98% of candidate pairs, common–preferred share pairs as the
structural pairs that remain, the KOSPI200 cash–futures basis, and price limits, sidecars and
circuit breakers. Ends with a verdict on which of the ten techniques carry over. Simulation
plus published regulatory values.

**SL05 · Pairs Trading, Empirical Validation I — Six Tests on Real US ETF Data.** Twenty US
ETFs, 2015–2026, in six sessions: a walk-forward backtest (S1), multi-pair capital
allocation (S2), an execution model (S3), a formal regime-switching fit (S4), a threshold
error-correction model (S5) and information shares (S6). On real data the cost-aware optimal
band of SL03 loses to the conventional ±2σ; the reason is a threshold near 2σ, with reversion
rates that rise with the size of the deviation.

**SL06 · Pairs Trading, Empirical Validation II — Single Stocks, Intraday Data, Pre-registered
Thresholds and Korean Data.** The four questions SL05 left open: single stocks — 5,886 pairs
from 109 US large caps, 5,239 of them tested (S7), 1-minute, 5-minute and 1-hour bars (S8), thresholds fixed before
the test (S9) and real Korean common–preferred data (S10). The 2σ threshold reproduces across
three markets and four frequencies, but estimating it pair by pair loses to a fixed ±2σ.
S10 corrects SL04: the actual common–preferred gap averages 49.1% (assumed 15%) and its
half-life is 81 days (assumed 25), which makes those pairs untradable after borrow costs —
teach SL04 together with S10.

## File names

`SL01_Cointegration_EG_Johansen_ECM_EN.pdf` — lecture number, slug, language. The two
languages of one lecture share a slug, so they sort next to each other. Numbers follow the
order the lectures were added; the pairs-trading series is SL03–SL06.
