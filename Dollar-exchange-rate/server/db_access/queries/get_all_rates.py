from db_access.connection import get_connection

def get_all_rates(order_by="month"):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        if order_by == "rate":
            query = """
                SELECT year, month, rate
                FROM dollar_rate
                ORDER BY rate ASC
            """
        else:
            query = """
                SELECT year, month, rate
                FROM dollar_rate
                ORDER BY year, month
            """

        cursor.execute(query)
        return cursor.fetchall()

    finally:
        if conn:
            conn.close()
