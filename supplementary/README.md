# Supplementary notes

Short decks written in answer to questions asked in class, and the decks of make-up classes. Each one takes a single point
that the main units treat quickly, and unfolds it at student pace — worked numbers,
a figure, and a page of summary.

These are the one place in this repository where material appears in **Korean as well as
English**. The course itself is taught in English, but questions arrive in both languages,
so each note ships as a pair: `_EN` and `_KR` carry the same slides and the same numbers.

New notes are added as questions come in, numbered in the order they were written.

| Note | Topic | Pages | Relates to |
|---|---|---|---|
| S01 | [Fat Tails and Power Laws](S01_Fat_Tails_and_Power_Laws_EN.pdf) · [한국어](S01_Fat_Tails_and_Power_Laws_KR.pdf) | 18 | U01 Part 2 — Stylized Facts |
| S02 | [Time Series Basics in 6 Hours](S02_Time_Series_Basics_6h_EN.pdf) · [한국어](S02_Time_Series_Basics_6h_KR.pdf) | 38 | Prerequisite refresher, before U01 |
| S03 | [ACF and PACF, Learned by Example](S03_ACF_PACF_Intro_EN.pdf) · [한국어](S03_ACF_PACF_Intro_KR.pdf) | 42 | U03 Part 2 — ARMA Identification |

## What each note covers

**S01 · Fat Tails and Power Laws.** Why a normal distribution understates financial risk.
Reads the power law `P(|R| > x) ∝ 1/x^α` through arithmetic first — a tenfold move keeps
one thousandth of the probability, not none — then the tail index α, why higher moments
become unstable, and how the Student-t realises a power-law tail through its degrees of
freedom ν. Written after a question about the line "the mean exists; higher moments barely
do" on the Stylized Facts deck.

**S02 · Time Series Basics in 6 Hours.** A refresher for students arriving without a time
series course: time order as information, level versus change, stationarity by eye,
autocorrelation at lag 1, and evaluating a forecast against a benchmark on held-out future
data. Six hours, each with a practice block.

**S03 · ACF and PACF, Learned by Example.** The two plots that name a model, built from a
salmon-price example rather than a formula: a lag as a shifted column, correlation between a
series and its shifted copy, then the difference between total resemblance (ACF) and direct
resemblance (PACF) through the grandfather–father–son analogy. Works AR(1) and MA(1) by hand,
checks each against a simulation, and ends with the rule — read the AR order from the PACF
cut-off and the MA order from the ACF cut-off — a quiz, and the statsmodels code that draws
both plots. The revised deck adds a worked derivation of the lag-2 PACF as the
Jan–Mar correlation once Feb is known, and why an MA(1) shock leaves a residual at every lag.

## Week 4 make-up class

| Class | Topic | Pages | Relates to |
|---|---|---|---|
| Week 4 make-up class | [From Stationarity to Seasonal ARIMA](W04_Makeup_ARIMA_Foundations_EN.pdf) · [한국어](W04_Makeup_ARIMA_Foundations_KR.pdf) | 64 | U02–U04 — Stationarity, ARMA, ARIMA, SARIMA |

The whole conditional-mean storyline in one deck: stationarity (strict versus weak, the
Cauchy counter-example, ADF and KPSS, spurious regression, first and seasonal differencing, why differencing cannot fix shifting variance),
AR as memory of past values, MA as memory of past errors, ARMA and ARIMA with Box–Jenkins
identification on ACF/PACF and information-criterion grids, and SARIMA with the airline model
on Mauna Loa CO₂. Cases include the T-bill half-life, the Roll bid-ask spread, and US real GDP
forecast bands. It lays the U02–U04 sequence out end to end before the mid-term.
A narrated video of the English deck (44 minutes) is on YouTube:
https://youtu.be/P0ultu9mB6E.

## File names

`S01_Fat_Tails_and_Power_Laws_EN.pdf` — note number, slug, language. The two languages of
one note share a slug, so they sort next to each other. A make-up class is filed by week
instead of by note number: `W04_Makeup_ARIMA_Foundations_EN.pdf`.
