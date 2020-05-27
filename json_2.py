import json

username = input("write your name")

filename = "user.json"
with open(filename, "w", encoding="utf-8") as f:
    json.dump(username,f, ensure_ascii=False)
