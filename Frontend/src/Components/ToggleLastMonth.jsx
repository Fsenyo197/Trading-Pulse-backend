import React, { useState } from "react";

const ToggleLastMonth = ({ handleSearch }) => {
    const [checked, setChecked] = useState(false);

    const handleToggleChange = (e) => {
        setChecked(e.target.checked);
        if (e.target.checked) {
            const currentDate = new Date();
            const lastMonthStartDate = new Date(
                currentDate.getFullYear(),
                currentDate.getMonth() - 1,
                1
            ).toISOString().split('T')[0];
            const lastMonthEndDate = new Date(
                currentDate.getFullYear(),
                currentDate.getMonth(),
                0
            ).toISOString().split('T')[0];
            handleSearch(lastMonthStartDate, lastMonthEndDate);
        } else {
            handleSearch("", "");
        }
    };

    return (
        <div className="mb-2">
            <label className="mr-4 text-sm text-black">
                <input
                    type="checkbox"
                    id="toggleLastMonth"
                    checked={checked}
                    onChange={handleToggleChange}
                    className="mr-2"
                />
                Last Month
            </label>
        </div>
    );
};

export default ToggleLastMonth;
