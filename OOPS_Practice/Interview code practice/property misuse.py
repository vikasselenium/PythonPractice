class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._area=0

    @property
    def area(self):
        return 3.14 * self._radius ** 2

c = Circle(5)
print(c.area)
