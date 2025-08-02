## 🧪 Methodology Overview

This analysis follows a structured, data-scientific approach to understand how geopolitical and economic events impact Brent crude oil prices over time. The workflow is designed to support robust statistical modeling, intuitive visualizations, and stakeholder-ready insights.

### Workflow Stages

1. **Data Preprocessing**  
   Parsing and cleaning the daily oil price data.

2. **Exploratory Data Analysis (EDA)**  
   Visualization of trends, volatility, and potential seasonality.

3. **Event Annotation**  
   Manual compilation of a key event dataset from global sources for correlation analysis.

4. **Time Series Diagnostics**  
   Statistical tests and transformations to evaluate model assumptions.

5. **Bayesian Modeling with PyMC3**  
   Structural change point detection using Bayesian inference and MCMC.

6. **Event-Change Point Correlation**  
   Visual and statistical alignment between modeled change points and known external shocks.

7. **Communication and Recommendations**  
   Presentation of results via a technical report and interactive dashboard tailored to investors, policymakers, and industry stakeholders.


# Interim Report – Bayesian Change Point Analysis of Brent Oil Prices

## 1. Introduction

This project aims to detect structural changes in Brent crude oil prices over time using a Bayesian change point modeling approach. The core motivation is to identify significant shifts in the price dynamics and relate them to real-world geopolitical and economic events such as wars, sanctions, and OPEC decisions. Such analysis offers valuable insights to energy analysts, policymakers, and financial institutions for risk forecasting and investment strategy.

In this interim phase, we focused on **data acquisition, cleaning, transformation, and exploratory data analysis (EDA)** to lay the foundation for a robust change point detection model. We also compiled contextual event metadata to enhance interpretability of future model results.

---

## 2. Data Analysis Workflow

Our process for Task 1 followed these sequential steps:

1. **Data Acquisition**: Collected historical Brent crude oil prices.
2. **Data Cleaning**: Handled missing values and anomalies.
3. **Feature Engineering**:
   - Calculated daily returns for stationarity.
   - Computed rolling volatility for capturing local fluctuations.
4. **Stationarity Testing**:
   - Applied ADF and KPSS tests to assess stationarity.
5. **Exploratory Data Analysis**:
   - Plotted raw prices, returns, and volatility.
   - Visualized patterns and changes in trends.
6. **Event Metadata Compilation**:
   - Collected major global events (e.g., policy shifts, wars) influencing oil markets.
   - Saved a CSV dataset (`event_data.csv`) with annotated descriptions and dates.

Each step is implemented in reusable Python modules, and all generated visualizations are saved under the `reports/` folder.

---

## 3. Time Series Properties

To evaluate the nature of the Brent oil price time series, we performed the following:

- **Trends & Seasonality**: Observed long-term upward and downward trends in price plots. No strong seasonal pattern detected.
- **Volatility Clustering**: High volatility periods aligned with known crises (e.g., Gulf War, 2008 crash).
- **Stationarity Testing**:
  - **ADF Test**: Statistic = -1.99, p-value = 0.289 → fails to reject non-stationarity.
  - **KPSS Test**: Statistic = 9.56, p-value = 0.01 → confirms strong non-stationarity.

Based on these findings, **daily returns** are used as the working stationary signal for modeling.

---

## 4. Event Dataset Quality

To contextualize future change points, we compiled a structured CSV (`event_data.csv`) of **10 major events** affecting oil prices from 1987 to 2022. Each event includes:

- Date  
- Title  
- Description  
- Relevance to oil prices  

In the next stage, we will expand this to include **15 events**, in line with the rubric.

---

## 5. Purpose of Change Point Models

Change point models are designed to detect moments in time where the statistical properties of a time series undergo structural shifts. These models allow us to:

- Identify regime shifts in oil pricing.
- Quantify uncertainty around change points using Bayesian inference.
- Attribute structural breaks to real-world causes (e.g., policy changes, conflicts).
- Enhance forecasting and risk analysis in dynamic markets.

By incorporating domain-relevant events, we aim to interpret detected changes not just statistically, but also in terms of **real business value**.

---

## 6. Challenges and Mitigation

- **Challenge**: Non-stationary data and fluctuating volatility made direct modeling infeasible.  
  **Mitigation**: We computed log returns and rolling volatility to stabilize the time series before analysis.

- **Challenge**: Aligning events with time series data required careful validation.  
  **Mitigation**: Cross-verified event dates from multiple sources and maintained metadata in a reusable CSV file.

---

## 7. Change Point Detection – Preparatory Work

While full implementation of Bayesian change point detection will occur in Task 2, we have:

- Transformed the raw price series to daily returns.
- Validated stationarity via ADF and KPSS tests.
- Built clear visualizations of volatility and return patterns.
- Prepared 10 contextual historical events for later model interpretation.

---

## 8. Completed Artifacts

- **Cleaned data**: `../data/processed/brent_clean.csv`
- **Event metadata**: `../data/event_data.csv`
- **Visualizations**:
  - `reports/price_plot.png`
  - `reports/daily_return_plot.png`
  - `reports/volatility_plot.png`
- **Stationarity test results**: Output printed in notebook logs

---

## 9. Next Steps

- Implement Bayesian change point detection using PyMC3.
- Validate change points using event metadata.
- Visualize posterior distributions over switch points.
- Derive insights and translate them into business implications.

---
