import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("SELECT Role FROM jobs LIMIT 50")

rows = cursor.fetchall()

for row in rows:
    print(row[0])

conn.close()