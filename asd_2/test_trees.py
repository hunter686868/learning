import unittest
from trees import SimpleTreeNode, SimpleTree  # импортируем классы из файла simple_tree.py

class TestSimpleTree(unittest.TestCase):

    def setUp(self):
        """
        Инициализируем дерево для тестов.
        """
        self.root = SimpleTreeNode(1, None)
        self.tree = SimpleTree(self.root)
        self.node2 = SimpleTreeNode(2, self.root)
        self.node3 = SimpleTreeNode(3, self.root)
        self.tree.AddChild(self.root, self.node2)
        self.tree.AddChild(self.root, self.node3)
        self.node4 = SimpleTreeNode(4, self.node2)
        self.tree.AddChild(self.node2, self.node4)

    def test_add_child(self):
        """
        Тестируем добавление нового дочернего узла.
        """
        node5 = SimpleTreeNode(5, self.node3)
        self.tree.AddChild(self.node3, node5)
        self.assertIn(node5, self.node3.Children)
        self.assertEqual(node5.Parent, self.node3)

    def test_delete_node(self):
        """
        Тестируем удаление узла.
        """
        self.tree.DeleteNode(self.node4)
        self.assertNotIn(self.node4, self.node2.Children)
        self.assertIsNone(self.node4.Parent)
        all_nodes = self.tree.GetAllNodes()
        self.assertNotIn(self.node4, all_nodes)

    def test_get_all_nodes(self):
        """
        Тестируем получение всех узлов дерева.
        """
        all_nodes = self.tree.GetAllNodes()
        self.assertEqual(len(all_nodes), 4)
        self.assertIn(self.root, all_nodes)
        self.assertIn(self.node2, all_nodes)
        self.assertIn(self.node3, all_nodes)
        self.assertIn(self.node4, all_nodes)

    def test_find_nodes_by_value(self):
        """
        Тестируем поиск узлов по значению.
        """
        nodes_with_value_2 = self.tree.FindNodesByValue(2)
        self.assertEqual(nodes_with_value_2[0], self.node2)
        self.assertEqual(len(nodes_with_value_2), 1)

    def test_move_node(self):
        """
        Тестируем перемещение узла.
        """
        self.tree.MoveNode(self.node2, self.node3)
        self.assertIn(self.node2, self.node3.Children)
        self.assertNotIn(self.node2, self.root.Children)
        self.assertEqual(self.node2.Parent, self.node3)
        self.assertEqual(self.node2.Level, self.node3.Level + 1)

    def test_count_nodes(self):
        """
        Тестируем подсчет всех узлов в дереве.
        """
        self.assertEqual(self.tree.Count(), 4)
        node5 = SimpleTreeNode(5, self.node3)
        self.tree.AddChild(self.node3, node5)
        self.assertEqual(self.tree.Count(), 5)

    def test_leaf_count(self):
        """
        Тестируем подсчет листьев в дереве.
        """
        self.assertEqual(self.tree.LeafCount(), 2)  # Листья: node3 и node4
        node5 = SimpleTreeNode(5, self.node3)
        self.tree.AddChild(self.node3, node5)
        self.assertEqual(self.tree.LeafCount(), 2)  # Листья: node4 и node5