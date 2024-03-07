import unittest
from queue import Queue, Queue_stack

class TestsLinkedList(unittest.TestCase):
    def setUp(self):
        self.queue1 = Queue()
        self.queue2 = Queue_stack()
    def test_enqueue(self):
        self.queue1.enqueue(1)
        self.queue2.enqueue(1)
        self.assertEqual(self.queue2.size(), 1)
        self.assertEqual(self.queue1.size(), 1)
    def test_dequeue(self):
        self.queue1.enqueue(1)
        self.queue2.enqueue(1)
        self.queue1.dequeue()
        self.queue2.dequeue()
        self.queue2.dequeue()
        #self.assertEqual(self.queue2.size(), 0)
        self.assertEqual(self.queue1.size(), 0)
    def test_size(self):
        self.queue2.enqueue(1)
        self.assertEqual(self.queue2.size(), 1)
        self.assertEqual(self.queue1.size(), 0)
