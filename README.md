# bayesian-change-point-analysis
# Bayesian Change Point Detection in Brent Crude Oil Prices

This project aims to detect structural changes in Brent crude oil prices using **Bayesian change point modeling**. The workflow involves **data cleaning**, **exploratory data analysis (EDA)**, **stationarity transformation**, **event metadata compilation**, and (in future steps) **probabilistic modeling** using `PyMC3`.

---

## 📌 Project Objective

To identify statistically significant change points in Brent oil price dynamics and correlate them with real-world geopolitical or economic events such as wars, sanctions, and OPEC decisions. This helps stakeholders interpret price shifts and enhance forecasting strategies.

---

## 🧱 Project Structure

    ├── .github/workflows/          # GitHub Actions CI setup
    │   └── ci.yml                 # Continuous integration configuration
    ├── backend/                   # Flask API backend serving data
    │   └── app.py                 # Flask app with REST API endpoints
    ├── data/                      # Raw and processed datasets
    │   ├── BrentOilPrices.csv     # Original historical data
    │   ├── brent_clean.csv        # Cleaned and processed data
    │   └── event_data.csv         # Metadata on real-world events
    ├── frontend/                  # React app frontend for interactive dashboard
    │   ├── src/                  # React components and API client
    │   ├── package.json          # Frontend dependencies and scripts
    │   └── public/               # Static assets
    ├── notebooks/                 # Jupyter notebooks for exploratory analysis
    │   ├── 01_EDA.ipynb          # Exploratory data analysis
    │   ├── 02_event_metadata_compilation.ipynb  # Compiling contextual events
    │   └── generate_report.ipynb # Generates interim report
    ├── reports/                   # Figures, outputs, and interim reports
    │   ├── figures/               # Saved EDA and visualization plots
    │   ├── analysis_report.pdf    # Interim PDF report
    │   ├── brent_report.md        # Interim markdown report
    │   └── change_points.csv      # Output of detected change points
    ├── src/                       # Python modules for data processing & EDA
    │   ├── data_processing.py     # Data cleaning & preparation functions
    │   ├── eda_utils.py           # EDA and plotting utilities
    │   └── eda_and_change_detection.py  # Modular pipeline (WIP)
    ├── venv/                      # Python virtual environment (ignored)
    ├── .gitignore                 # Ignore virtual env, node_modules, outputs, etc.
    ├── requirements.txt           # Python package dependencies
    ├── package.json               # Frontend dependencies
    └── README.md                  # Project documentation (this file)

---

## 📊 Key Features

- 📈 **Log return transformation** and **volatility tracking**
- 🔍 **Stationarity testing** with ADF and KPSS
- 🧠 **Event metadata** for causal interpretation of price shifts
- 📦 **Modular Python codebase** in `src/` for reuse in notebooks
- 📁 All figures and outputs are stored under `reports/`

---

##📊 Key Features

    📈 Log return transformation and volatility calculation of oil prices

    🔍 Stationarity testing using ADF and KPSS tests

    🧠 Event metadata compilation linking price shifts to real-world occurrences

    🛠️ Flask REST API backend serving processed data and change points

    📊 React frontend dashboard with interactive charts, filters, and event highlights

    📁 All outputs and figures stored under reports/ for easy access

⚙️ How to Run
Backend Setup

    Create and activate a Python virtual environment:

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

    Install dependencies:

pip install -r requirements.txt

    Run the Flask backend API:

python backend/app.py

API will be available at http://localhost:5000.
Frontend Setup

    Navigate to frontend folder:

cd frontend

    Install npm packages:

npm install

    Start React development server:

npm start

The dashboard will open at http://localhost:3000.
Running the Notebooks

Open Jupyter or VSCode and run notebooks sequentially:

    notebooks/01_EDA.ipynb — Exploratory Data Analysis

    notebooks/02_event_metadata_compilation.ipynb — Event Metadata

    notebooks/generate_report.ipynb — Generates interim report

📚 Interim Report

See the detailed progress report here:

    Markdown: reports/brent_report.md

    PDF: reports/analysis_report.pdf


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

Bayesian models provide posterior distributions over switch points, allowing us to reason about uncertainty and causality. This 