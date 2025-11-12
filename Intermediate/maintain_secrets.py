class Circle: #PascalCase GeometryCircle
    def __init__(self, radius):
        self.__radius = radius  # Conventionally, _ indicates a "protected" attribute

    @property
    def radius(self):
        """The radius property."""
        return self._radius # name mangling

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Radius must be a non-negative number.")
        self._radius = value


    @radius.deleter
    def radius(self):
        del self._radius

# Usage
c = Circle(5)
print(c.radius)  # Accesses the getter: 5

c.radius = 10  # Calls the setter
print(c.radius)  # 10


try:
    c.radius = -2  # Raises ValueError
except ValueError as e:
    print(e)

del c.radius  # Calls the deleter
# print(c.radius) # This would now raise an AttributeError
