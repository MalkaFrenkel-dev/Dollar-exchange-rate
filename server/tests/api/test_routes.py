from fastapi import HTTPException
from fastapi.testclient import TestClient

import main
from api import routes


def test_all_rates_endpoint(monkeypatch):
    monkeypatch.setattr(routes, "get_all_rates", lambda: [[2023, 1, 3.5]])
    client = TestClient(main.app)

    response = client.get("/all-rates")

    assert response.status_code == 200
    assert response.json() == [[2023, 1, 3.5]]


def test_single_rate_endpoint(monkeypatch):
    monkeypatch.setattr(routes, "validate_date", lambda _y, _m: None)
    monkeypatch.setattr(routes, "get_rate_by_month", lambda _y, _m: 3.7)
    client = TestClient(main.app)

    response = client.get("/2023/4")

    assert response.status_code == 200
    assert response.json() == 3.7


def test_single_rate_endpoint_validation_error(monkeypatch):
    def fail_validation(_y, _m):
        raise HTTPException(status_code=400, detail="Invalid month")

    monkeypatch.setattr(routes, "validate_date", fail_validation)
    client = TestClient(main.app)

    response = client.get("/2023/13")

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid month"


def test_forecasts_endpoint(monkeypatch):
    monkeypatch.setattr(routes, "forecasts", lambda: [{"year": 2023, "month": 4, "forecast": 4.0}])
    client = TestClient(main.app)

    response = client.get("/forecasts")

    assert response.status_code == 200
    assert response.json() == [{"year": 2023, "month": 4, "forecast": 4.0}]
