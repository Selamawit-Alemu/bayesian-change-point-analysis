# bayesian-change-point-analysis
# Bayesian Change Point Detection in Brent Crude Oil Prices

This project aims to detect structural changes in Brent crude oil prices using **Bayesian change point modeling**. The workflow involves **data cleaning**, **exploratory data analysis (EDA)**, **stationarity transformation**, **event metadata compilation**, and (in future steps) **probabilistic modeling** using `PyMC3`.

---

## 📌 Project Objective

To identify statistically significant change points in Brent oil price dynamics and correlate them with real-world geopolitical or economic events such as wars, sanctions, and OPEC decisions. This helps stakeholders interpret price shifts and enhance forecasting strategies.

---

## 🧱 Project Structure

    ├── .github/workflows/ # GitHub Actions CI setup
    │ └── ci.yml # Continuous integration configuration
    ├── dashboard/ # (Optional) Streamlit or Dash app (future extension)
    ├── data/ # Raw and processed datasets
    │ ├── BrentOilPrices.csv # Original historical data
    │ ├── brent_clean.csv # Cleaned and processed data
    │ └── event_data.csv # Metadata on real-world events
    ├── notebooks/ # Jupyter notebooks for each step
    │ ├── 01_EDA.ipynb # Exploratory data analysis
    │ ├── 02_event_metadata... # Compiling contextual events
    │ └── generate_report.ipynb # Generates interim report
    ├── reports/
    │ ├── figures/ # Saved plots (EDA visualizations)
    │ ├── analysis_report.pdf # PDF version of the interim report
    │ ├── brent_report.md # Markdown version of the report
    │ └── change_points.csv # Placeholder for model output
    ├── src/ # Python modules
    │ ├── data_processing.py # Data cleaning and preparation logic
    │ ├── eda_utils.py # EDA & visualization functions
    │ └── eda_and_change_detection.py # Modular pipeline (WIP)
    ├── venv/ # Python virtual environment
    ├── .gitignore # Ignore venv, outputs, etc.
    ├── requirements.txt # Required Python packages
    └── README.md # You're here!


---

## 📊 Key Features

- 📈 **Log return transformation** and **volatility tracking**
- 🔍 **Stationarity testing** with ADF and KPSS
- 🧠 **Event metadata** for causal interpretation of price shifts
- 📦 **Modular Python codebase** in `src/` for reuse in notebooks
- 📁 All figures and outputs are stored under `reports/`

---

## ⚙️ How to Run

### 1. Clone the Repo


    git clone https://github.com/Selamawit-Alemu/bayesian-change-point-analysis.git
    cd  bayesian-change-point-analysis

2. Create Virtual Environment

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Requirements

    pip install -r requirements.txt

4. Run the Notebooks

Open Jupyter or VSCode and step through:

    notebooks/01_EDA.ipynb

    notebooks/02_event_metadata_compilation.ipynb

    notebooks/generate_report.ipynb

All figures and results will be saved to the reports/ folder.
📚 Interim Report

A detailed progress report is included:

    Markdown: reports/brent_report.md

    PDF: reports/analysis_report.pdf

This covers all steps from data wrangling to EDA and metadata compilation.
🛠️ To Do (Next Phase)

Implement Bayesian Change Point Modeling using PyMC3

Align change points with contextual events

Build a dashboard or interactive report

    Evaluate model robustness and uncertainty

🧠 Why Bayesian Change Points?

Bayesian models provide posterior distributions over switch points, allowing us to reason about uncertainty and causality. This project connects statistical change detection with real-world signals for actionable business insights.