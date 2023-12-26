from random import randint
for i in range(1, 11):
    with open(f'{i}.txt', 'wt') as file:
        file.write(f'{randint(1, 999)}\n')
        file.write(f'{randint(1, 999)}\n')
        file.write(f'{randint(1, 999)}\n')


def func(a, b, path):
    try:
        s = 0
        for j in [a, b]:
            f_path = f'{path}{j}.txt'
            with open(f_path, 'rt') as file:
                for i in file:
                    s+= int(i.rstrip())
        return [s, 0]
        #print(f'Сумма шести чисел: {s}')

    except:
        return [0, 1]
        #print('Ошибка')
    finally:
        file.close()


print(func(2,10,'/Users/Sergei/Documents/GitHub/learning/files/'))

# Возьмем класс Unit из предыдущего задания
class Unit:

    def __init__(self, name, cost, damage, health, armor):
        self.name = name # название юнита
        self.cost = cost # цена обучения юнита
        self.damage = damage # урон юнита
        self.health = health # здоровье юнита
        self.armor = armor # броня юнита


def read_file(path):

    units = []
    try:
        with (open(path, 'rt') as file):
            count = 0
            for i in file:
                dt = i.rstrip().split(' ')
                if len(dt) == 5:
                    name, cost, damage, health, armor = dt
                    cost = int(cost)
                    damage = int(damage)
                    health = float(health)
                    armor = float(armor)
                    unit = Unit(name, cost, damage, health, armor)
                    units.append(unit)
                    count += 1
                else:
                    return False
                    #('Ошибка в строке')
        return [units, 0]
        #print(f'Добавлено юнитов: {count}')
    except:
        return [0, 1]
        #print('Ошибка, проблема с файлом')
    finally:
        file.close()


#units = read_file('test.txt')