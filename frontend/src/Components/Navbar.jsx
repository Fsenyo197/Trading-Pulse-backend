import React, { useState } from "react";
import logo from "@Images/eagle-logo.png";
import { Link } from "react-router-dom";

export default function Navbar() {

  const [activeChart, setActiveChart] = useState("");

  const handleLogoClick = () => {
    setActiveChart(""); // Clear the active icon when the logo is clicked
  };

  const handleSetActive = (chart) => {
    setActiveChart(chart);
  };


  return (
    <nav className="md:hidden h-16 bg-black sticky left-0 w-screen text-white flex">
      <div className="flex justify-between items-center mr-4">
        <img
          src={logo}
          alt="Logo"
          className="ml-4 my-2 h-12 w-12 filter brightness-0 invert"
        />
      </div>
      <div className="flex flew-col flex-wrap">
        <div className="ml-4">
          <Link
            to="/"
            className={`sidebar-item rounded-sm ${activeChart === "usd" ? "active" : ""}`}
            onClick={() => handleSetActive("usd")}
          >
            USD
          </Link>
          <Link
            to="/aud"
            className={`sidebar-item rounded-sm ${activeChart === "aud" ? "active" : ""}`}
            onClick={() => handleSetActive("aud")}
          >
            AUD
          </Link>
          <Link
            to="/cad"
            className={`sidebar-item rounded-sm ${activeChart === "cad" ? "active" : ""}`}
            onClick={() => handleSetActive("cad")}
          >
            CAD
          </Link>
          <Link
            to="/chf"
            className={`sidebar-item rounded-sm ${activeChart === "chf" ? "active" : ""}`}
            onClick={() => handleSetActive("chf")}
          >
            CHF
          </Link>
          <Link
            to="/cny"
            className={`sidebar-item rounded-sm ${activeChart === "cny" ? "active" : ""}`}
            onClick={() => handleSetActive("cny")}
          >
            CNY
          </Link>
        </div>
        <div className="ml-4">
          <Link
            to="/eur"
            className={`sidebar-item rounded-sm ${activeChart === "eur" ? "active" : ""}`}
            onClick={() => handleSetActive("eur")}
          >
            EUR
          </Link>
          <Link
            to="/gbp"
            className={`sidebar-item rounded-sm ${activeChart === "gbp" ? "active" : ""}`}
            onClick={() => handleSetActive("gbp")}
          >
            GBP
          </Link>
          <Link
            to="/jpy"
            className={`sidebar-item rounded-sm ${activeChart === "jpy" ? "active" : ""}`}
            onClick={() => handleSetActive("jpy")}
          >
            JPY
          </Link>
          <Link
            to="/nzd"
            className={`sidebar-item rounded-sm ${activeChart === "nzd" ? "active" : ""}`}
            onClick={() => handleSetActive("nzd")}
          >
            NZD
          </Link>
        </div>
      </div>
    </nav>
  );
}
