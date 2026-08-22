# Curriculum Map — Sixteen Units, Fourteen Teaching Weeks

## Summary

The material is written as sixteen units of three parts each (theory · deep dive ·
practice), 48 lectures in all. The semester is sixteen weeks, but **week 8 is the midterm
and week 16 is the final**, which leaves fourteen weeks to teach in. Two weeks therefore
carry two units.

The two pairings were not chosen to even out the page count. Each is a case where the
second unit opens by taking the first unit's conclusion as its premise, so the seam is
already written into the slides. Everything else runs one unit per week.

The split falls evenly: units 1–8 before the midterm, units 9–16 after it.

---

## 1. The fourteen teaching weeks

| Teaching week | Unit(s) | Topic | Module |
|---|---|---|---|
| 1 | U1 | Returns and Markets — definitions · stylized facts · efficiency | I |
| 2 | U2 | Stationarity and Cointegration — stationarity · unit roots · spurious regression | I |
| **3** | **U3 + U4** | **ARMA models + ARIMA and seasonality** | I |
| 4 | U5 | Volatility — ARCH · GARCH · VaR and pairs bands | II |
| 5 | U6 | Multivariate VAR — the model · Granger causality · IRF and FEVD | II |
| 6 | U7 | Cointegration and error correction — testing · ECM · pairs trading | II |
| 7 | U8 | State space and the Kalman filter — models · filtering and smoothing · synthesis | III |
| **8** | **Exam** | **Midterm — scope U1–U8** | — |
| 9 | U9 | Kalman filter deep dive — predict/update · the gain · pairs and nowcasting | III |
| 10 | U10 | Hidden Markov models — hidden states · Forward/Viterbi/Baum-Welch · regimes | III |
| **11** | **U11 + U12** | **Brownian motion, SDEs and OU + short rates and the term structure** | III |
| 12 | U13 | Bayesian foundations — Bayes' theorem · Beta-Binomial · intervals | IV |
| 13 | U14 | MCMC — sampling not integration · Metropolis and Gibbs · HMC and NUTS | IV |
| 14 | U15 | Bayesian state space — why point estimates lie · FFBS and TVP-SV · switching | IV |
| 15 | U16 | Model selection and capstone — three families · fair comparison · close | IV |
| **16** | **Exam** | **Final — scope U9–U16, capstone due** | — |

Bold rows are the two double weeks and the two exam weeks.

---

## 2. Why these two pairings

| Week | Units | The seam |
|---|---|---|
| 3 | U3 + U4 | ARIMA *is* ARMA with one idea added. U4 Part 1 opens on exactly that sentence: ARMA needs a stationary series, most real data trends, so difference until it is stationary, model the result, and integrate the forecast back. The identification and diagnostic apparatus from U3 carries over untouched — only the differencing step is new. |
| 11 | U11 + U12 | Vasicek is the Ornstein-Uhlenbeck process wearing a different name. U12 Part 1 is titled *"Vasicek and CIR — last week's OU machinery, applied to rates"*. Students who have just fitted an OU process to a spread are being handed the same SDE with the state relabelled as a short rate. |

Both double weeks land third in their half of the semester — early enough that the load
falls before the crunch, and after the ground has been laid.

### Pairings considered and rejected

- **U6 + U7 (VAR + cointegration/ECM).** Intellectually the tightest link in the course —
  a VECM is a cointegrated VAR. But it would put a double week immediately before the
  state-space week and the midterm, stacking the three heaviest weeks in a row.
- **U8 + U9 (state space + Kalman deep dive).** The most natural merge in the material,
  and impossible here: the midterm sits between them.
- **U13 + U14 (Bayes + MCMC).** Both are conceptual reboots for students trained on point
  estimates. Neither can absorb the other in one sitting.

---

## 3. Exam scope

**Midterm (week 8) — units 1–8.** The synthesis deck for this is already written:
U8 Part 3, *"Midterm Synthesis — seven weeks, one connected story"*, with a matching
practice deck that diagnoses a return series and trades a pair across units 6–8. Run it in
teaching week 7 as the review, then examine in week 8.

**Final (week 16) — units 9–16, capstone due.** U16 Part 3, *"The Final Project, and the
Course Close"*, sets the capstone: one asset, an honest train/test split, all three model
families fitted on the training data only, scored against a naive benchmark, then converted
into a trading decision graded on the test period alone. It is set in teaching week 15 and
collected in week 16.

Note that the practice decks carry an explicitly cumulative thread — the pairs trade is
built in stages (Stage III in U9, Stage IV in U10, Stage V in U11, Stage VI in U15) and each
stage assumes the last. Neither exam can treat its half as self-contained, and neither
should.

---

## 4. Weekly shape

Every unit runs in three parts, and a practice deck runs alongside each part.

| Part | Role | What happens |
|---|---|---|
| 1 | Theory | Core concepts and derivations — the assumptions and the intuition |
| 2 | Deep dive | Estimation, testing, extensions — the technical depth |
| 3 | Practice | Implement, back-test and interpret on real market data |

Each practice deck works two cases entirely by hand, every digit shown, then hands the same
computation to Claude Code as a lab with a stated deliverable and a self-check against the
printed numbers. The rule throughout: match the slide's arithmetic before you run anything.

In a double week, run the two units' parts in sequence rather than interleaving them — the
second unit's premise is the first unit's conclusion, and the order is what makes the pairing
work.

---

## 5. Data

No data set is distributed. `data/fetch_data.py` pulls all six series the course uses from
public sources, and `data/README.md` documents which week needs which. Week 1 Part 1 creates
`returns.csv` and Weeks 1–2 reuse it, so the extraction step belongs in teaching week 1.
