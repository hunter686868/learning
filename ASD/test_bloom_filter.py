import unittest
from bloom_filter import BloomFilter

class TestBloomFilter(unittest.TestCase):
    def setUp(self):
        self.bloom_filter = BloomFilter(32)

    def test_add_and_is_value(self):
        test_strings = ["0123456789", "1234567890", "2345678901", "3456789012", "4567890123",
                        "5678901234", "6789012345", "7890123456", "8901234567", "9012345678"]

        for string in test_strings:
            self.bloom_filter.add(string)

        for string in test_strings:
            self.assertTrue(self.bloom_filter.is_value(string))

        # Проверяем наличие строки, которая не была добавлена
        self.assertFalse(self.bloom_filter.is_value("abcdefghij"))  # Отсутствует в фильтре

        # Проверяем наличие строк, которые были добавлены
        for string in test_strings:
            self.assertTrue(self.bloom_filter.is_value(string))  # Должны быть присутствующими


