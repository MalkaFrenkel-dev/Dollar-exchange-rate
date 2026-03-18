from connection import get_connection


def init_schema():
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS dollar_rate (
            year INT NOT NULL,
            month INT NOT NULL,
            rate REAL NOT NULL,
            PRIMARY KEY (year, month)
        )
        """
    )
    conn.commit()
    conn.close()
