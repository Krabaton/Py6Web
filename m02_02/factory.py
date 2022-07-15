from abc import ABC, abstractmethod
from enum import Enum
from typing import Tuple, Any


class OperationType(str, Enum):
    SUM = 'sum'
    MUL = 'mul'


class Operation(ABC):
    def __init__(self):
        self.data = None

    @abstractmethod
    def operation(self) -> float:
        pass

    @abstractmethod
    def type_operation(self) -> str:
        pass


class Factory(ABC):
    @abstractmethod
    def create_operation(self):
        pass

    def make_operation(self) -> Operation:
        operation = self.create_operation()
        return operation


class SumFactory(Factory):
    def __init__(self, data: list[float]):
        self.data = data

    def create_operation(self) -> Operation:
        return Adder(self.data)


class MulFactory(Factory):
    def __init__(self, data: list[float]):
        self.data = data

    def create_operation(self) -> Operation:
        return Multiplier(self.data)


class Adder(Operation):
    def __init__(self, data: list[float]):
        super().__init__()
        self.data = data

    def operation(self) -> float | int:
        return sum(self.data)

    def type_operation(self) -> str:
        return OperationType.SUM.name


class Multiplier(Operation):
    def __init__(self, data: list[float]):
        super().__init__()
        self.data = data

    def operation(self) -> float:
        mul = 1
        for el in self.data:
            mul *= el
        return mul

    def type_operation(self) -> str:
        return OperationType.MUL.name


def calculation(factory: Factory) -> tuple[float, str, Any]:
    operator: Operation = factory.make_operation()
    result = operator.operation()
    return result, operator.type_operation(), operator.data


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print(calculation(SumFactory(data)))
    print(calculation(MulFactory(data)))
