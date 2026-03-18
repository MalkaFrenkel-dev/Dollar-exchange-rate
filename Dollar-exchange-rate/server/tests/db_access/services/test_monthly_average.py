from datetime import date

import pytest

from db_access.services import monthly_average


def test_last_month_range_handles_leap_year():
    start, end = monthly_average.last_month_range(date(2024, 3, 18))
    assert start == date(2024, 2, 1)
    assert end == date(2024, 2, 29)


def test_calculate_last_month_average_success(monkeypatch):
    monkeypatch.setattr(monthly_average, "update_dollar_rate", lambda _d: 2.0)

    avg = monthly_average.calculate_last_month_average(date(2024, 3, 1))
    assert avg == 2.0


def test_calculate_last_month_average_skips_failed_days(monkeypatch):
    def fake_rate(current):
        if current.day % 2 == 0:
            return 4.0
        raise RuntimeError("no data")

    monkeypatch.setattr(monthly_average, "update_dollar_rate", fake_rate)

    avg = monthly_average.calculate_last_month_average(date(2023, 2, 1))
    assert avg == 4.0


def test_calculate_last_month_average_raises_if_all_days_fail(monkeypatch):
    monkeypatch.setattr(
        monthly_average,
        "update_dollar_rate",
        lambda _d: (_ for _ in ()).throw(RuntimeError("no data")),
    )

    with pytest.raises(RuntimeError, match="No data for last month"):
        monthly_average.calculate_last_month_average(date(2024, 3, 1))
