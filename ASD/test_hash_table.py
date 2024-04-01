import unittest
from hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable(10, 1)

    def test_seek_slot(self):
        self.assertEqual(self.ht.seek_slot("value"), self.ht.hash_fun("value"))
        self.ht.put("value")
        self.assertEqual(self.ht.seek_slot("value"), 2)

    def test_put(self):
        self.assertEqual(self.ht.put("value"), self.ht.hash_fun("value"))
        value = self.ht.hash_fun("value") + 1
        self.ht.put("value")
        self.ht.put("value")
        self.ht.put("value")
        self.ht.put("value")
        self.ht.put("value")
        self.ht.put("value")
        self.ht.put("value")
        self.ht.put("value")
        self.ht.put("value")
        self.assertEqual(self.ht.put("value"), None)

    def test_find(self):
        self.ht.put("value")
        self.assertEqual(self.ht.find("value"), self.ht.hash_fun("value"))
        self.assertEqual(self.ht.find("unknown"), None)
