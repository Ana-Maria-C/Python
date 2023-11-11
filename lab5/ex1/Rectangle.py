from ex1.Shape import Shape


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f'Rectangle with length: {str(self.length)} and width: {str(self.width)} has area: {str(self.area())} and perimeter: {str(self.perimeter())}'