from connection import get_connection
from schema import init_schema
from seeds.seed_dollar_history import seed_dollar_history


def is_dollar_rate_empty() -> bool:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM dollar_rate")
    count = cur.fetchone()[0]

    conn.close()
    return count == 0


def init_db() -> None:
    try:
        init_schema()
        if is_dollar_rate_empty():
            seed_dollar_history()
    except Exception:
        pass


if __name__ == "__main__":
    init_db()
