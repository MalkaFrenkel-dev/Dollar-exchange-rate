import sqlite3

from db_access.queries import get_all_rates, get_rate_by_month


def _prepare_db(path):
    conn = sqlite3.connect(path)
    conn.execute(
        """
        CREATE TABLE dollar_rate (
            year INT NOT NULL,
            month INT NOT NULL,
            rate REAL NOT NULL,
            PRIMARY KEY (year, month)
        )
        """
    )
    conn.executemany(
        "INSERT INTO dollar_rate (year, month, rate) VALUES (?, ?, ?)",
        [
            (2023, 3, 3.1234),
            (2023, 1, 3.9876),
            (2023, 2, 3.4567),
        ],
    )
    conn.commit()
    conn.close()


def test_get_rate_by_month_returns_rounded_value(monkeypatch, tmp_path):
    db_path = tmp_path / "test.db"
    _prepare_db(db_path)

    monkeypatch.setattr(
        get_rate_by_month, "get_connection", lambda: sqlite3.connect(db_path)
    )

    assert get_rate_by_month.get_rate_by_month(2023, 2) == 3.457


def test_get_rate_by_month_returns_none_for_missing(monkeypatch, tmp_path):
    db_path = tmp_path / "test.db"
    _prepare_db(db_path)

    monkeypatch.setattr(
        get_rate_by_month, "get_connection", lambda: sqlite3.connect(db_path)
    )

    assert get_rate_by_month.get_rate_by_month(2024, 1) is None


def test_get_all_rates_sorts_by_month(monkeypatch, tmp_path):
    db_path = tmp_path / "test.db"
    _prepare_db(db_path)

    monkeypatch.setattr(get_all_rates, "get_connection", lambda: sqlite3.connect(db_path))

    result = get_all_rates.get_all_rates()
    assert result == [
        (2023, 1, 3.988),
        (2023, 2, 3.457),
        (2023, 3, 3.123),
    ]


def test_get_all_rates_sorts_by_rate(monkeypatch, tmp_path):
    db_path = tmp_path / "test.db"
    _prepare_db(db_path)

    monkeypatch.setattr(get_all_rates, "get_connection", lambda: sqlite3.connect(db_path))

    result = get_all_rates.get_all_rates(order_by="rate")
    assert result == [
        (2023, 3, 3.123),
        (2023, 2, 3.457),
        (2023, 1, 3.988),
    ]
