class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue = self.queue + [item]

    def dequeue(self):
        if self.size() == 0:
            return None

    def size(self):
        if not self.queue:
            return 0
        cnt = 0
        for _ in self.queue:
            cnt += 1
        return cnt
