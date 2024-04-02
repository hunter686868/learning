import unittest
from cache import NativeCache
class TestNativeCache(unittest.TestCase):
    def test_cache_eviction(self):
        cache = NativeCache(5)  # Создаем хэш-таблицу размером 5
        # Добавляем элементы, чтобы заполнить хэш-таблицу
        cache.put("apple")
        cache.put("banana")
        cache.put("orange")
        cache.put("grape")
        cache.put("kiwi")
        # После этого хэш-таблица заполнена

        # Добавляем новый элемент, чтобы вызвать вытеснение
        cache.put("peach")

        # Проверяем, что "apple" был вытеснен
        self.assertIsNone(cache.find("apple"))

        # Проверяем, что "peach" добавлен корректно
        self.assertEqual(cache.find("peach"), 0)

def test_hit_count(self):
    cache = NativeCache(5)  # Создаем хэш-таблицу размером 5
    # Добавляем элементы
    cache.put("apple")
    cache.put("banana")
    cache.put("orange")
    cache.put("grape")
    cache.put("kiwi")

    # Обращаемся к элементам несколько раз
    cache.find("apple")
    cache.find("banana")
    cache.find("apple")
    cache.find("banana")
    cache.find("banana")

    # Проверяем, что количество обращений к каждому ключу учитывается корректно
    self.assertEqual(cache.hits[0], 2)  # "apple

