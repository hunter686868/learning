В данном задании я продолжил тематику предыдущих и создал два пакета:
actions с действиями(аггресивные и влияющие на золото) и building с взаимодействиями со зданиями.

![Снимок экрана 2023-11-17 в 15.30.28.png](https://i.imgur.com/EGam5Gy.png)

### Агрессивные действия:
![Снимок экрана 2023-11-17 в 15.30.43.png](https://i.imgur.com/mUVxEPA.png)
  
### Действия с экономикой
![Снимок экрана 2023-11-17 в 15.30.50.png](https://i.imgur.com/VPrgneh.png)

### Действия со зданиями
![Снимок экрана 2023-11-17 в 15.30.58.png](https://i.imgur.com/3Wj1DY0.png)

### В основном файле задаем классы, создаем объекты
```
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
```
### В итоге выдача:
![Снимок экрана 2023-11-17 в 15.31.22.png](https://i.imgur.com/JUnSqeK.png)