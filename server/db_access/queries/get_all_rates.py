from db_access.connection import get_connection


def get_all_rates(order_by="month"):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        if order_by == "rate":
            query = """
                SELECT year, month, ROUND(rate, 3) AS rate
                FROM dollar_rate
                ORDER BY rate ASC
            """
        else:
            query = """
                SELECT year, month, ROUND(rate, 3) AS rate
                FROM dollar_rate
                ORDER BY year, month
            """

        cursor.execute(query)
        return cursor.fetchall()

    finally:
        if conn:
<<<<<<< HEAD:server/db_access/queries/get_all_rates.py
            conn.close()
=======
            conn.close()
>>>>>>> origin/main:Dollar-exchange-rate/server/db_access/queries/get_all_rates.py
