import React, { useState } from "react";

const ToggleLastYear = ({ handleSearch }) => {
    const [checked, setChecked] = useState(false);

    const handleToggleChange = (e) => {
        setChecked(e.target.checked);
        if (e.target.checked) {
            const currentDate = new Date();
            const lastYearStartDate = new Date(
                currentDate.getFullYear() - 1,
                0,
                1
            ).toISOString().split('T')[0];
            const lastYearEndDate = new Date(
                currentDate.getFullYear() - 1,
                11,
                31
            ).toISOString().split('T')[0];
            handleSearch(lastYearStartDate, lastYearEndDate);
        } else {
            handleSearch("", "");
        }
    };

    return (
        <div className="mb-2">
            <label className="mr-4 text-sm text-black">
                <input
                    type="checkbox"
                    id="toggleLastYear"
                    checked={checked}
                    onChange={handleToggleChange}
                    className="mr-2"
                />
                Last Year
            </label>
        </div>
    );
};

export default ToggleLastYear;
