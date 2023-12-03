# Возьмем функцию поиска подстрок, т.к. первую часть курса я не проходил.
# Функция находится в файле func, импортируем ее и модуль unittest
#

import unittest
from func import func


class FuncTests(unittest.TestCase):
    def test_substring_true(self):
        # Первый тест проверит, возвращает ли функция True, когда должна
        self.assertTrue(func("12345", "234"))

    def test_substring_false(self):
        # Второй тест проверит, возвращает ли функция False, когда должна
        self.assertFalse(func("12345", "235"))

    def

