class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        lst = []
        node = self.head
        while node is not None:
            if node.value == val:
                lst.append(node)
            node = node.next
        return lst

    def delete(self, val, all=False):
        if not self.head:
            return
        i = None
        node = self.head
        while node is not None:
            if node.value == val:
                if i is None:
                    self.head = node.next
                else:
                    i.next = node.next
                if node == self.tail:
                    self.tail = i
                if not all:
                    return
            else:
                i = node
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            if self.head.next is None:
                self.tail = self.head
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
            if newNode.next is None:
                self.tail = newNode

