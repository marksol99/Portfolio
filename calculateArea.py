
#calculates area of different shapes

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def computeArea(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def computeArea(self):
        areaSqr = self.side * self.side
        return areaSqr


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def computeArea(self):
        areaCircle = 3.14 * self.radius * self.radius
        return areaCircle


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def computeArea(self):
        a = self.a
        b = self.b
        c = self.c
        s = (a + b + c) / 2

        areaTriangle = (s * (s - a) * (s - b) * (s - c)) ** 0.5

        return areaTriangle


mySquare = Square(2)
myCircle = Circle(2)
myTriangle = Triangle(5, 4, 3)
print(f"Area of square: {mySquare.computeArea()}")
print(f"Area of circle: {myCircle.computeArea()}")
print(f"Area of triangle: {myTriangle.computeArea()}")
