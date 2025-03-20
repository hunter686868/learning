class NativeDictionary:
    # Статусы
    NIL = 0  # Функция/запрос не вызывался
    OK = 1  # Успех
    ERR = 2  # Ошибка

    def __init__(self, sz):
        self.size = sz
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self._insert_status = self.NIL
        self._remove_status = self.NIL
        self._get_status = self.NIL

    def _hash(self, value):
        return hash(value) % self.size

    def get(self, key):
        # предусловие: нет
        # постусловие: возвращает значение
        index = self._hash(key)
        if self.keys[index] == key:
            self._get_status = self.OK
            return self.values[index]
        self._get_status = self.ERR
        return

    def insert(self, key, value):
        # предусловие: нет
        # постусловие: в словарь добавлена пара ключ-значение,
        # если есть свободное место или обновлено значение
        f_index = self._hash(key)
        index = f_index
        if self.keys[index] is None or self.keys[index] == key:
            self.keys[index] = key
            self.values[index] = value
        else:
            while self.keys[index] is not None:
                index = (index + 1) % self.size
                if self.keys[index] is None or self.keys[index] == key:
                    self.keys[index] = key
                    self.values[index] = value
                    self._insert_status = self.OK
                    return
                if index == f_index:
                    self._insert_status = self.ERR
                    return
        self._insert_status = self.OK

    def remove(self, key):
        # предусловие: ключ есть в словаре
        # постусловие: ключ и его значение удалены
        index = self._hash(key)
        if self.keys[index] == key:
            self.keys[index] = None
            self.values[index] = None
            self._remove_status = self.OK
            return
        self._remove_status = self.ERR

    def get_insert_status(self):
        return self._insert_status

    def get_remove_status(self):
        return self._remove_status

    def get_get_status(self):
        return self._get_status

