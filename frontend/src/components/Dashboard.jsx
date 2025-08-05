import React, { useEffect, useState } from 'react';
import { fetchOilPrices, fetchChangePoints } from '../api/apiClient';
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ReferenceLine
} from 'recharts';

export default function Dashboard() {
  const [oilPrices, setOilPrices] = useState([]);
  const [changePoints, setChangePoints] = useState([]);
  const [loading, setLoading] = useState(false);
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  const loadData = async (start, end) => {
    setLoading(true);
    try {
      const prices = await fetchOilPrices(start, end);
      const changes = await fetchChangePoints();
      setOilPrices(prices);
      setChangePoints(changes);
    } catch (err) {
      alert('Failed to load data: ' + err.message);
    }
    setLoading(false);
  };

  useEffect(() => {
    loadData();
  }, []);

  // Filter handlers
  const handleFilter = () => {
    loadData(startDate || undefined, endDate || undefined);
  };

  // Prepare change point dates as strings to match XAxis format
  const changePointDates = changePoints.map(cp => cp.change_date);

  return (
    <div style={{ maxWidth: 900, margin: 'auto', padding: 20, fontFamily: 'Arial, sans-serif' }}>
      <h1>Brent Oil Price Dashboard</h1>

      <div style={{ marginBottom: 20 }}>
        <label>
          Start Date:{' '}
          <input
            type="date"
            value={startDate}
            onChange={e => setStartDate(e.target.value)}
            max={endDate || ''}
          />
        </label>{' '}
        <label>
          End Date:{' '}
          <input
            type="date"
            value={endDate}
            onChange={e => setEndDate(e.target.value)}
            min={startDate || ''}
          />
        </label>{' '}
        <button onClick={handleFilter}>Apply</button>
      </div>

      {loading ? (
        <p>Loading data...</p>
      ) : (
        <ResponsiveContainer width="100%" height={400}>
          <LineChart data={oilPrices}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis
              dataKey="Date"
              tickFormatter={(str) => str.slice(0, 10)}
              minTickGap={20}
              allowDuplicatedCategory={false}
            />
            <YAxis domain={['auto', 'auto']} />
            <Tooltip />
            <Legend />
            <Line
              type="monotone"
              dataKey="Price"
              stroke="#8884d8"
              dot={false}
              strokeWidth={2}
              name="Brent Oil Price"
            />

            {/* Add vertical lines for each change point */}
            {changePointDates.map((date) => (
              <ReferenceLine
                key={date}
                x={date}
                stroke="red"
                strokeDasharray="3 3"
                label={{ value: 'Change Point', position: 'top', fill: 'red', fontSize: 10 }}
              />
            ))}
          </LineChart>
        </ResponsiveContainer>
      )}
    </div>
  );
}

