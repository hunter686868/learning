import unittest


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
            afterNode.next = self.head
            self.head = newNode
            if self.tail is None:
                self.tail = newNode
        else:
            newNode.next = afterNode


class TestsLinkedList(unittest.TestCase):

    def initialization(self):
        self.linked_list = LinkedList()
        self.linked_list.add_in_tail(Node(0))
        self.linked_list.add_in_tail(Node(1))
        self.linked_list.add_in_tail(Node(2))
        self.linked_list.add_in_tail(Node(1))

    # test delete (False, True)
    def test_delete(self):
        self.linked_list.delete(1)
        self.assertEqual([0,2,2], self.linked_list)
    # test clean
    def test_clean(self):
    # test find_all
    def test_find_all(self):
    # test len
    def test_len(self):
    # test insert
    def test_insert(self):


