from ex1.Circle import Circle
from ex1.Rectangle import Rectangle
from ex1.Triangle import Triangle


def main():
    circle = Circle(5)
    print(circle)

    rectangle = Rectangle(4, 6)
    print(rectangle)

    triangle = Triangle(3, 4, 5)
    print(triangle)


if __name__ == '__main__':
    main()