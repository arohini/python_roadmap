from functools import reduce

"""
List Comprehension :
List comprehensions in Python offer a concise and efficient way to create new lists based on 
existing iterables. They provide a more readable and often faster alternative to traditional 
for loops and append operations when constructing lists.
"""

numbers = [1, 2, 3, 4, 5]
squared_numbers = [num * num for num in numbers]

# Adding Conditional Logic
"""
Condition: An optional boolean expression that filters which item values are included 
in the new list. 
Only items for which the condition evaluates to True are processed by the expression.
"""

# even_numbers 
numbers = range(1, 11)
even_numbers = [num for num in numbers if num % 2 == 0]

# If Else Condition
numbers = [1, 2, 3, 4, 5]
transformed_numbers = [num * num if num % 2 == 0 else num for num in numbers]


# Anonymous (lambda) and map functions

sensor_readings = [21.4, 22.0, 21.9, 22.3]
addon_sensor_readings = list(map(lambda reading : reading + 1, sensor_readings))
undercontrol_sensor_readings = list(filter(lambda reading : reading < 22, sensor_readings))
total_sensor_readings = reduce(lambda reading_1, reading_2 : reading_1 + reading_2, sensor_readings)


print(addon_sensor_readings)
print(undercontrol_sensor_readings)
print(total_sensor_readings)




