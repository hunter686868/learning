from ASD.linked_list import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def head(self):
        if self.head is None:
            return None
        else:
            return self.head

    def tail(self):
        if self.head is None:
            return None
        else:
            return self.head
    def right(self):
        if self.head is None:
            return None
        else:
            return self.head.right

    def get(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def put_right(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = None
            return
        else:
            self.head.next = Node(data)
            self.head = self.head.next
            return

    def put_left(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = None
            return
        else:
            self.head.next = Node(data)
            self.head = self.head.next
            return

    def remove(self):
        if self.head is None:
            return None
        else:
            self.head = self.head.next
            return

    def clear(self):
        if self.head is None:
            return None
        else:
            self.head = None
            return

    def size(self):
        if self.head is None:
            return 0
        else:
            return self.head.size()

    def add_to_empty(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            self.head.next = Node(data)
            return

    def add_tail(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            self.head.next = Node(data)
            return

    def replace(self, data):
        if self.head is None:
            return None
        else:
            self.head = self.head.next
            return

    def find(self, data):
        if self.head is None:
            return None
        else:
            return self.head.data

    def remove_all(self, data):
        if self.head is None:
            return None
        else:
            self.head = self.head.next
            return

    def is_head(self):
        if self.head is None:
            return False
        else:
            return True

    def is_tail(self):
        if self.head is None:
            return False
        else:
            return True

    def is_value(self):
        if self.head is None:
            return False
        else:
            return True

