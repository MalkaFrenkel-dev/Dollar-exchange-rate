from dateutil.relativedelta import relativedelta

from db_access.services.update_dollar_exchange import update_dollar_rate


def last_month_range(date):
    first_of_this_month = date.replace(day=1)
    last_day_last_month = first_of_this_month - relativedelta(days=1)
    first_day_last_month = last_day_last_month.replace(day=1)
    return first_day_last_month, last_day_last_month


def calculate_last_month_average(date):
    start, end = last_month_range(date)
    total = 0.0
    days = 0
    current = start

    while current <= end:
        try:
            rate: float = update_dollar_rate(current)
            total += rate
            days += 1
        except Exception:
            pass
        current += relativedelta(days=1)

    if days == 0:
        raise RuntimeError("No data for last month")

<<<<<<< HEAD:server/db_access/services/monthly_average.py
    return total / days
=======
    return total / days
>>>>>>> origin/main:Dollar-exchange-rate/server/db_access/services/monthly_average.py
