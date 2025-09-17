# ===============================
# DICTIONARIES IN PYTHON - NOTES 
# ===============================

student = {
    "name": "Ali",
    "age": 21,
    "grade": "A"
}

# 2. Accessing Values
print(student["name"])         # Ali
print(student.get("age"))      # 21
print(student.get("school", "Not Found"))  # Default if key missing

# 3. Changing Values
student["age"] = 22
print(student)

# 4. Adding Key-Value Pairs
student["city"] = "Hyderabad"
print(student)

# 5. Removing Items
student.pop("grade")      # remove by key
print(student)

last_item = student.popitem()   # removes last key-value pair
print("Removed:", last_item)

del student["city"]       # delete specific key
print(student)

student.clear()           # remove all items
print(student)

# 6. Useful Methods
student = {"name": "Ali", "age": 21, "grade": "A"}

print(student.keys())     # dict_keys(['name','age','grade'])
print(student.values())   # dict_values(['Ali',21,'A'])
print(student.items())    # dict_items([('name','Ali'),('age',21),('grade','A')])

print(len(student))       # 3 (total key-value pairs)
