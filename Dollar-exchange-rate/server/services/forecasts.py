from datetime import date
from db_access.queries.get_rate_by_month import get_rate_by_month

today = date.today()

def prev_month(year: int, month: int, steps: int = 1):
    month -= steps
    while month <= 0:
        month += 12
        year -= 1
    return year, month

def forecasts():
    try:
        forecasts = []
        START_YEAR = 2023

        for year in range(START_YEAR, today.year + 1):
            for month in range(1, 13):
                if year == today.year and month > today.month:
                    break

                year1, month1 = prev_month(year, month, 1)
                year2, month2 = prev_month(year, month, 2)
                year3, month3 = prev_month(year, month, 3)

                rate1:float = get_rate_by_month(year1, month1)
                rate2:float = get_rate_by_month(year2, month2)
                rate3:float = get_rate_by_month(year3, month3)
                if rate1 is None or rate2 is None or rate3 is None:
                            continue
                forecast_avg = (rate1 + rate2 + rate3) / 3
                forecasts.append({
                    "year": year,
                    "month": month,
                    "forecast": forecast_avg
                })

        return forecasts
    except Exception as e:
        print(f"Error in forecasts calculation: {e}")
        return []
