import unittest
from linked_list_dummy import LinkedList2, Node, Dummy

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList2()
        self.node1 = Node(1)
        self.node2 = Node(2)
        self.node3 = Node(3)
        self.node4 = Node(4)

    def test_add_in_tail(self):
        self.list.add_in_tail(self.node1)
        self.assertEqual(self.list.head.next, self.node1)
        self.assertEqual(self.list.tail.prev, self.node1)

        self.list.add_in_tail(self.node2)
        self.assertEqual(self.list.head.next, self.node1)
        self.assertEqual(self.node1.next, self.node2)
        self.assertEqual(self.node2.prev, self.node1)
        self.assertEqual(self.list.tail.prev, self.node2)

    def test_find(self):
        self.list.add_in_tail(self.node1)
        self.list.add_in_tail(self.node2)
        self.list.add_in_tail(self.node3)

        self.assertEqual(self.list.find(2), self.node2)
        self.assertIsNone(self.list.find(4))  # Нет элемента со значением 4 в списке

    def test_find_all(self):
        self.list.add_in_tail(self.node1)
        self.list.add_in_tail(self.node2)
        self.list.add_in_tail(self.node3)
        self.list.add_in_tail(self.node2)

        nodes = self.list.find_all(2)
        self.assertEqual(len(nodes), 2)
        self.assertIn(self.node2, nodes)
        self.assertIn(self.node2, nodes)

    def test_delete(self):
        self.list.add_in_tail(self.node1)
        self.list.add_in_tail(self.node2)
        self.list.add_in_tail(self.node3)
        self.list.add_in_tail(self.node2)
        self.list.add_in_tail(self.node2)
        self.list.add_in_tail(self.node2)

        self.list.delete(2)
        self.assertEqual(self.list.len(), 3)  # Удален один элемент со значением 2

        self.list.delete(2, all=True)
        print(self.list.find_all(2))
        self.assertEqual(self.list.len(), 2)  # Удалены все элементы со значением 2

    def test_clean(self):
        self.list.add_in_tail(self.node1)
        self.list.add_in_tail(self.node2)
        self.list.add_in_tail(self.node3)

        self.list.clean()

    def test_len(self):
        self.assertEqual(self.list.len(), 0)
        self.list.add_in_tail(self.node1)
        self.list.add_in_tail(self.node2)
        self.list.add_in_tail(self.node3)
        self.assertEqual(self.list.len(), 3)

    def test_insert(self):
        self.list.add_in_tail(self.node1)
        self.list.add_in_tail(self.node3)

        self.list.insert(self.node1, self.node2)
        self.assertEqual(self.node1.next, self.node2)
        self.assertEqual(self.node2.prev, self.node1)
        self.assertEqual(self.node2.next, self.node3)
        self.assertEqual(self.node3.prev, self.node2)

    def test_add_in_head(self):
        self.list.add_in_tail(self.node1)
        self.list.add_in_tail(self.node3)

        self.list.add_in_head(self.node2)
        self.assertEqual(self.list.head.next, self.node2)
        self.assertEqual(self.node2.next, self.node1)
        self.assertEqual(self.node1.prev, self.node2)
