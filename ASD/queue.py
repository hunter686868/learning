class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def rotate(self, n):
        if self.size() == 0:
            raise IndexError('Nothing to rotate')
        for i in range(n):
            self.enqueue(self.dequeue())

