# ===============================
# VARIABLES & DATA TYPES - NOTES
# ===============================

# Python has different built-in data types:
# int, float, string, boolean, list, tuple, set, dictionary

# -------------------------------
# 1. NUMBERS (int, float)
# -------------------------------
a = 10        # int
b = 3.5       # float

# Useful operations
print(a + b)   # 13.5
print(a * 2)   # 20
print(a // 3)  # 3 (floor division)
print(a % 3)   # 1 (modulus)
print(a ** 2)  # 100 (power)

# Methods
print(abs(-5))      # 5 (absolute value)
print(round(3.141, 2))  # 3.14 (round off)
print(pow(2, 3))    # 8 (power)

# -------------------------------
# 2. STRINGS (str)
# -------------------------------
name = "Python"

# Useful methods
print(name.lower())     # "python"
print(name.upper())     # "PYTHON"
print(name.title())     # "Python"
print(name.startswith("Py"))   # True
print(name.endswith("on"))     # True
print(name.replace("Py", "My")) # "Mython"
print(name.split("t"))   # ['Py', 'hon']
print(" ".join(["I", "love", "Python"]))  # "I love Python"

# Indexing & Slicing
print(name[0])    # "P"
print(name[-1])   # "n"
print(name[0:4])  # "Pyth"

# -------------------------------
# 3. BOOLEAN (bool)
# -------------------------------
is_active = True
is_logged = False

print(5 > 3)    # True
print(5 == 5)   # True
print(5 != 3)   # True
print(bool("")) # False (empty string is False)

# -------------------------------
# 4. LISTS (ordered, changeable)
# -------------------------------
fruits = ["apple", "banana", "cherry"]

# Useful methods
fruits.append("mango")     # add at end
fruits.insert(1, "orange") # insert at index
fruits.remove("banana")    # remove value
fruits.pop()               # remove last item
print(fruits.index("apple"))   # index of "apple"
print(fruits.count("apple"))   # how many "apple"
fruits.sort()              # sort ascending
fruits.reverse()           # reverse list
print(len(fruits))         # length

# -------------------------------
# 5. TUPLES (ordered, unchangeable)
# -------------------------------
coords = (10, 20, 30)

print(coords[0])   # 10
print(len(coords)) # 3
print(coords.count(20))  # 1
print(coords.index(30))  # 2

# -------------------------------
# 6. SETS (unordered, no duplicates)
# -------------------------------
nums = {1, 2, 3, 3, 4}
print(nums)   # {1,2,3,4}

nums.add(5)        # add element
nums.remove(2)     # remove element
nums.discard(10)   # safely remove if exists
print(nums.union({6,7}))      # combine
print(nums.intersection({3,4,5}))  # common values

# -------------------------------
# 7. DICTIONARIES (key-value pairs)
# -------------------------------
student = {"name": "Ali", "age": 21, "grade": "A"}

print(student["name"])      # Ali
print(student.get("city", "Not Found"))  # default if missing
student["age"] = 22         # update
student["city"] = "Hyd"     # add new
student.pop("grade")        # remove key
print(student.keys())       # dict_keys(['name','age','city'])
print(student.values())     # dict_values([...])
print(student.items())      # dict_items([...])
