import unittest
from stack import Stack

class TestsLinkedList(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_push(self):
        self.stack.push(2)
        self.stack.push(2)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 3)
    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)
