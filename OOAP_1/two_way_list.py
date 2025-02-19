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
        """
        Перемещает курсор на последний узел.
        Предусловие: список не пуст.
        """
        if self.tail is None:
            self._tail_status = self.EMP
        else:
            self.cursor = self.tail
            self._tail_status = self.OK

    def right(self):
        """
        Сдвигает курсор вправо (на следующий узел).
        Предусловие: справа от текущего узла есть элемент.
        """
        if self.cursor is None or self.cursor.next is None:
            self._right_status = ParentList.NO_RIGHT
        else:
            self.cursor = self.cursor.next
            self._right_status = self.OK

    def put_right(self, value):
        """
        Вставляет новый узел со значением value после текущего.
        Предусловие: список не пуст.
        """
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
        """
        Вставляет новый узел со значением value перед текущим.
        Предусловие: список не пуст.
        """
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
        """
        Удаляет текущий узел. Курсор после удаления перемещается:
          – к правому соседу, если он есть;
          – иначе – к левому.
        Предусловие: список не пуст.
        """
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
        """
        Очищает список – удаляет все узлы.
        """
        self.head = None
        self.tail = None
        self.cursor = None
        self._size = 0

    def add_tail(self, value):
        """
        Добавляет новый узел со значением value в конец списка.
        """
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
        """
        Удаляет из списка все узлы, содержащие значение value.
        """
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
        """
        Заменяет значение текущего узла на value.
        Предусловие: список не пуст.
        """
        if self.cursor is None:
            self._replace_status = self.EMP
            return
        self.cursor.value = value
        self._replace_status = self.OK

    def find(self, value):
        """
        Ищет следующий узел, значение которого равно value.
        Если найден, курсор перемещается на этот узел.
        """
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

    # === Запросы (операции, возвращающие данные) ===

    def get(self):
        """
        Возвращает значение текущего узла.
        Предусловие: список не пуст.
        """
        if self.cursor is None:
            self._get_status = self.EMP
            return None
        self._get_status = self.OK
        return self.cursor.value

    def is_head(self):
        """Возвращает True, если текущий узел является первым в списке."""
        return self.cursor is not None and self.cursor == self.head

    def is_tail(self):
        """Возвращает True, если текущий узел является последним в списке."""
        return self.cursor is not None and self.cursor == self.tail

    def is_value(self):
        """Возвращает True, если курсор установлен (то есть список не пуст)."""
        return self.cursor is not None

    def size(self):
        """Возвращает количество узлов в списке."""
        return self._size

    # === Методы для запроса статусов операций ===

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


# ================================================================
# Класс LinkedList – наследник ParentList, но не предоставляет метод left()
# ================================================================

class LinkedList(ParentList):
    def __init__(self):
        super().__init__()
    # Метод left() не доступен пользователю данного класса.


# ================================================================
# Класс TwoWayList – наследник ParentList, добавляет операцию left()
# ================================================================

class TwoWayList(ParentList):
    def __init__(self):
        super().__init__()
        self._left_status = None  # статус для метода left

    def left(self):
        """
        Сдвигает курсор влево (на предыдущий узел).
        Предусловие: список не пуст и существует узел слева.
        """
        if self.cursor is None or self.cursor.prev is None:
            self._left_status = ParentList.NO_LEFT
        else:
            self.cursor = self.cursor.prev
            self._left_status = self.OK

    def get_left_status(self):
        return self._left_status
