import sqlite3

from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent
PROJECT_ROOT = FILE_PATH.parent
db_path = PROJECT_ROOT / "colmeia.db"

conn = sqlite3.connect(db_path)
