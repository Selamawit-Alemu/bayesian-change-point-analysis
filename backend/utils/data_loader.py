# backend/utils/data_loader.py
import pandas as pd
import os

def load_change_points():
    csv_path = os.path.join('data', 'change_points.csv')
    df = pd.read_csv(csv_path)
    return df.to_dict(orient='records')
