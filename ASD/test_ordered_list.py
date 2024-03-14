import unittest
from ordered_list import OrderedList


class TestOrderedList(unittest.TestCase):

    def setUp(self):
        self.ordered_list = OrderedList(asc=True)
        self.ordered_list.add(3)
        self.ordered_list.add(1)
        self.ordered_list.add(2)

    def test_add(self):
        self.assertEqual(self.ordered_list.len(), 3)
        self.ordered_list.clean(asc=False)
        self.ordered_list.add(3)
        self.ordered_list.add(1)
        self.ordered_list.add(2)
        ol = self.ordered_list.get_all()
        self.assertEqual(ol, [3, 2, 1])

    def test_delete(self):
        self.ordered_list.delete(1)
        al = self.ordered_list.get_all()
        self.assertEqual(al, [2, 3])
        self.ordered_list.delete(3)
        al = self.ordered_list.get_all()
        self.assertEqual(al, [2])
        self.ordered_list.delete(2)
        al = self.ordered_list.get_all()
        self.assertEqual(al, [])

    def test_find(self):
        self.assertEqual(self.ordered_list.find(1).value, 1)
        self.assertEqual(self.ordered_list.find(4), None)
        self.assertEqual(self.ordered_list.find(2).value, 2)
