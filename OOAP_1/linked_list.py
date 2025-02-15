from ASD.linked_list import Node


class LinkedList:
    def __init__(self):
        self.head = None

    # КОМАНДЫ
    # Предусловие - список не пустой
    # Постусловие - курсор на первом узле
    def head(self):
        # установить курсор на первый узел в списке
        if self.head is None:
            return None
        else:
            return self.head

    # Предусловие - список не пустой
    # Постусловие - курсор на последнем узле
    def tail(self):
        # установить курсор на последний узел в списке
        if self.head is None:
            return None
        else:
            return self.head

    # Предусловие - список не пустой, курсор не на последнем узле
    # Постусловие - курсор смещен направо
    def right(self):
        # сдвинуть курсор на один узел вправо
        if self.head is None:
            return None
        else:
            return self.head.right

    # Предусловие - список не пустой
    def put_right(self, data):
        # вставить следом за текущим узлом
        # новый узел с заданным значением
        if self.head is None:
            self.head = Node(data)
            self.head.next = None
            return
        else:
            self.head.next = Node(data)
            self.head = self.head.next
            return

    # Предусловие - список не пустой
    def put_left(self, data):
        # вставить перед текущим узлом
        # новый узел с заданным значением
        if self.head is None:
            self.head = Node(data)
            self.head.next = None
            return
        else:
            self.head.next = Node(data)
            self.head = self.head.next
            return

    # Предусловие - список не пустой
    def remove(self):
        # удалить текущий узел
        # (курсор смещается к правому соседу, если он есть,
        # в противном случае курсор смещается к левому соседу,
        # если он есть)
        if self.head is None:
            return None
        else:
            self.head = self.head.next
            return

    # Предусловие - список не пустой
    def clear(self):
        # очистить список
        if self.head is None:
            return None
        else:
            self.head = None
            return

    # Предусловие - список не пустой
    def add_to_empty(self, data):
        # добавить новый узел в пустой список
        if self.head is None:
            self.head = Node(data)
            return
        else:
            self.head.next = Node(data)
            return

    def add_tail(self, data):
        # добавить новый узел в хвост списка
        if self.head is None:
            self.head = Node(data)
            return
        else:
            self.head.next = Node(data)
            return

    # Предусловие - список не пустой
    def replace(self, data):
        # заменить значение текущего узла на заданное
        if self.head is None:
            return None
        else:
            self.head = self.head.next
            return

    # Предусловие - список не пустой
    def find(self, data):
        # установить курсор на следующий узел
        # с искомым значением (по отношению к текущему узлу);
        if self.head is None:
            return None
        else:
            return self.head.data

    # Предусловие - список не пустой
    def remove_all(self, data):
        # удалить в списке все узлы с заданным значением
        if self.head is None:
            return None
        else:
            self.head = self.head.next
            return

    # ЗАПРОСЫ
    # Предусловие - список не пустой
    def get(self):
        # получить значение текущего узла
        if self.head is None:
            return None
        else:
            return self.head.data

    def size(self):
        # посчитать количество узлов в списке
        if self.head is None:
            return 0
        else:
            return self.head.size()

    def is_head(self):
        # находится ли курсор в начале списка?
        if self.head is None:
            return False
        else:
            return True

    def is_tail(self):
        # находится ли курсор в конце списка?
        if self.head is None:
            return False
        else:
            return True

    def is_value(self):
        # установлен ли курсор на какой-либо узел в списке
        # (по сути, непустой ли список)
        if self.head is None:
            return False
        else:
            return True

