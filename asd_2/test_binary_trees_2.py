import unittest
from binary_trees_2 import aBST

class TestArrayBST(unittest.TestCase):
    def setUp(self):
        self.bst = aBST(3)  # Tree with depth 3 (size = 2^(3+1) - 1 = 15)
        self.keys = [10, 5, 15, 3, 7, 13, 17]

    def test_add_key(self):
        # Add keys
        for key in self.keys:
            self.assertTrue(self.bst.AddKey(key))

        # Test duplicates
        for key in self.keys:
            self.assertFalse(self.bst.AddKey(key))

    def test_find_key(self):
        # Add keys
        for key in self.keys:
            self.bst.AddKey(key)

        # Find keys
        for index, key in enumerate(self.keys):
            self.assertEqual(self.bst.FindKeyIndex(key), self.bst.Tree.index(key))

        # Find non-existent keys
        self.assertIsNone(self.bst.FindKeyIndex(20))
        self.assertIsNone(self.bst.FindKeyIndex(6))

    def test_tree_structure(self):
        # Add keys
        for key in self.keys:
            self.bst.AddKey(key)

        # Check tree structure
        expected_tree = [10, 5, 15, 3, 7, 13, 17] + [None] * 8
        self.assertEqual(self.bst.Tree, expected_tree)