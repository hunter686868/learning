class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        if not self.stack:
            return 0
        count = 0
        for _ in self.stack:
            count += 1
        return count

    def pop(self):
        if self.size() == 0:
            return None
        value = self.stack[0]
        new_stack = []
        for i in range(1, self.size()):
            new_stack.append(self.stack[i])
        self.stack = new_stack
        return value

    def push(self, value):
        self.stack = [value] + self.stack

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[0]

    def brackets(self, string):
        if self.stack:
            raise IndexError('Stack is not empty')
        for i in string:
            if i == '(':
                self.push(i)
            elif i == ')':
                if self.size() == 0 or self.pop() != '(':
                    return False
        return self.size() == 0


