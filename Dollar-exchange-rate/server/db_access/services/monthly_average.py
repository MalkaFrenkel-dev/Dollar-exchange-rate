import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from update_dollar_exchange import update_dollar_rate
from dateutil.relativedelta import relativedelta


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
        except Exception as e:
            print(f"Failed for day{current}: {e}")
        current += relativedelta(days=1)

    if days == 0:
        raise RuntimeError("No data for last month")

    return total / days
