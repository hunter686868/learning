class HashTable:
    def __init__(self, sz, stp):
        self._size = sz
        self.step = stp
        self.slots = [None] * self._size

    def hash_fun(self, value):
        value = str(value)
        summ = 0
        for i in value.encode():
            summ += i
        return summ % self._size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        f_index = index
        while self.slots[index] is not None:
            index = (index + self.step) % self._size
            if index == f_index:
                return None
        return index

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
            return index
        return None

    def find(self, value):
        index = self.hash_fun(value)
        if self.slots[index] == value:
            return index
        f_index = index
        while self.slots[index] and self.slots[index] != value:
            index = (index + self.step) % self._size
            if index == f_index:
                return None
        if self.slots[index] == value:
            return index
        return None


class PowerSet(HashTable):
    def __init__(self, sz=None, stp=None):
        if sz is None:
            sz = 10
        if stp is None:
            stp = 1
        super().__init__(sz, stp)
        self.slots = [None] * sz

    def size(self):
        count = 0
        for i in self.slots:
            if i is not None:
                count += 1
        return count

    def put(self, value):
        if self.find(value) is not None:
            return None
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
            return index
        return None

    def get(self, value):
        for i in range(self._size):
            if self.slots[i] == value:
                return True
        return False

    def remove(self, value):
        index = self.find(value)
        if index is not None:
            self.slots[index] = None
            return True
        return False

    def intersection(self, set2):
        if self.slots is None or set2.slots is None:
            return None
        new_set = PowerSet(self._size, self.step)
        for i in self.slots:
            if i is not None and set2.get(i) is True:
                new_set.put(i)
        return new_set

    def union(self, set2):
        if self.slots is None and set2.slots is None:
            return None
        new_set = PowerSet(self._size, self.step)
        for i in self.slots:
            if i is not None:
                new_set.put(i)
        for i in set2.slots:
            if i is not None:
                new_set.put(i)
        return new_set

    def difference(self, set2):
        if self.slots is None or set2.slots is None:
            return None
        new_set = PowerSet(self._size, self.step)
        for i in self.slots:
            if i is not None and set2.get(i) is False:
                new_set.put(i)
        return new_set

    def issubset(self, set2):
        if set2.slots is None:
            return True
        for i in set2.slots:
            if i is not None and self.get(i) is False:
                return False
        return True

