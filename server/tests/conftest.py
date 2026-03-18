import sys
from pathlib import Path


SERVER_DIR = Path(__file__).resolve().parents[1]
PROJECT_ROOT = SERVER_DIR.parent
DB_ACCESS_DIR = SERVER_DIR / "db_access"

for path in (PROJECT_ROOT, SERVER_DIR, DB_ACCESS_DIR):
    path_str = str(path)
    if path_str in sys.path:
        sys.path.remove(path_str)
    sys.path.append(path_str)
