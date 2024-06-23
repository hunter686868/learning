from balanced_binary_trees import GenerateBBSTArray
import unittest


class TestGenerateBBSTArray(unittest.TestCase):

    def test_balanced_bst(self):
        self.assertEqual(GenerateBBSTArray([3, 1, 2, 5, 4]), [3, 2, 5, 1, None, 4, None])
        self.assertEqual(GenerateBBSTArray([1, 2, 3, 4, 5, 6, 7]), [4, 2, 6, 1, 3, 5, 7])
        self.assertEqual(GenerateBBSTArray([7, 6, 5, 4, 3, 2, 1]), [4, 2, 6, 1, 3, 5, 7])
        self.assertEqual(GenerateBBSTArray([1, 2, 3]), [2, 1, 3])
        self.assertEqual(GenerateBBSTArray([1]), [1])
        self.assertEqual(GenerateBBSTArray([]), [])

    def test_large_balanced_bst(self):
        arr = list(range(1, 16))  # 1 to 15
        expected_result = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        self.assertEqual(GenerateBBSTArray(arr), expected_result)

    def test_unbalanced_input(self):
        self.assertEqual(GenerateBBSTArray([1, 2, 3, 4, 5, 6]), [4, 2, 6, 1, 3, 5])