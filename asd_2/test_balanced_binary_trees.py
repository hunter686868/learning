from balanced_binary_trees import GenerateBBSTArray
import unittest


class TestGenerateBBSTArray(unittest.TestCase):
    def test_sorted_input(self):
        self.assertEqual(GenerateBBSTArray([1, 2, 3, 4, 5]), [3, 1, 2, 4, 5])

    def test_reverse_sorted_input(self):
        self.assertEqual(GenerateBBSTArray([5, 4, 3, 2, 1]), [3, 1, 2, 4, 5])

    def test_unsorted_input(self):
        self.assertEqual(GenerateBBSTArray([3, 1, 2, 5, 4]), [3, 1, 2, 4, 5])

    def test_single_element(self):
        self.assertEqual(GenerateBBSTArray([1]), [1])

    def test_empty_array(self):
        self.assertEqual(GenerateBBSTArray([]), [])

    def test_large_input(self):
        input_array = list(range(1, 16))  # Дерево глубины 3 (15 элементов)
        expected_output = [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]
        self.assertEqual(GenerateBBSTArray(input_array), expected_output)
