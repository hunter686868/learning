# Наследование реализации
class Plant:
    def __init__(self, name: str):
        self.name = name

    def photosynthesize(self):
        print(f"{self.name}: поглощаю солнечный свет и выделяю кислород.")

    def absorb_water(self):
        print(f"{self.name}: корни впитывают воду из почвы.")


class Cactus(Plant):
    def store_water(self):
        print(f"{self.name}: накапливаю влагу в стебле.")

class Rose(Plant):
    def bloom(self):
        print(f"{self.name}: раскрываю цветок и источаю аромат.")


# Льготное наследование
from abc import ABC, abstractmethod
class AbstractPlant(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def photosynthesize(self):
        pass

    @abstractmethod
    def absorb_water(self):
        pass


class Moss(AbstractPlant):
    def photosynthesize(self):
        print(f"{self.name}: фотосинтез идёт даже при низкой освещённости.")

    def absorb_water(self):
        print(f"{self.name}: впитываю влагу всей поверхностью тела.")


class Fern(AbstractPlant):
    def photosynthesize(self):
        print(f"{self.name}: фотосинтезирую крупными листьями.")

    def absorb_water(self):
        print(f"{self.name}: впитываю воду корнями.")