# Сделаем пример с растениями
class Plant:
    # Базовый класс растения
    def __init__(self, name):
        self.name = name  # Название растения

    def grow(self):
        # Растение растет
        pass

# Запас воды - композиция
class WaterStorage:
    def __init__(self, capacity):
        self.capacity = capacity

    def store_water(self, amount):
        pass

# Класс Succulent - вид растений - наследование
class Succulent(Plant):
    def __init__(self, name, water_capacity):
        super().__init__(name)
        self.water_storage = WaterStorage(water_capacity)  # Объект WaterStorage - композиция

    def grow(self):
        # Суккуленты потребляют меньше воды
        self.water_storage.store_water(0.5)

# Класс Cactus, наследование
class Cactus(Succulent):
    def __init__(self, name, water_capacity, has_spines=True):
        super().__init__(name, water_capacity)
        self.has_spines = has_spines  # Колючки

    def grow(self):
        # Кактусу нужно еще меньше воды
        self.water_storage.store_water(0.2)

# Выращивание разных растений - полиморфизм
def cultivate(plant):
    # Мы можем выращивать разные растения и метод grow будет работать по ра
    plant.grow()



