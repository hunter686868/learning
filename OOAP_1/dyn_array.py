import ctypes


class DynArray:
    # Минимальная емкость
    MIN_CAPACITY = 16
    # Статусы
    NIL = 0 # функция/запрос не вызывался
    EMP = 1 # Пусто
    OK = 2 # Успех
    ERR = 3 # Ошибка

    def __init__(self):
        self.capacity = self.MIN_CAPACITY
        self.array = [None] * self.capacity
        self._insert_status = self.NIL
        self._remove_status = self.NIL
        self._get_status = self.NIL

    def insert(self, index, value):
        if index < 0 or index > self.size():
            self._insert_status = self.ERR
            return

        if self.size() >= self.capacity:
            self._resize(self.capacity * 2)

        for i in range(self.size(), index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = value
        self._insert_status = self.OK

    def remove(self, index):
        if index < 0 or index >= self.size():
            self._remove_status = self.ERR
            return

        for i in range(index, self.size() - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size() - 1] = None

        if self.size() < self.capacity // 2 and self.capacity > 16:
            self._resize(max(16, self.capacity // 2))

        self._remove_status = self.OK

    def get_item(self, index):
        if index < 0 or index >= self.size():
            self._get_status = self.ERR
            return

        self._get_status = self.OK
        return self.array[index]

    def size(self):
        count = 0
        for item in self.array:
            if item is not None:
                count += 1
        return count

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size()):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def get_insert_status(self):
        return self._insert_status

    def get_remove_status(self):
        return self._remove_status

    def get_get_status(self):
        return self._get_status



