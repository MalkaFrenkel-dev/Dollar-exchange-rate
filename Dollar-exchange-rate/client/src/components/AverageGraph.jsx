import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
);

import flashStyles from "../styles/flash.module.css";
import styles from "./AverageGraph.module.css";

export default function AverageGraph({
  months,
  averages,
  selectedMonth,
  flash
}) {
  const data = {
    labels: months,
    datasets: [
      {
        data: averages,
        borderColor: "rgba(47, 129, 247, 0.6)",
        pointRadius: months.map(m => (m === selectedMonth ? 7 : 3)),

    pointBackgroundColor: months.map(m =>
      m === selectedMonth
        ? "rgb(88, 101, 242)"  
        : "rgba(47, 129, 247, 0.8)"
    ),

    pointBorderColor: months.map(m =>
      m === selectedMonth
        ? "rgba(168, 85, 247, 0.8)" 
        : "transparent"
    ),

    pointBorderWidth: months.map(m =>
      m === selectedMonth ? 6 : 0
    ),}]
  

  };
const options = {
  responsive: true,
  maintainAspectRatio: false,
};

  return (
    <div className={`${styles.container} ${flash ? flashStyles.flash : ""}`}>
      <Line data={data} options={options} />
    </div>
  );
}
