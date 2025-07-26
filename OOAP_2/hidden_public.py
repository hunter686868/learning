# 1. метод публичен в родительском классе А и публичен в его потомке B
class Succulent:
    def water(self):
        print("Поливаем")

class Cactus(Succulent):
    # Наследует water() без изменений.
    pass

# 2. метод публичен в родительском классе А и скрыт в его потомке B
# В python можем скрыть метод только переопределив его

# 3. метод скрыт в родительском классе А и публичен в его потомке B
class Succulent:
    def _absorb_water(self):
        print("Поглощает воду")

class Cactus(Succulent):
    # Делаем публичный метод
    def absorb(self):
        self._absorb_water()

# 4. метод скрыт в родительском классе А и скрыт в его потомке B
class Succulent:
    def _store_water(self):
        print("Хранит воду")

class Cactus(Succulent):
    def _store_water(self):
        print("Эффективно хранит воду")

