<<<<<<< HEAD:client/src/App.jsx
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

  const selectedIndex = months.indexOf(selectedMonth);
  const selectedAverage = selectedIndex !== -1 ? averages[selectedIndex] : null;

  function handleMonthSelect(month) {
    setSelectedMonth(month || null);
  }

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

  useEffect(() => {
    if (selectedMonth) {
      setFlash(true);
      const timer = setTimeout(() => setFlash(false), 300);
      return () => clearTimeout(timer);
    }
  }, [selectedMonth]);

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

  useEffect(() => {
    if (forecasts.length === 0 || sortedAverages.length === 0) return;

    const diffs = months.map((month, i) => {
      const forecastObj = forecasts.find(f => `${f.year}-${f.month}` === month);
      const forecastValue = forecastObj?.forecast ?? null;
      return forecastValue !== null ? forecastValue - sortedAverages[i] : null;
    });

    setDifferences(diffs);
  }, [months, sortedAverages, forecasts]);

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
            forecasts={forecasts}
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
=======
import { useEffect, useState, useRef } from "react";
import { fetchAllRates, fetchForecasts } from "./api/api";
import AverageGraph from "./components/AverageGraph";
import Table from "./components/Table";
import MonthSelector from "./components/MonthSelector";
import MonthPopup from "./components/MonthPopup";
import AvgDiffTable from "./components/AvarageDifferenceTable";
import SortSelector from "./components/SortSelector";

import styles from "./App.module.css";

export default function App() {
    const [months, setMonths] = useState([]);
    const [averages, setAverages] = useState([]);
    const [forecasts, setForecasts] = useState([]);
    const [differences, setDifferences] = useState([]);
    const [selectedMonth, setSelectedMonth] = useState(null);
    const [flash, setFlash] = useState(false);
    const [sortMethod, setSortMethod] = useState("month");


    const selectedIndex = months.indexOf(selectedMonth);
    const selectedAverage =
        selectedIndex !== -1 ? averages[selectedIndex] : null;

    function handleMonthSelect(month) {
        setSelectedMonth(month || null);
    }

    function getSortedData() {
        if (sortMethod === "month") return { months, averages };

        const combined = months.map((m, i) => [m, averages[i]]);
        combined.sort((a, b) => a[1] - b[1]);

        return {
            months: combined.map(i => i[0]),
            averages: combined.map(i => i[1])
        };
    }

    const { months: sortedMonths, averages: sortedAverages } = getSortedData();

    useEffect(() => {
        if (!selectedMonth) return;
        setFlash(true);
        const t = setTimeout(() => setFlash(false), 300);
        return () => clearTimeout(t);
    }, [selectedMonth]);

    useEffect(() => {
        async function loadData() {
            const data = await fetchAllRates();
            setMonths(data.map(i => `${i[0]}-${i[1]}`));
            setAverages(data.map(i => i[2]));

            const forecastData = await fetchForecasts();
            setForecasts(forecastData);
        }
        loadData();
    }, []);

    useEffect(() => {
        if (!forecasts.length || !sortedAverages.length) return;

        const diffs = months.map((month, i) => {
            const f = forecasts.find(x => `${x.year}-${x.month}` === month);
            return f?.forecast != null ? f.forecast - sortedAverages[i] : null;
        });

        setDifferences(diffs);
    }, [months, sortedAverages, forecasts]);

    return (


        <div className={styles.app} >
            <div className={styles.heroSection}>
                <div className={styles.selectorWrapper}>
                    <MonthSelector months={months} onSelect={handleMonthSelect} />
                    <SortSelector
                        value={sortMethod}
                        onChange={setSortMethod}
                    />
                </div>

                <div className={styles.monthPopupWrapper}>
                    <MonthPopup
                        month={selectedMonth}
                        average={selectedAverage}
                        onClose={() => setSelectedMonth(null)}
                    />
                </div>

                {/* Graph full width */}
                <div className={styles.graphWrapper}>
                    <AverageGraph
                        months={sortedMonths}
                        averages={sortedAverages}
                        selectedMonth={selectedMonth}
                        flash={flash}
                    />
                </div>
            </div>

            {/* Table */}
            <div className={styles.tableWrapper}>
                <Table
                    months={sortedMonths}
                    averages={sortedAverages}
                    forecasts={forecasts}
                    selectedMonth={selectedMonth}
                    flash={flash}
                />
            </div>

            {/* Average Difference Table */}
            <div className={styles.avgDiffWrapper}>
                <AvgDiffTable months={months} differences={differences} />
            </div>
            <div className={styles.scrollHint} />
        </div>
    );
}
>>>>>>> origin/main:Dollar-exchange-rate/client/src/App.jsx
