# ===============================
# LISTS IN PYTHON - NOTES & PRACTICE
# ===============================


fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Ali", 25, True, 5.9]

# 2. Indexing & Slicing

print(fruits[0])      # apple (first item, index 0)
print(fruits[-1])     # cherry (last item)
print(fruits[0:2])    # ['apple','banana'] (slice)

# 3. Changing Items

fruits[1] = "mango"
print(fruits)         # ['apple','mango','cherry']

# 4. Adding Items

fruits.append("orange")    # add at end
fruits.insert(1, "grapes") # insert at index
print(fruits)

# 5. Removing Items

fruits.remove("mango")     # remove by value
popped = fruits.pop()      # remove last
print("Removed:", popped)
del fruits[0]              # delete by index

# 🔹 6. Useful Methods
numbers = [10, 20, 30, 40, 50]

print(len(numbers))        # 5 (length)
print(max(numbers))        # 50 (largest)
print(min(numbers))        # 10 (smallest)
print(sum(numbers))        # 150

numbers.reverse()
print(numbers)             # reversed

numbers.sort()
print(numbers)             # sorted ascending

numbers.sort(reverse=True)
print(numbers)             # sorted descending

copy_fruits = fruits.copy()
print(copy_fruits)
