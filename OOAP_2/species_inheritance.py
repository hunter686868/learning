from abc import ABC, abstractmethod

# Иерархия - Среда обитания
class Habitat(ABC):
    @abstractmethod
    def description(self) -> str:
        pass

class Succulent(Habitat):
    def description(self) -> str:
        return "растение, приспособленное к засушливым условиям"

class AquaticPlant(Habitat):
    def description(self) -> str:
        return "растение, обитающее в воде"

class ForestPlant(Habitat):
    def description(self) -> str:
        return "растение, обитающее в лесу"


# Иерархия - Способ размножения
class Reproduction(ABC):
    @abstractmethod
    def method(self) -> str:
        pass

class BySeeds(Reproduction):
    def method(self) -> str:
        return "размножается семенами"

class BySpores(Reproduction):
    def method(self) -> str:
        return "размножается спорами"

class Vegetative(Reproduction):
    def method(self) -> str:
        return "размножается вегетативно"


# Класс Растение содержит обе характеристики
class Plant:
    def __init__(self, name: str, habitat: Habitat, reproduction: Reproduction):
        self.name = name
        self.habitat = habitat
        self.reproduction = reproduction

