from db_access.connection import get_connection


def get_rate_by_month(year, month):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT ROUND(rate, 3) AS rate
            FROM dollar_rate
            WHERE year = ? AND month = ?
            """,
            (year, month),
        )
        row = cursor.fetchone()
        return round(row[0], 3) if row else None
    finally:
        conn.close()
