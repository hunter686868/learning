import unittest
from linked_list import Node, LinkedList


class TestsLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()
        self.linked_list.add_in_tail(Node(0))
        self.linked_list.add_in_tail(Node(1))
        self.linked_list.add_in_tail(Node(2))
        self.linked_list.add_in_tail(Node(1))

    # test delete (False, True)
    def test_delete(self):
        self.linked_list.delete(1)
        self.assertEqual(3, self.linked_list.len())

    def test_del_true(self):
        self.linked_list.delete(1, True)
        self.assertEqual(2, self.linked_list.len())
    # test clean
    def test_clean(self):
        self.linked_list.clean()
        self.assertEqual(self.linked_list.len(), 0)
        self.assertEqual(self.linked_list.head, None)
        self.assertEqual(self.linked_list.tail, None)
    # test find_all
    def test_find_all(self):
        self.assertEqual(len(self.linked_list.find_all(1)), 2)
        self.assertEqual(self.linked_list.find_all(4), [])
    # test len
    def test_len(self):
        self.assertEqual(self.linked_list.len(), 4)
    # test insert
    def test_insert(self):
        self.linked_list.insert(None, Node(6))
        self.assertEqual(self.linked_list.len(), 5)
        self.assertEqual(self.linked_list.head.value, 6)
        self.assertEqual(self.linked_list.head.next.value, 0)
        self.assertEqual(self.linked_list.tail.value, 1)
        self.node = self.linked_list.find(0)
        self.linked_list.insert(self.node, Node(44))
        self.assertEqual(self.linked_list.len(), 6)
        self.assertEqual(self.linked_list.head.value, 6)
        self.assertEqual(self.linked_list.tail.value, 1)

