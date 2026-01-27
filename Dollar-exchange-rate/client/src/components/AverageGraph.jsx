import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export default function AverageGraph({ months, averages, selectedMonth }) {
  const data = {
    labels: months,
    datasets: [
      {
        label: "Average Rate",
        data: averages,
        borderColor: "blue",
        backgroundColor: "blue",
        fill: false,
        pointRadius: months.map(m => (m === selectedMonth ? 8 : 3)),
        pointBackgroundColor: months.map(m => (m === selectedMonth ? "yellow" : "blue")),
      },
    ],
  };

  return <Line data={data} />;
}
