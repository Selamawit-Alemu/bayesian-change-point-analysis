import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ReferenceLine, ResponsiveContainer
} from 'recharts';

export default function ChangePointChart({ events }) {
  const data = [/* your oil price + change detection data */];

  return (
    <ResponsiveContainer width="100%" height={400}>
      <LineChart data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis
          dataKey="date"
          tickFormatter={(tick) => new Date(tick).getFullYear()}
        />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="price" stroke="#8884d8" name="Oil Price" />
        <Line type="monotone" dataKey="changepoint_prob" stroke="#82ca9d" name="Change Point Prob." />

        {/* Event Markers */}
        {events.map((event, index) => (
          <ReferenceLine
            key={index}
            x={event.date.toISOString().split('T')[0]}
            stroke="red"
            strokeDasharray="3 3"
            label={{
              value: event.description,
              angle: -90,
              position: 'insideTop',
              fontSize: 10,
              fill: 'red',
              textAnchor: 'start'
            }}
          />
        ))}
      </LineChart>
    </ResponsiveContainer>
  );
}

