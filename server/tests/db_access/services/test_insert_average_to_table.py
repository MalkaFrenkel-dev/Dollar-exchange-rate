import sqlite3

from db_access.services import insert_average_to_table as insert_service


def test_insert_average_to_table_inserts_row(monkeypatch, tmp_path):
    db_path = tmp_path / "insert.db"
    conn = sqlite3.connect(db_path)
    conn.execute(
        "CREATE TABLE dollar_rate (year INT NOT NULL, month INT NOT NULL, rate REAL NOT NULL, PRIMARY KEY (year, month))"
    )
    conn.commit()
    conn.close()

    monkeypatch.setattr(insert_service, "get_connection", lambda: sqlite3.connect(db_path))

    insert_service.insert_average_to_table(2024, 6, 3.85)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT year, month, rate FROM dollar_rate")
    row = cur.fetchone()
    conn.close()

    assert row == (2024, 6, 3.85)
