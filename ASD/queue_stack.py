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
            value = self.stack2.pop()
            return value
        else:
            return None

    def size(self):
        return self.stack1.size() + self.stack2.size(

