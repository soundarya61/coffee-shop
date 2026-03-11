import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "users.db")

conn = sqlite3.connect(DB_PATH)
rows = conn.execute("SELECT * FROM feedback").fetchall()

for row in rows:
    print(row)

conn.close()