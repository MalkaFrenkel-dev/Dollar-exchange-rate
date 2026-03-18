from datetime import date

from dateutil.relativedelta import relativedelta

from db_access.services.insert_average_to_table import insert_average_to_table
from db_access.services.monthly_average import calculate_last_month_average


START_DATE = date(2023, 2, 1)


def seed_dollar_history():
    today = date.today()
    current = START_DATE

    while current <= today:
        rate = calculate_last_month_average(current)
        if rate is not None:
            last_month = current - relativedelta(months=1)
            insert_average_to_table(last_month.year, last_month.month, rate)
<<<<<<< HEAD:server/db_access/seeds/seed_dollar_history.py
        current += relativedelta(months=1)
=======
        current += relativedelta(months=1)
>>>>>>> origin/main:Dollar-exchange-rate/server/db_access/seeds/seed_dollar_history.py
