import time

"""
| Method                     | Use                                              |
| -------------------------- | ------------------------------------------------ |
| `range(start, stop, step)` | Iterate over a sequence of numbers               |
| `enumerate(iterable)`      | Get index and value at the same time             |
| `zip(list1, list2)`        | Iterate over two lists in parallel               |
| `.items()`                 | Iterate over dictionary key-value pairs          |
| `.split()`                 | Split a string into a list for looping           |
| `.append()`                | Add items to a list during iteration (if needed) |

"""

sensor_value = 1000
break_condition = "On Track"
tyre_air_check = 30

# Simulate a threshold test
# If statements
if sensor_value:
    print("Good to test other fuctionalities")

if sensor_value > 100:
    print("Warning: Sensor value too high!")
elif sensor_value < 10:
    print("Warning: Sensor value too low!")
else:
    print("Sensor value normal.")

if break_condition == "On Track":
    print("Break unit is working as expected")
else:
    print("Break unit is out of control, fix it quickly !")

# Simulate a threshold test
if tyre_air_check < 30:
    print("Warning: Less air in tyre! Fill in some air !")

age = 20
status = "Adult" if age >= 18 else "Minor"


# for loop
# Keywords for conditional statements : break continue pass
test_inputs = [5, 0,10, -1, 15]

for input_val in test_inputs:
    if input_val == 0:
        continue # skip invalid input
    if input_val < 0:
        print("Invalid input. Stopping tests.")
        break
    print(f"Tested with input: {input_val}")

# setpoints = [100, 200, 300]

# for idx, sp in enumerate(setpoints):
#     print(f"Test #{idx+1}: Setting motor speed to {sp} RPM")


# While Loop
# timeout = 10  # seconds
# elapsed = 0
# interval = 1

# start_time = time.time()

correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter password: ")
    if user_input == correct_password:
        print("Access granted.")
        break
    else:
        attempts += 1
        print(f"Wrong password. Attempts left: {max_attempts - attempts}")
else:
    print("Too many attempts. Access denied.")



responses = [
    {"status": "success", "data": {"id": 1, "name": "Alice"}},
    {"status": "success", "data": [{"id": 2, "name": "Bob"}, {"id": 3, "name": "Carol"}]},
    {"status": "error", "code": 404, "message": "User not found"},
    {"status": "error", "code": 500, "message": "Internal Server Error"},
    {"status": "redirect", "url": "https://api.example.com/v2/user"},
    {"unexpected": "something odd"}
]


def handle_response(response):
    match response:
        # Single data object
        case {"status": "success", "data": {"id": user_id, "name": name}}:
            print(f"Single user found: {name} (ID={user_id})")
        
        # List of data objects
        case {"status": "success", "data": list(users)}:
            print(f"Multiple users found: {len(users)} total")
        
        # Client-side error
        case {"status": "error", "code": 404, "message": msg}:
            print(f"Not Found: {msg}")
        
        # Server-side error
        case {"status": "error", "code": 500, "message": msg}:
            print(f"Server Error: {msg}")
        
        # Redirect response
        case {"status": "redirect", "url": url}:
            print(f"Redirecting to: {url}")
        
        # Catch-all for weird or unknown data
        case _:
            print("Unknown response format:", response)

for r in responses:
    handle_response(r)

# if interval:
#     pass # TO DO 