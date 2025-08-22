class Plant:
    def grow(self) -> str:
        return "Растение растёт"


class Tree(Plant):
    def grow(self) -> str:
        return "Дерево растет"


class Flower(Plant):
    def grow(self) -> str:
        return "Цветок растет"


def observe_growth(plant: Plant) -> None:
    # Полиморфный вызов: для разных объектов вызывается своя версия grow()
    print(plant.grow())

# ----------------------

from typing import Generic, TypeVar

T_co = TypeVar("T_co", covariant=True)

class Greenhouse(Generic[T_co]):
    # Теплица с растением
    def __init__(self, plant: T_co):
        self._plant = plant

    def get(self) -> T_co:
        return self._plant


class Plant:
    def __str__(self):
        return "Растение"


class Tree(Plant):
    def __str__(self):
        return "Дерево"


# Функция принимает теплицу с любым растением
def describe_greenhouse(g: Greenhouse[Plant]) -> None:
    print("В теплице растёт:", g.get())
