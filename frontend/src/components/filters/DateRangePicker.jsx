import React from 'react';
import PropTypes from 'prop-types';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';

export default function DateRangePicker({ startDate, endDate, onChange }) {
  return (
    <div className="date-range-picker">
      <DatePicker
        selected={startDate}
        onChange={(date) => onChange({ startDate: date, endDate })}
        selectsStart
        startDate={startDate}
        endDate={endDate}
        maxDate={new Date()}
        placeholderText="Start Date"
      />
      <DatePicker
        selected={endDate}
        onChange={(date) => onChange({ startDate, endDate: date })}
        selectsEnd
        startDate={startDate}
        endDate={endDate}
        minDate={startDate}
        maxDate={new Date()}
        placeholderText="End Date"
      />
    </div>
  );
}

DateRangePicker.propTypes = {
  startDate: PropTypes.instanceOf(Date),
  endDate: PropTypes.instanceOf(Date),
  onChange: PropTypes.func.isRequired,
};
