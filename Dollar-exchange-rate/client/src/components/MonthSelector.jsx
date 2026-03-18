import { useState } from "react";
import styles from "./MonthSelector.module.css";

export default function MonthSelector({ months, onSelect }) {
  const [open, setOpen] = useState(false);
  const [selected, setSelected] = useState("");

  function handleSelect(month) {
    setSelected(month);
    onSelect(month);
    setOpen(false);
  }

  return (
    <div className={styles.wrapper}>
      <div 
        className={styles.selected} 
        onClick={() => setOpen(!open)}
      >
        {selected || "בחר חודש"}
      </div>
      {open && (
        <div className={styles.dropdown}>
          {months.map((month) => (
            <div 
              key={month} 
              className={styles.option}
              onClick={() => handleSelect(month)}
            >
              {month}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
