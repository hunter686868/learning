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
        self.massive.insert(1, 444)
        self.assertEqual(self.massive[1], 444)
        for j in [1, 2, 3, 4, 5, 6]:
            self.massive.append(j)
            print(f'{self.massive.count} шаг{j}')
        print(self.massive.capacity)
        self.massive.insert(1, 43)
        print(self.massive.capacity)

    def test_delete(self):
        self.massive.delete(0)
        print(self.massive.capacity)
        self.massive.delete(1)
        self.massive.delete(1)
        #self.massive.delete(-1)
        print(self.massive.capacity)
