import React from 'react';

export default function Loader() {
  return (
    <div className="loader" role="status" aria-label="Loading">
      <svg
        className="spinner"
        viewBox="0 0 50 50"
        aria-hidden="true"
        focusable="false"
        width="50"
        height="50"
      >
        <circle
          className="path"
          cx="25"
          cy="25"
          r="20"
          fill="none"
          strokeWidth="5"
          stroke="#4fa94d"
          strokeLinecap="round"
        />
      </svg>
    </div>
  );
}
