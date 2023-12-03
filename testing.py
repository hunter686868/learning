# Функция находится в файле func, импортируем ее и модуль unittest

import unittest
from func import func


class FuncTests(unittest.TestCase):
    def test_substring_true(self):
        # Первый тест проверит, возвращает ли функция True, когда должна
        self.assertTrue(func("12345", "234"))

    def test_substring_false(self):
        # Второй тест проверит, возвращает ли функция False, когда должна
        self.assertFalse(func("12345", "235"))

    def test_strings_empty(self):
        # Третий тест проверит, будет ли функция работать с пустыми значениями
        self.assertFalse(func('', ''))

    def test_substring_abroad(self):
        # Четвертый тест проверит, будет ли функция корректно работать, если подстрока начинает
        # совпадать с середины строки и продолжается после конца строки
        self.assertFalse(func('12345', '3456'))

    def test_substring_full_string(self):
        # Пятый тест проверит, вернет ли функция True, если строка и подстрока равны
        self.assertTrue(func('12345', '12345'))

input('Нажмите любую клавишу')