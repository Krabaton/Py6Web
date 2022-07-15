from enum import Enum
from math import pi


class ShapeType(str, Enum):
    CIRCLE = 'circle'
    SQUARE = 'square'
    TRIANGLE = 'triangle'


class Square:
    def __init__(self, side: float):
        self.side = side

    def area_of(self) -> float:
        return self.side ** 2


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area_of(self) -> float:
        return pi * (self.radius ** 2)


class Shape:
    def __init__(self, size: float):
        self.square = Square(size)
        self.circle = Circle(size)

    def area_of(self, type_shape: ShapeType):
        __store = {
            ShapeType.CIRCLE: self.circle.area_of(),
            ShapeType.SQUARE: self.square.area_of()
        }
        return __store.get(type_shape, None)


if __name__ == '__main__':
    shape = Shape(42)
    print(shape.area_of(type_shape=ShapeType.CIRCLE))
    print(shape.area_of(type_shape=ShapeType.SQUARE))
    print(shape.area_of(type_shape=ShapeType.TRIANGLE))
    