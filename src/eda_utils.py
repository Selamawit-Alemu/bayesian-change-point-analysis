# eda_utils.py

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Set a consistent style for plots
sns.set(style="whitegrid")

# Define directories for data and reports, ensuring they exist
REPORTS_DIR = "../reports"
os.makedirs(os.path.join(REPORTS_DIR, 'figures'), exist_ok=True)
os.makedirs("../data", exist_ok=True)

def load_cleaned_data(filepath):
    """
    Load the cleaned Brent oil price data with a datetime index.

    Args:
        filepath (str): Path to cleaned CSV data.

    Returns:
        pd.DataFrame: DataFrame indexed by datetime.
    """
    print(f"Loading cleaned data from: {filepath}")
    try:
        df = pd.read_csv(filepath, index_col=0, parse_dates=True)
        print(f"Data loaded: {df.shape} from {df.index.min()} to {df.index.max()}")
        return df
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
        return None

def plot_and_save(df, column, title, filename, y_label=None):
    """
    Plot a time series and save the figure.

    Args:
        df (pd.DataFrame): DataFrame with a datetime index.
        column (str): Column name to plot.
        title (str): Plot title.
        filename (str): Path to save the figure.
        y_label (str, optional): Y-axis label. Defaults to column name.
    """
    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df[column], label=column)
    plt.title(title, fontsize=16)
    plt.xlabel("Date")
    plt.ylabel(y_label if y_label else column)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(REPORTS_DIR, 'figures', filename))
    plt.show()
    plt.close()
    print(f"Saved plot: {filename}")

def plot_rolling_means(df, save_path):
    """
    Plots the time series with rolling mean overlays.
    """
    plt.figure(figsize=(14, 6))
    plt.plot(df['Price'], label='Original Price', alpha=0.6)
    
    # Calculate and plot rolling means
    df['Price'].rolling(window=30).mean().plot(label='30-day MA', linestyle='--')
    df['Price'].rolling(window=90).mean().plot(label='90-day MA', linestyle='--')
        
    plt.title("Brent Oil Price with Rolling Means", fontsize=16)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
    plt.close()
    print(f"Plot saved to {save_path}")

def decompose_seasonality(df, save_path):
    """
    Decomposes the time series into trend, seasonal, and residual components.
    """
    df_monthly = df['Price'].resample('M').mean()
    # Need at least two full cycles for seasonal decomposition, usually 24 months
    if len(df_monthly.dropna()) < 24:
        print("Not enough data to perform seasonal decomposition.")
        return
        
    decomposition = seasonal_decompose(df_monthly.dropna(), model='additive')
    fig = decomposition.plot()
    fig.set_size_inches(14, 10)
    plt.suptitle("Seasonal Decomposition of Monthly Brent Oil Price", fontsize=16)
    plt.tight_layout()
    fig.savefig(save_path)
    plt.show()
    plt.close()
    print(f"Plot saved to {save_path}")

def plot_distribution_of_returns(df, save_path):
    """
    Plots a histogram of daily returns to analyze their distribution.
    """
    plt.figure(figsize=(10, 5))
    sns.histplot(df['daily_return'].dropna() * 100, bins=100, kde=True, color='orange')
    plt.title("Distribution of Daily Returns", fontsize=16)
    plt.xlabel("Daily Return (%)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
    plt.close()
    print(f"Plot saved to {save_path}")

def plot_acf_pacf(df, save_path):
    """
    Plots the Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF).
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    plot_acf(df['daily_return'].dropna(), ax=axes[0], lags=50)
    plot_pacf(df['daily_return'].dropna(), ax=axes[1], lags=50)
    axes[0].set_title("Autocorrelation (ACF)")
    axes[1].set_title("Partial Autocorrelation (PACF)")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
    plt.close()
    print(f"Plot saved to {save_path}")

def stationarity_tests(series):
    """
    Perform ADF and KPSS stationarity tests on a series.

    Args:
        series (pd.Series): Time series data.

    Returns:
        dict: Dictionary with ADF and KPSS results.
    """
    print("\n--- Running Stationarity Tests ---")
    
    # ADF Test
    print("Augmented Dickey-Fuller (ADF) Test:")
    adf_result = adfuller(series.dropna())
    print(f"ADF Statistic: {adf_result[0]:.4f}, p-value: {adf_result[1]:.4f}")

    # KPSS Test
    print("\nKwiatkowski-Phillips-Schmidt-Shin (KPSS) Test:")
    kpss_result = kpss(series.dropna(), nlags="auto")
    print(f"KPSS Statistic: {kpss_result[0]:.4f}, p-value: {kpss_result[1]:.4f}")

    return {
        "adf_statistic": adf_result[0],
        "adf_pvalue": adf_result[1],
        "kpss_statistic": kpss_result[0],
        "kpss_pvalue": kpss_result[1]
    }

def compile_event_metadata():
    """
    Creates a DataFrame with major geopolitical, economic, and OPEC-related events.

    Returns:
        pd.DataFrame: DataFrame with columns ['Date', 'EventType', 'Description'].
    """
    data = [
        {"Date": "1990-08-02", "EventType": "Geopolitical", "Description": "Iraq invades Kuwait - Gulf War begins"},
        {"Date": "1997-07-02", "EventType": "Economic", "Description": "Asian Financial Crisis"},
        {"Date": "2001-09-11", "EventType": "Geopolitical", "Description": "9/11 Attacks"},
        {"Date": "2003-03-20", "EventType": "Geopolitical", "Description": "Iraq War begins"},
        {"Date": "2008-09-15", "EventType": "Economic", "Description": "Lehman Brothers collapse - Financial Crisis"},
        {"Date": "2010-01-01", "EventType": "OPEC", "Description": "OPEC production cuts"},
        {"Date": "2014-06-01", "EventType": "Economic", "Description": "US shale oil boom impacts prices"},
        {"Date": "2016-01-17", "EventType": "OPEC", "Description": "OPEC agreement to cut production"},
        {"Date": "2020-03-11", "EventType": "Economic", "Description": "COVID-19 declared a pandemic"},
        {"Date": "2022-02-24", "EventType": "Geopolitical", "Description": "Russia invades Ukraine"},
    ]
    df_events = pd.DataFrame(data)
    df_events["Date"] = pd.to_datetime(df_events["Date"])
    print(f"Compiled {len(df_events)} key events.")
    return df_events

def save_event_metadata(df_events, filepath="../data/event_data.csv"):
    """
    Save event metadata DataFrame to CSV.

    Args:
        df_events (pd.DataFrame): Event metadata DataFrame.
        filepath (str): Output CSV path.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df_events.to_csv(filepath, index=False)
    print(f"Event metadata saved to: {filepath}")

def load_event_metadata(filepath="../data/event_data.csv"):
    """
    Load event metadata CSV into a DataFrame.

    Args:
        filepath (str): Path to event metadata CSV.

    Returns:
        pd.DataFrame: Event metadata.
    """
    print(f"Loading event metadata from: {filepath}")
    df_events = pd.read_csv(filepath, parse_dates=["Date"])
    print(f"Loaded {len(df_events)} events.")
    return df_events

def main(cleaned_data_path="../data/processed/brent_clean.csv"):
    """
    Main function to run the full EDA analysis pipeline.
    """
    print("=== Starting EDA Analysis ===")
    
    # Load cleaned data
    df = load_cleaned_data(cleaned_data_path)
    if df is None:
        print("Failed to load data. Please check the file path.")
        return

    # Calculate key features for analysis
    df['daily_return'] = df['Price'].pct_change()
    df['volatility'] = df['daily_return'].rolling(window=30).std() * (252**0.5)

    # Check missing data summary
    print("\nMissing values summary:\n", df.isna().sum())

    # Generate and save all plots to the 'reports/figures' directory
    print("\nGenerating plots...")
    plot_and_save(df, "Price", "Brent Oil Price (USD)", "price_plot.png", "Price (USD)")
    plot_and_save(df, "daily_return", "Daily Returns", "daily_return_plot.png", "Daily Return")
    plot_and_save(df, "volatility", "Rolling Volatility (30-day Annualized)", "volatility_plot.png", "Volatility")
    
    # These functions already handle their own file saving logic
    plot_rolling_means(df, os.path.join(REPORTS_DIR, 'figures', "rolling_means.png"))
    decompose_seasonality(df, os.path.join(REPORTS_DIR, 'figures', "seasonal_decomposition.png"))
    plot_distribution_of_returns(df, os.path.join(REPORTS_DIR, 'figures', "daily_return_distribution.png"))
    plot_acf_pacf(df, os.path.join(REPORTS_DIR, 'figures', "acf_pacf.png"))

    # Perform stationarity tests
    stationarity_tests(df["Price"])

    # Compile event metadata and save it
    events = compile_event_metadata()
    save_event_metadata(events)

    print("\n=== EDA Complete ===")
    print("Please check the '../reports/figures' and '../data' directories for all outputs.")

if __name__ == "__main__":
    main()