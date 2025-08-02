# eda_and_change_detection_utils.py

import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import warnings

# Suppress all warnings for a cleaner output
warnings.filterwarnings('ignore')

# Set a consistent style for plots
sns.set(style="whitegrid")

# Get the absolute path of the script's directory and then the project root.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

# Define directories for data and reports relative to the project root.
REPORTS_DIR = os.path.join(PROJECT_ROOT, 'reports')
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')

# Ensure directories exist
os.makedirs(os.path.join(REPORTS_DIR, 'figures'), exist_ok=True)
os.makedirs(os.path.join(DATA_DIR, 'processed'), exist_ok=True)

def load_cleaned_data(filename: str = 'brent_clean.csv'):
    """
    Load the cleaned Brent oil price data from the data/processed directory.

    Args:
        filename (str): The name of the data file.

    Returns:
        pd.DataFrame: DataFrame indexed by datetime.
    """
    data_path = os.path.join(DATA_DIR, 'processed', filename)
    try:
        print(f"Attempting to load data from: {data_path}")
        df = pd.read_csv(data_path, index_col=0, parse_dates=True)
        print(f"Data loaded: {df.shape} from {df.index.min()} to {df.index.max()}")
        return df
    except FileNotFoundError:
        print(f"Error: The file {data_path} was not found.")
        print("Please ensure the data file exists at the specified path.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None

def compile_event_metadata():
    """
    Create a DataFrame of major geopolitical, economic, and OPEC events.
    """
    print("Compiling key event metadata...")
    events = [
        {"Date": "1990-08-02", "Event_Type": "Geopolitical", "Description": "Iraq invades Kuwait - Gulf War begins"},
        {"Date": "2001-09-11", "Event_Type": "Economic/Shock", "Description": "9/11 Terrorist Attacks - impact on global economy"},
        {"Date": "2003-03-20", "Event_Type": "Geopolitical", "Description": "US-led Iraq War starts"},
        {"Date": "2008-09-15", "Event_Type": "Economic/Shock", "Description": "Lehman Brothers bankruptcy - Global financial crisis"},
        {"Date": "2011-02-15", "Event_Type": "Geopolitical", "Description": "Arab Spring uprisings begin"},
        {"Date": "2014-06-01", "Event_Type": "OPEC", "Description": "OPEC decides not to cut production amid falling prices"},
        {"Date": "2016-01-17", "Event_Type": "OPEC", "Description": "OPEC and allies agree to production cuts"},
        {"Date": "2020-03-09", "Event_Type": "Economic/Shock", "Description": "COVID-19 pandemic triggers oil price crash"},
        {"Date": "2022-02-24", "Event_Type": "Geopolitical", "Description": "Russia invades Ukraine - global energy uncertainty"},
        {"Date": "2023-01-01", "Event_Type": "Economic/Shock", "Description": "Rising inflation and tightening monetary policies impact oil demand"},
    ]
    df_events = pd.DataFrame(events)
    df_events['Date'] = pd.to_datetime(df_events['Date'], format='%Y-%m-%d', errors='raise')
    print(f"Compiled {len(df_events)} events.")
    return df_events

def plot_and_save(df, column, title, filename, y_label=None):
    """Plot a time series and save the figure."""
    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df[column], label=column)
    plt.title(title, fontsize=16)
    plt.xlabel("Date")
    plt.ylabel(y_label if y_label else column)
    plt.legend()
    plt.tight_layout()
    save_path = os.path.join(REPORTS_DIR, 'figures', filename)
    plt.savefig(save_path)
    plt.show()
    plt.close()
    print(f"Saved plot: {save_path}")

def plot_rolling_means(df):
    """Plots the time series with rolling mean overlays."""
    save_path = os.path.join(REPORTS_DIR, 'figures', "rolling_means.png")
    plt.figure(figsize=(14, 6))
    plt.plot(df['Price'], label='Original Price', alpha=0.6)
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

def decompose_seasonality(df):
    """Decomposes the time series into trend, seasonal, and residual components."""
    save_path = os.path.join(REPORTS_DIR, 'figures', "seasonal_decomposition.png")
    df_monthly = df['Price'].resample('M').mean()
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

def plot_distribution_of_returns(df):
    """Plots a histogram of daily returns to analyze their distribution."""
    save_path = os.path.join(REPORTS_DIR, 'figures', "daily_return_distribution.png")
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

def plot_acf_pacf(df):
    """Plots the Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF)."""
    save_path = os.path.join(REPORTS_DIR, 'figures', "acf_pacf.png")
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

def plot_price_with_events(df, df_events):
    """Plots the Brent oil price time series with key events as vertical lines."""
    save_path = os.path.join(REPORTS_DIR, 'figures', 'price_with_events.png')
    print(f"Generating plot with events: {save_path}")
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(df.index, df['Price'], label='Brent Oil Price', color='cornflowerblue')
    for _, event in df_events.iterrows():
        ax.axvline(event['Date'], color='red', linestyle='--', alpha=0.7, linewidth=1)
        ax.text(event['Date'], df['Price'].max() * 0.95, event['Description'], 
                rotation=90, va='bottom', ha='left', color='red', fontsize=8,
                bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.5, ec='black', lw=0.5))
    ax.set_title('Brent Oil Price with Key Historical Events', fontsize=18, pad=20)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')
    ax.legend()
    ax.xaxis.set_major_locator(mdates.YearLocator(base=5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
    plt.close()
    print(f"Plot saved successfully to: {save_path}")

def stationarity_tests(series):
    """Perform ADF and KPSS stationarity tests on a series."""
    print("\n--- Running Stationarity Tests ---")
    print("Augmented Dickey-Fuller (ADF) Test:")
    adf_result = adfuller(series.dropna())
    print(f"ADF Statistic: {adf_result[0]:.4f}, p-value: {adf_result[1]:.4f}")
    print("\nKwiatkowski-Phillips-Schmidt-Shin (KPSS) Test:")
    kpss_result = kpss(series.dropna(), nlags="auto")
    print(f"KPSS Statistic: {kpss_result[0]:.4f}, p-value: {kpss_result[1]:.4f}")
    return {
        "adf_statistic": adf_result[0],
        "adf_pvalue": adf_result[1],
        "kpss_statistic": kpss_result[0],
        "kpss_pvalue": kpss_result[1]
    }

def main():
    """
    Main function to run the full EDA and change detection pipeline.
    """
    print("=== Starting Analysis Pipeline ===")
    
    df = load_cleaned_data()
    if df is None:
        print("Failed to load data. Exiting.")
        return

    df['daily_return'] = df['Price'].pct_change()
    df['volatility'] = df['daily_return'].rolling(window=30).std() * (252**0.5)

    print("\nMissing values summary:\n", df.isna().sum())
    print("\nGenerating all EDA and change detection plots...")
    
    plot_and_save(df, "Price", "Brent Oil Price (USD)", "price_plot.png", "Price (USD)")
    plot_and_save(df, "daily_return", "Daily Returns", "daily_return_plot.png", "Daily Return")
    plot_and_save(df, "volatility", "Rolling Volatility (30-day Annualized)", "volatility_plot.png", "Volatility")
    
    plot_rolling_means(df)
    decompose_seasonality(df)
    plot_distribution_of_returns(df)
    plot_acf_pacf(df)

    df_events = compile_event_metadata()
    plot_price_with_events(df, df_events)

    stationarity_tests(df["Price"])
    
    print("\n=== Analysis Complete ===")
    print(f"All plots are saved in the '{REPORTS_DIR}/figures' directory.")

if __name__ == "__main__":
    main()