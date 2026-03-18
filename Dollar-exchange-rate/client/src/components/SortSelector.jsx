import { useState } from "react";
import styles from "./SortSelector.module.css";

export default function SortSelector({ value, onChange }) {
  const [open, setOpen] = useState(false);

  const options = [
    { value: "month", label: "מיון לפי חודש" },
    { value: "value", label: "מיון לפי גובה שער" },
  ];

  const selectedLabel =
    options.find(o => o.value === value)?.label || "בחר מיון";

  function handleSelect(option) {
    onChange(option.value);
    setOpen(false);
  }

  return (
    <div className={styles.wrapper}>
      <div
        className={styles.selected}
        onClick={() => setOpen(!open)}
      >
        {selectedLabel}
      </div>

      {open && (
        <div className={styles.dropdown}>
          {options.map(option => (
            <div
              key={option.value}
              className={styles.option}
              onClick={() => handleSelect(option)}
            >
              {option.label}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
