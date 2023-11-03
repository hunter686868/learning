# 5.1 Разделим видимость полей.
# Сделаем приватными поля в наших трех классах
# После этого добавим небоходимые методы для получения и записи полей

# Юнит
class Unit:

    def __init__(self, name, cost, damage, health, armor):
        self.__name = name # название юнита
        self.__cost = cost # цена обучения юнита
        self.__damage = damage # урон юнита
        self.__health = health # здоровье юнита
        self.__armor = armor # броня юнита

    def get_name(self):
        return self.__name

    def get_cost(self):
        return self.__cost

    def get_damage(self):
        return self.__damage

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health += health

    def get_armor(self):
        return self.__armor

    def attack(self, target):
        print(f'{self.__name} атакует {target.get_name()}')
        target.take_damage(self.__damage)

    def take_damage(self, damage):
        self.__health -= damage * (1 - self.__armor)
        print(f'У {self.__name} осталось {self.__health} здоровья')

    def heal(self, heal):
        self.__health += heal
        print(f'{self.__name} восстанавливает {heal} здоровья')


# Здание:
class Building:

    def __init__(self, name, health, cost, production_rate=0, training_rate=0):
        self.__name = name # название здания
        self.__health = health # здоровье здания
        self.__cost = cost # стоимость здания
        self.__production_rate = production_rate # сколько ресурсов производит здание
        self.__training_rate = training_rate # как быстро здание производит юниты

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health += health

    def get_production_rate(self):
        return self.__production_rate

    def get_training_rate(self, rate):
        self.__training_rate += rate

    def product(self, player):
        player.set_gold(self.__production_rate)
        print(f'{player.get_name()} получает {self.__production_rate} золота от {self.__name}')

    def upgrade(self, player):
        cost = 1000
        if player.get_gold() >= cost:
            player.set_gold(-cost)
            self.__production_rate *= 2
            self.__training_rate *= 2
            print(f'{player.get_name()} улучшает {self.__name}, производство ресурсов удвоено')
        else:
            print(f'Нужно больше золота')

    def train(self, player, unit):
        if player.get_gold() >= unit.get_cost():
            player.set_gold(- unit.get_cost())
            player.add_unit(unit)
            days = unit.get_cost() / self.__training_rate
            print(f'{player.get_name()} обучил {unit.get_name()} за {days} дней')
        else:
            print(f'Нужно больше золота')


# Отряд
class Squad:

    def __init__(self, player, name, gold):
        self.__player = player # чей отряд
        self.__name = name # название отряда
        self.__gold = gold # количество золота на старте
        self.__units = []

    def get_player(self):
        return self.__player

    def get_name(self):
        return self.__name

    def get_gold(self):
        return self.__gold

    def set_gold(self, gold):
        self.__gold += gold

    def add_unit(self, unit):
        self.__units.append(unit.get_name())
        print(f'{unit.get_name()} добавляется к отряду {self.__name}')

    def delete_unit(self, unit):
        self.__units.remove(unit)


# Тестируем

soldier1 = Unit('Soldier', 100, 10, 100, 0.2)
soldier2 = Unit('Soldier1', 100, 10, 100, 0.2)

mine = Building('Mine', 500, 1000, 10)
barracks = Building('Barracks', 1000, 1500, 0, 10)
squad = Squad('player1', 'hunter686', 1500)

squad.add_unit(soldier1)
barracks.train(squad, soldier1)
soldier1.attack(soldier2)
soldier2.heal(5)
mine.product(squad)
mine.upgrade(squad)
mine.product(squad)
mine.upgrade(squad)

# 5.2
# Построим иерархию - Юнит1 - Самолет/Корабль


class Unit1:

    def __init__(self, cost, damage, health, armor):
        self.cost = cost # цена обучения юнита
        self.damage = damage # урон юнита
        self.health = health # здоровье юнита
        self.armor = armor # броня юнита

    def attack(self, target):
        target.take_damage(self.damage)

    def take_damage(self, damage):
        self.health -= damage * (1 - self.armor)

    def heal(self, heal):
        self.health += heal


# Самолет
class Airplane(Unit1):

    def __init__(self, name, cost, damage, health, armor):
        super().__init__(cost, damage, health, armor)
        self.name = name
        self.height = 0

    def takeoff(self):
        self.height = 1000

    def landing(self):
        self.height = 0

    def height_change(self, height):
        self.height += height


# Корабль
class Ship(Unit1):

    def __init__(self, name, cost, damage, health, armor, capacity):
        super().__init__(cost, damage, health, armor)
        self.name = name
        self.capacity = capacity # Вместительность для перевозки отряда
        self.units = 0
        self.aboard = []

    def load(self, unit):
        self.units += 1
        self.aboard.append(unit.name)
        print(f'{unit.name} погружен на борт {self.name}')

    def unload(self, unit):
        self.load -= 1
        self.aboard.remove(unit.get_name())


airplane = Airplane('Самолет', 1000, 50, 100, 0.1)
airplane.takeoff()

ship = Ship('Корабль', 750, 0, 1000, 0.5, 10)

airplane.attack(ship)
print(ship.health)
airplane.landing()

ship.load(airplane)


