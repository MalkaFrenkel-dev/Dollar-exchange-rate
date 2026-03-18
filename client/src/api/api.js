const SERVER_URL = import.meta.env.VITE_SERVER_URL;


export async function fetchMonthlyAverages(year, month) {
    try {
        const response = await fetch(`${SERVER_URL}/${year}/${month}`);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        return await response.json();
    } catch {
        return null;
    }
}


export async function fetchAllRates() {
    try {
        const response = await fetch(`${SERVER_URL}/all-rates`);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        return await response.json();
    } catch {
        return [];
    }
}


export async function fetchForecasts() {
    try {
        const response = await fetch(`${SERVER_URL}/forecasts`);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        return await response.json();
    } catch {
        return [];
    }
}
