from datetime import date

import pytest
from fastapi import HTTPException

from services import data_validation


def test_validate_date_accepts_valid_date():
    data_validation.validate_date(2023, 1)


def test_validate_date_rejects_invalid_month():
    with pytest.raises(HTTPException) as exc:
        data_validation.validate_date(2024, 13)
    assert exc.value.status_code == 400
    assert "Invalid month" in exc.value.detail


def test_validate_date_rejects_year_before_2023():
    with pytest.raises(HTTPException) as exc:
        data_validation.validate_date(2022, 12)
    assert exc.value.status_code == 400


def test_validate_date_rejects_future_date(monkeypatch):
    class FakeDate:
        @classmethod
        def today(cls):
            return date(2025, 6, 15)

    monkeypatch.setattr(data_validation, "date", FakeDate)

    with pytest.raises(HTTPException) as exc:
        data_validation.validate_date(2025, 7)
    assert exc.value.status_code == 400
    assert "Future date not allowed" in exc.value.detail
