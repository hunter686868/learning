# За основу взял код из второго задания по ООП.
# Добавим в него логгирование и accert`ы
import logging

# Юнит
class Unit:

    def __init__(self, name, cost, damage, health, armor):
        self.name = name # название юнита
        self.cost = cost # цена обучения юнита
        self.damage = damage # урон юнита
        self.health = health # здоровье юнита
        self.armor = armor # броня юнита
        logging.info(f'Создан юнит: {self.name}')

    def attack(self, target):
        print(f'{self.name} атакует {target.name}')
        target.take_damage(self.damage)

    def take_damage(self, damage):
        assert damage >= 0, "Урон не может быть отрицательным"
        self.health -= damage * (1 - self.armor)
        print(f'У {self.name} осталось {self.health} здоровья')
        logging.info(f'{self.name} полчил урон')

    def heal(self, heal):
        assert heal >= 0, "Восстановление здоровья не может быть отрицательным"
        self.health += heal
        print(f'{self.name} восстанавливает {heal} здоровья')
        logging.info(f'{self.name} лечится')
# Здание:
class Building:

    def __init__(self, name, health, cost, production_rate, training_rate):
        self.name = name # название здания
        self.health = health # здоровье здания
        self.cost = cost # стоимость здания
        self.production_rate = production_rate # сколько ресурсов производит здание
        self.training_rate = training_rate # как быстро здание производит юниты
        logging.info(f'Создано здание: {self.name}')

    def product(self, player):
        player.gold += self.production_rate
        print(f'{player.name} получает {self.production_rate} золота от {self.name}')
        logging.info(f'{self.name} производит золото')

    def upgrade(self, player, cost):
        assert cost >= 0, "Стоимость улучшения не может быть отрицательной"
        if player.gold >= cost:
            player.gold -= cost
            self.production_rate *= 2
            self.training_rate *= 2
            print(f'{player.name} улучшает {self.name}, производство ресурсов удвоено')
            logging.info(f'{self.name} улучшено')
        else:
            print(f'Нужно больше золота')
            logging.info(f'На улучшение {self.name} нет золота')

    def train(self, player, unit):
        if player.gold >= unit.cost:
            player.gold -= unit.cost
            player.units.append(unit.name)
            print(f'{player.name} обучил {unit.name}')
            logging.info(f'{unit.name} обучен')
        else:
            print(f'Нужно больше золота')
            logging.info(f'На обучение {self.name} нет золота')


class Squad:

    def __init__(self, player, name, gold):
        self.player = player # чей отряд
        self.name = name # название отряда
        self.gold = gold # количество золота на старте
        self.units = []
        logging.info(f'Создан отряд: {self.name}')


# Создадим отряд игрока
player1 = Squad("player1", "hunter686", 100)

# Создадим двух юнитов
soldier_1 = Unit("Солдат 1", 100, 10, 100, 0.2)
soldier_2 = Unit("Солдат 2", 150, 15, 150, 0.1)

#Создадим здания
mine = Building('Шахта', 500, 1000, 10, 0)
barracks = Building('Казармы', 1500, 1500, 0, 10)

# Используем методы:

# Юниты
soldier_1.attack(soldier_2)
soldier_2.attack(soldier_1)
soldier_1.heal(10)
soldier_2.attack(soldier_1)

# Здания
mine.product(player1)
barracks.train(player1, soldier_1)
barracks.train(player1, soldier_2)
barracks.upgrade(player1, 1000)