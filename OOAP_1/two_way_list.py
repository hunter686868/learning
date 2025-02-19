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
        self._size = 0

        # Статусы
        self._head_status = self.NIL
        self._tail_status = self.NIL
        self._right_status = self.NIL
        self._put_right_status = self.NIL
        self._put_left_status = self.NIL
        self._remove_status = self.NIL
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
        if self.cursor.next is not None:
            self.cursor.next.prev = new_node
        else:
            # Если текущий был последним, обновляем tail
            self.tail = new_node
        self.cursor.next = new_node
        self._size += 1
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
        if self.cursor.prev is not None:
            self.cursor.prev.next = new_node
        else:
            # Если текущий был первым, обновляем head
            self.head = new_node
        self.cursor.prev = new_node
        self._size += 1
        self._put_left_status = self.OK

    def remove(self):
        # Список не пуст
        # Текущий узел удален
        # Курсор смещен вправо или влево (приоритет право -> лево)

        if self.cursor is None:
            self._remove_status = self.EMP
            return
        removed = self.cursor
        # Определяем, куда сдвинуть курсор
        if removed.next is not None:
            new_cursor = removed.next
        elif removed.prev is not None:
            new_cursor = removed.prev
        else:
            new_cursor = None

        # Обновляем связи
        if removed.prev is not None:
            removed.prev.next = removed.next
        else:
            # Если удаляемый был первым узлом
            self.head = removed.next
        if removed.next is not None:
            removed.next.prev = removed.prev
        else:
            # Если удаляемый был последним узлом
            self.tail = removed.prev

        self.cursor = new_cursor
        self._size -= 1
        self._remove_status = self.OK

    def clear(self):
        # Список пустой

        self.head = None
        self.tail = None
        self.cursor = None
        self._size = 0

    def add_tail(self, value):
        # Добавлен узел в конец списка

        new_node = Node(value)
        if self.head is None:
            # Если список пуст, новый узел становится и head, и tail, и курсором
            self.head = new_node
            self.tail = new_node
            self.cursor = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def remove_all(self, value):
        # Все узлы с заданным значением удалены

        node = self.head
        while node is not None:
            next_node = node.next  # сохраняем ссылку на следующий узел
            if node.value == value:
                # Если удаляется текущий узел, обновляем курсор
                if node == self.cursor:
                    if node.next is not None:
                        self.cursor = node.next
                    elif node.prev is not None:
                        self.cursor = node.prev
                    else:
                        self.cursor = None
                # Обновляем связи
                if node.prev is not None:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev
                self._size -= 1
            node = next_node

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
        while node is not None:
            if node.value == value:
                self.cursor = node
                self._find_status = self.OK
                return
            node = node.next
        self._find_status = self.ERR

    # Запросы

    def get(self):
        # Список не пуст

        if self.cursor is None:
            self._get_status = self.EMP
            return None
        self._get_status = self.OK
        return self.cursor.value

    def is_head(self):
        return self.cursor is not None and self.cursor == self.head

    def is_tail(self):
        return self.cursor is not None and self.cursor == self.tail

    def is_value(self):
        return self.cursor is not None

    def size(self):
        return self._size

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
