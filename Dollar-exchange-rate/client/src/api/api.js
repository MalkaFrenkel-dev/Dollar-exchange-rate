const SERVER_URL = import.meta.env.VITE_SERVER_URL;


export async function fetchMonthlyAverages(year, month) {
    try {
        const response = await fetch(`${SERVER_URL}/${year}/${month}`);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error("Failed to fetch monthly averages:", error);
        return null; // או [] בהתאם למה שהקומפוננטה שלך מצפה
    }
}

export async function fetchAllRates() {
    try {
        const response = await fetch(`${SERVER_URL}/all-rates`);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        console.log("Response from fetchAllRates:", response);
        return await response.json();
    } catch (error) {
        console.error("Failed to fetch all rates:", error);
        return [];
    }
}

export async function fetchForecasts() {
    try {
        const response = await fetch(`${SERVER_URL}/forecasts`);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error("Failed to fetch forecast:", error);
        return [];
    }
}
