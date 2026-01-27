from db_access.connection import get_connection

def get_rate_by_month(year, month):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT rate
            FROM dollar_rate
            WHERE year = ? AND month = ?
            """,
              (year, month)
        )      
      
        row = cursor.fetchone()
        return row[0] if row else None
    finally:
        conn.close()
