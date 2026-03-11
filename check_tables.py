import sqlite3

conn = sqlite3.connect("users.db")
rows = conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table';"
).fetchall()

for row in rows:
    print(row)

conn.close()