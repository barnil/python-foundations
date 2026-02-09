#checks whether a given dictionary has required fields
def is_valid_user(user):
    if "name" not in user:
        return False
    if "age" not in user:
        return False
    if user["age"] <= 0:
        return False
    return True

user1 = {"name" : "Alice", "age" : 22}
user2 = {"name" : "Bob"}
user3 = {"age" : 30}

print(is_valid_user(user1))
print(is_valid_user(user2))
print(is_valid_user(user3))

user4 = {"name" : "Charlie", "age" : 0}
print(is_valid_user(user4))