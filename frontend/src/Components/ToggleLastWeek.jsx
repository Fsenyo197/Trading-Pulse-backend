import React, { useState } from "react";

const ToggleLastWeek = ({ handleSearch }) => {
    const [checked, setChecked] = useState(false);

    const handleToggleChange = (e) => {
        setChecked(e.target.checked);
        if (e.target.checked) {
            const currentDate = new Date();
            const lastWeekStartDate = new Date(
                currentDate.getFullYear(),
                currentDate.getMonth(),
                currentDate.getDate() - currentDate.getDay() - 6
            ).toISOString().split('T')[0];
            const lastWeekEndDate = new Date(
                currentDate.getFullYear(),
                currentDate.getMonth(),
                currentDate.getDate() - currentDate.getDay()
            ).toISOString().split('T')[0];
            handleSearch(lastWeekStartDate, lastWeekEndDate);
        } else {
            handleSearch("", "");
        }
    };

    return (
        <div className="mb-2">
            <label className="mr-4 text-sm text-black">
                <input
                    type="checkbox"
                    id="toggleLastWeek"
                    checked={checked}
                    onChange={handleToggleChange}
                    className="mr-2"
                />
                Last Week
            </label>
        </div>
    );
};

export default ToggleLastWeek;
