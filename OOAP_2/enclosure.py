# Код из предыдущего задания с классом General
import copy
import pickle
import base64
from typing import Type

# Создаем класс general
class General(object):

    # Копирование
    def copy_to(self, other : 'General') -> None:
        if not isinstance(other, General):
            raise TypeError("Копируемый объект должен быть экземпляром General")
        other.__dict__.clear()
        other.__dict__.update(copy.deepcopy(self.__dict__))

    # Клонирование с глубоким копированием
    def clone(self) -> 'General':
        # создаём новый пустой экземпляр и копируем в него self
        new_obj = self.__class__()
        new_obj.__dict__.update(copy.deepcopy(self.__dict__))
        return new_obj

    # Сравнение (Включая глубокое)
    def equals(self, other) -> bool:
        # Проверяем поверхностное равенство атрибутов
        if not isinstance(other, General):
            return False
        return self.__dict__ == other.__dict__

    # Сериализация
    def serialize(self) -> str:
        # Сериализуем объект в строку с помощью pickle + base64.
        raw_bytes = pickle.dumps(self)
        return base64.b64encode(raw_bytes).decode('utf-8')

    @classmethod
    def deserialize(cls, data: str) -> 'General':
        # Восстанавливаем объект из строки после serialize
        raw_bytes = base64.b64decode(data.encode('utf-8'))
        obj = pickle.loads(raw_bytes)
        if not isinstance(obj, cls):
            raise TypeError("Неверный тип")
        return obj

    def __str__(self) -> str:
        # Текстовое представление объекта
        return f"{self.__class__.__name__}: {self.__dict__}"


    def is_type(self, t: Type) -> bool:
        # Проверка, что объект - экземпляр класса
        return isinstance(self, t)

    def get_real_type(self) -> Type:
        # Получение реального типа объекта
        return type(self)

# Базовый класс для всех остальных классов
class Any(General):
    pass

