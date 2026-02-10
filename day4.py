import json

with open("data.json", "r") as file:
    users = json.load(file)

for user in users:
    user["age"] = user["age"] + 1
    
with open("output.json", "w") as file:
    json.dump(users, file)

print("Done")