# 4.1 Как я понимаю, ранее я применял композицию, когда указывал игрока в параметрах задния.
# Также здания могут производить юнитов для определенных игроков.

# 4.2 Для этого задания выберем иерархию Юнит- Корабль/Самолет.
# Методы внутри будут печатать названия классов


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

    def func(self):
        print('Unit')


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

    def func(self):
        print('Airplane')


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

    def func(self):
        print('Ship')


# Вторая иерархия - Здание - Казармы/шахта

class Building1:

    def __init__(self, name, health, cost, player):
        self.name = name # название здания
        self.health = health # здоровье здания
        self.cost = cost # стоимость здания
        self.player = player

    def take_damage(self, damage):
        self.health -= damage

    def repair(self, amount):
        self.health += amount


# Шахта

class Mine(Building1):
    def __init__(self, name, health, cost, player):
        super().__init__(name, health, cost, player)
        self.pr_rate = 10

    def upgrade(self, amount):
        if self.player.get_gold() >= amount:
            self.player.set_gold(-amount)
            self.pr_rate *= 2
            print(f'{self.player.get_name()} улучшает {self.name}, производство ресурсов удвоено')
        else:
            print(f'Нужно больше золота')

    def product(self):
        self.player.set_gold(self.pr_rate)


class Barracks(Building1):
    def __init__(self, name, health, cost, player):
        super().__init__(name, health, cost, player)
        self.tr_rate = 10

    def upgrade(self, amount):
        if self.player.get_gold() >= amount:
            self.player.set_gold(-amount)
            self.tr_rate *= 2
            print(f'{self.player.get_name()} улучшает {self.name}, производство войск удвоено')
        else:
            print(f'Нужно больше золота')

    def produce(self, unit):
        if self.player.get_gold() >= unit.get_cost():
            self.player.set_gold(- unit.get_cost())
            self.player.add_unit(unit)
            days = unit.get_cost() / self.tr_rate
            print(f'{self.player.get_name()} обучил {unit.get_name()} за {days} дней')
        else:
            print(f'Нужно больше золота')


# Создадим массив объектов
import random as rnd

units = []
for i in range(0,499):
    random_number = rnd.randint(1,2)
    if random_number == 1:
        units.append(Airplane('Airplane', 1000, 100, 100, 0.1))
    elif random_number == 2:
        units.append(Ship('Ship', 1500, 10, 1000, 0.5, 10))

for unit in units:
    unit.func()

# Соответственно для каждого класса вызывается свой метод, так как мы переопределили
# ранее отдельно. Полиморфизм в действии.

# 4.3 При ad hoc полиморфизме методы с одинаковыми названиями  могут применяться
# при помощи разных параметров и выдавать разный результат.
# В теории в качестве примера был метод сложения.

# В качестве наглядного примера я хочу добавить метод speed_up классу поезд
# Если параметр будет не числом, выведем "Введите число"
# Так один и тот же метод сработает по разному при разных параметрах


class Train:

    def __init__(self, name, speed):
        self.weight = 1000
        self.name = name
        self.speed = speed

    def speed_up(self, spd):
        if type(spd) is int:
            self.speed += spd
            print(f'Поезд ускорился и едет {self.speed} километров в час')
        elif type(spd) is str:
            print('Введите число')
        else:
            print('Ошибка')




train = Train('Choo', 100)

train.speed_up(10)
train.speed_up('choo')
train.speed_up(1.2)



