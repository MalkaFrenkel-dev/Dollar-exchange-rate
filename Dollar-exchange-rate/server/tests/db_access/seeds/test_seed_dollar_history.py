from datetime import date

from db_access.seeds import seed_dollar_history


def test_seed_dollar_history_inserts_monthly_values(monkeypatch):
    calls = []

    class FakeDate:
        @classmethod
        def today(cls):
            return date(2023, 4, 1)

    def fake_calculate(current):
        return float(current.month)

    def fake_insert(year, month, rate):
        calls.append((year, month, rate))

    monkeypatch.setattr(seed_dollar_history, "date", FakeDate)
    monkeypatch.setattr(seed_dollar_history, "calculate_last_month_average", fake_calculate)
    monkeypatch.setattr(seed_dollar_history, "insert_average_to_table", fake_insert)

    seed_dollar_history.seed_dollar_history()

    assert calls == [
        (2023, 1, 2.0),
        (2023, 2, 3.0),
        (2023, 3, 4.0),
    ]
