class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        if self.size() == 0:
            self.deque.append(item)
        self.deque = [item] + self.deque

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.size() == 0:
            return None
        elif self.size() == 1:
            self.deque = []
        else:
            new_queue = []
            for i in range(1, self.size()):
                new_queue.append(self.deque[i])
            self.deque = new_queue

    def removeTail(self):
        if self.size() == 0:
            return None
        self.deque.pop()

    def size(self):
        if not self.deque:
            return 0
        count = 0
        for _ in self.deque:
            count += 1
        return count

