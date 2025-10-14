"""
| Method             | Description                                             | Time Complexity                       | Space Complexity |
| ------------------ | ------------------------------------------------------- | ------------------------------------- | ---------------- |
| `append(x)`        | Adds item `x` to the end of the list                    | **O(1)** (amortized)                  | O(1)             |
| `extend(iterable)` | Adds all items from another iterable                    | O(k), where *k* = len(iterable)       | O(k)             |
| `insert(i, x)`     | Inserts item `x` at index `i`                           | O(n)                                  | O(1)             |
| `remove(x)`        | Removes the **first occurrence** of `x`                 | O(n)                                  | O(1)             |
| `pop([i])`         | Removes and returns item at index `i` (default is last) | O(1) for last, O(n) for arbitrary `i` | O(1)             |
| `clear()`          | Removes all items from the list                         | O(n)                                  | O(1)             |
| `index(x)`         | Returns index of first occurrence of `x`                | O(n)                                  | O(1)             |
| `count(x)`         | Counts how many times `x` appears                       | O(n)                                  | O(1)             |
| `sort()`           | Sorts the list in-place (ascending by default)          | O(n log n) (Timsort)                  | O(n)             |
| `reverse()`        | Reverses the list in-place                              | O(n)                                  | O(1)             |
| `copy()`           | Returns a shallow copy of the list                      | O(n)                                  | O(n)             |

"""

# Creating a list of car models
car_models = ["Toyota", "Honda", "Ford"]

# Add an item
car_models.append("Tesla")       # ["Toyota", "Honda", "Ford", "Tesla"]

# Add multiple items
car_models.extend(["BMW", "Audi"])  # ["Toyota", "Honda", "Ford", "Tesla", "BMW", "Audi"]

# Insert at position 2
car_models.insert(2, "Kia")      # ["Toyota", "Honda", "Kia", "Ford", "Tesla", "BMW", "Audi"]

# Remove "Ford"
car_models.remove("Ford")        # ["Toyota", "Honda", "Kia", "Tesla", "BMW", "Audi"]

# Pop the last item
last_car = car_models.pop()      # Audi removed

# Index of "Tesla"
idx = car_models.index("Tesla")  # 3

# Count occurrences of "Honda"
honda_count = car_models.count("Honda")  # 1

# Sort the list
car_models.sort()                # ["BMW", "Honda", "Kia", "Tesla", "Toyota"]

# Reverse the list
car_models.reverse()             # ["Toyota", "Tesla", "Kia", "Honda", "BMW"]

# Copy the list
backup = car_models.copy()

# Clear the list
car_models.clear()

# List Comprehension

