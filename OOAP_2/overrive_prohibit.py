# Для запрета переопределения метода можем использовать декоратор:
def final_method(method):
    method.__is_final__ = True
    return method

# Родитель
class Plant:
    def __init__(self, name):
        self.name = name
    @final
    def grow(self):
        print("Growing")

# Наследник
class Cactus(Plant):
    def __init__(self, name):
        super().__init__(name)

    def grow(self):
        print("Growing very slow")

plant = Plant('Plant')
cactus = Cactus("Cactus")

plant.grow()
cactus.grow()