import unittest
from binary_trees_2 import aBST

class TestaBST(unittest.TestCase):

    def setUp(self):
        self.tree = aBST(3)  # Дерево глубины 3

    def test_find_key_index(self):
        self.assertEqual(self.tree.FindKeyIndex(10), None)