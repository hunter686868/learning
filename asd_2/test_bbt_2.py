import unittest
from balanced_binary_trees_2 import BalancedBST, BSTNode
class TestBalancedBST(unittest.TestCase):

    def setUp(self):
        self.bst = BalancedBST()

    def test_generate_tree_empty(self):
        self.bst.GenerateTree([])
        self.assertIsNone(self.bst.Root)

    def test_generate_tree_single_element(self):
        self.bst.GenerateTree([10])
        self.assertIsNotNone(self.bst.Root)
        self.assertEqual(self.bst.Root.NodeKey, 10)
        self.assertIsNone(self.bst.Root.LeftChild)
        self.assertIsNone(self.bst.Root.RightChild)

    def test_generate_tree_multiple_elements(self):
        self.bst.GenerateTree([3, 1, 4, 2])
        self.assertIsNotNone(self.bst.Root)
        self.assertEqual(self.bst.Root.NodeKey, 2)
        self.assertEqual(self.bst.Root.LeftChild.NodeKey, 1)
        self.assertEqual(self.bst.Root.RightChild.NodeKey, 3)
        self.assertEqual(self.bst.Root.RightChild.RightChild.NodeKey, 4)

    def test_is_balanced_empty(self):
        self.assertTrue(self.bst.IsBalanced(None))

    def test_is_balanced_single_element(self):
        self.bst.GenerateTree([10])
        self.assertTrue(self.bst.IsBalanced(self.bst.Root))

    def test_is_balanced_balanced_tree(self):
        self.bst.GenerateTree([1, 2, 3, 4, 5, 6, 7])
        self.assertTrue(self.bst.IsBalanced(self.bst.Root))

    def test_is_balanced_unbalanced_tree(self):
        # Создание искусственно несбалансированного дерева
        root = BSTNode(1, None)
        left_child = BSTNode(2, root)
        root.LeftChild = left_child
        left_left_child = BSTNode(3, left_child)
        left_child.LeftChild = left_left_child
        self.assertFalse(self.bst.IsBalanced(root))