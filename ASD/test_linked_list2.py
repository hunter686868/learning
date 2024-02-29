import unittest
from linked_list_dummy import Node, LinkedList2


class TestsLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList2()
        self.node1 = Node(1)
        self.node5 = Node(5)
        self.node10 = Node(10)
        self.linked_list.add_in_tail(Node(0))
        self.linked_list.add_in_tail(Node(1))
        self.linked_list.add_in_tail(Node(2))
        self.linked_list.add_in_tail(Node(1))

    # test add in tail
    def test_add_in_tail(self):
        self.linked_list.add_in_tail(Node(0))
        self.linked_list.add_in_tail(Node(1))
        self.linked_list.add_in_tail(Node(2))
        self.linked_list.add_in_tail(Node(1))
        self.linked_list.add_in_tail(self.node5)
        self.assertEqual(self.linked_list.len(), 9)
        self.assertEqual(self.linked_list.head.next.value, 0)
        self.assertEqual(self.linked_list.tail.prev.value, 5)
        self.linked_list1 = LinkedList2()
        self.linked_list1.add_in_tail(self.node5)
        self.assertEqual(self.linked_list.tail.value, self.node5.next.value)
    # test delete (False, True)
    def test_delete(self):
        self.linked_list.delete(1)
        self.linked_list.add_in_tail(Node(4))
        self.linked_list.add_in_tail(Node(6))
        self.assertEqual(5, self.linked_list.len())
        self.linked_list.add_in_tail(self.node5)
        self.node = self.linked_list.find(0)
        print(self.node.prev)
        print(self.node.next.value)
        print(self.linked_list.head.value)
        self.linked_list.delete(0)
        print(self.linked_list.head.value)
        self.linked_list.delete(self.linked_list.head.next.value)
        self.linked_list.delete(5)
        self.assertEqual(3, self.linked_list.len())
        self.assertEqual(self.linked_list.tail.prev.value, 6)
        self.linked_list1 = LinkedList2()
        self.linked_list1.insert(None, self.node10)
        self.linked_list1.delete(10)
        self.assertEqual(0, self.linked_list1.len())
        self.linked_list1.delete(10)
        self.linked_list1.insert(None, self.node10)
        self.linked_list1.insert(None, Node(3))
        self.linked_list1.delete(10)
        self.linked_list1.delete(3)
        self.assertEqual(0, self.linked_list1.len())

    def test_del_true(self):
        self.linked_list.delete(1, True)
        self.assertEqual(2, self.linked_list.len())
    # test clean
    def test_clean(self):
        self.linked_list.clean()
        self.assertEqual(self.linked_list.len(), 0)
        self.assertEqual(self.linked_list.head.value, None)
        self.assertEqual(self.linked_list.tail.value, None)
    # test find_all
    def test_find_all(self):
        self.assertEqual(len(self.linked_list.find_all(1)), 2)
        self.assertEqual(self.linked_list.find_all(4), [])
    # test len
    def test_len(self):
        self.assertEqual(self.linked_list.len(), 4)
    # Test find
    def test_find(self):
        self.linked_list.insert(None, Node(6))
        self.assertEqual(self.linked_list.find(6).value, 6)
    # test insert
    def test_insert(self):
        self.linked_list.insert(None, Node(6))
        self.assertEqual(self.linked_list.len(), 5)
        self.assertEqual(self.linked_list.tail.prev.value, 6)
        self.node = self.linked_list.find(6)
        self.linked_list.insert(self.linked_list.tail.prev, Node(44))
        self.linked_list.insert(self.node, Node(5))
        self.assertEqual(self.linked_list.len(), 7)
        self.assertEqual(self.linked_list.head.next.value, 0)
        self.assertEqual(self.linked_list.tail.prev.value, 44)
        self.assertEqual(self.linked_list.head.next.value, 0)
        self.assertEqual(self.linked_list.tail.prev.value, 44)
        self.linked_list1 = LinkedList2()
        self.linked_list1.insert(None, self.node10)
        self.assertEqual(self.linked_list1.head.next.value, 10)
        self.assertEqual(self.linked_list1.tail.prev.value, 10)
        self.linked_list1.insert(self.node10, self.node5)
        self.linked_list1.insert(self.node10, Node(5))
        self.assertEqual(self.linked_list1.tail.prev.value, 5)
        self.assertEqual(self.linked_list.len(), 7)
        self.assertEqual(self.linked_list1.len(), 3)
    def test_add_head(self):
        self.linked_list.add_in_head(Node(10))
        self.assertEqual(self.linked_list.head.next.value, 10)
        self.linked_list1 = LinkedList2()
        self.linked_list1.add_in_head(Node(10))
        self.assertEqual(self.linked_list1.head.next.value, 10)

