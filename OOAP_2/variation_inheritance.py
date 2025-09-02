# Наследование с вариацией типа
class Plant:
    def __init__(self, name: str):
        self.name = name

    def respond_to_drought(self):
        print(f"{self.name}: закрываю устьица и уменьшаю испарение.")

class Cactus(Plant):
    def respond_to_drought(self):
        print(f"{self.name}: накапливаю влагу и замедляю метаболизм.")

class Fern(Plant):
    def respond_to_drought(self):
        print(f"{self.name}: сбрасываю часть листьев.")

# Наследование с конкретизацией
from abc import ABC, abstractmethod

class Plant(ABC):
    def __init__(self, name: str):
        self.name = name

    def photosynthesize(self):
        print(f"{self.name}: выполняю фотосинтез.")

    @abstractmethod
    def reproduce(self):
        pass


class Cactus(Plant):
    def reproduce(self):
        print(f"{self.name}: размножаюсь семенами.")


class Moss(Plant):
    def reproduce(self):
        print(f"{self.name}: размножаюсь спорами.")

# Структурное наследование
from typing import Protocol, List

class Bloomable(Protocol):
    def bloom(self) -> str: ...


class Rose:
    def __init__(self, name: str):
        self.name = name

    def bloom(self) -> str:
        return f"{self.name}: распускается бутон."


class Cactus:
    def __init__(self, name: str):
        self.name = name

    def bloom(self) -> str:
        return f"{self.name}: редкое, но очень яркое цветение."

def show_bloomers(plants: List[Bloomable]):
    for p in plants:
        print(p.bloom())