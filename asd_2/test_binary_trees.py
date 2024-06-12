from binary_trees import BSTFind, BST, BSTNode
import unittest

class TestBST(unittest.TestCase):
    def setUp(self):
        self.root = BSTNode(10, "Root", None)
        self.tree = BST(self.root)

    def test_initial_count(self):
        self.assertEqual(self.tree.Count(), 1)

    def test_add_key_value(self):
        self.assertTrue(self.tree.AddKeyValue(5, "Left"))
        self.assertTrue(self.tree.AddKeyValue(15, "Right"))
        self.assertEqual(self.tree.Count(), 3)
        self.assertFalse(self.tree.AddKeyValue(5, "Left"))  # Duplicate key

    def test_find_node_by_key(self):
        self.tree.AddKeyValue(5, "Left")
        self.tree.AddKeyValue(15, "Right")
        self.assertTrue(self.tree.FindNodeByKey(10).NodeHasKey)
        self.assertTrue(self.tree.FindNodeByKey(5).NodeHasKey)
        self.assertTrue(self.tree.FindNodeByKey(15).NodeHasKey)
        self.assertFalse(self.tree.FindNodeByKey(20).NodeHasKey)

    def test_find_min_max(self):
        self.tree.AddKeyValue(5, "Left")
        self.tree.AddKeyValue(15, "Right")
        self.assertEqual(self.tree.FinMinMax(self.tree.Root, False).NodeKey, 5)  # Min from root
        self.assertEqual(self.tree.FinMinMax(self.tree.Root, True).NodeKey, 15)  # Max from root
        self.assertEqual(self.tree.FinMinMax(self.tree.Root.LeftChild, False).NodeKey, 5)  # Min from left child
        self.assertEqual(self.tree.FinMinMax(self.tree.Root.LeftChild, True).NodeKey, 5)  # Max from left child
        self.assertEqual(self.tree.FinMinMax(self.tree.Root.RightChild, False).NodeKey, 15)  # Min from right child
        self.assertEqual(self.tree.FinMinMax(self.tree.Root.RightChild, True).NodeKey, 15)  # Max from right child

    def test_delete_node_by_key(self):
        self.tree.AddKeyValue(5, "Left")
        self.tree.AddKeyValue(15, "Right")
        self.assertTrue(self.tree.DeleteNodeByKey(5))
        self.assertFalse(self.tree.FindNodeByKey(5).NodeHasKey)
        self.assertEqual(self.tree.Count(), 2)
        self.assertTrue(self.tree.DeleteNodeByKey(10))
        self.assertFalse(self.tree.FindNodeByKey(10).NodeHasKey)
        self.assertEqual(self.tree.Count(), 1)
        self.assertTrue(self.tree.DeleteNodeByKey(15))
        self.assertFalse(self.tree.FindNodeByKey(15).NodeHasKey)
        self.assertEqual(self.tree.Count(), 0)
        self.assertFalse(self.tree.DeleteNodeByKey(20))  # Non-existent key

if __name__ == "__main__":
    unittest.main()
