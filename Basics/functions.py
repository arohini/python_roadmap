"""
Functions : Functions are fundamental to organizing and structuring Python programs, promoting code 
reusability and modularity. 

"""

def maintenance_reminder(current_mileage, last_service_mileage, interval=5000):
    """_summary_

    Args:
        current_mileage (int): vehicle mileage at the current state
        last_service_mileage (int): vehicle's last service noted mileage value
        interval (int, optional): Miles to be passed between services.  Defaults to 5000.
        Its a keyword argument

    Returns:
        str: Time for next service
    """
    next_service = last_service_mileage + interval
    if current_mileage >= next_service:
        return "Service due now!"
    return f"Next service due in {next_service - current_mileage} miles."

# Example
print(maintenance_reminder(12000, 8000))

"""
*args handles a variable number of positional arguments as a tuple.
**kwargs handles a variable number of keyword arguments as a dictionary. 
They provide flexibility in function design when the number of arguments is not fixed.
You can use both *args and **kwargs in the same function definition. 
The order is crucial: *args must come before **kwargs
"""
def send_signals(system_name, *signals, **signal_values):
    print(f"Sending signals to HIL system: {system_name}")
    
    for signal in signals:
        print(f"- Preparing signal: {signal}")
    
    for name, value in signal_values.items():
        print(f"- Setting {name} to {value}")


# Example usage
send_signals(
    "EngineControlUnit",
    "RPM", "Throttle",  # *args
    RPM=3000, Throttle=0.75  # **kwargs
)

# Annotations
def steering_threshold_check(action_score: int, turn_side: str = 'steady') -> str:
    # print("Annotations:", steering_threshold_check.__annotations__)
    # print("Arguments:", action_score, turn_side)
    if action_score > 100:
        return f"Steering {turn_side} turn is out of control and the score received is {action_score} "
    else:
        return f"Steering {turn_side} turn is in control"

print(steering_threshold_check('50', 'left'))
