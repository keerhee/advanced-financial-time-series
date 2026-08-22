# Advanced Financial Time Series

Yonsei University · for 3rd- and 4th-year undergraduates · 16 units · 48 lectures

**Browse and download → https://keerhee.github.io/advanced-financial-time-series/**

A listing page organised by week. Filter by title or type, open a deck in the browser, or
pull the whole week as one file.

From the language of time series (stationarity, ARMA, ARIMA) through volatility (GARCH),
the multivariate world (VAR), state space (Kalman, HMM) and stochastic processes (SDE), to
Bayesian inference (MCMC). Every unit runs in three parts — theory, deep dive, practice —
and every part connects directly to code and market data.

**113 PDFs · 2,317 slides.** 48 lecture decks, 48 practice decks, one syllabus, plus one
merged file per week. **Only PDFs, code and Markdown are tracked here** — the editable
PPTX sources are excluded by `.gitignore`, since a binary rewrites its whole blob into
history on every save.

---

## Layout

| Path | Contents |
|---|---|
| `W01_Returns_and_Markets/` … `W16_Model_Selection_and_Capstone/` | Six decks per week — a lecture and a practice deck for each of the three parts — plus `*_Complete.pdf`, the whole week in one file |
| `course/` | Syllabus and the [curriculum map](course/curriculum_map.md) |
| `data/` | `fetch_data.py` and the [data guide](data/README.md) — the course ships no data set |
| `site/` | The GitHub Pages listing page (`index.html`, one file) |

Page counts match the source slide counts one for one. GitHub renders PDFs in the browser,
so nothing needs cloning to read. Ask separately if you need the PPTX originals.

### File names

| Form | Example |
|---|---|
| Lecture deck | `W05_P2_GARCH_Lecture.pdf` |
| Practice deck | `W05_P2_GARCH_Practice.pdf` |
| Whole week | `W05_Volatility_Models_Complete.pdf` |

`W05_P2` reads as week 5, part 2. Lecture and practice decks for the same part share a
slug, so they sort next to each other.

---

## The four modules

| Module | Units | Topic |
|---|---|---|
| I · Language of Time Series | 1–4 | Returns, stationarity, ARMA, ARIMA — the grammar |
| II · Volatility and the Multivariate World | 5–7 | GARCH, VAR, cointegration — risk and interaction |
| III · State Space, Latent States and Processes | 8–12 | Kalman, HMM, SDE, short-rate models |
| IV · Bayesian Financial Time Series | 13–16 | Bayes, MCMC, Bayesian state space, model choice |

---

## Sixteen units, fourteen teaching weeks

Week 8 is the midterm and week 16 is the final, so the sixteen units are taught in
fourteen weeks. Two weeks carry two units: **week 3** takes ARMA together with ARIMA, and
**week 11** takes SDEs and the OU process together with short rates. Both are cases where
the second unit opens by taking the first unit's conclusion as its premise — ARIMA is ARMA
plus differencing, and Vasicek is the OU process with the state relabelled as a rate.

The split falls evenly: units 1–8 before the midterm, units 9–16 after it. The full table,
the rejected pairings and the exam scopes are in
[`course/curriculum_map.md`](course/curriculum_map.md).

---

## How each week runs

| Part | Role |
|---|---|
| 1 · Theory | Core concepts and derivations — the assumptions and the intuition |
| 2 · Deep dive | Estimation, testing, extensions — the technical depth |
| 3 · Practice | Implement, back-test and interpret on real market data |

A practice deck runs alongside each part. Each works two cases entirely by hand, every
digit shown, then hands the same computation to Claude Code as a lab with a stated
deliverable and a self-check against the printed numbers. The rule throughout: match the
slide's arithmetic before you run anything.

The pairs trade is built cumulatively across the semester — Stage III in unit 9, Stage IV
in unit 10, Stage V in unit 11, Stage VI in unit 15 — and each stage assumes the last.

---

## Practice data

**Nothing is distributed here.** Every series the labs use is public, and pulling it
yourself is the first exercise.

```bash
cd data
pip install -r requirements.txt
python fetch_data.py --end 2026-08-20
```

Six CSVs land in `data_out/`: the primary asset with both return definitions, a KO/PEP
pair, the S&P 500, the VIX, the KOSPI, and a short-rate series. That is the entire data
footprint of the sixteen weeks.

`returns.csv` is the spine — Week 1 Part 1 creates it, Labs 2 and 3 reuse it, and Week 2
runs ADF and KPSS on it. From week 3 onward the labs say "a real asset" without naming
one, deliberately; any of these files answers it.

**Pin the end date.** The lab prompts say "to today", which means no two students hold the
same series. Pass `--end` for anything you hand in, and quote the `MANIFEST.json` the
script writes. Details, including what to do if Yahoo is unreachable, are in
[`data/README.md`](data/README.md).

Several weeks need no download at all — the Week 9 nowcasting lab builds its own synthetic
indicators on purpose, the simulation cases fix a seed, and every "Worked by Hand" case
prints its numbers on the slide.

---

## Tooling

Python with `pandas`, `numpy` and `statsmodels`; `arch` for GARCH; `filterpy` for the
Kalman filter; `PyMC` or `NumPyro` for the Bayesian units. `data/requirements.txt` pins the
first group and comments the rest until you reach them.

Prerequisites: probability and statistics, linear algebra (essential for state space), and
calculus. Prior regression experience helps.

---

## Licence

Course materials under [CC BY-NC-SA 4.0](LICENSE); the code in `data/` under MIT. Market
data belongs to its providers and is pulled under their terms — nothing here redistributes it.
