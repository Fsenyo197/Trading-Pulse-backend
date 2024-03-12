import React, { useEffect, useRef, useState } from "react";
import Chart from "chart.js/auto";
import { CategoryScale } from "chart.js";

Chart.register(CategoryScale);

const BarChart = ({ chartData }) => {
  const chartRef = useRef(null);
  const [screenWidth, setScreenWidth] = useState(window.innerWidth);

  useEffect(() => {
    const handleResize = () => {
      setScreenWidth(window.innerWidth);
    };

    window.addEventListener("resize", handleResize);

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  useEffect(() => {
    let chartInstance = null;

    if (chartRef.current) {
      const canvas = chartRef.current;

      if (chartInstance) {
        chartInstance.destroy();
      }

      chartInstance = new Chart(canvas, {
        type: "bar",
        data: chartData,
        options: {
          scales: {
            x: {
              type: "category",
              ticks: {
                color: 'black'
              },
            },
            y: {
              ticks: {
                color: 'black'
              },
            }
          },
          plugins: {
            legend: {
              display: true,
              position: "top",
            },
          },
          responsive: true,
          elements: {
            bar: {
              borderWidth: 2,
            },
          },
          barPercentage: 0.5,
        },
      });
    }

    return () => {
      if (chartInstance) {
        chartInstance.destroy();
      }
    };
  }, [screenWidth, chartData]);

  return (
    <div style={{ width: "100%", maxWidth: "900px", margin: "0 auto" }}>
      <canvas ref={chartRef} />
    </div>
  );
};

export default BarChart;
