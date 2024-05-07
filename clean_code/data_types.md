1) В классе BloomFilter заменил два числа для хэширования на константы HASH_CONST_1, HASH_CONST_2.
В дальнейшем это упростит понимание кода.

2) В условии добавил переменную для понимания
```
equality = zero == one
        if equality:
```

3) Добавил проверку в функцию с поиском подматрицы
```
def matrix(n, m, matrix):
    if n == 0 or m == 0:
        return [] 
```

4) При сравнении двух вещественных чисел можно использовать погрешность в виде дельты, равной например 1e-10

5) Использование логических переменных:
```
finished = element_index < 0 or element_index > last_element_index
repeated_entry = element_index == last_element_index
if finished:
if repeated_entry:
```

6) message = u"Привет, мир!"  - Используем префикс u для строки Unicode

7) Проверка на переполнение:
```
try:
    z = x * y
except OverflowError:
    print('Overflow error')
```

8) Замена чисел с плавающей запятой на целые, если возможно:
```
if x % 1 == 0:
    x = int(x)
```

9) Проверка библиотеки:
```
try:
    import numpy as np
except ImportError:
    print('Numpy is not installed')
```

10) Целочисленное деление:
```
if x % y == 0:
    z = x // y
else:
    print("Not integer")
```

11) Константа для строки:
```
SUCCESS_STATUS = "OK"
if status == SUCCESS_STATUS:
    print("Success")
```

12) Использование библиотеки decimal для большей точности
```
from decimal import Decimal
x = Decimal('3.14159')
```
