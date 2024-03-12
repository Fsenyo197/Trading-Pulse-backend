import React, { useState } from "react";

const ToggleThisMonth = ({ handleSearch }) => {
    const [checked, setChecked] = useState(false);

    const handleToggleChange = (e) => {
        setChecked(e.target.checked);
        if (e.target.checked) {
            const currentDate = new Date();
            const firstDayOfMonth = new Date(
                currentDate.getFullYear(),
                currentDate.getMonth(),
                1
            ).toISOString().split('T')[0];
            const lastDayOfPreviousWeek = new Date(
                currentDate.getFullYear(),
                currentDate.getMonth(),
                currentDate.getDate() - currentDate.getDay()
            ).toISOString().split('T')[0];
            handleSearch(firstDayOfMonth, lastDayOfPreviousWeek);
        } else {
            handleSearch("", "");
        }
    };

    return (
        <div className="mb-2">
            <label className="mr-4 text-sm text-black">
                <input
                    type="checkbox"
                    id="toggleThisMonth"
                    checked={checked}
                    onChange={handleToggleChange}
                    className="mr-2"
                />
                This Month
            </label>
        </div>
    );
};

export default ToggleThisMonth;
