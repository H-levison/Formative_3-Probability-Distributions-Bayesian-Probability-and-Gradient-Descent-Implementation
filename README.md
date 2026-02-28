# Formative 3 — Probability Distributions, Bayesian Probability & Gradient Descent

This repository contains coursework for **Formative 3**, covering:

- **Probability distributions** — bivariate normal (PDF from scratch, visualizations, real-world data)
- **Bayesian probability** — sentiment analysis with the IMDB dataset
- **Gradient descent** — implementation and iterations

---

## Repository contents

| Item | Description |
|------|-------------|
| **`bivariate_normal.ipynb`** | Bivariate normal distribution: PDF from scratch, sampling, stock log-returns (AMZN/NVDA), contour & 3D plots |
| **`Bayesian.ipynb`** | Bayesian probability for sentiment analysis (IMDB reviews); priors, likelihoods, posteriors |
| **`Gradient_descent_implementation/`** | Gradient descent implementation with **handwritten calculations** for ŷ (y predict), **m** (slope), and **b** (intercept) |
| **`stock_details_5_years.csv`** | Optional: local copy of Yahoo Finance stock data for `bivariate_normal.ipynb` Section 8 |

---

## Bivariate Normal Distribution (`bivariate_normal.ipynb`)

A self-contained notebook that:

- **Implements the bivariate normal (BVN) PDF from scratch** — no statistical libraries (e.g. no `scipy.stats`). Only NumPy is used for basic math (`exp`, `sqrt`, arrays).
- **Simulates BVN samples from scratch** — uses two independent \(N(0,1)\) variates and the standard transformation (no `np.random.multivariate_normal`).
- **Computes the PDF at each data point** — for both simulated data and the real-world dataset.
- **Uses a real-world dataset sourced online** — [Yahoo Finance stock data](https://www.kaggle.com/datasets/iveeaten3223times/massive-yahoo-finance-dataset) (Kaggle): AMZN and NVDA log returns. Mean, standard deviation, and covariance are computed from scratch.
- **Visualizes the PDF** with Matplotlib:
  - Contour plot
  - 3D surface plot  
  Both show the characteristic elliptical shape and are clearly labeled (parameters μ, Σ, ρ).

### Notebook structure

1. **Parameters & covariance matrix** — mean vector μ, covariance matrix Σ, correlation ρ.
2. **Simulating data** — BVN samples from scratch (no statistical libraries).
3. **PDF from scratch** — bivariate normal PDF formula implemented by hand.
4. **PDF at each data point** — density computed for every simulated point.
5. **Evaluation grid** — grid used for contour and 3D plots.
6. **Visualizations** — contour and 3D surface of the density.
7. **Simulated samples on the density** — scatter of samples over the contour.
8. **Real-world dataset: stock log returns** — load data (Kaggle or local CSV), log returns and stats from scratch, PDF at each point, contour and 3D for AMZN vs NVDA.

### Requirements

- **Python 3** (e.g. 3.11+)
- **NumPy**, **Matplotlib** (for all sections)
- **Pandas** (for Section 8 — stock data)

Optional (Section 8):

- **kagglehub** and [Kaggle API credentials](https://www.kaggle.com/settings) to download the dataset automatically.

If you don’t use Kaggle, place **`stock_details_5_years.csv`** in the same folder as the notebook; the notebook will load it from there.

### How to run

1. Install dependencies:  
   `pip install numpy matplotlib pandas`
2. Open **`bivariate_normal.ipynb`** in Jupyter, JupyterLab, or VS Code/Cursor.
3. Use **Run All** (or run cells in order).

For Section 8, either have the Kaggle dataset downloaded via `kagglehub` or place `stock_details_5_years.csv` in the project folder.

---

## Bayesian Probability (`Bayesian.ipynb`)

**Part 2** of Formative 3: Bayesian probability applied to **sentiment analysis** using the [IMDB movie reviews dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) (50k reviews).

- **Keywords:** positive — *awesome*, *great*, *incredible*; negative — *garbage*, *worst*, *bad*
- **Probabilities computed for each keyword:**
  - **Prior:** P(Positive)
  - **Likelihood:** P(keyword | Positive)
  - **Marginal:** P(keyword)
  - **Posterior:** P(Positive | keyword)

Uses Bayes’ rule to update belief in positive sentiment given each keyword. Requires **pandas** and the IMDB Dataset CSV (path in the notebook may need updating for your environment).

### How to run

1. Install pandas: `pip install pandas`
2. Download the [IMDB Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) and set the CSV path in the first code cell.
3. Open **`Bayesian.ipynb`** and run all cells.

---

## Gradient descent (`Gradient_descent_implementation/`)

Contains the **gradient descent implementation** with **handwritten calculations** to find:

- **ŷ (y predict)** — predicted values from the linear model
- **m** — slope (gradient descent updates)
- **b** — intercept (bias term)

Materials include iteration write-ups (e.g. **`Iteration_2.pdf`**, **`Iteration 4`**) showing the step-by-step gradient descent calculations. Open the folder for the full handwritten working.

---
