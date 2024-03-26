class PowerSet():
    def __init__(self):
        self.slots = []

    def size(self):
        return len(self.slots)

    def put(self, value):
        for i in self.slots:
            if i == value:
                return None
        self.slots.append(value)

    def get(self, value):
        for i in self.slots:
            if i == value:
                return True
        return False

    def remove(self, value):
        for i in self.slots:
            if i == value:
                self.slots.remove(value)
                return True
        return False

    def intersection(self, set2):
        if self.slots is None or set2.slots is None:
            return None
        new_set = PowerSet()
        for i in self.slots:
            if set2.get(i) is True:
                new_set.put(i)
        return new_set

    def union(self, set2):
        if self.slots is None and set2.slots is None:
            return None
        new_set = PowerSet()
        for i in self.slots:
            new_set.put(i)
        for i in set2.slots:
            new_set.put(i)
        return new_set

    def difference(self, set2):
        if self.slots is None or set2.slots is None:
            return None
        new_set = PowerSet()
        for i in self.slots:
            if set2.get(i) is False:
                new_set.put(i)
        return new_set

    def issubset(self, set2):
        if set2.slots is None:
            return True
        for i in set2.slots:
            if self.get(i) is False:
                return False
        return True

