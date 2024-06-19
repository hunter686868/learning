import unittest
from binary_trees_2 import aBST

class TestaBST(unittest.TestCase):

    def setUp(self):
        self.tree = aBST(3)  # Дерево глубины 3

    def test_add_key(self):
        # Добавляем ключи и проверяем возвратимые значения
        self.assertEqual(self.tree.AddKey(10), 0)
        self.assertEqual(self.tree.AddKey(5), 1)
        self.assertEqual(self.tree.AddKey(15), 2)
        self.assertEqual(self.tree.AddKey(3), 3)
        self.assertEqual(self.tree.AddKey(8), 4)
        self.assertEqual(self.tree.AddKey(12), 5)
        self.assertEqual(self.tree.AddKey(18), 6)

        # Попытка добавления существующего ключа
        self.assertEqual(self.tree.AddKey(10), 0)
        self.assertEqual(self.tree.AddKey(5), 1)

        # Проверка на переполнение
        self.assertEqual(self.tree.AddKey(20), -1)

    def test_find_key_index(self):
        # Добавляем ключи
        self.tree.AddKey(10)
        self.tree.AddKey(5)
        self.tree.AddKey(15)
        self.tree.AddKey(3)
        self.tree.AddKey(8)
        self.tree.AddKey(12)
        self.tree.AddKey(18)

        # Проверяем индексы ключей
        self.assertEqual(self.tree.FindKeyIndex(10), 0)
        self.assertEqual(self.tree.FindKeyIndex(5), 1)
        self.assertEqual(self.tree.FindKeyIndex(15), 2)
        self.assertEqual(self.tree.FindKeyIndex(3), 3)
        self.assertEqual(self.tree.FindKeyIndex(8), 4)
        self.assertEqual(self.tree.FindKeyIndex(12), 5)
        self.assertEqual(self.tree.FindKeyIndex(18), 6)

        # Поиск несуществующего ключа
        self.assertIsNone(self.tree.FindKeyIndex(20))

    def test_tree_structure(self):
        # Добавляем ключи
        self.tree.AddKey(10)
        self.tree.AddKey(5)
        self.tree.AddKey(15)
        self.tree.AddKey(3)
        self.tree.AddKey(8)
        self.tree.AddKey(12)
        self.tree.AddKey(18)

        # Ожидаемая структура дерева
        expected_tree = [10, 5, 15, 3, 8, 12, 18, None, None, None, None, None, None, None, None]
        self.assertEqual(self.tree.Tree, expected_tree)

    def test_empty_tree(self):
        # Проверка пустого дерева
        self.assertIsNone(self.tree.FindKeyIndex(10))  # Должно вернуть None, так как ключ 10 не добавлен
        self.assertEqual(self.tree.AddKey(10), 0)  # Добавляем ключ 10
        self.assertEqual(self.tree.FindKeyIndex(10), 0)

