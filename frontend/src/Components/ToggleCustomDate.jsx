import React, { useState } from "react";

const ToggleCustomDate = ({ handleSearch }) => {
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const handleStartDateChange = (e) => {
    setStartDate(e.target.value);
  };

  const handleEndDateChange = (e) => {
    setEndDate(e.target.value);
  };

  const handleSearchClick = () => {
    handleSearch(startDate, endDate);
  };

  return (
    <div className={"flex items-center mb-4"}>
      <label className="mr-4 text-sm text-black">
        <span className="mr-2 text-sm">Start Date:</span>
        <input
          type="date"
          id="startDate"
          value={startDate}
          onChange={handleStartDateChange}
          className="border rounded px-2 py-1"
        />
      </label>
      <label className="mr-4 text-sm text-black">
        <span className="mr-2 text-sm">End Date:</span>
        <input
          type="date"
          id="endDate"
          value={endDate}
          onChange={handleEndDateChange}
          className="border rounded solid px-2 py-1"
        />
      </label>
      <button onClick={handleSearchClick} className="bg-black text-white px-2 rounded">
        Search
      </button>
    </div>
  );
};

export default ToggleCustomDate;
