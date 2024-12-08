import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

character_data = data["chars"]

character_data.sort(key=lambda x: x["gainTime"], reverse=True)

qwq = 1