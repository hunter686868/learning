class NativeCache:
    def __init__(self, sz):
        self.size: int = sz
        self.slots: list = [None] * self.size
        self.values: list = [None] * self.size
        self.hits: list = [0] * self.size

    def hash_fun(self, value):
        summ = 0
        for i in value.encode():
            summ += i
        return summ % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        f_index = index
        while self.slots[index] is not None:
            index = (index + 1) % self.size
            if index == f_index:
                return None
        f_index = -1
        return index

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
            self.values[index] = value
            self.hits[index] = 0
            return index
        else:
            min_hits_index = self.hits.index(min(self.hits))
            self.slots[min_hits_index] = value
            self.values[min_hits_index] = value
            self.hits[min_hits_index] = 0
            return min_hits_index

    def find(self, value):
        index = self.hash_fun(value)
        if self.slots[index] == value:
            self.hits[index] += 1
            return index
        f_index = index
        while self.slots[index] and self.slots[index] != value:
            index = (index + 1) % self.size
            if index == f_index:
                return None
        if self.slots[index] == value:
            self.hits[index] += 1
            return index
        return None

