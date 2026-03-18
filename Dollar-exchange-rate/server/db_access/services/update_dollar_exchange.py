import os

import requests
from dotenv import load_dotenv


load_dotenv()
BASE_URL = os.getenv("BASE_URL")


def update_dollar_rate(date):
    headers = {
        "Authorization": f"Bearer {os.getenv('API_KEY')}",
        "Accept": "application/json",
    }
    response = requests.get(
        verify=False,
        timeout=10,
        url=f"{BASE_URL}/{date.year}/{date.month}/{date.day}",
        headers=headers,
    )
    response.raise_for_status()

    data = response.json()
    rate = float(data["conversion_rates"]["ILS"])
    return rate
