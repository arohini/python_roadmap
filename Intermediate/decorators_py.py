import time
import functools

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

@timer_decorator
def function():
    time.sleep(1)
    print("Inside my_function")
function()



def my_decorator(func):
    # @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before the original function
        result = func(*args, **kwargs)
        # Do something after the original function
        return result
    return wrapper

@my_decorator
def my_function(x, y):
    """This is the docstring for my_function."""
    return x + y

def test_func():
    """
    test func doc test comment
    """
    return "working"
print(test_func.__doc__)

