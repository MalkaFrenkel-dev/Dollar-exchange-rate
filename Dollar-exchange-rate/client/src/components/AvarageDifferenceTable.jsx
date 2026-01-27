export default function AvgDiffTable({ months, differences }) {
  const avgDiff3Months = [];

  for (let i = 0; i <= differences.length - 3; i++) {
    const window = differences.slice(i, i + 3).filter(v => v != null);
    if (window.length === 3) {
      const avg = window.reduce((a, b) => a + b, 0) / 3;
      avgDiff3Months.push({
        period: `${months[i]} – ${months[i + 2]}`,
        value: avg.toFixed(2),
      });
    }
  }

  return (
    <table style={{ marginTop: "20px", width: "50%" }}>
      <thead>
        <tr>
          <th>Period</th>
          <th>Avg difference</th>
        </tr>
      </thead>
      <tbody>
        {avgDiff3Months.map(row => (
          <tr key={row.period}>
            <td>{row.period}</td>
            <td>{row.value}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
