import styles from "./AvarageDifferenceTable.module.css";

export default function AvgDiffCards({ months, differences }) {
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
    <div className={styles.cardsContainer}>
      {avgDiff3Months.map(row => (
        <div key={row.period} className={styles.card}>
          <div className={styles.period}>{row.period}</div>
          <div className={styles.value}>{row.value}</div>
        </div>
      ))}
    </div>
  );
}
