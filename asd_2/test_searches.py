import unittest
from binary_trees import BSTFind, BST, BSTNode

class TestBSTTraversal(unittest.TestCase):
    def setUp(self):
        self.root = BSTNode(10, "Root", None)
        self.tree = BST(self.root)
        self.tree.AddKeyValue(5, "Left")
        self.tree.AddKeyValue(15, "Right")
        self.tree.AddKeyValue(2, "Left.Left")
        self.tree.AddKeyValue(7, "Left.Right")
        self.tree.AddKeyValue(12, "Right.Left")
        self.tree.AddKeyValue(20, "Right.Right")

    def test_wide_all_nodes(self):
        nodes = self.tree.WideAllNodes()
        keys = [node.NodeKey for node in nodes]
        self.assertEqual(keys, [10, 5, 15, 2, 7, 12, 20])

    def test_deep_all_nodes_in_order(self):
        nodes = self.tree.DeepAllNodes(0)
        keys = [node.NodeKey for node in nodes]
        self.assertEqual(keys, [2, 5, 7, 10, 12, 15, 20])

    def test_deep_all_nodes_post_order(self):
        nodes = self.tree.DeepAllNodes(1)
        keys = [node.NodeKey for node in nodes]
        self.assertEqual(keys, [2, 7, 5, 12, 20, 15, 10])

    def test_deep_all_nodes_pre_order(self):
        nodes = self.tree.DeepAllNodes(2)
        keys = [node.NodeKey for node in nodes]
        self.assertEqual(keys, [10, 5, 2, 7, 15, 12, 20])