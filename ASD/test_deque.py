import unittest
from deque import Deque


class TestDequeMethods(unittest.TestCase):
    def setUp(self):
        self.deq = Deque()
        self.deq.addFront(1)
        self.deq.addTail(2)

    def test_addFront(self):
        self.assertEqual(self.deq.size(), 2)
        self.assertEqual(self.deq.removeFront(), "f1")

    def test_addTail(self):
        self.deq.addTail("t1")
        self.assertEqual(self.deq.size(), 1)
        self.assertEqual(self.deq.removeTail(), "t1")

    def test_removeFront(self):
        self.assertEqual(self.deq.removeFront(), "f1")
        self.assertEqual(self.deq.size(), 1)

    def test_removeTail(self):
        self.assertEqual(self.deq.removeTail(), "t1")
        self.assertEqual(self.deq.size(), 1)

