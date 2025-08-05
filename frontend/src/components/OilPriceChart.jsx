import React, { useEffect, useState } from 'react';
import Papa from 'papaparse';

export default function TestCSV() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    Papa.parse('/data/event_data.csv', {
      download: true,
      header: true,
      complete: (results) => {
        console.log('CSV Parse Result:', results.data); // ✅ See if data loads
        setEvents(results.data);
      },
      error: (err) => {
        console.error('CSV Load Error:', err); // ❌ Catch fetch/parse errors
      }
    });
  }, []);

  return (
    <div>
      <h3>Event Count: {events.length}</h3>
      <pre>{JSON.stringify(events.slice(0, 3), null, 2)}</pre>
    </div>
  );
}
