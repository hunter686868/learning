# Рекурсия

## Решение задач с помощью рекурсии

### 1. Возведение числа N в степень M
```
def exponentiation(n, m):
    if m == 0:
        return 1

    return n * exponentiation(n, m - 1)
```

### 2. Вычисление суммы цифр числа
```
def digits_sum(number):
    if number < 10:
        return number

    return number % 10 + digits_sum(number // 10)
```
### 3. Расчёт длины списка, для которого разрешена только операция удаления первого элемента pop(0) (и получение длины конечно)
```
def list_len(lst):
    if not lst:
        return 0

    lst.pop(0)
    return 1 + list_len(lst)
```
### 4. Проверка, является ли строка палиндромом
```
def palindrome(string):
    if len(string) < 2:
        return True
    return chk_plndr(string, 0)


def chk_plndr(string, i):
    if i >= len(string)/2:
        return True
    if string[i] != string[-i - 1]:
        return False
    return chk_plndr(string, i + 1)
```
### 5. Печать только чётных значений из списка
```
def even_numbers(lst):
    return chk_even_n(lst, 0)


def chk_even_n(lst, i):
    if i == len(lst):
        return []
    if lst[i] % 2 == 0:
        return [lst[i]] + chk_even_n(lst, i + 1)
    return chk_even_n(lst, i + 1)
```
### 6. Печать элементов списка с чётными индексами
```
def even_index(lst):
    return chk_even_i(lst, 0)


def chk_even_i(lst, i):
    if i >= len(lst):
        return []
    return [lst[i]] + chk_even_i(lst, i + 2)
```
### 7. Нахождение второго максимального числа в списке (с учётом, что максимальных может быть несколько, если они равны).
```
def second_max(lst: list) -> int:
    if len(lst) < 2:
        return 0
    return find_second_max(lst, 1, lst[0], lst[1])


def find_second_max(lst: list, i: int, m1: int, m2: int) -> int:
    if i == len(lst):
        return m2
    n = lst[i]
    if n > m1:
        m2 = m1
        m1 = n
    elif n > m2:
        m2 = n
    i += 1
    return find_second_max(lst, i, m1, m2)
```
### 8. Поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности.
```

```