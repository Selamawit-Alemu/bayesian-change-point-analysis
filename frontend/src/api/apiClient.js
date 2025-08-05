const API_BASE = 'http://127.0.0.1:5000/api';

export async function fetchOilPrices(start, end) {
  if (start || end) {
    const params = new URLSearchParams();
    if (start) params.append('start', start);
    if (end) params.append('end', end);
    const url = `${API_BASE}/oil-prices/filter?${params.toString()}`;
    const res = await fetch(url);
    if (!res.ok) throw new Error('Failed to fetch filtered oil prices');
    return res.json();
  } else {
    const res = await fetch(`${API_BASE}/oil-prices`);
    if (!res.ok) throw new Error('Failed to fetch oil prices');
    return res.json();
  }
}
export async function fetchEvents() {
  const response = await fetch('http://localhost:5000/api/events');
  if (!response.ok) throw new Error('Failed to fetch events');
  return response.json();
}


export async function fetchChangePoints() {
  const res = await fetch(`${API_BASE}/change-points`);
  if (!res.ok) throw new Error('Failed to fetch change points');
  return res.json();
}
