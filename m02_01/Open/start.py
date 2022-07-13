from math import pi
from typing import List


class Rect:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius: float):
        self.radius = radius


class AreaCalculator:
    def __init__(self, shapes: List[Rect | Circle]):
        self.shapes = shapes

    def total_area(self) -> float:
        sum = 0
        for shape in self.shapes:
            if isinstance(shape, Rect):
                sum += shape.width * shape.height
            if isinstance(shape, Circle):
                sum += shape.radius ** 2 * pi
        return sum


ex = AreaCalculator([Rect(10, 10), Rect(3, 4), Rect(5, 7), Rect(1, 2), Circle(20), Circle(10)])
print(ex.total_area())
