import styles from "./Table.module.css";

export default function Table({
  months,
  averages,
  forecasts,
  selectedMonth,
  flash
}) {
  const min = Math.min(...averages);
  const max = Math.max(...averages);

  function getColor(value) {
    const ratio = (value - min) / (max - min);
    return `rgb(
      ${Math.floor(255 * (1 - ratio))},
      ${Math.floor(255 * ratio)},
      0
    )`;
  }

  return (
    <table className={styles.table}>
      <thead>
        <tr>
          <th>Month</th>
          <th>Average</th>
          <th>Forecast</th>
          <th>Difference</th>
        </tr>
      </thead>

      <tbody>
        {months.map((month, i) => {
          const isSelected = month === selectedMonth;
          const forecastObj = forecasts.find(
            f => `${f.year}-${f.month}` === month
          );
          const forecastValue = forecastObj?.forecast ?? null;
          const difference =
            forecastValue !== null
              ? (forecastValue - averages[i]).toFixed(2)
              : "";

          return (
            <tr
              key={month}
              className={isSelected ? styles.selectedRow : ""}
              style={{
                backgroundColor: getColor(averages[i])
              }}
            >
              <td>{month}</td>
              <td>{averages[i]}</td>
              <td>{forecastValue ?? ""}</td>
              <td>{difference}</td>
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}
