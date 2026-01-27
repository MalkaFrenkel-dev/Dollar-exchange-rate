
function MonthSelector({ months, onSelect }) {
  return (
    <select onChange={e => onSelect(e.target.value || null)}>
      <option value="">בחר חודש</option>
      {months.map(m => (
        <option key={m} value={m}>{m}</option>
      ))}
    </select>
  );
}

export default MonthSelector;
