# Dequeue расширяет возможности queue,
# добавляя возможность получения элемента
# из конца очереди и добавления элемента в ее конец.
# Расширим класс, добавив эти два метода.
# Также добавим запросы статусов этих методов.

class Queue:
    # Статусы
    NIL = 0  # Функция/запрос не вызывался
    EMP = 1  # Очередь пуста
    OK = 2  # Успех
    ERR = 3  # Ошибка

    def __init__(self):
        # постусловие: создана пустая очередь
        self.queue = []
        self._enqueue_status = self.NIL
        self._dequeue_status = self.NIL
        self._peek_status = self.NIL

    # Команды

    def enqueue(self, value):
        # постусловие: элемент добавлен в конец очереди
        self.queue.append(value)
        self._enqueue_status = self.OK

    def dequeue(self):
        # предусловие: очередь не пуста
        # постусловие: первый элемент удалён из очереди и возвращён
        if not self.queue:
            self._dequeue_status = self.EMP
            return

        value = self.queue.pop(0)
        self._dequeue_status = self.OK
        return value

    # Запросы

    def peek_front(self):
        # предусловие: очередь не пуста
        # постусловие: возвращён первый элемент без удаления
        if not self.queue:
            self._peek_status = self.EMP
            return

        self._peek_status = self.OK
        return self.queue[0]

    def current_size(self):
        return len(self.queue)

    def get_enqueue_status(self):
        return self._enqueue_status

    def get_dequeue_status(self):
        return self._dequeue_status

    def get_peek_status(self):
        return self._peek_status

class Deque(Queue):
    def __init__(self):
        super().__init__()
        self._enqueue_front_status = self.NIL
        self._dequeue_back_status = self.NIL

    def enqueue_front(self, value):
        # постусловие: элемент добавлен в начало очереди
        self.queue.insert(0, value)
        self._enqueue_status = self.OK

    def dequeue_back(self):
        # предусловие: очередь не пуста
        # постусловие: последний элемент удалён из очереди и возвращён
        if not self.queue:
            self._dequeue_status = self.EMP
            return

        value = self.queue.pop()
        self._dequeue_status = self.OK
        return value

    def get_enqueue_front_status(self):
        return self._enqueue_front_status

    def get_dequeue_back_status(self):
        return self._dequeue_back_status