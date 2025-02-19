from ASD.linked_list import Node

class ParentList:
    # Для упрощения напишем общие константы статусов:
    NIL = 0 # функция/запрос не вызывался
    EMP = 1 # Список пуст
    OK = 2 # Успех
    ERR = 3 # Ошибка

    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor = None

        # Статусы
        self._head_status = self.NIL
        self._tail_status = self.NIL
        self._right_status = self.NIL
        self._put_right_status = self.NIL
        self._put_left_status = self.NIL
        self._remove_status = self.NIL
        self._add_status = self.NIL
        self._replace_status = self.NIL
        self._find_status = self.NIL
        self._get_status = self.NIL

    # Команды

    def head(self):
        # Список не пуст
        # Курсор установлен на первый узел
        if self.head is None:
            self._head_status = self.EMP
        else:
            self.cursor = self.head
            self._head_status = self.OK

    def tail(self):
        # Список не пуст
        # Курсор установлен на последний узел
        if self.tail is None:
            self._tail_status = self.EMP
        else:
            self.cursor = self.tail
            self._tail_status = self.OK

    def right(self):
        # Правее есть элемент
        # Курсор сдвинут на один узел правее
        if self.cursor is None or self.cursor.next is None:
            self._right_status = self.ERR
        else:
            self.cursor = self.cursor.next
            self._right_status = self.OK

    def put_right(self, value):
        # Список не пуст
        # Справа от курсора добавлен новый узел
        if self.cursor is None:
            self._put_right_status = self.EMP
            return
        new_node = Node(value)
        new_node.prev = self.cursor
        new_node.next = self.cursor.next

        if self.cursor.next:
            self.cursor.next.prev = new_node
        else:
            self.tail = new_node
        self.cursor.next = new_node
        self._put_right_status = self.OK

    def put_left(self, value):
        # Список не пуст
        # Слева от курсора добавлен новый узел
        if self.cursor is None:
            self._put_left_status = self.EMP
            return
        new_node = Node(value)
        new_node.next = self.cursor
        new_node.prev = self.cursor.prev

        if self.cursor.prev:
            self.cursor.prev.next = new_node
        else:
            self.head = new_node
        self.cursor.prev = new_node
        self._put_left_status = self.OK

    def remove(self):
        # Список не пуст
        # Текущий узел удален
        # Курсор смещен вправо или влево (приоритет право -> лево)
        if self.cursor is None:
            self._remove_status = self.EMP
            return
        removed = self.cursor

        if removed.next:
            new_cursor = removed.next
        elif removed.prev:
            new_cursor = removed.prev
        else:
            new_cursor = None

        if removed.prev:
            removed.prev.next = removed.next
        else:
            self.head = removed.next
        if removed.next:
            removed.next.prev = removed.prev
        else:
            self.tail = removed.prev

        self.cursor = new_cursor
        self._remove_status = self.OK

    def clear(self):
        # Список пустой
        self.head = None
        self.tail = None
        self.cursor = None

    def add_to_empty(self, data):
        # Список не пустой
        if self.head:
            self._add_status = self.EMP
            return
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        self.cursor = new_node
        self._add_status = self.OK

    def add_tail(self, value):
        # Добавлен узел в конец списка
        if self.head is None:
            self.add_to_empty(value)
        else:
            new_node = Node(value)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self._add_status = self.OK

    def replace(self, value):
        # Список не пуст
        # Значение узла изменено
        if self.cursor is None:
            self._replace_status = self.EMP
            return
        self.cursor.value = value
        self._replace_status = self.OK

    def find(self, value):
        # Курсор установлен на следующий узел
        # с искомым значением (если найден).

        if self.cursor is None:
            self._find_status = self.ERR
            return

        node = self.cursor.next
        while node:
            if node.value == value:
                self.cursor = node
                self._find_status = self.OK
                return
            node = node.next
        self._find_status = self.ERR

    def remove_all(self, value):
        # Все узлы с заданным значением удалены
        if self.cursor is None:
            self._remove_status = self.OK
            return

        self.cursor = self.head
        while self.cursor:
            next_node = self.cursor.next
            if self.cursor.value != value:
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
        self._remove_status = self.OK

    # Запросы

    def get(self):
        # Список не пуст
        if self.cursor is None:
            self._get_status = self.EMP
            return None
        self._get_status = self.OK
        return self.cursor.value

    def size(self):
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
        if self.head == self.cursor:
            self._head_status = self.OK
        self._head_status = self.ERR

    def is_tail(self):
        if self.tail == self.cursor:
            self._tail_status = self.OK
        self._tail_status = self.ERR

    def is_value(self):
        return self.cursor is not None

    # Запросы статусов

    def get_head_status(self):
        return self._head_status

    def get_tail_status(self):
        return self._tail_status

    def get_right_status(self):
        return self._right_status

    def get_put_right_status(self):
        return self._put_right_status

    def get_put_left_status(self):
        return self._put_left_status

    def get_add_status(self):
        return self._add_status

    def get_remove_status(self):
        return self._remove_status

    def get_replace_status(self):
        return self._replace_status

    def get_find_status(self):
        return self._find_status

    def get_get_status(self):
        return self._get_status


# Связный список
class LinkedList(ParentList):
    def __init__(self):
        super().__init__()

# Двунаправленный связный список
class TwoWayList(ParentList):
    def __init__(self):
        super().__init__()
        self._left_status = None

    def left(self):
        # Правее есть элемент
        # Курсор сдвинут на один узел левее

        if self.cursor is None or self.cursor.prev is None:
            self._left_status = self.ERR
        else:
            self.cursor = self.cursor.prev
            self._left_status = self.OK

    def get_left_status(self):
        return self._left_status
