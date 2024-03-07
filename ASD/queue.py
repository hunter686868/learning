class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue = self.queue + [item]

    def dequeue(self):
        if self.size() == 0:
            return None
        value = self.queue[0]
        if self.size() > 1:
            new_queue = []
            for i in range(1, self.size()):
                new_queue.append(self.queue[i])
            self.queue = new_queue
        elif self.size() == 1:
            self.queue = []
        return value

    def size(self):
        if not self.queue:
            return 0
        count = 0
        for _ in self.queue:
            count += 1
        return count

    def rotation(self, n):
        if self.size() == 0:
            raise IndexError('Nothing to rotate')
        for _ in range(n):
            val = self.dequeue()
            self.enqueue(val)



