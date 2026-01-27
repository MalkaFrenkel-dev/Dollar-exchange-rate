from datetime import date
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.monthly_average import calculate_last_month_average
from services.insert_average_to_table import insert_average_to_table
from dateutil.relativedelta import relativedelta

START_DATE = date(2023, 2, 1)


def seed_dollar_history():

    today = date.today()
    current = START_DATE

    while current <= today:
        rate = calculate_last_month_average(current)
        if rate is not None:
            last_month = current - relativedelta(months=1)
            print(f"Seeding {last_month.isoformat()} with rate {rate}")
            insert_average_to_table(last_month.year, last_month.month, rate)
        current += relativedelta(months=1)
