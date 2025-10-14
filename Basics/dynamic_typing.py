# This script is showcases the dynamic typing and its examples

"""
No explicit type declaration: Directly can assign values
Variable type can change: A single variable can hold values of different data types throughout 
the program's execution.
Flexibility and rapid development: Dynamic typing contributes to Python's reputation for 
ease of use and rapid prototyping, allows for more flexible variable usage.

WARNING: Potential for runtime errors: While flexible, dynamic typing can sometimes 
lead to runtime errors if type mismatches are not carefully managed,
as these errors are caught during execution rather than during a compile-time check.

"""

def get_engine_status(signal_code):
    """get_engine_status returns the status of the engine based upon the signal code

    Args:
        signal_code (_type_): 

    Raises:
        SystemExit: when exceeding value
    """
    return "ON"


threshold_value = "twenty"

threshold_value = 20 # in newton per meter

signal_sensor = 1 # 1 represents its functioning as expected

received_value = 30 # from real device
DEVICE_ACTION = "Steering Rotation Left"

if received_value > threshold_value:
    raise SystemExit(" Exceeded the threshold Value ")

expected_value = signal_sensor + DEVICE_ACTION # TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(expected_value)