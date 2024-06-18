import unittest
from binary_trees_2 import aBST

class TestaBST(unittest.TestCase):
    def setUp(self):
        self.bst = aBST(3)  # Tree with depth 3 (size = 2^(3+1) - 1 = 15)
        self.keys = [10, 5, 15, 3, 7, 13, 17]

    def test_add_key(self):
        # Add keys
        for key in self.keys:
            added_index = self.bst.AddKey(key)
            self.assertGreaterEqual(added_index, 0, f"Failed to add key {key}, returned {added_index}")

        # Test duplicates
        for key in self.keys:
            self.assertEqual(self.bst.AddKey(key), -1)

    def test_find_key_index(self):
        # Add keys
        for key in self.keys:
            self.bst.AddKey(key)

        # Find keys
        for key in self.keys:
            found_index = self.bst.FindKeyIndex(key)
            self.assertIsNotNone(found_index, f"Key {key} not found")
            self.assertEqual(self.bst.Tree[found_index], key)

        # Find non-existent keys
        self.assertIsNone(self.bst.FindKeyIndex(20))
        self.assertIsNone(self.bst.FindKeyIndex(6))

    def test_tree_structure(self):
        # Add keys
        for key in self.keys:
            self.bst.AddKey(key)

        # Check tree structure
        expected_tree = [10, 5, 15, 3, 7, 13, 17] + [None] * (self.bst.tree_size - 7)
        self.assertEqual(self.bst.Tree, expected_tree)