class BoundedStack:
    POP_NIL = 0
    POP_OK = 1
    POP_ERR = 2
    PEEK_NIL = 0
    PEEK_OK = 1
    PEEK_ERR = 2
    PUSH_NIL = 0
    PUSH_OK = 1
    PUSH_ERR = 2
    def __init__(self, max_capacity: int = 32) -> None:
        if max_capacity <= 0:
            raise ValueError("max_capacity must be more than 0")
        self._capacity = max_capacity
        self.clear()
    # Постусловие - создан пусто стек
    def clear(self) -> None:
        self._stack = []
        self._pop_status = self.POP_NIL
        self._peek_status = self.PEEK_NIL
        self._push_status = self.PUSH_NIL

    # Предусловие - в стеке есть свободное место
    # Постусловие - добавлен новый элемент
    def push(self, value) -> None:
        if self.size() < self._capacity:
            self._stack.append(value)
            self._push_status = self.PUSH_OK
        else:
            self._push_status = self.PUSH_ERR

    # Предусловие - стек не пустой
    # Постусловие - удален элемент
    def pop(self):
        if self.size() > 0:
            self._stack.pop()
            self._pop_status = self.POP_OK
        else:
            self._pop_status = self.POP_ERR

    # Предусловие - стек не пустой
    def peek(self):
        if self.size() > 0:
            result = self._stack[-1]
            self._peek_status = self.PEEK_OK
        else:
            result = None
            self._peek_status = self.PEEK_ERR
        return result

    def size(self) -> int:
        return len(self._stack)

    def get_pop_status(self) -> int:
        return self._pop_status

    def get_peek_status(self) -> int:
        return self._peek_status

    def get_push_status(self) -> int:
        return self._push_status

