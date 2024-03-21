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
        index = self.hash_fun(key)
        if self.slots[index] == key:
            return True
        return False

    def put(self, key, value):
        f_index = self.hash_fun(key)
        index = f_index
        if self.slots[index] is None or self.slots[index] == key:
            self.slots[index] = key
            self.values[index] = value
        else:
            while self.slots[index] is not None:
                index = (index + 1) % self.size
                if self.slots[index] is None or self.slots[index] == key:
                    self.slots[index] = key
                    self.values[index] = value
                    return

    def get(self, key):
        f_index = self.hash_fun(key)
        if self.slots[f_index] == key:
            return self.values[f_index]
        else:
            index = f_index
            while self.slots[index] is not None:
                index = (index + 1) % self.size
                if self.slots[index] == key:
                    return self.values[index]
        return None

