import unittest
from deque import Deque

class TestDequeMethods(unittest.TestCase):

    def test_addFront(self):
        deq = Deque()
        deq.addFront("f1")
        self.assertEqual(deq.size(), 1)
        self.assertEqual(deq.removeFront(), "f1")

    def test_addTail(self):
        deq = Deque()
        deq.addTail("t1")
        self.assertEqual(deq.size(), 1)
        self.assertEqual(deq.removeTail(), "t1")

    def test_removeFront(self):
        deq = Deque()
        deq.addFront("f1")
        deq.addTail("t1")
        self.assertEqual(deq.removeFront(), "f1")
        self.assertEqual(deq.size(), 1)

    def test_removeTail(self):
        deq = Deque()
        deq.addFront("f1")
        deq.addTail("t1")
        self.assertEqual(deq.removeTail(), "t1")
        self.assertEqual(deq.size(), 1)