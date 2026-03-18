import os
import sys

from fastapi import APIRouter


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../db_access")))

from db_access.queries.get_all_rates import get_all_rates
from db_access.queries.get_rate_by_month import get_rate_by_month
from services.data_validation import validate_date
from services.forecasts import forecasts


router = APIRouter()


@router.get("/all-rates")
def all_rates():
    return get_all_rates()


@router.get("/{year}/{month}")
def one_rate(year: int, month: int):
    validate_date(year, month)
    return get_rate_by_month(year, month)


@router.get("/forecasts")
def all_forecasts():
    return forecasts()
