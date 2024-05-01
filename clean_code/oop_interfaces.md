Создание отряда
```
class SquadFactory:
    @staticmethod
    def create_squad(player, name, gold):
        return Squad(player, name, gold)
```
Создание юнита
```
class UnitFactory:
    @staticmethod
    def create_unit(name, cost, damage, health, armor):
        return Unit(name, cost, damage, health, armor)
```
Создание здания
```
class BuildingFactory:
    @staticmethod
    def create_building(name, health, cost, production_rate=0, training_rate=0):
        return Building(name, health, cost, production_rate, training_rate)
```