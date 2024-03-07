class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item): # O(1)
        self.queue = self.queue + [item]

    def dequeue(self): # O(n)
        if self.size() == 0:
            return None
        value = self.queue[0]
        new_queue = []
        for i in range(1, self.size()):
            new_queue.append(self.queue[i])
        self.queue = new_queue
        return value

    def size(self):
        if not self.queue:
            return 0
        cnt = 0
        for _ in self.queue:
            cnt += 1
        return cnt

    def rotation(self, n):
        if self.size() == 0:
            raise IndexError('Nothing to rotate')
        for _ in range(n):
            val = self.dequeue()
            self.enqueue(val)

from stack import Stack

class Queue_stack:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.push(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            return None

    def size(self):
        return self.stack1.size() + self.stack2.size()

