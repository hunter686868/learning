import unittest
from dynamic_massive import DynArray

class TestsLinkedList(unittest.TestCase):

    def setUp(self):
        self.massive = DynArray()
        for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            self.massive.append(i)

    def test_insert(self):
        self.massive.insert(1, 43)
        self.assertEqual(self.massive[1], 43)
        print(self.massive.capacity)
        #for i in [1, 2, 3, 4, 5, 6]:
        #    self.massive.append(i)
        self.massive.resize(20)
        print(self.massive.capacity)
        self.massive.insert(1, 43)
        print(self.massive.capacity)

    def test_delete(self):
        self.massive.delete(1)
        print(self.massive.capacity)
        self.massive.delete(1)
        self.massive.delete(1)
        self.massive.delete(1)
        self.massive.delete(1)
        self.massive.delete(1)
        self.massive.delete(1)
        print(self.massive.capacity)
