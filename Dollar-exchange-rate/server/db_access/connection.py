import os
import sqlite3

from dotenv import load_dotenv


BASE_DIR = os.path.dirname(__file__)
load_dotenv(os.path.join(BASE_DIR, ".env"))
DB_PATH = os.getenv("DB_PATH", "/app/database/exchange_rates.db")


def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)
