from ASD.linked_list import Node

# 2.3 Операция выдачи всех узлов не нужна, т.к. мы работаем со значениями.
# Если нам нужно перебрать все узлы с заданными значениями - будем
# вызывать метод find(), пока не обойдем весь список.

class LinkedList:
    # Добавим статусы добавления, удаления и курсора
    ADD_NIL = 0
    ADD_OK = 1
    ADD_ERR = 2
    DEL_NIL = 0
    DEL_OK = 1
    DEL_ERR = 2
    CURS_NIL = 0
    CURS_OK = 1
    CURS_ERR = 2

    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor = None
        self._add_status = self.ADD_NIL
        self._del_status = self.DEL_NIL
        self._curs_status = self.CURS_NIL

    # КОМАНДЫ
    # Предусловие - список не пустой
    # Постусловие - курсор на первом узле
    def head(self):
        # установить курсор на первый узел в списке
        if self.head is None:
            self._curs_status = self.CURS_ERR
        self.cursor = self.head
        self._curs_status = self.CURS_OK

    # Предусловие - список не пустой
    # Постусловие - курсор на последнем узле
    def tail(self):
        # установить курсор на последний узел в списке.
        # Делаем операцию автомарной, т.к. если будем идти от head
        # и переключать курсор до конца - получим сложность O(n)
        if self.head is None:
            self._curs_status = self.CURS_ERR
        self.cursor = self.tail
        self._curs_status = self.CURS_OK

    # Предусловие - список не пустой, курсор не на последнем узле
    # Постусловие - курсор смещен направо
    def right(self):
        # сдвинуть курсор на один узел вправо
        if self.head is None or self.cursor.next is None:
            self._curs_status = self.CURS_ERR
        self.cursor = self.cursor.next
        self._curs_status = self.CURS_OK

    # Предусловие - список не пустой и курсор установлен
    def put_right(self, data):
        # вставить следом за текущим узлом
        # новый узел с заданным значением
        if self.cursor is None or self.head is None:
            self._add_status = self.ADD_ERR

        new_node = Node(data)
        new_node.prev = self.cursor
        new_node.next = self.cursor.next

        if self.cursor.next:
            self.cursor.next.prev = new_node
        self.cursor.next = new_node

        if self.cursor == self.tail:
            self.tail = new_node
        self._add_status = self.ADD_OK

    # Предусловие - список не пустой и курсор установлен
    def put_left(self, data):
        # вставить перед текущим узлом
        # новый узел с заданным значением
        if self.head is None or self.cursor is None:
            self._add_status = self.ADD_ERR

        new_node = Node(data)
        new_node.next = self.cursor
        new_node.prev = self.cursor.prev

        if self.cursor.prev:
            self.cursor.prev.next = new_node
        self.cursor.prev = new_node

        if self.cursor == self.head:
            self.head = new_node
        self._add_status = self.ADD_OK

    # Предусловие - список не пустой
    def remove(self):
        # удалить текущий узел
        # (курсор смещается к правому соседу, если он есть,
        # в противном случае курсор смещается к левому соседу,
        # если он есть)
        if self.head is None:
            self._del_status = self.DEL_ERR

        removed = self.cursor

        new_cursor = None
        if removed.next:
            new_cursor = removed.next
        elif removed.prev:
            new_cursor = removed.prev

        if removed.prev:
            removed.prev.next = removed.next
        else:
            self.head = removed.next

        if removed.next:
            removed.next.prev = removed.prev
        else:
            self.tail = removed.prev

        self.cursor = new_cursor
        self._del_status = self.DEL_OK

    # Предусловие - список не пустой
    def clear(self):
        # очистить список
        self.head = None
        self.tail = None
        self.cursor = None
        self._del_status = self.DEL_OK

    # Предусловие - список не пустой
    def add_to_empty(self, data):
        # добавить новый узел в пустой список
        if self.head is not None:
            self._add_status = self.ADD_ERR
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        self.cursor = new_node
        self._add_status = self.ADD_OK

    def add_tail(self, data):
        # добавить новый узел в хвост списка
        if self.head is None:
            self.add_to_empty(data)
        else:
            new_node = Node(data)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self._add_status = self.ADD_OK

    # Предусловие - список не пустой
    def replace(self, data):
        # заменить значение текущего узла на заданное
        if self.cursor is None:
            self._add_status = self.ADD_ERR
        else:
            self.cursor.value = data
            self._add_status = self.ADD_OK

    # Предусловие - список не пустой
    def find(self, data):
        # установить курсор на следующий узел
        # с искомым значением (по отношению к текущему узлу);
        if self.head is None:
            self._curs_status = self.CURS_ERR

        node = self.cursor.next
        while node:
            if node.value == data:
                self.cursor = node
                self._curs_status = self.CURS_OK
                return
            node = node.next
        self._curs_status = self.CURS_ERR

    # Предусловие - список не пустой
    def remove_all(self, data):
        # удалить в списке все узлы с заданным значением
        if self.head is None:
            self._del_status = self.DEL_ERR

        self.cursor = self.head
        while self.cursor:
            next_node = self.cursor.next
            if self.cursor.value != data:
                self.cursor = next_node
                continue

            if self.cursor.prev:
                self.cursor.prev.next = self.cursor.next
            else:
                self.head = self.cursor.next

            if self.cursor.next:
                self.cursor.next.prev = self.cursor.prev
            else:
                self.tail = self.cursor.prev

            self.cursor = next_node

        self.cursor = self.head
        self._del_status = self.DEL_OK

    # ЗАПРОСЫ
    # Предусловие - список не пустой
    def get(self):
        # получить значение текущего узла
        if self.head is None:
            return None
        else:
            return self.cursor.value

    def size(self):
        # посчитать количество узлов в списке
        if self.head is None:
            return 0
        else:
            count = 0
            node = self.head
            while node:
                count += 1
                node = node.next
            return count

    def is_head(self):
        # находится ли курсор в начале списка?
        if self.head == self.cursor:
            self._curs_status = self.CURS_OK
        self._curs_status = self.CURS_ERR

    def is_tail(self):
        # находится ли курсор в конце списка?
        if self.tail == self.cursor:
            self._curs_status = self.CURS_OK
        self._curs_status = self.CURS_ERR

    def is_value(self):
        # установлен ли курсор на какой-либо узел в списке
        # (по сути, непустой ли список)
        if self.cursor:
            self._curs_status = self.CURS_OK
        self._curs_status = self.CURS_ERR

