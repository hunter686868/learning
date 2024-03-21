class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        summ = 0
        for i in key.encode():
            summ += i
        return summ % self.size

    def is_key(self, key):
        if self.size == 0:
            return False
        for slot in self.slots:
            if slot == key:
                return True
        return False

    def put(self, key, value):
        index = self.hash_fun(key)

         # гарантированно записываем
         # значение value по ключу key

    def get(self, key):
         # возвращает value для key,
         # или None если ключ не найден
        return None