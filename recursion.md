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
    def subfnc(index=0):
        if index >= len(string)/2:
            return True
        if string[index] != string[-index - 1]:
            return False
        return subfnc(index + 1)
    return subfnc()
```
### 5. Печать только чётных значений из списка
```
def even_numbers(lst):
    if not lst:
        return []
    if lst[0] % 2 == 0:
        return [lst.pop(0)] + even_numbers(lst)
    lst.pop(0)
    return even_numbers(lst)
```
### 6. Печать элементов списка с чётными индексами
```
def even_index(lst):
    if not lst:
        return []
    even = lst.pop(0)
    if not lst:
        return [even]
    lst.pop(0)
    return [even] + even_index(lst)
```
### 7. Нахождение второго максимального числа в списке (с учётом, что максимальных может быть несколько, если они равны).
```

```
### 8. Поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности.
```

```