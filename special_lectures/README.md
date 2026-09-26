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

## File names

`SL01_Cointegration_EG_Johansen_ECM_EN.pdf` — lecture number, slug, language. The two
languages of one lecture share a slug, so they sort next to each other.
