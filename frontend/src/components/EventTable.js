import events from '../public/data/event_data.csv'; // we’ll change this to actual parsed data
import { useEffect, useState } from 'react';
import Papa from 'papaparse';

const eventColors = {
  Geopolitical: 'red',
  Economic: 'blue',
  OPEC: 'green'
};

export default function EventTable() {
  const [eventData, setEventData] = useState([]);

  useEffect(() => {
    fetch('/data/event_data.csv')
      .then(response => response.text())
      .then(csvText => {
        Papa.parse(csvText, {
          header: true,
          skipEmptyLines: true,
          complete: (results) => {
            setEventData(results.data);
          }
        });
      });
  }, []);

  return (
    <div className="overflow-x-auto mt-6">
      <h2 className="text-lg font-bold mb-2">Historical Events</h2>
      <table className="min-w-full text-sm text-left border">
        <thead className="bg-gray-100">
          <tr>
            <th className="border px-2 py-1">Date</th>
            <th className="border px-2 py-1">Type</th>
            <th className="border px-2 py-1">Description</th>
          </tr>
        </thead>
        <tbody>
          {eventData.map((event, idx) => (
            <tr key={idx}>
              <td className="border px-2 py-1">{event.Date}</td>
              <td className="border px-2 py-1" style={{ color: eventColors[event.EventType] || 'black' }}>
                {event.EventType}
              </td>
              <td className="border px-2 py-1">{event.Description}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
