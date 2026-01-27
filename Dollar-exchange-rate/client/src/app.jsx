import { useEffect, useState, useRef } from "react";
import { fetchAllRates, fetchForecasts } from "./api/api";
import AverageGraph from "./components/AverageGraph";
import Table from "./components/Table";
import MonthSelector from "./components/MonthSelector";
import MonthPopup from "./components/MonthPopup";
import AvgDiffTable from "./components/AvarageDifferenceTable";

export default function App() {
  const [months, setMonths] = useState([]);
  const [averages, setAverages] = useState([]);
  const [forecasts, setForecasts] = useState([]);
  const [differences, setDifferences] = useState([]);
  const [selectedMonth, setSelectedMonth] = useState(null);
  const [flash, setFlash] = useState(false);
  const [sortMethod, setSortMethod] = useState("month");

  const appRef = useRef(null);

  // חישוב הבחירה הנוכחית
  const selectedIndex = months.indexOf(selectedMonth);
  const selectedAverage = selectedIndex !== -1 ? averages[selectedIndex] : null;

  // פונקציה לבחירת חודש
  function handleMonthSelect(month) {
    setSelectedMonth(month || null);
  }

  // מיון לפי חודשים או ממוצע
  function getSortedData() {
    if (sortMethod === "month") {
      return { months, averages };
    } else {
      const combined = months.map((m, i) => [m, averages[i]]);
      combined.sort((a, b) => a[1] - b[1]);
      return {
        months: combined.map(item => item[0]),
        averages: combined.map(item => item[1])
      };
    }
  }
  const { months: sortedMonths, averages: sortedAverages } = getSortedData();

  // הבהוב
  useEffect(() => {
    if (selectedMonth) {
      setFlash(true);
      const timer = setTimeout(() => setFlash(false), 300);
      return () => clearTimeout(timer);
    }
  }, [selectedMonth]);

  // טעינת נתונים ותחזיות מהשרת
  useEffect(() => {
    async function loadData() {
      const data = await fetchAllRates();
      setMonths(data.map(item => `${item[0]}-${item[1]}`));
      setAverages(data.map(item => item[2]));

      const forecastData = await fetchForecasts();
      setForecasts(forecastData);
    }
    loadData();
  }, []);

  // חישוב differences
  useEffect(() => {
    if (forecasts.length === 0 || sortedAverages.length === 0) return;

    const diffs = months.map((month, i) => {
      const forecastObj = forecasts.find(f => `${f.year}-${f.month}` === month);
      const forecastValue = forecastObj?.forecast ?? null;
      return forecastValue !== null ? forecastValue - sortedAverages[i] : null;
    });

    setDifferences(diffs);
  }, [months, sortedAverages, forecasts]);

  // ביטול בחירה בלחיצה מחוץ לאזורי גרף/טבלה/selector
  useEffect(() => {
    function handleClickOutside(e) {
      const graph = document.querySelector("#graph-content");
      const table = document.querySelector("#table-content");
      const selector = document.querySelector("#month-selector select");
      if (!graph?.contains(e.target) &&
          !table?.contains(e.target) &&
          !selector?.contains(e.target)) {
        setSelectedMonth(null);
      }
    }
    document.addEventListener("click", handleClickOutside);
    return () => document.removeEventListener("click", handleClickOutside);
  }, []);

  return (
    <div ref={appRef} id="app-container" style={{ padding: "20px" }}>
      
      <div id="month-selector" style={{ marginBottom: "20px" }}>
        <MonthSelector months={months} onSelect={handleMonthSelect} />
      </div>

      <div id="graph-container" style={{ marginBottom: "20px", display: "inline-block" }}>
        <div id="graph-content">
          <AverageGraph
            months={sortedMonths}
            averages={sortedAverages}
            selectedMonth={selectedMonth}
            flash={flash}
          />
        </div>
      </div>

      <div id="table-container" style={{ display: "inline-block", marginLeft: "20px" }}>
        <div id="table-content">
          <Table
            months={sortedMonths}
            averages={sortedAverages}
            forecasts={forecasts}   // <-- מעבירים props בלבד
            selectedMonth={selectedMonth}
            flash={flash}
          />
        </div>
      </div>

      <AvgDiffTable
        months={months}
        differences={differences}
      />

      <MonthPopup month={selectedMonth} average={selectedAverage} />

      <div style={{ marginTop: "20px" }}>
        <select value={sortMethod} onChange={e => setSortMethod(e.target.value)}>
          <option value="month">סדר לפי חודשים</option>
          <option value="average">סדר לפי גובה השער</option>
        </select>
      </div>

    </div>
  );
}
