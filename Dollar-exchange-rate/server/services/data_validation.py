from datetime import date
from fastapi import HTTPException

MIN_YEAR = 2023  
def validate_date(year: int, month: int):
    if month < 1 or month > 12:
        raise HTTPException(status_code=400, detail="Invalid month")

    if year < MIN_YEAR:
        raise HTTPException(status_code=400, detail="There is no information for dates befor 2023")
    today = date.today()
    if (year, month) > (today.year, today.month):
        raise HTTPException(status_code=400, detail="Future date not allowed")
