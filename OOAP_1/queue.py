# Основная концепция очереди - FIFO
# first-in first-out
# Соответственно реализуем на основе списка, добавим необходимые методы

class Queue:
    # Статусы
    NIL = 0 # функция/запрос не вызывался
    EMP = 1 # Пусто
    OK = 2 # Успех
    ERR = 3 # Ошибка

    def __init__(self):
        self.items = []
        self.front = 0
        self.back = 0
        self.size = 0

    def enqueue(self, item):
        self.items.append(item)
        self.size += 1
    def dequeue(self):
        if self.front == self.size:
            self.front = 0
            self.size -= 1
            return self.items.pop(0)
        else:
            self.size -= 1
            return self.items.pop(0)
