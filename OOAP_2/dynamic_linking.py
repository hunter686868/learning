# Создаем базовый класс растение, от которого будем наследоваться
class Plant:
    def __init__(self, name):
        self.name = name

    def grow(self):
        print("Growing")

# Создаем три разных растения, наследуясь от базового класса
class Cactus(Plant):
    def __init__(self, name):
        super().__init__(name)

    def grow(self):
        print("Growing very slow")

class Succulent(Plant):
    def __init__(self, name):
        super().__init__(name)

    def grow(self):
        print("Growing slow")

class Fern(Plant):
    def __init__(self, name):
        super().__init__(name)

    def grow(self):
        print("Growing very fast")
# Функция будет принимать в качестве аргумента класс Plant,
# при выполнении кода python определит конечный класс и в зависимости
# от типа Plant вызовется соответствующий метод
def water_plant(plant: Plant):
    plant.grow()

# Создаем экземпляры классов
cactus = Cactus("Cactus")
succ = Succulent("Succulent")
fern = Fern("Fern")

water_plant(cactus) # Выводит Growing very slow
water_plant(succ) # Выводит Growing slow
water_plant(fern) # Выводит Growing very fast
