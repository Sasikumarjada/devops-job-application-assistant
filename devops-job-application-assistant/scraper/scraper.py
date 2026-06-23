import requests
import pandas as pd

url = "https://remoteok.com/api"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

data = response.json()

jobs = []

for job in data[1:]:
    company = job.get("company")
    position = job.get("position")

    if company and position:
        jobs.append({
            "Company": company,
            "Role": position
        })

df = pd.DataFrame(jobs)

print("=" * 50)
print("### NEW VERSION RUNNING ###")
print("=" * 50)

print(f"Total Jobs Found: {len(df)}")

df.to_csv("jobs.csv", index=False)

print("Saved to jobs.csv")