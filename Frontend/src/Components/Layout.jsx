import React from "react";
import Sidebar from "./Sidebar";
import Navbar from "./Navbar";

export default function Layout({ children }) {
  return (
    <div className="min-h-screen flex">
      <div className="flex">
        <Sidebar />
      </div>
      <div className="">
        <Navbar />
        <main className="flex-grow p-8">{children}</main>
      </div>
    </div>
  );
}