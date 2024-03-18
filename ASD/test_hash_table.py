import unittest
from hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable(10, 1)  # Создаем хэш-таблицу размером 10 и шагом 1

    def test_seek_slot(self):
        self.assertEqual(self.ht.seek_slot("value"), self.ht.hash_fun("value"))  # Должно вернуться значение 0, так как это начальный индекс
        self.ht.put("value")  # Занимаем слот
        self.assertEqual(self.ht.seek_slot("value"), 2)  # Следующий свободный слот

    def test_put(self):
        self.assertEqual(self.ht.put("value"), self.ht.hash_fun("value"))  # Добавляем значение в слот
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
        self.assertEqual(self.ht.put("value"), None)  # Попытка добавить значение, когда все слоты заняты

    def test_find(self):
        self.ht.put("value")  # Помещаем значение в слот
        self.assertEqual(self.ht.find("value"), self.ht.hash_fun("value"))  # Ищем значение, оно должно быть в слоте 0
        self.assertEqual(self.ht.find("unknown"), None)  # Ищем значение, которого нет, должно вернуться None
