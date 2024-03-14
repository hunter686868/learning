import unittest
from ordered_list import OrderedList

class TestOrderedList(unittest.TestCase):
    def test_add(self):
        ordered_list_asc = OrderedList(asc=True)
        ordered_list_asc.add(3)
        ordered_list_asc.add(1)
        ordered_list_asc.add(2)
        self.assertEqual([node.value for node in ordered_list_asc.get_all()], [1, 2, 3])

        ordered_list_desc = OrderedList(asc=False)
        ordered_list_desc.add(3)
        ordered_list_desc.add(1)
        ordered_list_desc.add(2)
        self.assertEqual([node.value for node in ordered_list_desc.get_all()], [3, 2, 1])

    def test_delete(self):
        ordered_list = OrderedList(asc=True)
        ordered_list.add(3)
        ordered_list.add(1)
        ordered_list.add(2)
        ordered_list.delete(1)
        self.assertEqual([node.value for node in ordered_list.get_all()], [2, 3])
        ordered_list.delete(3)
        self.assertEqual([node.value for node in ordered_list.get_all()], [2])
        ordered_list.delete(2)
        self.assertEqual([node.value for node in ordered_list.get_all()], [])

    def test_find(self):
        ordered_list = OrderedList(asc=True)
        ordered_list.add(3)
        ordered_list.add(1)
        ordered_list.add(2)
        self.assertEqual(ordered_list.find(1).value, 1)
        self.assertEqual(ordered_list.find(4), None)
        self.assertEqual(ordered_list.find(2).value, 2)
