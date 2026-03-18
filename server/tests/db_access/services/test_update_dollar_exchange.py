from datetime import date

import pytest
import requests

from db_access.services import update_dollar_exchange


def test_update_dollar_rate_builds_expected_request(monkeypatch):
    called = {}

    class FakeResponse:
        url = "https://example.test/rates/2024/1/2"

        def raise_for_status(self):
            return None

        def json(self):
            return {"conversion_rates": {"ILS": 3.77}}

    def fake_get(**kwargs):
        called.update(kwargs)
        return FakeResponse()

    monkeypatch.setattr(update_dollar_exchange, "BASE_URL", "https://example.test/rates")
    monkeypatch.setattr(update_dollar_exchange.requests, "get", fake_get)
    monkeypatch.setattr(update_dollar_exchange.os, "getenv", lambda key: "token" if key == "API_KEY" else None)

    rate = update_dollar_exchange.update_dollar_rate(date(2024, 1, 2))

    assert rate == 3.77
    assert called["url"] == "https://example.test/rates/2024/1/2"
    assert called["timeout"] == 10
    assert called["verify"] is False
    assert called["headers"]["Authorization"] == "Bearer token"


def test_update_dollar_rate_raises_http_errors(monkeypatch):
    class FakeResponse:
        url = "https://example.test/fail"

        def raise_for_status(self):
            raise requests.HTTPError("bad request")

        def json(self):
            return {}

    monkeypatch.setattr(update_dollar_exchange, "BASE_URL", "https://example.test/rates")
    monkeypatch.setattr(update_dollar_exchange.requests, "get", lambda **_kwargs: FakeResponse())

    with pytest.raises(requests.HTTPError):
        update_dollar_exchange.update_dollar_rate(date(2024, 1, 2))
