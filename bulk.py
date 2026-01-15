#Downloaded flag images avialable in that website in flag folder using this python program.
import os
import requests

BASE = "https://flagcdn.com/w320"
os.makedirs("flags", exist_ok=True)

with open("countries.csv", encoding="utf-8-sig") as f:
    lines = f.read().splitlines()

for line in lines:
    if "," not in line:
        continue

    parts = line.split(",")
    if len(parts) < 2:
        continue

    name = parts[0].strip().lower().replace(" ", "-")
    code = parts[1].strip().lower()

    if name == "country":   # skip header if present
        continue

    url = f"{BASE}/{code}.png"
    path = f"flags/{name}.png"

    r = requests.get(url)
    with open(path, "wb") as img:
        img.write(r.content)

    print("Downloaded:", name)

