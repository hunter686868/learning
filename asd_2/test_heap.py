import unittest
from heap import Heap

class TestHeap(unittest.TestCase):

    def test_make_heap(self):
        h = Heap()
        h.MakeHeap([4, 10, 3, 5, 1], 2)
        self.assertEqual(h.HeapArray, [10, 5, 3, 4, 1, None, None])

    def test_get_max(self):
        h = Heap()
        h.MakeHeap([4, 10, 3, 5, 1], 2)
        self.assertEqual(h.GetMax(), 10)
        self.assertEqual(h.HeapArray, [5, 4, 3, 1, None, None, None])

    def test_add(self):
        h = Heap()
        h.MakeHeap([4, 10, 3], 2)
        self.assertTrue(h.Add(5))
        self.assertEqual(h.HeapArray, [10, 5, 3, 4, None, None, None])

        self.assertTrue(h.Add(1))
        self.assertEqual(h.HeapArray, [10, 5, 3, 4, 1, None, None])

        self.assertFalse(h.Add(7))  # куча заполнена, добавление невозможно
        self.assertEqual(h.HeapArray, [10, 5, 3, 4, 1, None, None])

    def test_get_max_empty_heap(self):
        h = Heap()
        self.assertEqual(h.GetMax(), -1)

    def test_add_to_full_heap(self):
        h = Heap()
        h.MakeHeap([4, 10, 3, 5, 1], 2)
        self.assertFalse(h.Add(7))
        self.assertEqual(h.HeapArray, [10, 5, 3, 4, 1, None, None])

