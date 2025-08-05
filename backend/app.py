# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
from utils.data_loader import load_change_points
import pandas as pd
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from React frontend

@app.route('/api/change-points', methods=['GET'])
def get_change_points():
    try:
        data = load_change_points()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/oil-prices', methods=['GET'])
def get_oil_prices():
    df = pd.read_csv('data/brent_clean.csv', parse_dates=['Date'])
    df = df[['Date', 'Price']]
    df['Date'] = df['Date'].astype(str)
    return jsonify(df.to_dict(orient='records'))


@app.route('/api/oil-prices/filter', methods=['GET'])
def get_filtered_oil_prices():
    start = request.args.get('start')  # e.g. '2020-01-01'
    end = request.args.get('end')      # e.g. '2021-01-01'
    df = pd.read_csv('data/brent_clean.csv', parse_dates=['Date'])
    df = df[['Date', 'Price']]
    if start:
        df = df[df['Date'] >= start]
    if end:
        df = df[df['Date'] <= end]
    df['Date'] = df['Date'].astype(str)
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/oil-metrics', methods=['GET'])
def get_oil_metrics():
    df = pd.read_csv('data/brent_clean.csv', parse_dates=['Date'])
    df = df[['Date', 'daily_return', 'volatility']]
    df['Date'] = df['Date'].astype(str)
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/events', methods=['GET'])
def get_events():
    """Serve historical geopolitical/economic events."""
    try:
        events = pd.read_csv('data/event_data.csv', parse_dates=['Date'])
        events['Date'] = events['Date'].astype(str)
        return jsonify(events.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)