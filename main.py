import building.damage.take_damage as damage
import actions.agressive as agr
import actions.economics as economy


class Squad:

    def __init__(self, player, name, gold):
        self.__player = player # чей отряд
        self.__name = name # название отряда
        self.gold = gold # количество золота на старте
        self.__units = []


class Unit:

    def __init__(self, name, cost, damage, health, armor):
        self.name = name
        self.cost = cost # цена обучения юнита
        self.damage = damage # урон юнита
        self.health = health # здоровье юнита
        self.armor = armor # броня юнита


class Building:

    def __init__(self, name, health, cost, player):
        self.name = name # название здания
        self.health = health # здоровье здания
        self.cost = cost # стоимость здания
        self.player = player


squad = Squad('player1', 'hunter', 10000)
unit = Unit('Soldier',100, 10, 150, 0.1)
building = Building('Barracks', 1500, 1000, 'player1')

agr.attack(unit, building)
damage.receive_damage(building, 100)

economy.income(squad,100)
