from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return pi * (self.radius ** 2)


if __name__ == "__main__":
    shapes = [
        Rectangle(5, 10),
        Circle(7)
    ]

    for shape in shapes:
        print(f"Площадь фигуры ({shape.__class__.__name__}): {shape.area():.2f}")
