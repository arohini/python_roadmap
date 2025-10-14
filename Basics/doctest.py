# """
# This is the "example" module.

# >>> factorial(5)
# 120
# """

def add(a, b):
    """_summary_

    Args:
        a : variable one
        b : variable to be added with one
    
    >>> add(5, 7)
    12

    >>> add(5, 0.7)
    Traceback (most recent call last):
        ...
    ValueError: input params should be of type integers

    >>> add(5, 0.7)
    5.7
    
    """

    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise ValueError("input params should be of type integers")

if __name__ == "__main__":
    import doctest
    doctest.testmod()