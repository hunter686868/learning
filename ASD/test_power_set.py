import time
import random
import string
import unittest
from power_set import PowerSet


class TestPowerSet(unittest.TestCase):
    def test_put(self):
        power_set = PowerSet()
        power_set.put(1)
        self.assertTrue(power_set.get(1))  # Проверка наличия добавленного элемента
        self.assertIsNone(power_set.put(1))  # Попытка добавить дубликат

    def test_remove(self):
        power_set = PowerSet()
        power_set.put(1)
        self.assertTrue(power_set.remove(1))  # Проверка удаления существующего элемента
        self.assertFalse(power_set.remove(2))  # Попытка удалить отсутствующий элемент

    def test_intersection(self):
        power_set1 = PowerSet()
        power_set2 = PowerSet()
        power_set1.put(1)
        power_set1.put(2)
        power_set2.put(2)
        power_set2.put(3)
        result_set = power_set1.intersection(power_set2)
        self.assertTrue(result_set.get(2))  # Проверка наличия общего элемента
        self.assertFalse(result_set.get(1))  # Проверка отсутствия уникального элемента
        self.assertFalse(result_set.get(3))  # Проверка отсутствия уникального элемента

    def test_union(self):
        power_set1 = PowerSet(10, 1)
        power_set2 = PowerSet(10, 1)
        power_set1.put(1)
        power_set1.put(2)
        power_set2.put(2)
        power_set2.put(3)
        result_set = power_set1.union(power_set2)
        self.assertTrue(result_set.get(1))  # Проверка наличия элемента из первого множества
        self.assertTrue(result_set.get(2))  # Проверка наличия элемента из обоих множеств
        self.assertTrue(result_set.get(3))  # Проверка наличия элемента из второго множества

    def test_difference(self):
        power_set1 = PowerSet(10, 1)
        power_set2 = PowerSet(10, 1)
        power_set1.put(1)
        power_set1.put(2)
        power_set2.put(2)
        power_set2.put(3)
        result_set = power_set1.difference(power_set2)
        self.assertTrue(result_set.get(1))  # Проверка наличия уникального элемента
        self.assertFalse(result_set.get(2))  # Проверка отсутствия общего элемента
        self.assertFalse(result_set.get(3))  # Проверка отсутствия элемента из второго множества

    def test_issubset(self):
        power_set1 = PowerSet(10, 1)
        power_set2 = PowerSet(10, 1)
        power_set1.put(1)
        power_set1.put(2)
        power_set2.put(1)
        power_set2.put(2)
        power_set2.put(3)
        self.assertTrue(power_set2.issubset(power_set1))  # Проверка, что все элементы первого множества входят во второе
        self.assertFalse(power_set1.issubset(power_set2))  # Проверка, что не все элементы второго множества входят в первое
        self.assertTrue(power_set1.issubset(PowerSet(10, 1)))  # Проверка, что все элементы пустого множества входят в первое

    def test_performance(self):

        # Генерируем два множества из десятков тысяч элементов
        power_set1 = PowerSet(10010, 1)
        power_set2 = PowerSet(10010, 1)
        for i in range(10000):
            power_set1.put(i)
        start_time = time.time()
        set = power_set2.issubset(power_set1)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Time for union operation on sets with 100,000 elements: {:.4f} seconds".format(elapsed_time))

