import pandas as pd
import numpy as np
import os
from datetime import datetime

def load_and_clean_data(filepath):
    """
    Load Brent oil price data from a CSV file, clean and preprocess it.
    Steps:
    - Load CSV
    - Parse and standardize date format
    - Handle missing/invalid values
    - Sort by date and set date as index
    
    Args:
        filepath (str): Path to the raw data CSV file

    Returns:
        pd.DataFrame: Cleaned time series data indexed by date
    """
    print(f"Loading data from: {filepath}")
    try:
        df = pd.read_csv(filepath)

        # Rename columns to standard format if necessary
        if 'Date' not in df.columns:
            date_col = [col for col in df.columns if col.lower() == 'date']
            if date_col:
                df.rename(columns={date_col[0]: 'Date'}, inplace=True)
            else:
                raise ValueError("Missing 'Date' column")

        if 'Price' not in df.columns:
            price_col = [col for col in df.columns if col.lower() in ['price', 'value', 'close']]
            if price_col:
                df.rename(columns={price_col[0]: 'Price'}, inplace=True)
            else:
                raise ValueError("Missing 'Price' column")

        # Parse date column
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df.dropna(subset=['Date'], inplace=True)
        df.sort_values('Date', inplace=True)
        df.set_index('Date', inplace=True)

        # Handle missing price values
        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
        df['Price'] = df['Price'].interpolate(method='time')
        df.dropna(subset=['Price'], inplace=True)

        print(f"Data loaded: {df.shape[0]} records from {df.index.min().date()} to {df.index.max().date()}")
        return df

    except Exception as e:
        print(f"Data loading failed: {e}")
        return None

def calculate_daily_returns(df):
    """
    Compute daily percentage return of Brent oil price.

    Args:
        df (pd.DataFrame): Cleaned Brent oil price data

    Returns:
        pd.DataFrame: DataFrame with daily_return column added
    """
    df['daily_return'] = df['Price'].pct_change() * 100
    return df

def calculate_volatility(df, window=30):
    """
    Compute rolling volatility (standard deviation of daily return).

    Args:
        df (pd.DataFrame): Time series with daily_return column
        window (int): Rolling window size in days (default=30)

    Returns:
        pd.DataFrame: DataFrame with volatility column added
    """
    df['volatility'] = df['daily_return'].rolling(window=window).std()
    return df

def save_processed_data(df, output_path):
    """
    Save processed DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): DataFrame to save
        output_path (str): Path to output CSV
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path)
    print(f"Data saved to: {output_path}")

def main():
    """
    Script entry point for testing the data processing pipeline
    """
    print("=== Running Brent Oil Data Processor ===")
    raw_path = '../data/BrentOilPrices.csv'
    processed_path = '../data/processed/brent_clean.csv'

    df = load_and_clean_data(raw_path)

    if df is not None:
        df = calculate_daily_returns(df)
        df = calculate_volatility(df)
        print(df.head())
        save_processed_data(df, processed_path)
    else:
        print("Data processing failed.")

if __name__ == '__main__':
    main()
