import unittest
from deque import Deque


class TestDequeMethods(unittest.TestCase):
    def setUp(self):
        self.deq = Deque()
        self.deq.addFront(1)
        self.deq.addTail(2)
        self.deq.addFront(4)
        self.deq.addTail(3)

    def test_addFront(self):
        self.assertEqual(self.deq.size(), 4)
        self.deq.removeFront()
        self.assertEqual(self.deq.removeFront(), 1)
        self.assertEqual(self.deq.size(), 2)
        self.deq.addFront("f1")
        self.deq.addTail("t1")
        self.deq.addFront("f2")
        self.deq.addTail("t2")
        while self.deq.size() > 0:
            print(self.deq.removeFront())
            print(self.deq.removeTail())

    def test_addTail(self):
        self.deq.addTail(6)
        self.assertEqual(self.deq.size(), 5)
        self.assertEqual(self.deq.removeTail(), 6)

    def test_removeFront(self):
        self.deq.removeFront()
        self.assertEqual(self.deq.size(), 3)
        self.assertEqual(self.deq.removeFront(), 1)

    def test_removeTail(self):
        self.deq.removeTail()
        self.assertEqual(self.deq.size(), 3)
        self.assertEqual(self.deq.removeTail(), 2)


