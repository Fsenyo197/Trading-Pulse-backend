import React from "react";
import "./Components/index.css";
import NotFound from "./Components/NotFound";
import Layout from "./Components/Layout";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import AUDChart from "./Components/AUDChart";
import USDChart from "./Components/USDChart";
import CADChart from "./Components/CADChart";
import CHFChart from "./Components/CHFChart";
import CNYChart from "./Components/CNYChart";
import EURChart from "./Components/EURChart";
import GBPChart from "./Components/GBPChart";
import JPYChart from "./Components/JPYChart";
import NZDChart from "./Components/NZDChart";

export default function App() {
  return (
    <Router>
      <Layout>
        <div className="flex">
          <Routes>
            <Route exact path="/aud" element={<AUDChart />} />
            <Route exact path="/" element={<USDChart />} />
            <Route exact path="/cad" element={<CADChart />} />
            <Route exact path="/chf" element={<CHFChart />} />
            <Route exact path="/cny" element={<CNYChart />} />
            <Route exact path="/eur" element={<EURChart />} />
            <Route exact path="/gbp" element={<GBPChart />} />
            <Route exact path="/jpy" element={<JPYChart />} />
            <Route exact path="/nzd" element={<NZDChart />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </div>
      </Layout>
    </Router>
  );
}
