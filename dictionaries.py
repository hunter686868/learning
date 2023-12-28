# 1. Напишите небольшую программу, которая добавляет в словарь 100 случайных пар (предварительно в массив например ключи записываем)
# целый ключ + значение строка,
# затем считывает по ключам все значения и выводит, и затем удаляет все пары.

import random


def dct():
    # Создаем словарь с ключами - случайными числами от 1 до 100 и значениями - строками, включающими эти числа
    dictionary = {}
    for i in range(100):
        key = random.randint(1,100)
        dictionary[key] = f'key_{key}'

# По ключам выводим значения и в конце очищаем словарь
    key_list = []
    for key in dictionary.keys():
        key_list.append(key)
        #print(dictionary[key])

    dictionary.clear()
    return key_list


dct()

# 2. Напишите функцию, которая получает список из 100 значений (сгенерируйте его заранее с числами в диапазоне от 1 до 10)
# и число N, и выдаёт список из тех значений в этом списке,
# которые повторяются не менее N раз. Используйте словарь для этого.

# Создаем список из 100 значений
values = []
for j in range(100):
    value = random.randint(1,10)
    values.append(value)


def hundred_values(lst, n):
    # Добавляем в словарь к значениям, соответствующим ключам по +1 за итерацию. По умолчанию стоит None, нам нужен 0, добавим.
    dictionary_1 = {}
    for item in lst:
        dictionary_1[item] = dictionary_1.get(item, 0) + 1
    result = []
    # Смотрим значения, которые повторились n раз и добавляем ключи в список, который в итоге печатаем.
    for key, vle in dictionary_1.items():
        if vle == n:
            result.append(key)
    #print(result)
    return result


hundred_values(values, 10)
