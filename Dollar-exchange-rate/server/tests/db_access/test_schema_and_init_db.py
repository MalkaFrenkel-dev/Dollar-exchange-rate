import sqlite3

from db_access import init_db as init_db_module
from db_access import schema as schema_module


def test_init_schema_creates_table(monkeypatch, tmp_path):
    db_path = tmp_path / "schema.db"

    monkeypatch.setattr(schema_module, "get_connection", lambda: sqlite3.connect(db_path))

    schema_module.init_schema()

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='dollar_rate'"
    )
    row = cur.fetchone()
    conn.close()

    assert row is not None


def test_is_dollar_rate_empty_true_and_false(monkeypatch, tmp_path):
    db_path = tmp_path / "init.db"
    conn = sqlite3.connect(db_path)
    conn.execute(
        "CREATE TABLE dollar_rate (year INT NOT NULL, month INT NOT NULL, rate REAL NOT NULL, PRIMARY KEY (year, month))"
    )
    conn.commit()
    conn.close()

    monkeypatch.setattr(init_db_module, "get_connection", lambda: sqlite3.connect(db_path))

    assert init_db_module.is_dollar_rate_empty() is True

    conn = sqlite3.connect(db_path)
    conn.execute("INSERT INTO dollar_rate (year, month, rate) VALUES (2023, 1, 3.5)")
    conn.commit()
    conn.close()

    assert init_db_module.is_dollar_rate_empty() is False


def test_init_db_seeds_only_when_empty(monkeypatch):
    calls = {"init_schema": 0, "seed": 0}

    def fake_init_schema():
        calls["init_schema"] += 1

    def fake_seed():
        calls["seed"] += 1

    monkeypatch.setattr(init_db_module, "init_schema", fake_init_schema)
    monkeypatch.setattr(init_db_module, "seed_dollar_history", fake_seed)
    monkeypatch.setattr(init_db_module, "is_dollar_rate_empty", lambda: True)

    init_db_module.init_db()
    assert calls == {"init_schema": 1, "seed": 1}

    calls = {"init_schema": 0, "seed": 0}
    monkeypatch.setattr(init_db_module, "init_schema", lambda: calls.__setitem__("init_schema", 1))
    monkeypatch.setattr(init_db_module, "seed_dollar_history", lambda: calls.__setitem__("seed", 1))
    monkeypatch.setattr(init_db_module, "is_dollar_rate_empty", lambda: False)

    init_db_module.init_db()
    assert calls == {"init_schema": 1, "seed": 0}
