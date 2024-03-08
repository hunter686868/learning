import unittest
from queue import Queue


class TestsLinkedList(unittest.TestCase):
    def setUp(self):
        self.queue1 = Queue()

    def test_enqueue(self):
        self.queue1.enqueue(1)
        self.assertEqual(self.queue1.size(), 1)

    def test_dequeue(self):
        self.queue1.enqueue(1)
        self.queue1.dequeue()
        self.assertEqual(self.queue1.size(), 0)

    def test_size(self):
        self.assertEqual(self.queue1.size(), 0)

    def test_rotate(self):
        self.queue1.enqueue(1)
        self.queue1.enqueue(2)
        self.queue1.enqueue(3)
        self.queue1.rotate(2)
        self.assertEqual(self.queue1.size(), 3)
        self.assertEqual(self.queue1.dequeue(), 3)
        self.assertEqual(self.queue1.dequeue(), 1)
        self.assertEqual(self.queue1.dequeue(), 2)
