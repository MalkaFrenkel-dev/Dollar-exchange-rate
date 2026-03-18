from datetime import date

from services import forecasts as forecasts_service


def test_prev_month_with_year_wrap():
    assert forecasts_service.prev_month(2023, 1, 1) == (2022, 12)
    assert forecasts_service.prev_month(2023, 1, 3) == (2022, 10)
    assert forecasts_service.prev_month(2024, 5, 2) == (2024, 3)


def test_forecasts_returns_expected_months(monkeypatch):
    monkeypatch.setattr(forecasts_service, "today", date(2023, 5, 1))

    rates = {
        (2023, 1): 3.0,
        (2023, 2): 4.0,
        (2023, 3): 5.0,
        (2023, 4): 6.0,
    }

    def fake_get_rate(year, month):
        return rates.get((year, month))

    monkeypatch.setattr(forecasts_service, "get_rate_by_month", fake_get_rate)

    result = forecasts_service.forecasts()

    assert result == [
        {"year": 2023, "month": 4, "forecast": 4.0},
        {"year": 2023, "month": 5, "forecast": 5.0},
    ]


def test_forecasts_returns_empty_list_on_error(monkeypatch):
    monkeypatch.setattr(forecasts_service, "today", date(2023, 5, 1))

    def broken_get_rate(*_args, **_kwargs):
        raise RuntimeError("boom")

    monkeypatch.setattr(forecasts_service, "get_rate_by_month", broken_get_rate)

    assert forecasts_service.forecasts() == []
