# Основная концепция очереди - FIFO
# first-in first-out
# Соответственно реализуем на основе списка, добавим необходимые методы
#

class Queue:
    # Статусы
    NIL = 0  # Функция/запрос не вызывался
    EMP = 1  # Очередь пуста
    OK = 2  # Успех
    ERR = 3  # Ошибка

    def __init__(self):
        # постусловие: создана пустая очередь
        self.array = []
        self._enqueue_status = self.NIL
        self._dequeue_status = self.NIL
        self._peek_status = self.NIL

    # Команды

    def enqueue(self, value):
        # постусловие: элемент добавлен в конец очереди
        self.array.append(value)
        self._enqueue_status = self.OK

    def dequeue(self):
        # предусловие: очередь не пуста
        # постусловие: первый элемент удалён из очереди и возвращён
        if not self.array:
            self._dequeue_status = self.EMP
            return

        value = self.array.pop(0)
        self._dequeue_status = self.OK
        return value

    # Запросы

    def peek_front(self):
        # предусловие: очередь не пуста
        # постусловие: возвращён первый элемент без удаления
        if not self.array:
            self._peek_status = self.EMP
            return

        self._peek_status = self.OK
        return self.array[0]

    def current_size(self):
        return len(self.array)

    def get_enqueue_status(self):
        return self._enqueue_status

    def get_dequeue_status(self):
        return self._dequeue_status

    def get_peek_status(self):
        return self._peek_status



