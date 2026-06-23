import sqlite3

devops_keywords = [
    "devops",
    "cloud",
    "aws",
    "azure",
    "gcp",
    "sre",
    "site reliability",
    "kubernetes",
    "docker",
    "platform engineer",
    "linux"
]

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("SELECT Company, Role FROM jobs")

jobs = cursor.fetchall()

print("\n=== DevOps Related Jobs ===\n")

count = 0

for company, role in jobs:

    role_lower = role.lower()

    if any(keyword in role_lower for keyword in devops_keywords):
        count += 1
        print(f"{count}. {company} | {role}")

conn.close()

print(f"\nTotal DevOps Jobs Found: {count}")