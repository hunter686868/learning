import ctypes

class DynArray:

    MIN_CAPACITY = 16

    def __init__(self):
        self.count = 0
        self.capacity = self.MIN_CAPACITY
        self.array = [None] * self.capacity

    def make_array(self):
        self.array = [None] * self.capacity
        self.count = 0
        self.capacity = self.MIN_CAPACITY

    def insert(self, value):
        self.count += 1




