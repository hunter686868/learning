# Для запрета переопределения метода можем использовать декоратор, обозначение метода защищенным _method
# но эти приемы не запретят переопределение, это больше пометка для разработчиков:

# Для запрета переопределения необходимо использовать метаклассы
class FinalMethodMeta(type):
    def __new__(cls, name, bases, dct):
        # Собираем все финальные методы из родительских классов
        final_methods = set()
        for base in bases:
            if hasattr(base, '_final_methods'):
                final_methods.update(base._final_methods)
            for attr_name, attr in base.__dict__.items():
                if getattr(attr, '_final', False):
                    final_methods.add(attr_name)

        # Проверяем, не переопределяются ли они
        for method in final_methods:
            if method in dct:
                raise TypeError(f"Метод '{method}' запрещено переопределять в классе '{name}'")

        own_finals = {name for name, val in dct.items() if getattr(val, '_final', False)}
        dct['_final_methods'] = final_methods.union(own_finals)

        return super().__new__(cls, name, bases, dct)

def final_method(func):
    func._final = True
    return func

# Родитель
class Plant(metaclass=FinalMethodMeta):
    def __init__(self, name):
        self.name = name
    @final_method
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