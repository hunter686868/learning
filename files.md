# Работа с файлами

## 3.1 Для записи файлов была написана следующая функция:

```
from random import randint
for i in range(1, 11):
    with open(f'{i}.txt', 'wt') as file:
        file.write(f'{randint(1, 999)}\n')
        file.write(f'{randint(1, 999)}\n')
        file.write(f'{randint(1, 999)}\n')
```
## 3.2 Функция, считающая сумму чисел из двух файлов:

```
def func(a,b, path):
    try:
        s = 0
        for j in [a,b]:
            f_path = f'{path}{j}.txt'
            with open(f_path, 'rt') as file:
                for i in file:
                    s+= int(i.rstrip())
        print(f'Сумма шести чисел: {s}')
    except:
        print('Ошибка')
    finally:
        file.close()
        
func(2,10,'/Users/Sergei/Documents/GitHub/learning/files/')
```
### Вывод функции в консоль представлен ниже:
![скрин](https://i.imgur.com/cp2Xv5N.png)

## 3.3 Функция, которая создает список объектов на основе данных из текстового файла:
```
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
        with open(path, 'rt') as file:
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
                    print('Ошибка в строке')
        print(f'Добавлено юнитов: {count}')
        return units
    except:
        print('Ошибка, проблема с файлом')
    finally:
        file.close()


units = read_file('test.txt')
```
## В качестве информации функция выводит количество добавленных объектов:
![screen](https://i.imgur.com/wbxzZqU.png)
