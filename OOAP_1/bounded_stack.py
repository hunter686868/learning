class BoundedStack:
    def __init__(self):
        self.items = []
        self.top = None
        self.is_empty = True

    def push(self, item):
        self.items.append(item)
        self.is_empty = False
        self.top = item
    def pop(self):
        if self.is_empty:
            raise IndexError("Stack is empty")
        else:
            self.is_empty = False
            self.top = self.items.pop()
            self.is_empty = True
            return self.top
    def peek(self):
        if self.is_empty:
            raise IndexError("Stack is empty")
        else:
            self.is_empty = False
            self.top = self.items[-1]
            self.is_empty = True
            return self.top


