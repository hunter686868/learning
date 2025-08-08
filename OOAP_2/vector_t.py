from typing import TypeVar, Generic, List, Optional
from abc import ABC, abstractmethod
from assignment_attempt import General

T = TypeVar("T", bound=General)

class Vector(General, Generic[T]):
    def __init__(self, values: List[T]):
        if not all(isinstance(v, General) for v in values):
            raise TypeError("Все элементы вектора должны наследоваться от General")
        self.values = values

    def __add__(self, other: "Vector[T]") -> Optional["Vector[T]"]:
        if not isinstance(other, Vector):
            return None
        if len(self.values) != len(other.values):
            return None
        try:
            result = [a + b for a, b in zip(self.values, other.values)]
        except TypeError:
            return None
        return Vector(result)

    def __repr__(self):
        return f"Vector({self.values})"


# Пример класса с поддержкой сложения
class MyNumber(General):
    def __init__(self, value: int):
        self.value = value

    def __add__(self, other: "MyNumber") -> "MyNumber":
        if not isinstance(other, MyNumber):
            raise TypeError("Складывать можно только с MyNumber")
        return MyNumber(self.value + other.value)

    def __repr__(self):
        return str(self.value)

# Проверка Vector<Vector<Vector<T>>>
v1 = Vector([MyNumber(1), MyNumber(2)])
v2 = Vector([MyNumber(3), MyNumber(4)])

vv1 = Vector([v1, v2])
vv2 = Vector([v2, v1])

vvv1 = Vector([vv1])
vvv2 = Vector([vv2])
print(vvv1 + vvv2)