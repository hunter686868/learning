class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        if self.size() == 0:
            self.deque = [item]
        else:
            self.deque = [item] + self.deque

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.size() == 0:
            return None
        else:
            return self.deque.pop(0)

    def removeTail(self):
        if self.size() == 0:
            return None
        return self.deque.pop()

    def size(self):
        if not self.deque:
            return 0
        count = 0
        for _ in self.deque:
            count += 1
        return count



