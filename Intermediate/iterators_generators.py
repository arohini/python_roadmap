"""
Iterators and Generators are used to efficiently handle large
sequential data without using much memory

"""

class CustomRange:
    """
    Custom class to have functional logic enabled in memory efficient way

        Raises:
        StopIteration: Raise exception and stops executing when condition is not satisfied

    """
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += 2
            return num
        raise StopIteration

# Using the custom iterator
for num in CustomRange(1, 4):
    print(num)


def filter_data(data_generator: object) -> object:
    """
    Typically filters the data as per the condition defined

    Args:
        data_generator (object): Sequence of data of any data type belongs to list, tuple, Set

    Returns:
        object: Iteratable object

    Yields:
        Iterator[object]: condition satisfied single object
    """
    for item in data_generator:
        if item > 5:
            yield item


def transform_data(filtered_generator: object) -> object:
    """
    Transforms the data for the provided generator input 

    Args:
        filtered_generator (iter): iterable object

    Yields:
        item: transformational logic is apllied to each data and returned as iterable object
    """
    for item in filtered_generator:
        yield item * 2

# Example usage with a list for simplicity, but imagine a large data source
initial_data = [1, 7, 3, 9, 2, 8]
data_gen = (x for x in initial_data) # A simple generator expression

processed_data = transform_data(filter_data(data_gen))
for result in processed_data:
    print(result)
