import React, { useState } from "react";

const ToggleThisYear = ({ handleSearch }) => {
    const [checked, setChecked] = useState(false);

    const handleToggleChange = (e) => {
        setChecked(e.target.checked);
        if (e.target.checked) {
            const currentDate = new Date();
            const thisYearStartDate = new Date(
                currentDate.getFullYear(),
                0,
                1
            ).toISOString().split('T')[0];
            const lastWeekEndDate = new Date(
                currentDate.getFullYear(),
                currentDate.getMonth(),
                currentDate.getDate() - currentDate.getDay()
            ).toISOString().split('T')[0];
            handleSearch(thisYearStartDate, lastWeekEndDate);
        } else {
            handleSearch("", "");
        }
    };

    return (
        <div className="mb-2">
            <label className="mr-4 text-sm text-black">
                <input
                    type="checkbox"
                    id="toggleThisYear"
                    checked={checked}
                    onChange={handleToggleChange}
                    className="mr-2"
                />
                This Year
            </label>
        </div>
    );
};

export default ToggleThisYear;
