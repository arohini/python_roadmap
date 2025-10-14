import sys

# Errors and Exceptions
# Syntax Errors
def maintenance_reminder(current_mileage, last_service_mileage, interval=5000):
    """
    By passing current_mileage, last_service_mileage, interval values you can get
    the next service due period.

    Args:
        current_mileage (int): vehicle mileage at the current state
        last_service_mileage (int): vehicle's last service noted mileage value
        interval (int, optional): Miles to be passed between services.  Defaults to 5000.

    Returns:
        str: Time for next service
    """
    try:
        next_service = last_service_mileage + interval
        if next_service:
            print(f"next service miles is {next_service}")
    except TypeError as te:
        print(f"Expected integer values to calculate the maintenance reminder {te}")
        
    if current_mileage >= next_service:
        return "Service due now!"
    return f"Next service due in {next_service - current_mileage} miles."

print(maintenance_reminder(12000, 8000))


# # Raising and Handling Multiple Unrelated Exceptions
def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)


# Handling Exceptions and executing with finally
def steering_threshold_check(action_score: int, turn_side: str = 'steady') -> str:
    print("Annotations:", steering_threshold_check.__annotations__)
    print("Arguments:", action_score, turn_side)
    
    try:
        print("before condition check")
        if action_score > 100:
            print("after condition check")
            return f"Steering {turn_side} turn is out of control and \
                the score received is {action_score} "
        else:
            print("after condition check")
            return f"Steering {turn_side} turn is in control"
    except (TypeError, ValueError) as ve:
        print("value expected to be int", ve)
    finally:
        print(100+2)
        print("SEND ME THE RIGHT VALUE !!")

steering_threshold_check('50', 'left')


# Sequential Exceptions
try:
    f = open('Basics/myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError as ve:
    print("Could not convert data to an integer.", ve)
except Exception as err: # Wildcard Exception
    print(f"Unexpected {err=}, {type(err)=}")
    raise


# Chaining Exception
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error") # Raising exceptions

# User-defined Exceptions
class InvalidInputError(Exception):
    def __init__(self, value, message="Invalid input provided"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: '{self.value}' was provided."

def process_data(data):
    if not isinstance(data, int):
        raise InvalidInputError(data, "Expected an integer")
    if data < 0:
        raise InvalidInputError(data, "Input cannot be negative")

try:
    process_data("hello")
except InvalidInputError as e:
    print(e) # This will call the __str__ method of InvalidInputError

try:
    process_data(-5)
except InvalidInputError as e:
    print(str(e)) # Explicitly calling str() also invokes __str__
