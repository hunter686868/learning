class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        summ = 0
        for i in value.encode():
            summ += i
        return summ % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        f_index = index
        while self.slots[index] is not None:
            index = (index + self.step) % self.size
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
            index = (index + self.step) % self.size
            if index == f_index:
                return None
        if self.slots[index] == value:
            return index
        return None

