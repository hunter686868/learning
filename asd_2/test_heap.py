import unittest
from heap import Heap  # предполагаем, что класс Heap находится в файле heap.py


class TestHeap(unittest.TestCase):

    def setUp(self):
        self.heap = Heap()

    def test_make_heap(self):
        self.heap.MakeHeap([4, 7, 6, 2, 5, 9, 3], 2)
        self.assertEqual(self.heap.HeapArray, [9, 7, 6, 2, 5, 4, 3])

    def test_get_max(self):
        self.heap.MakeHeap([4, 7, 6, 2, 5, 9, 3], 2)
        max_value = self.heap.GetMax()
        self.assertEqual(max_value, 9)
        self.assertEqual(self.heap.HeapArray, [7, 5, 6, 2, 3, 4, None])

    def test_get_max_empty_heap(self):
        max_value = self.heap.GetMax()
        self.assertEqual(max_value, -1)

    def test_add(self):
        self.heap.MakeHeap([4, 7, 6, 2, 5], 2)
        added = self.heap.Add(9)
        self.assertTrue(added)
        self.assertEqual(self.heap.HeapArray, [9, 7, 6, 2, 5, 4, None])

    def test_add_full_heap(self):
        self.heap.MakeHeap([4, 7, 6, 2, 5, 9, 3], 2)
        added = self.heap.Add(10)
        self.assertFalse(added)
        self.assertEqual(self.heap.HeapArray, [9, 7, 6, 2, 5, 4, 3])

    def test_heap_property_after_multiple_additions(self):
        self.heap.MakeHeap([], 2)
        self.heap.Add(4)
        self.heap.Add(7)
        self.heap.Add(6)
        self.heap.Add(2)
        self.heap.Add(5)
        self.assertEqual(self.heap.HeapArray, [7, 5, 6, 2, 4, None, None])

    def test_heap_property_after_multiple_get_max(self):
        self.heap.MakeHeap([4, 7, 6, 2, 5, 9, 3], 2)
        self.assertEqual(self.heap.GetMax(), 9)
        self.assertEqual(self.heap.GetMax(), 7)
        self.assertEqual(self.heap.GetMax(), 6)
        self.assertEqual(self.heap.GetMax(), 5)
        self.assertEqual(self.heap.GetMax(), 4)
        self.assertEqual(self.heap.GetMax(), 3)
        self.assertEqual(self.heap.GetMax(), 2)
        self.assertEqual(self.heap.GetMax(), -1)

