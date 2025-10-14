import time

# If statements

sensor_value = 1000

# Simulate a threshold test
if sensor_value > 100:
    print("Warning: Sensor value too high!")
elif sensor_value < 10:
    print("Warning: Sensor value too low!")
else:
    print("Sensor value normal.")


# for loop
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

# Keywords for conditional statements : break continue pass
test_inputs = [5, 10, -1, 15]

for input_val in test_inputs:
    if input_val == 0:
        continue # skip invalid input
    if input_val < 0:
        print("Invalid input. Stopping tests.")
        break
    simulate_input(input_val)
    print(f"Tested with input: {input_val}")

setpoints = [100, 200, 300]

for idx, sp in enumerate(setpoints):
    print(f"Test #{idx+1}: Setting motor speed to {sp} RPM")
    set_motor_speed(sp)


# While Loop

timeout = 10  # seconds
elapsed = 0
interval = 1

start_time = time.time()

while not is_device_ready():
    if time.time() - start_time > timeout:
        print("Timeout: Device not ready.")
        break
    print("Waiting for device...")
    time.sleep(1)

if is_motor_running():
    print("Motor started successfully.")
else:
    print("Motor failed to start within timeout.")


if interval:
    pass # TO DO : 