import React, { useState } from "react";
import logo from "@Images/eagle-logo.png";
import { Link } from "react-router-dom";

const Sidebar = () => {
  const [activeChart, setActiveChart] = useState("");

  const handleLogoClick = () => {
    setActiveChart(""); // Clear the active icon when the logo is clicked
  };

  const handleSetActive = (chart) => {
    setActiveChart(chart);
  };

  return (
    <nav className="bg-black text-white w-24 flex-col hidden md:flex">
      <div>
        <Link to="/" onClick={handleLogoClick}>
          <img
            src={logo}
            alt="logo"
            className="w-16 h-16 ml-2 mb-20 filter brightness-0 invert"
          />
        </Link>
      </div>
      <div className="flex flex-col h-full justify-normal items-center">
        <Link
          to="/"
          className={`sidebar-item mb-4 rounded-sm ${activeChart === "usd" ? "active" : ""}`}
          onClick={() => handleSetActive("usd")}
        >
          USD
        </Link>
        <Link
          to="/aud"
          className={`sidebar-item mb-4 rounded-sm ${activeChart === "aud" ? "active" : ""}`}
          onClick={() => handleSetActive("aud")}
        >
          AUD
        </Link>
        <Link
          to="/cad"
          className={`sidebar-item mb-4 rounded-sm ${activeChart === "cad" ? "active" : ""}`}
          onClick={() => handleSetActive("cad")}
        >
          CAD
        </Link>
        <Link
          to="/chf"
          className={`sidebar-item mb-4 rounded-sm ${activeChart === "chf" ? "active" : ""}`}
          onClick={() => handleSetActive("chf")}
        >
          CHF
        </Link>
        <Link
          to="/cny"
          className={`sidebar-item mb-4 rounded-sm ${activeChart === "cny" ? "active" : ""}`}
          onClick={() => handleSetActive("cny")}
        >
          CNY
        </Link>
        <Link
          to="/eur"
          className={`sidebar-item mb-4 rounded-sm ${activeChart === "eur" ? "active" : ""}`}
          onClick={() => handleSetActive("eur")}
        >
          EUR
        </Link>
        <Link
          to="/gbp"
          className={`sidebar-item mb-4 rounded-sm ${activeChart === "gbp" ? "active" : ""}`}
          onClick={() => handleSetActive("gbp")}
        >
          GBP
        </Link>
        <Link
          to="/jpy"
          className={`sidebar-item mb-4 rounded-sm ${activeChart === "jpy" ? "active" : ""}`}
          onClick={() => handleSetActive("jpy")}
        >
          JPY
        </Link>
        <Link
          to="/nzd"
          className={`sidebar-item mb-4 rounded-sm ${activeChart === "nzd" ? "active" : ""}`}
          onClick={() => handleSetActive("nzd")}
        >
          NZD
        </Link>
      </div>
    </nav>
  );
};

export default Sidebar;
