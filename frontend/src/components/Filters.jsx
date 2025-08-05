import React, { useState } from 'react';

export default function Filters({ onFilter }) {
  const [start, setStart] = useState('');
  const [end, setEnd] = useState('');

  const handleApply = () => {
    onFilter({ start, end });
  };

  return (
    <div style={{ marginBottom: '20px' }}>
      <label>
        Start Date:
        <input
          type="date"
          value={start}
          onChange={e => setStart(e.target.value)}
          style={{ marginLeft: 8, marginRight: 20 }}
        />
      </label>
      <label>
        End Date:
        <input
          type="date"
          value={end}
          onChange={e => setEnd(e.target.value)}
          style={{ marginLeft: 8, marginRight: 20 }}
        />
      </label>
      <button onClick={handleApply}>Apply Filter</button>
    </div>
  );
}
