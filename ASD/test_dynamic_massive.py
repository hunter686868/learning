import unittest
from dynamic_massive import DynArray

class TestsLinkedList(unittest.TestCase):

    def setUp(self):
        self.massive = DynArray()
        for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            self.massive.append(i)

    def test_rttt(self):
        self.massive.resize(20)
    def test_insert(self):
        self.assertEqual(self.massive.count, 10)
        self.massive.insert(1, 444)
        self.assertEqual(self.massive[1], 444)
        for j in [1, 2, 3, 4, 5, 6]:
            self.massive.append(j)
        self.assertEqual(self.massive.count, 17)
        self.massive.insert(17, 43)
        self.assertEqual(self.massive.count, 18)
        self.massive.insert(20, 20)

    def test_delete(self):
        self.massive.delete(0)
        self.assertEqual(self.massive.capacity, 16)
        for j in [1, 2, 3, 4, 5, 6, 7, 8]:
            self.massive.append(j)
        self.assertEqual(self.massive.capacity, 32)
        self.massive.delete(0)
        self.massive.delete(0)
        self.assertEqual(self.massive.capacity, 16)
        self.massive.delete(0)
        self.massive.delete(0)
        self.assertEqual(self.massive.capacity, 16)
        self.massive.delete(20)

