import sqlite3
import pandas as pd

conn = sqlite3.connect("jobs.db")

df = pd.read_csv("jobs.csv")

df.to_sql(
    "jobs",
    conn,
    if_exists="replace",
    index=False
)

print("Jobs stored successfully!")

conn.close()