# polymorphism_demo.py

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Example usage
if __name__ == "__main__":
    shapes = [
        Rectangle(10, 5),
        Circle(7),
        Rectangle(3.5, 2),
        Circle(1.2)
    ]

    for shape in shapes:
        print(f"{type(shape).__name__} area: {shape.area():.2f}")
