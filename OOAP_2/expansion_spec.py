class Vehicle:
    # Базовый класс
    def __init__(self, name):
        self.name = name

    def move(self, speed):
        pass

class Car(Vehicle):
    def __init__(self, name, fuel_capacity):
        super().__init__(name)
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 0

    # Расширим класс-родитель:
    def move(self, speed):
        super().move(speed)
        if self.fuel_level == 0:
            print('No fuel')

class Bicycle(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def move(self, speed):
        # Специализация - переопределяем метод
        print('Водитель крутит педали')

