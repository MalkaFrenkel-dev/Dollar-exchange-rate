function MonthPopup({ month, average }) {
  if (!month) return null;

  return (
    <div className="popup">
      <h3>{month}</h3>
      <p>ממוצע: {average}</p>
    </div>
  );
}
export default MonthPopup;