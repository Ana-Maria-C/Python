import math

from ex1.Shape import Shape


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return f'Triangle with sides: {str(self.side1)}, {str(self.side2)}, {str(self.side3)} has area: {str(self.area())} and perimeter: {str(self.perimeter())}'