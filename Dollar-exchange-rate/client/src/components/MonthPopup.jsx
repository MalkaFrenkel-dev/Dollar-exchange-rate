import styles from "./MonthPopup.module.css";

function MonthPopup({ month, average, onClose }) {
  if (!month) return null;

  return (
    <div className={styles.popup}>
      <div className={styles.title}>{month}</div>
      <div className={styles.value}>{average}</div>

      <button className={styles.close} onClick={onClose}>
        X
      </button>
    </div>
  );
}

export default MonthPopup;
