users = [{"name": "Alice", "age": 22},
         {"name": "Bob", "age": 17},
         {"name": "Charlie", "age": 30},
         {"name": "Dave", "age": 19},
         ]

adults = []

for user in users:
    if user["age"] >= 21:
        adults.append(user)

print(adults)
