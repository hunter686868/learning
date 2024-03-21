import unittest
from native_dictionary import NativeDictionary


class TestNativeDictionary(unittest.TestCase):
    def setUp(self):
        self.native_dict = NativeDictionary(5)

    def test_put_new_key(self):
        self.native_dict.put("apple", 5)
        self.assertEqual(self.native_dict.get("apple"), 5)

    def test_put_existing_key(self):
        self.native_dict.put("apple", 5)
        self.native_dict.put("apple", 10)
        self.assertEqual(self.native_dict.get("apple"), 10)

    def test_is_key_present(self):
        self.native_dict.put("apple", 5)
        self.assertTrue(self.native_dict.is_key("apple"))

    def test_is_key_not_present(self):
        self.assertFalse(self.native_dict.is_key("banana"))

    def test_get_existing_key(self):
        self.native_dict.put("apple", 5)
        self.assertEqual(self.native_dict.get("apple"), 5)

    def test_get_non_existing_key(self):
        self.assertIsNone(self.native_dict.get("banana"))