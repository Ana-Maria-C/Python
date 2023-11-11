import math

from Shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi ** self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f'Circle with radius: {str(self.radius)} has area: {str(self.area())} and perimeter: {str(self.perimeter())}'
