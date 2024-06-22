from balanced_binary_trees import GenerateBBSTArray
import unittest


class TestGenerateBBSTArray(unittest.TestCase):

    def is_bbst(self, arr, idx=0):
        """ Helper function to check if the array represents a BBST. """
        if idx >= len(arr):
            return True

        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2

        if left_idx < len(arr) and arr[left_idx] >= arr[idx]:
            return False
        if right_idx < len(arr) and arr[right_idx] <= arr[idx]:
            return False

        return self.is_bbst(arr, left_idx) and self.is_bbst(arr, right_idx)

    def test_empty_array(self):
        self.assertEqual(GenerateBBSTArray([]), [])

    def test_single_element(self):
        self.assertEqual(GenerateBBSTArray([10]), [10])

    def test_two_elements(self):
        self.assertEqual(GenerateBBSTArray([10, 20]), [10, 20])

    def test_three_elements(self):
        result = GenerateBBSTArray([10, 20, 30])
        self.assertTrue(self.is_bbst(result))

    def test_multiple_elements(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result = GenerateBBSTArray(data)
        self.assertTrue(self.is_bbst(result))

    def test_large_array(self):
        data = list(range(1, 1024))
        result = GenerateBBSTArray(data)
        self.assertTrue(self.is_bbst(result))
