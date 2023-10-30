# 1.1
# А) Steam: Класс - игра. Структура: название, цена, отзывы, жанр, дата выхода...
# Б) Word: Класс - документ. Структура: название, расширение, количество символов, шрифт...
# В) Outlook: Класс - письмо. Структура: тема, вложения, дата, от кого, категория...
#
# 1.2
# Возьмем игру - стратегию. 3 класса - Юнит, Здание, Отряд игрока
#
# Юнит:
class Unit:
    name = '' # название юнита
    cost = 0 # цена обучения юнита
    damage = 0 # урон юнита
    health = 0 # здоровье юнита
    armor = 0 # броня юнита
# Здание:
class Building:
    name = 'mine' # название здания
    health = 0 # здоровье здания
    cost = 0 # стоимость здания
    production_rate = 0 # сколько ресурсов производит здание
    training_rate = 0 # как быстро здание производит юниты
#
# Отряд игрока:
class Squad:
    player = "Player1" # чей отряд
    name = 'Winner' # название отряда
    gold = 0 # количество золота на старте


# Создадим несколько объектов
squad1 = Squad()
squad1.player = 'Player1'
squad1.name = 'hunter686'
squad1.gold = 10000

soldier = Unit()
soldier.cost = 100
soldier.health = 150
soldier.damage = 10
soldier.armor = 3

soldier1 = soldier

mine = Building()
mine.health = 1000
mine.cost = 1000
mine.production_rate = 10

print(soldier, "\n", soldier1, "\n", mine, "\n", squad1)
#
#1.3
# Ранее мы записали в переменную soldier объект Unit().
# Потом мы присвоили переменной soldier1 значения soldier.
# В связи с этим, если мы изменим параметр у soldier, этот же параметр
# изменится и у soldier1:
soldier.cost = 1000

print(soldier, '\n', soldier1)