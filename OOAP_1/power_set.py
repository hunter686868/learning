class HashTable:
    # Статусы
    NIL = 0  # Функция/запрос не вызывался
    OK = 1  # Успех
    ERR = 2  # Ошибка

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
            self._insert_status = self.ERR
            return

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

    def get_insert_status(self):
        return self._insert_status

    def get_remove_status(self):
        return self._remove_status

    def get_contains_status(self):
        return self._contains_status

class PowerSet(HashTable):
    def __init__(self, max_size=16):
        super().__init__(max_size)
        self._intersection_status = self.NIL
        self._union_status = self.NIL
        self._difference_status = self.NIL
        self._issubset_status = self.NIL
        self._equals_status = self.NIL

    def intersection(self, other_set):
        # предусловие: other_set должно быть экземпляром PowerSet
        # постусловие: возвращает множество,
        # содержащее пересечение текущего и переданного множеств
        result = PowerSet(self.max_size)
        for item in self.table:
            if item is not None and other_set.contains(item):
                result.insert(item)
        self._intersection_status = self.OK
        return result

    def union(self, other_set):
        # предусловие: other_set должно быть экземпляром PowerSet
        # постусловие: возвращает объединение текущего и переданного множеств
        result = PowerSet(self.max_size + other_set.max_size)
        for item in self.table:
            if item is not None:
                result.insert(item)
        for item in other_set.table:
            if item is not None:
                result.insert(item)
        self._union_status = self.OK
        return result

    def difference(self, other_set):
        # предусловие: other_set должно быть экземпляром PowerSet
        # постусловие: возвращает множество, содержащее элементы
        # текущего множества, отсутствующие в other_set
        result = PowerSet(self.max_size)
        for item in self.table:
            if item is not None and not other_set.contains(item):
                result.insert(item)
        self._difference_status = self.OK
        return result

    def issubset(self, other_set):
        # предусловие: other_set должно быть экземпляром PowerSet
        # постусловие: возвращает True, если other_set
        # является подмножеством текущего множества
        for item in other_set.table:
            if item is not None and not self.contains(item):
                self._issubset_status = self.ERR
                return False
        self._issubset_status = self.OK
        return True

    def equals(self, other_set):
        # предусловие: other_set должно быть экземпляром PowerSet
        # постусловие: возвращает True, если множества равны
        if self.issubset(other_set) and other_set.issubset(self):
            self._equals_status = self.OK
            return True
        self._equals_status = self.ERR
        return False

    def get_intersection_status(self):
        return self._intersection_status

    def get_union_status(self):
        return self._union_status

    def get_difference_status(self):
        return self._difference_status

    def get_issubset_status(self):
        return self._issubset_status

    def get_equals_status(self):
        return self._equals_status
