from datetime import date

from db_access.init_db import init_db
from db_access.services.insert_average_to_table import insert_average_to_table
from db_access.services.monthly_average import calculate_last_month_average


today = date.today()


try:
    init_db()
    avg = calculate_last_month_average(today)
    insert_average_to_table(today.year, today.month, avg)
except Exception:
    pass
