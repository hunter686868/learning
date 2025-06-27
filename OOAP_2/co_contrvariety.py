# Покажем на примере растений
class Plant:
    def describe(self) -> str:
        return "Растение"

class Succulent(Plant):
    def describe(self) -> str:
        return "Суккулент"

class Cactus(Succulent):
    def describe(self) -> str:
        return "Кактус"

# Ковариативность на примере теплицы

class Greenhouse:
    def __init__(self, plants):
        self.plants = plants

    def show_plants(self):
        return [p.describe() for p in self.plants]

# Две теплицы с кактусами и суккулентами
cactus_greenhouse = Greenhouse([Cactus(), Cactus()])
succulent_greenhouse = Greenhouse([Succulent(), Succulent()])

def display_greenhouse(greenhouse):
    for plant in greenhouse.plants:
        print(plant.describe())

# Демонстрируя ковариативонсть данная функция будет работать для теплицы с любыми растениями,
# т.к. все они потомки одного родительского класса и у них есть его методы


# Контрвариативность на примере системы полива
class WateringSystem:
    def __init__(self, water_function):
        self.water_plant = water_function

    def execute(self, plant):
        self.water_plant(plant)


# Функции полива для разных растений
def water_any_plant(plant):
    print(f"Полив: {plant.describe()}")

def water_succulents_only(succulent):
    print(f"Уменьшенный полив: {succulent.describe()}")

# Системы полива
universal_watering = WateringSystem(water_any_plant)
succulent_watering = WateringSystem(water_succulents_only)


# Полив кактусов:
def water_cactus(system, cactus):
    system.execute(cactus)

cactus = Cactus()

# Теперь вызвав water_cactus(universal_watering, cactus) все будет работать,
# но если попробовать вызвать succulent_watering.execute(Plant()) получим ошибку,
# т.к. любое растение не является суккулентом