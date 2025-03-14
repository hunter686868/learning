class HashTable:
    # Статусы
    NIL = 0  # Функция/запрос не вызывался
    OK = 1  # Успех
    ERR = 2  # Ошибка (например, коллизия неразрешима или таблица переполнена)

    def __init__(self, max_size=16):
        # постусловие: создана пустая хэш-таблица заданного размера
        self.max_size = max_size
        self.size = 0
        self.table = [None] * self.max_size
        self._insert_status = self.NIL
        self._remove_status = self.NIL
        self._contains_status = self.NIL

    def _hash(self, value):
        return hash(value) % self.max_size

    def _rehash(self, index):
        return (index + 1) % self.max_size

    def insert(self, value):
        # предусловие: нет
        # постусловие: значение добавлено в таблицу, если есть свободное место
        if self.size >= self.max_size:
            self._resize()

        index = self._hash(value)
        original_index = index

        while self.table[index] is not None:
            if self.table[index] == value:
                self._insert_status = self.OK  # Уже есть в таблице
                return
            index = self._rehash(index)
            if index == original_index:  # Вернулись в исходную позицию
                self._insert_status = self.ERR
                return

        self.table[index] = value
        self.size += 1
        self._insert_status = self.OK

    def remove(self, value):
        # предусловие: значение есть в таблице
        # постусловие: значение удалено из таблицы
        index = self._hash(value)
        original_index = index

        while self.table[index] is not None:
            if self.table[index] == value:
                self.table[index] = None
                self.size -= 1
                self._remove_status = self.OK
                return
            index = self._rehash(index)
            if index == original_index:
                break

        self._remove_status = self.ERR

    def contains(self, value):
        # предусловие: нет
        # постусловие: возвращает True, если значение есть в таблице, иначе False
        index = self._hash(value)
        original_index = index

        while self.table[index] is not None:
            if self.table[index] == value:
                self._contains_status = self.OK
                return True
            index = self._rehash(index)
            if index == original_index:
                break

        self._contains_status = self.ERR
        return False

    def _resize(self):
        # Увеличивает размер хэш-таблицы в 2 раза при необходимости
        old_table = self.table
        self.max_size *= 2
        self.size = 0
        self.table = [None] * self.max_size

        for item in old_table:
            if item is not None:
                self.insert(item)

    def get_insert_status(self):
        return self._insert_status

    def get_remove_status(self):
        return self._remove_status

    def get_contains_status(self):
        return self._contains_status
