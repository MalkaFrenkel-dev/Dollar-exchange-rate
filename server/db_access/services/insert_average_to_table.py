<<<<<<< HEAD:server/db_access/services/insert_average_to_table.py
from db_access.connection import get_connection
=======
import os
import sys


sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from connection import get_connection
>>>>>>> origin/main:Dollar-exchange-rate/server/db_access/services/insert_average_to_table.py


def insert_average_to_table(year: int, month: int, rate: float):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO dollar_rate (year, month, rate)
        VALUES (?, ?, ?)
        """,
        (year, month, rate),
    )

    conn.commit()
<<<<<<< HEAD:server/db_access/services/insert_average_to_table.py
    conn.close()
=======
    conn.close()
>>>>>>> origin/main:Dollar-exchange-rate/server/db_access/services/insert_average_to_table.py
