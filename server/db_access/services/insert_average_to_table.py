from db_access.connection import get_connection


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
    conn.close()
